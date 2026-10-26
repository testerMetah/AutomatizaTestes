"""Cinco variações por campo; diário cronológico gravado após cada ação.

Uso: python scripts/testar_auditorias_cronologico.py PID MODULO PASTA_SAIDA [INDICES_PULAR...]
Somente consulta a interface e o banco de teste para escolher amostras.
"""

import json
import os
import sys
import traceback
import win32api
import win32con
import win32process
from dataclasses import replace
from datetime import datetime, timedelta
from pathlib import Path

from pywinauto import Desktop
from pywinauto.timings import TimeoutError as WaitTimeoutError, wait_until

from automatiza.config import Settings
from automatiza.database import SqlServer
from automatiza.diario_auditorias import DiarioAuditorias
from levantar_auditorias_runtime import click_tab, tabs
from testar_filtros_auditorias import (TABLES, application_error, button,
                                       controls_on_page, count_from, date_for,
                                       filter_column, period_values,
                                       sample_values, select_history)


def executavel_e_versao(pid):
    handle = win32api.OpenProcess(
        win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
    try:
        caminho = win32process.GetModuleFileNameEx(handle, 0)
    finally:
        handle.Close()
    info = win32api.GetFileVersionInfo(caminho, "\\")
    maior, menor = divmod(info["FileVersionMS"], 65536)
    compilacao, revisao = divmod(info["FileVersionLS"], 65536)
    return caminho, f"{maior}.{menor}.{compilacao}.{revisao}"


def dialogs(pid, emit, screenshot_dir=None):
    found = []
    for _ in range(8):
        windows = [w for w in Desktop(backend="win32").windows(process=pid)
                   if w.class_name() == "#32770" and w.is_visible()]
        if not windows:
            break
        for window in windows:
            uia = Desktop(backend="uia").window(handle=window.handle)
            messages = [c.window_text() for c in uia.descendants(control_type="Text")
                        if c.window_text()]
            dialog = {"titulo": window.window_text(), "mensagens": messages}
            found.append(dialog)
            for message in messages:
                emit(f"Exibiu mensagem/aviso/erro: {message}")
            if not messages:
                emit(f"Exibiu diálogo: {window.window_text()} (sem texto detectável)")
            # A caixa precisa aparecer na evidência. Capturar antes de fechá-la;
            # a imagem do formulário após o OK mostrava apenas a janela de fundo.
            if screenshot_dir is not None and application_error([dialog]):
                name = f"erro-dialogo-{datetime.now():%Y%m%d-%H%M%S-%f}.png"
                path = screenshot_dir / name
                try:
                    window.capture_as_image().save(path)
                    dialog["screenshot"] = str(path)
                    emit(f"Salvou screenshot da caixa de erro ainda aberta: {path}")
                except Exception as capture_error:
                    emit(f"Falha ao salvar screenshot da caixa de erro: "
                         f"{type(capture_error).__name__}: {capture_error}")
            buttons = [c for c in window.descendants()
                       if c.class_name() == "Button" and c.window_text() == "OK"]
            if len(buttons) != 1:
                raise RuntimeError("Diálogo sem botão OK único")
            buttons[0].click()
            emit("Clicou em: OK (fechou o diálogo)")
    return found


def visible_sheet(form, name):
    return any(c.class_name() == "TTabSheet" and c.is_visible()
               and c.window_text() == name for c in form.descendants())


def choose_lower(form, label, emit, pid=None, screenshot_dir=None):
    if pid is not None:
        dialogs(pid, emit, screenshot_dir)
    if visible_sheet(form, label):
        return
    for _ in range(3):
        form.set_focus()
        items = [t for t in tabs(form.handle, upper=False) if t.window_text() == label]
        if len(items) != 1:
            raise RuntimeError(f"Aba {label}: encontradas {len(items)}")
        click_tab(items[0])
        emit(f"Clicou na aba: {label}")
        try:
            wait_until(3, 0.1, lambda: visible_sheet(form, label))
            return
        except WaitTimeoutError:
            emit(f"Aba {label} não ficou visível; repetirá o clique")
            if pid is not None:
                dialogs(pid, emit, screenshot_dir)
    raise RuntimeError(f"Aba {label} não ficou visível após três cliques")


def set_period(form, moment, variant, emit, pid, extreme=False, screenshot_dir=None):
    periods = [t.window_text() for t in tabs(form.handle, upper=False)
               if t.window_text().startswith("Per")]
    if len(periods) != 1:
        raise RuntimeError("Aba Período não localizada")
    choose_lower(form, periods[0], emit, pid, screenshot_dir)
    edits = sorted([c for c in form.descendants()
                    if c.class_name() == "TMaskEdit" and c.is_visible()],
                   key=lambda c: c.rectangle().left)
    if len(edits) != 4:
        raise RuntimeError(f"Período: {len(edits)} campos visíveis")
    values = extreme_periods(moment, variant) if extreme else period_values(moment, variant)
    names = ("Data inicial", "Hora inicial", "Data final", "Hora final")
    for edit, name, value in zip(edits, names, values):
        edit.set_edit_text(value)
        emit(f"Campo {name} preencheu com: {value}")
    return values


def unique_values(samples):
    result = []
    for value in samples[:2] + ["", "0", "1", "999999999", "abc", "-1", "0001"]:
        if value not in result:
            result.append(value)
        if len(result) == 5:
            return result
    return result


def extreme_values():
    """Cinco classes de entrada que não dependem do conteúdo do banco."""
    return ["-1", "0000000001", "áç漢字", "' OR 1=1 --", "9" * 256]


def extreme_periods(moment, variant):
    next_minute = moment + timedelta(minutes=1)
    previous_minute = moment - timedelta(minutes=1)
    cases = [
        # Início maior que fim, ambos perto de um registro real.
        (next_minute.strftime("%d/%m/%Y"), next_minute.strftime("%H:%M"),
         previous_minute.strftime("%d/%m/%Y"), previous_minute.strftime("%H:%M")),
        ("01/01/1900", "00:00", "01/01/1900", "00:00"),
        ("31/12/2099", "23:59", "31/12/2099", "23:59"),
        ("29/02/2024", "00:00", "29/02/2024", "00:00"),
        ("31/12/2025", "23:59", "01/01/2026", "00:00"),
    ]
    return cases[variant]


def run(pid, module, output, skip):
    output.mkdir(parents=True, exist_ok=True)
    from automatiza.perfis_teste import configuracao
    settings = configuracao(os.environ.get("AUTOMATIZA_PERFIL", "auditorias"))
    db = SqlServer(settings)
    banco_efetivo = db.assert_database()
    main = [w for w in Desktop(backend="win32").windows(process=pid)
            if w.class_name().endswith("Principal") and w.is_visible()]
    if len(main) != 1:
        raise RuntimeError(f"Janela principal de {module}: encontradas {len(main)}")
    forms = [c for c in main[0].descendants()
             if "AuditoriaHistorico" in c.class_name() and c.is_visible()]
    if len(forms) != 1:
        raise RuntimeError(f"Auditorias/Históricos de {module}: encontradas {len(forms)}")
    form = forms[0]
    only_filter = os.environ.get("AUDITORIA_ONLY_FILTER")
    extreme = os.environ.get("AUDITORIA_EXTREME") == "1"
    histories = tabs(form.handle, upper=True) or [None]
    datafile = output / "tentativas.jsonl"
    completed = set()
    if os.environ.get("AUDITORIA_RESUME") == "1" and datafile.exists():
        with datafile.open(encoding="utf-8") as previous:
            for line in previous:
                try:
                    old = json.loads(line)
                    if old.get("modulo") == module:
                        completed.add((old["indice_historico"], old["filtro"],
                                       old["subcampo"], old["tentativa"]))
                except (ValueError, KeyError, TypeError):
                    continue
    executavel, versao = executavel_e_versao(pid)
    pasta_resultados = Path(__file__).resolve().parents[1] / "resultados"
    contexto = {
        "modulo": module, "pid_aplicacao": pid, "pid_automacao": os.getpid(),
        "executavel": executavel, "versao_build": versao,
        "servidor_sql": settings.sql_server, "banco_sql_confirmado": banco_efetivo,
        "janela_principal": main[0].window_text(), "classe_janela_principal": main[0].class_name(),
        "janela_auditoria": form.window_text(), "classe_janela_auditoria": form.class_name(),
        "handle_janela_auditoria": form.handle,
        "modo_extremo": extreme, "filtro_restrito": only_filter,
        "perfil": os.environ.get("AUTOMATIZA_PERFIL", "auditorias"),
        "indices_historicos_pulados": sorted(skip),
        "pasta_evidencias": str(output.resolve()),
        "script": str(Path(__file__).resolve()), "python": sys.version.split()[0],
    }
    with DiarioAuditorias(pasta_resultados, contexto) as journal:
        journal.acao(module, "(execução)", "(início)",
                     f"Iniciou execução; evidências da rodada: {output}")
        for hidx, item in enumerate(histories):
            if hidx in skip:
                continue
            history = item.window_text() if item else form.window_text()
            emit_history = lambda action: journal.acao(module, history, "(seleção)", action)
            try:
                dialogs(pid, emit_history, output)
                if item is not None:
                    select_history(form, hidx, history)
                emit_history(f"Clicou na aba do histórico: {history}; aba visível confirmada")
                table, datecol = TABLES[module][hidx]
                moment = date_for(db, table, datecol)
                labels = [t.window_text() for t in tabs(form.handle, upper=False)]
            except Exception as exc:
                emit_history(f"ERRO ao abrir histórico: {type(exc).__name__}: {exc}")
                continue
            history_broken = False
            for label in labels:
                if history_broken:
                    break
                if only_filter and not label.startswith(only_filter):
                    continue
                field_name = "Período" if label.startswith("Per") else label
                emit = lambda action, field_name=field_name: journal.acao(
                    module, history, field_name, action)
                try:
                    choose_lower(form, label, emit, pid, output)
                    if label.startswith("Per"):
                        fields = [(0, "TMaskEdit", [None] * 5)]
                    else:
                        controls = controls_on_page(form)
                        expected = 2 if "Coletor/Fun" in label else 1
                        fields = []
                        for subindex, control in enumerate(controls[:expected]):
                            if control.class_name() == "TComboBox":
                                opts = control.item_texts()
                                values = list(range(min(5, len(opts))))
                                while len(values) < 5:
                                    values.append(len(values) % len(opts))
                            else:
                                column = filter_column(label, subindex, module)
                                samples = sample_values(db, table, column, datecol, moment) if column else []
                                values = extreme_values() if extreme else unique_values(samples)
                            fields.append((subindex, control.class_name(), values))
                        if len(fields) != expected:
                            raise RuntimeError(f"Esperados {expected} controles; encontrados {len(fields)}")
                except Exception as exc:
                    emit(f"ERRO ao preparar filtro: {type(exc).__name__}: {exc}")
                    continue
                for subindex, kind, values in fields:
                    for variant, value in enumerate(values):
                        if (hidx, field_name, subindex, variant + 1) in completed:
                            continue
                        started = datetime.now().astimezone().isoformat(timespec="milliseconds")
                        record = {"modulo": module, "historico": history, "filtro": field_name,
                                  "subcampo": subindex, "tentativa": variant + 1,
                                  "tipo": kind, "valor_planejado": value,
                                  "inicio": started, "indice_historico": hidx,
                                  "tabela_referencia": table, "coluna_data_referencia": datecol,
                                  "data_referencia": moment.isoformat()}
                        journal.iniciar_tentativa(record)
                        try:
                            emit(f"Iniciou tentativa {variant + 1}/5 no campo {subindex + 1}")
                            dialogs(pid, emit, output)
                            form.set_focus()
                            button(form, "Limpar Filtros").click()
                            emit("Clicou em: Limpar Filtros (Ctrl+X)")
                            dialogs(pid, emit, output)
                            period = set_period(form, moment, variant if kind == "TMaskEdit" else 0,
                                                emit, pid, extreme=extreme and kind == "TMaskEdit",
                                                screenshot_dir=output)
                            record["periodo"] = period
                            if kind != "TMaskEdit":
                                choose_lower(form, label, emit, pid, output)
                                control = controls_on_page(form)[subindex]
                                record["handle_controle"] = control.handle
                                rect = control.rectangle()
                                record["retangulo_controle"] = [
                                    rect.left, rect.top, rect.right, rect.bottom]
                                if kind == "TComboBox":
                                    control.select(value)
                                    entered = control.window_text()
                                else:
                                    control.set_edit_text(value)
                                    entered = control.window_text()
                                record["valor_exibido"] = entered
                                emit(f"Campo {field_name} (posição {subindex + 1}) preencheu com: {entered!r}")
                            form.set_focus()
                            button(form, "Consultar").click()
                            emit("Clicou em: Consultar (F6)")
                            consultation = dialogs(pid, emit, output)
                            record["mensagens_consulta"] = consultation
                            if not consultation:
                                emit("Consulta não exibiu mensagem/aviso/erro")
                            if application_error(consultation):
                                record["status"] = "ERRO_APLICACAO"
                                emit("Resultado: erro da aplicação; a contagem não é válida")
                                if any("Access violation" in msg for d in consultation
                                       for msg in d["mensagens"]):
                                    history_broken = True
                            else:
                                button(form, "Contar Registros").click()
                                emit("Clicou em: Contar Registros (F5)")
                                counted = dialogs(pid, emit, output)
                                record["mensagens_contagem"] = counted
                                record["contagem"] = count_from(counted)
                                record["status"] = "CONSULTADO" if record["contagem"] is not None else "SEM_CONTAGEM"
                                emit(f"Resultado da tentativa: {record['status']}; contagem: {record['contagem']}")
                                from automatiza.oraculos_auditorias import verificar
                                oracle = verificar(db, record)
                                if oracle is not None:
                                    record["oraculo_contagem"] = oracle
                                    emit(f"Oráculo de contagem: {oracle['status']}; "
                                         f"esperado {oracle['esperado']}, obtido {oracle['obtido']}")
                        except Exception as exc:
                            record["status"] = "ERRO_AUTOMACAO"
                            record["erro"] = f"{type(exc).__name__}: {exc}"
                            record["traceback"] = traceback.format_exc()
                            emit(f"ERRO da automação: {record['erro']}")
                            try:
                                path = output / f"falha-{module}-{hidx}-{subindex}-{variant+1}.png"
                                form.capture_as_image().save(path)
                                record["screenshot"] = str(path)
                                emit(f"Salvou screenshot da falha de automação: {path}")
                            except Exception as capture_error:
                                record["erro_screenshot"] = (
                                    f"{type(capture_error).__name__}: {capture_error}")
                        journal.finalizar_tentativa(record)
                        with datafile.open("a", encoding="utf-8") as data:
                            data.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
                            data.flush()
                            os.fsync(data.fileno())
                        if history_broken:
                            emit("Histórico interrompido após Access violation; demais filtros exigem reinicialização do módulo")
                            break
            emit_history(f"Concluiu histórico; bloqueado por exceção: {history_broken}")
            if history_broken and os.environ.get("AUDITORIA_STOP_ON_AV") == "1":
                journal.acao(module, history, "(supervisor)", "Access violation: solicitou reinício e retomada")
                return 75


if __name__ == "__main__":
    raise SystemExit(run(int(sys.argv[1]), sys.argv[2], Path(sys.argv[3]),
                         {int(s) for s in sys.argv[4:]}) or 0)
