"""Cadastra crachás titulares pelo Frequência e confere API e Acessus."""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import replace
from datetime import datetime, timedelta
from pathlib import Path

from automatiza.ciclos_sirh import SirhBackend
from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer
from automatiza.observador import observer_lock
from automatiza.perfis import destinations_match, import_destination
from automatiza.rh import RhApp, _fill_without_logging


SERVICE = "FrmSyncImpViewsPrincipal"
LOG = Path("C:/acesso/Logs/AcessusSyncProcessoService.log")


def validate_plan(plan):
    if not isinstance(plan, dict) or plan.get("versao") != 1:
        raise ValueError("Plano de crachás exige versao=1.")
    if plan.get("origem") != "RHFagundes" or plan.get("destino") != "novo123":
        raise ValueError("Origem e destino precisam corresponder ao ambiente mapeado.")
    cases = plan.get("casos")
    if not isinstance(cases, list) or len(cases) < 2:
        raise ValueError("Informe pelo menos dois casos de crachá.")
    seen = set()
    for case in cases:
        if not isinstance(case, dict) or not {"unidade", "contrato", "pessoa_origem",
                                                "pessoa_destino", "novo_cracha"} <= set(case):
            raise ValueError("Caso sem unidade, contrato, pessoa e novo crachá.")
        key = (case["unidade"], case["contrato"])
        badge = case["novo_cracha"]
        previous_badge = case.get("cracha_anterior")
        if (not re.fullmatch(r"\d{4}", case["unidade"]) or type(case["contrato"]) is not int
                or type(case["pessoa_origem"]) is not int or type(case["pessoa_destino"]) is not int
                or not isinstance(badge, str) or not re.fullmatch(r"\d{6,12}", badge)
                or (previous_badge is not None and (not isinstance(previous_badge, str)
                    or not re.fullmatch(r"\d{6,12}", previous_badge) or previous_badge == badge))
                or key in seen or badge in seen):
            raise ValueError("Caso duplicado ou com chave/crachá inválido.")
        seen.update((key, badge))
    timeout = plan.get("timeout_segundos", 240)
    if type(timeout) is not int or not 30 <= timeout <= 1800:
        raise ValueError("timeout_segundos deve estar entre 30 e 1800.")
    return plan


class Diary:
    def __init__(self, folder, plan):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=False)
        (self.folder / "plano.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
        self.state = {"status": "INICIADO", "casos": [], "servico": None}
        self.save()

    def save(self):
        (self.folder / "resultado.json").write_text(
            json.dumps(self.state, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    def event(self, step, result, *, case=None, expected=None, observed=None):
        row = {"horario": datetime.now().astimezone().isoformat(), "etapa": step,
               "caso": case, "resultado": result, "esperado": expected, "observado": observed}
        with (self.folder / "passos.jsonl").open("a", encoding="utf-8") as output:
            output.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
            output.flush()
        with (self.folder / "passos.log").open("a", encoding="utf-8") as output:
            output.write(f"[{row['horario']}] {result} {step} caso={case} "
                         f"esperado={expected} observado={observed}\n")
            output.flush()


def classify(case, source, api, target):
    badge = case["novo_cracha"]
    origin_ok = source == badge
    api_ok = api == badge
    matches = [row for row in target if str(row["Codigo"]) == badge]
    target_ok = (len(matches) == 1 and matches[0]["IdPessoa"] == case["pessoa_destino"]
                 and matches[0]["excluido"] == "N")
    if not origin_ok:
        status = "NAO_GRAVADO_ORIGEM"
    elif not api_ok:
        status = "NAO_PUBLICADO_API"
    elif not matches:
        status = "NAO_IMPORTADO"
    elif not target_ok:
        status = "DIVERGENTE_DESTINO"
    else:
        status = "IMPORTADO_EXATO"
    return {"status": status, "origem": source, "api": api, "destino": matches}


class BadgeRunner:
    def __init__(self, plan, output):
        self.plan = validate_plan(plan)
        self.diary = Diary(output, plan)
        self.settings = Settings.load()
        self.origin = SqlServer(replace(self.settings, sql_database=plan["origem"]))
        self.dest = SqlServer(replace(self.settings, sql_database=plan["destino"]))
        self.integration = None
        self.ui = None
        self.screen = None

    def _source(self, case):
        rows = self.origin.query("SELECT PESSOA,CRACHA FROM RHCONTRATOS WHERE UNIDADE=? AND CONTRATO=?",
                                 (case["unidade"], case["contrato"]))
        if len(rows) != 1 or rows[0]["PESSOA"] != case["pessoa_origem"]:
            raise RuntimeError("Contrato de origem não corresponde ao plano.")
        return rows[0]["CRACHA"]

    def _api(self, case):
        query = urllib.parse.urlencode({"unidade": case["unidade"], "contrato": case["contrato"], "pagina": 1})
        request = urllib.request.Request(self.plan["api"].rstrip("/") + "/colaborador/contratos?" + query,
                                         headers={"Authorization": "Bearer " + self.integration.token})
        with urllib.request.urlopen(request, context=self.integration.context, timeout=30) as response:
            rows = json.load(response)
        exact = [row for row in rows if row.get("unidade") == case["unidade"]
                 and row.get("contrato") == case["contrato"]
                 and row.get("pessoa") == case["pessoa_origem"]]
        if len(rows) != 1 or len(exact) != 1:
            raise RuntimeError("API não devolveu exatamente o contrato/pessoa solicitado.")
        return exact[0].get("cracha")

    def _target(self, case):
        return self.dest.query("SELECT id,IdPessoa,Codigo,TipoCracha,TipoUso,excluido "
                               "FROM RegCrachas WHERE IdPessoa=? OR Codigo=? ORDER BY id",
                               (case["pessoa_destino"], case["novo_cracha"]))

    def _source_badge_record(self, case):
        return self.origin.query(
            "SELECT NROCRACHA,SITUACAOCRACHA,DATAHORATERMINO FROM RHREGCRACHAS "
            "WHERE UNIDADE=? AND CONTRATO=? AND NROCRACHA=?",
            (case["unidade"], case["contrato"], case["novo_cracha"]))

    def preflight(self):
        self.origin.assert_database()
        self.dest.assert_database()
        actual = import_destination(Path(self.settings.app_work_dir or "C:/acesso") / "ConexaoConfig.ini")
        if not destinations_match(actual, {"servidor": self.settings.sql_server,
                                           "banco": self.plan["destino"]}):
            raise RuntimeError("Importador aponta para outro destino.")
        if self.dest.scalar("SELECT COUNT(*) FROM DADOS_IMPORTACAO_API WHERE id=1 AND atualizar_crachas='S'") != 1:
            raise RuntimeError("Atualização de crachás desativada no importador.")
        if not LOG.is_file():
            raise RuntimeError("Log do serviço não encontrado.")
        base_config = {**self.plan, "pessoa": self.plan["casos"][0]["pessoa_destino"],
                       "contrato": self.plan["casos"][0]["contrato"]}
        self.integration = SirhBackend(base_config)
        self.integration.preflight()
        for case in self.plan["casos"]:
            source = self._source(case)
            api = self._api(case)
            target = self._target(case)
            people = self.dest.query("SELECT Id,IdExportacao FROM Pessoas WHERE Id=?",
                                     (case["pessoa_destino"],))
            if len(people) != 1 or str(people[0]["IdExportacao"]) != str(case["contrato"]):
                raise RuntimeError("Pessoa do destino não corresponde ao contrato do caso.")
            collision_origin = self.origin.scalar("SELECT COUNT(*) FROM RHREGCRACHAS WHERE NROCRACHA=?",
                                                   (case["novo_cracha"],))
            collision_target = self.dest.scalar("SELECT COUNT(*) FROM RegCrachas WHERE Codigo=?",
                                                 (case["novo_cracha"],))
            already_registered = source == case["novo_cracha"]
            if already_registered:
                records = self._source_badge_record(case)
                if (len(records) != 1 or records[0]["SITUACAOCRACHA"] != "01"
                        or records[0]["DATAHORATERMINO"] is not None or api != source):
                    raise RuntimeError("Crachá já registrado diverge entre origem e API.")
                if case.get("cracha_anterior"):
                    previous = self.origin.query(
                        "SELECT TOP 1 SITUACAOCRACHA FROM RHREGCRACHAS "
                        "WHERE UNIDADE=? AND CONTRATO=? AND NROCRACHA=? ORDER BY DATAHORAINICIO DESC",
                        (case["unidade"], case["contrato"], case["cracha_anterior"]))
                    if len(previous) != 1 or previous[0]["SITUACAOCRACHA"] != "05":
                        raise RuntimeError("Crachá anterior não aparece Cancelado na origem.")
            elif (collision_origin or collision_target or api != source
                  or (case.get("cracha_anterior") and source != case["cracha_anterior"])):
                raise RuntimeError("Crachá novo já existe ou origem/API divergem antes do teste.")
            self.diary.state["casos"].append({"unidade": case["unidade"], "contrato": case["contrato"],
                                              "pessoa_origem": case["pessoa_origem"],
                                              "pessoa_destino": case["pessoa_destino"],
                                              "cracha_anterior": case.get("cracha_anterior", source),
                                              "novo_cracha": case["novo_cracha"],
                                              "destino_antes": target,
                                              "status": "CADASTRADO_ORIGEM" if already_registered else "PREPARADO"})
            self.diary.event("Fotografar origem, API e destino", "PASSOU", case=case["contrato"],
                             expected=source, observed={"api": api, "destino": target})
        self.diary.save()

    @staticmethod
    def _field_at(form, klass, point, *, require_enabled=True):
        origin = form.rectangle()
        matches = []
        for control in form.descendants(class_name=klass):
            if not control.is_visible() or (require_enabled and not control.is_enabled()):
                continue
            rect = control.rectangle()
            distance = abs(rect.left - origin.left - point[0]) + abs(rect.top - origin.top - point[1])
            if distance <= 22:
                matches.append((distance, control))
        matches.sort(key=lambda entry: entry[0])
        if len(matches) != 1:
            raise RuntimeError(f"Campo {klass} na posição {point} não identificado de forma única.")
        return matches[0][1]

    def _window(self, klass, timeout=10):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            found = [w for w in self.ui.window.descendants() if w.class_name() == klass and w.is_visible()]
            if len(found) == 1:
                return found[0]
            time.sleep(0.2)
        raise RuntimeError(f"Janela {klass} não abriu.")

    def _save_badge(self, registration, case, badge, situation_name):
        from pywinauto import Desktop, mouse

        badge_field = self._field_at(registration, "TEdit", (312, 268), require_enabled=False)
        previous = badge_field.window_text()
        if previous != badge:
            if not badge_field.is_enabled():
                raise RuntimeError("Campo do crachá está desabilitado.")
            self.diary.event("Preencher crachá", "ANTES", case=case["contrato"],
                             expected=badge, observed=previous)
            _fill_without_logging(badge_field, badge)
        if badge_field.window_text() != badge:
            raise RuntimeError("Campo do crachá não reteve o valor.")
        if badge_field.is_enabled():
            badge_field.type_keys("{TAB}")
        self.diary.event("Conferir crachá na tela", "PASSOU", case=case["contrato"],
                         expected=badge, observed=badge_field.window_text())
        if situation_name == "Ativo":
            latest = self.origin.scalar(
                "SELECT MAX(DATAHORAINICIO) FROM RHREGCRACHAS WHERE UNIDADE=? AND CONTRATO=?",
                (case["unidade"], case["contrato"]))
            if latest is not None:
                proposed = latest.replace(second=0, microsecond=0) + timedelta(minutes=1)
                time_field = self._field_at(registration, "TMaskEdit", (219, 268), require_enabled=False)
                current = datetime.strptime(time_field.window_text(), "%H:%M").time()
                if proposed.date() == datetime.now().date() and current <= latest.time():
                    if not time_field.is_enabled():
                        raise RuntimeError("Horário automático do cadastro não avançou após o último registro; aguarde o próximo minuto.")
                    self.diary.event("Ajustar horário posterior ao último registro", "ANTES",
                                     case=case["contrato"], expected=proposed.strftime("%H:%M"),
                                     observed=time_field.window_text())
                    _fill_without_logging(time_field, proposed.strftime("%H:%M"))
                    if time_field.window_text() != proposed.strftime("%H:%M"):
                        raise RuntimeError("Horário do novo registro não reteve valor posterior.")
                    time_field.type_keys("{TAB}")
                    self.diary.event("Conferir horário do novo registro", "PASSOU",
                                     case=case["contrato"], observed=time_field.window_text())
        situation = self._field_at(registration, "TDBComboMeta", (81, 299))
        self.diary.event("Selecionar situação do crachá", "ANTES", case=case["contrato"],
                         expected=situation_name, observed=badge)
        situation.click_input()
        situation.type_keys("{HOME}{ENTER}" if situation_name == "Ativo"
                            else "{HOME}{DOWN 2}{ENTER}")
        selected = situation.window_text().strip()
        if selected != situation_name:
            raise RuntimeError(f"Situação do crachá não foi selecionada: {selected!r}.")
        self.diary.event("Conferir situação do crachá na tela", "PASSOU", case=case["contrato"],
                         expected=situation_name, observed=selected)
        footer = [p for p in registration.descendants(class_name="TPanel")
                  if p.is_visible() and p.rectangle().top - registration.rectangle().top > 370]
        if len(footer) != 1:
            raise RuntimeError("Rodapé do cadastro de crachás não identificado.")
        r = footer[0].rectangle()
        self.diary.event("Solicitar gravação pela tela Voltar", "ANTES", case=case["contrato"],
                         expected={"cracha": badge, "situacao": situation_name})
        mouse.click(coords=(r.left + r.width() - 50, r.top + 19))
        deadline = time.monotonic() + 7
        confirmation = None
        while time.monotonic() < deadline:
            dialogs = [w for w in Desktop(backend="win32").windows(process=self.ui.window.process_id())
                       if w.class_name() == "TMessageForm" and w.is_visible()]
            if len(dialogs) == 1:
                confirmation = dialogs[0]
                break
            time.sleep(0.2)
        if confirmation is None:
            raise RuntimeError("Confirmação de gravação não apareceu.")
        buttons = {b.window_text().replace("&", "").strip().casefold(): b
                   for b in confirmation.descendants() if b.class_name() == "TButton" and b.is_visible()}
        if set(buttons) != {"sim", "não"}:
            raise RuntimeError("Confirmação de gravação inesperada.")
        self.diary.event("Confirmar gravação do crachá", "ANTES", case=case["contrato"],
                         expected={"cracha": badge, "situacao": situation_name})
        buttons["sim"].click_input()
        time.sleep(0.4)
        dialogs = [w for w in Desktop(backend="win32").windows(process=self.ui.window.process_id())
                   if w.class_name() == "TMessageForm" and w.is_visible()]
        if dialogs:
            self.ui.window.capture_as_image().save(str(self.diary.folder / f"erro-cadastro-{case['contrato']}.png"))
            raise RuntimeError("Cadastro mostrou mensagem inesperada após salvar; veja erro-cadastro no relatório.")

    def _register(self, case):
        from pywinauto import Desktop, mouse

        if self.ui is None:
            settings = replace(self.settings, rh_continue_invalid_config="yes")
            app = RhApp(settings)
            visible_frequency = [w for w in app._frequency() if w.is_visible()]
            if len(visible_frequency) == 1:
                app.window = visible_frequency[0]
                self.ui = app
            elif visible_frequency:
                raise RuntimeError("Mais de um módulo Frequência visível.")
            else:
                self.ui = app.start()
            existing = [w for w in self.ui.window.descendants()
                        if w.class_name() == "TFrm_RHPA4300" and w.is_visible()]
            if len(existing) > 1:
                raise RuntimeError("Mais de uma tela Pessoas e Contratos aberta.")
            self.screen = existing[0] if existing else self.ui.open_screen("pessoas")
        form = self.screen
        dialogs = [w for w in Desktop(backend="win32").windows(process=self.ui.window.process_id())
                   if w.class_name() == "TMessageForm" and w.is_visible()]
        if dialogs:
            buttons = [b for b in dialogs[0].descendants()
                       if b.class_name() == "TButton" and b.window_text().replace("&", "") == "OK"]
            if len(dialogs) != 1 or len(buttons) != 1:
                raise RuntimeError("Mensagem pendente inesperada no Frequência.")
            self.diary.event("Dispensar aviso da tentativa anterior", "PASSOU", case=case["contrato"])
            buttons[0].click_input()
        registrations = [w for w in self.ui.window.descendants()
                         if w.class_name() == "TFrm_RH0940" and w.is_visible()]
        if len(registrations) > 1:
            raise RuntimeError("Mais de um cadastro de crachá aberto.")
        registration = registrations[0] if registrations else None
        if registration is None:
            person = self._field_at(form, "TEdit", (57, 37))
            self.diary.event("Selecionar pessoa no Frequência", "ANTES", case=case["contrato"],
                             expected=case["pessoa_origem"])
            _fill_without_logging(person, str(case["pessoa_origem"]))
            person.type_keys("{ENTER}")
            tabs = Desktop(backend="uia").window(handle=form.handle).descendants(control_type="TabItem")
            tab = [item for item in tabs if item.window_text() == "Dados Contratuais" and item.is_visible()]
            if len(tab) != 1:
                raise RuntimeError("Aba Dados Contratuais não identificada.")
            tab[0].click_input()
        unit = self._field_at(form, "TEdit", (68, 105), require_enabled=False).window_text()
        contract = self._field_at(form, "TEdit", (68, 129), require_enabled=False).window_text()
        if unit != case["unidade"] or contract != str(case["contrato"]):
            raise RuntimeError(f"Seleção da tela diverge do caso: unidade={unit}, contrato={contract}.")
        self.diary.event("Confirmar pessoa/unidade/contrato na tela", "PASSOU", case=case["contrato"],
                         expected=(case["unidade"], case["contrato"]), observed=(unit, contract))
        if registration is not None:
            stale_badge = self._field_at(registration, "TEdit", (312, 268), require_enabled=False)
            stale_value = stale_badge.window_text()
            if not stale_badge.is_enabled() and stale_value != self._source(case):
                footer = [p for p in registration.descendants(class_name="TPanel")
                          if p.is_visible() and p.rectangle().top - registration.rectangle().top > 370]
                if len(footer) != 1:
                    raise RuntimeError("Não foi possível descartar cadastro pendente.")
                r = footer[0].rectangle()
                mouse.click(coords=(r.left + r.width() - 50, r.top + 19))
                time.sleep(0.3)
                dialogs = [w for w in Desktop(backend="win32").windows(process=self.ui.window.process_id())
                           if w.class_name() == "TMessageForm" and w.is_visible()]
                if len(dialogs) != 1:
                    raise RuntimeError("Confirmação para descartar cadastro pendente não apareceu.")
                no = [b for b in dialogs[0].descendants()
                      if b.class_name() == "TButton" and b.window_text().replace("&", "").casefold() == "não"]
                if len(no) != 1:
                    raise RuntimeError("Botão Não para descartar cadastro pendente não encontrado.")
                no[0].click_input()
                self.diary.event("Descartar cadastro pendente da tentativa anterior", "PASSOU",
                                 case=case["contrato"], observed=stale_value)
                registration = None
        if registration is None:
            form.set_focus()
            form.type_keys("^r")
            registration = self._window("TFrm_RH0940")
        else:
            self.diary.event("Retomar cadastro de crachá já aberto", "PASSOU", case=case["contrato"])
        old_badge = self._source(case)
        old_records = self.origin.query(
            "SELECT TOP 1 NROCRACHA,SITUACAOCRACHA,DATAHORATERMINO FROM RHREGCRACHAS "
            "WHERE UNIDADE=? AND CONTRATO=? AND NROCRACHA=? ORDER BY DATAHORAINICIO DESC",
            (case["unidade"], case["contrato"], old_badge))
        if len(old_records) != 1:
            raise RuntimeError("Registro anterior do crachá não localizado.")
        if old_records[0]["SITUACAOCRACHA"] == "01" and old_records[0]["DATAHORATERMINO"] is None:
            self._save_badge(registration, case, old_badge, "Cancelado")
            latest = self.origin.query(
                "SELECT TOP 1 SITUACAOCRACHA,DATAHORATERMINO FROM RHREGCRACHAS "
                "WHERE UNIDADE=? AND CONTRATO=? AND NROCRACHA=? ORDER BY DATAHORAINICIO DESC",
                (case["unidade"], case["contrato"], old_badge))
            if len(latest) != 1 or latest[0]["SITUACAOCRACHA"] == "01":
                raise RuntimeError("Crachá anterior continua Ativo na origem.")
            self.diary.event("Conferir cancelamento do crachá anterior na origem", "PASSOU",
                             case=case["contrato"], expected=old_badge, observed=latest[0])
            last_time = self.origin.scalar(
                "SELECT MAX(DATAHORAINICIO) FROM RHREGCRACHAS WHERE UNIDADE=? AND CONTRATO=?",
                (case["unidade"], case["contrato"]))
            if datetime.now().replace(second=0, microsecond=0) <= last_time:
                self.diary.event("Aguardar horário do próximo registro", "ANTES",
                                 case=case["contrato"], expected=str(last_time + timedelta(minutes=1)))
                deadline = time.monotonic() + 90
                while datetime.now().replace(second=0, microsecond=0) <= last_time:
                    if time.monotonic() >= deadline:
                        raise RuntimeError("Horário do próximo registro não avançou em 90 segundos.")
                    time.sleep(1)
            form.set_focus()
            form.type_keys("^r")
            registration = self._window("TFrm_RH0940")
        self._save_badge(registration, case, case["novo_cracha"], "Ativo")
        deadline = time.monotonic() + 12
        while time.monotonic() < deadline:
            source = self._source(case)
            records = self._source_badge_record(case)
            if source == case["novo_cracha"] and len(records) == 1:
                situation_code = records[0]["SITUACAOCRACHA"]
                if situation_code != "01" or records[0]["DATAHORATERMINO"] is not None:
                    raise RuntimeError(f"Situação gravada diverge de Ativo: {situation_code!r}.")
                self.diary.event("Confirmar gravação na origem SQL", "PASSOU", case=case["contrato"],
                                 expected={"cracha": case["novo_cracha"], "situacao": "01"},
                                 observed={"cracha": source, "registro": records[0]})
                return
            time.sleep(0.5)
        raise RuntimeError("Origem RHCONTRATOS.CRACHA não recebeu o novo valor.")

    def _service(self):
        import win32service
        import win32serviceutil

        state = win32serviceutil.QueryServiceStatus(SERVICE)[1]
        if state == win32service.SERVICE_RUNNING:
            self.diary.event("Serviço Acessus - Importação API", "JA_EXECUTANDO",
                             observed=SERVICE)
        elif state == win32service.SERVICE_STOPPED:
            win32serviceutil.StartService(SERVICE)
            self.diary.event("Iniciar serviço Acessus - Importação API", "SOLICITADO",
                             observed=SERVICE)
        else:
            raise RuntimeError(f"Serviço em estado inesperado: {state}.")
        deadline = time.monotonic() + 25
        while time.monotonic() < deadline:
            if win32serviceutil.QueryServiceStatus(SERVICE)[1] == win32service.SERVICE_RUNNING:
                self.diary.state["servico"] = "EXECUTANDO"
                self.diary.save()
                return
            time.sleep(0.5)
        raise RuntimeError("Serviço não alcançou estado Running.")

    def _observe(self, position):
        deadline = time.monotonic() + self.plan.get("timeout_segundos", 240)
        cycles = 0
        latest = []
        while time.monotonic() < deadline:
            if LOG.stat().st_size < position:
                position = 0
            with LOG.open("rb") as stream:
                stream.seek(position)
                chunk = stream.read()
                position = stream.tell()
            cycles += chunk.count(b"Finalizou GetContratos com sucesso")
            latest = []
            for case in self.plan["casos"]:
                result = classify(case, self._source(case), self._api(case), self._target(case))
                latest.append(result)
                self.diary.event("Conferir origem, API e destino", result["status"],
                                 case=case["contrato"], expected=case["novo_cracha"], observed=result)
            if cycles >= 1 and all(result["status"] == "IMPORTADO_EXATO" for result in latest):
                break
            time.sleep(10)
        for entry, result in zip(self.diary.state["casos"], latest):
            entry.update(result)
        self.diary.state["ciclos_get_contratos"] = cycles
        self.diary.state["status"] = ("PASSOU" if cycles >= 1 and all(
            result["status"] == "IMPORTADO_EXATO" for result in latest) else "FALHOU")
        self.diary.save()

    def run(self):
        try:
            self.preflight()
            self.diary.state["status"] = "CADASTRANDO"
            self.diary.save()
            for case in self.plan["casos"]:
                if self._source(case) == case["novo_cracha"]:
                    self.diary.event("Cadastro já validado na origem", "PASSOU",
                                     case=case["contrato"], observed=case["novo_cracha"])
                else:
                    self._register(case)
            position = LOG.stat().st_size
            self._service()
            self.diary.state["status"] = "OBSERVANDO"
            self.diary.save()
            self._observe(position)
        except Exception as exc:
            self.diary.state["status"] = "ERRO_EXECUCAO"
            self.diary.state["erro"] = f"{type(exc).__name__}: {exc}"
            self.diary.event("Interromper execução", "ERRO_EXECUCAO", observed=self.diary.state["erro"])
            self.diary.save()
            raise
        return self.diary.state


def main(argv=None):
    parser = argparse.ArgumentParser(description="Cadastra crachás no Frequência e confere API/Acessus.")
    parser.add_argument("--arquivo", type=Path, required=True)
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args(argv)
    plan = validate_plan(json.loads(args.arquivo.read_text(encoding="utf-8-sig")))
    with observer_lock(ROOT / "reports/controle-executor", label="teste de importação de crachás"):
        result = BadgeRunner(plan, args.saida).run()
    print(json.dumps({"status": result["status"], "casos": result["casos"],
                      "ciclos_get_contratos": result.get("ciclos_get_contratos", 0)},
                     ensure_ascii=False, default=str))
    return 0 if result["status"] == "PASSOU" else 1


if __name__ == "__main__":
    raise SystemExit(main())
