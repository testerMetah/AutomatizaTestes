"""Executa dez consultas por campo de filtro, sem alterar o banco.

Uso: python scripts/testar_filtros_auditorias.py <pid> <modulo>
Cada tentativa é gravada imediatamente em JSONL para preservar evidência.
"""

import json
import re
import sys
from dataclasses import replace
from datetime import datetime, timedelta
from pathlib import Path

from pywinauto import Desktop
from pywinauto.timings import TimeoutError as WaitTimeoutError, wait_until

from automatiza.config import Settings
from automatiza.database import SqlServer
from consultar_auditorias_runtime import PROGRAMS, dialogs
from levantar_auditorias_runtime import ROOT, click_tab, tabs


TABLES = {
    "acesso": [("HISTORICO_ACESSO_RAPIDO_REG", "data_hora_operacao"),
               ("HISTORICO_CREDENCIAIS", "data_hora_registro"),
               ("HISTORICO_FILA_COMANDOS", "data_hora_registro"),
               ("HISTORICO_METAH_FILTROS", "data_hora"),
               ("HISTORICO_PESSOAS", "data_hora"),
               ("HISTORICO_PRE_CADASTROS", "data_hora"),
               ("HISTORICO_REGRAS_ACESSO", "data_hora")],
    "refeitorio": [("HISTORICO_CARDAPIOS", "data_hora_operacao"),
                   ("HISTORICO_FILA_COMANDOS", "data_hora_registro"),
                   ("HISTORICO_REFEICOES", "data_hora_operacao"),
                   ("HISTORICO_REFEICOES_RESERVAS", "data_hora_operacao"),
                   ("HISTORICO_REFEITORIOS", "data_hora_operacao"),
                   ("HISTORICO_REGRAS_ACESSO", "data_hora")],
    "portaria": [("VisitantesTerceirosHistoricosReg", "data_criacao")],
    "estacionamento": [("HISTORICO_FILA_COMANDOS", "data_hora_registro"),
                        ("HISTORICO_REGRAS_ACESSO", "data_hora"),
                        ("HISTORICO_VEICULOS", "data_hora")],
    "escola": [("HISTORICO_ALUNOS", "data_hora"),
               ("HISTORICO_CREDENCIAIS", "data_hora_registro"),
               ("HISTORICO_FILA_COMANDOS", "data_hora_registro"),
               ("HISTORICO_REGRAS_ACESSO", "data_hora"),
               ("HISTORICO_RESPONSAVEIS", "data_hora"),
               ("HISTORICO_TURMAS", "data_hora"),
               ("HISTORICO_TURNOS", "data_hora")],
    "administracao": [("HISTORICO_USUARIOS", "data_hora_operacao"),
                       ("HISTORICO_ACESSUSSYNC_AGENDAMENTOS", "data_hora"),
                       ("HISTORICO_ACESSUSSYNC_TAREFAS", "data_hora")],
}

FILTER_COLS = {
    "pessoa": "id_pessoa", "pré-cadastro": "id_precadastro",
    "usuário": "id_usuario", "crachá": "codigo",
    "coletor": "id_coletor", "refeitório": "id_refeitorio",
    "cardápio": "id_cardapio", "aluno": "id_aluno",
    "turma": "id_turma", "turno": "id_turno",
    "responsável": "id_responsavel", "veículo": "id_veiculo",
    "filtro": "id_filtro", "unidade": "id_unidade", "setor": "id_setor",
    "visitante": "id_visitante",
}


def normalized(value):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFKD", value.casefold())
                   if not unicodedata.combining(c))


def date_for(db, table, column):
    # Escolhe minuto com até dez linhas para não travar o grid Delphi.
    rows = db.query(
        f"SELECT TOP (1) CONVERT(varchar(16), [{column}], 120) AS minuto "
        f"FROM [{table}] WHERE [{column}] >= '2020-01-01' AND [{column}] < '2030-01-01' "
        f"GROUP BY CONVERT(varchar(16), [{column}], 120) "
        f"HAVING COUNT(*) BETWEEN 1 AND 10 ORDER BY minuto DESC")
    return datetime.strptime(rows[0]["minuto"], "%Y-%m-%d %H:%M") if rows else datetime(2026, 10, 21, 9, 30)


def sample_values(db, table, column, datecol, moment):
    columns = {r["name"].casefold() for r in db.query(
        "SELECT name FROM sys.columns WHERE object_id=OBJECT_ID(?)", (table,))}
    if column.casefold() not in columns:
        return []
    rows = db.query(
        f"SELECT DISTINCT TOP (5) CONVERT(varchar(80), [{column}]) AS valor "
        f"FROM [{table}] WHERE [{column}] IS NOT NULL "
        f"AND [{datecol}] >= ? AND [{datecol}] < ? ORDER BY valor DESC",
        (moment, moment + timedelta(minutes=1)))
    return [r["valor"] for r in rows if r["valor"]]


def period_values(moment, case=0):
    # Todos os intervalos abrangem no máximo três minutos.
    offsets = ((0, 0), (-1, -1), (1, 1), (-1, 0), (0, 1),
               (-2, 0), (0, 2), (-2, -1), (1, 2), (1, 0))
    first, last = offsets[case]
    begin = moment + timedelta(minutes=first)
    finish = moment + timedelta(minutes=last)
    return (begin.strftime("%d/%m/%Y"), begin.strftime("%H:%M"),
            finish.strftime("%d/%m/%Y"), finish.strftime("%H:%M"))


def set_period(form, moment, case=0):
    period = [t for t in tabs(form.handle, upper=False)
              if normalized(t.window_text()).startswith("periodo")]
    if len(period) != 1:
        raise RuntimeError("Aba Período não encontrada de forma única")
    click_tab(period[0])
    wait_until(5, 0.1, lambda: any(c.class_name() == "TTabSheet" and c.is_visible()
                                    and normalized(c.window_text()).startswith("periodo")
                                    for c in form.descendants()))
    wait_until(5, 0.1, lambda: len([c for c in form.descendants()
                                    if c.class_name() == "TMaskEdit" and c.is_visible()]) == 4)
    edits = sorted([c for c in form.descendants()
                    if c.class_name() == "TMaskEdit" and c.is_visible()],
                   key=lambda c: c.rectangle().left)
    if len(edits) != 4:
        raise RuntimeError(f"Período contém {len(edits)} campos; esperados 4")
    values = period_values(moment, case)
    for control, value in zip(edits, values):
        control.set_edit_text(value)
    return values


def filter_column(label, subindex, module=None):
    key = normalized(label.split(" (")[0]).replace("s/", "").rstrip("s")
    if module == "portaria":
        for name, column in {"visitante": "id_visitantes", "cracha": "nr_cracha",
                             "coletor": "coletor", "usuario": "usuario",
                             "refeitorio": "refeitorio", "cardapio": "cardapio"}.items():
            if name in key:
                return column
    if key.startswith("coletor/funcao"):
        return "id_coletor" if subindex == 0 else "id_funcao"
    for name, column in FILTER_COLS.items():
        if normalized(name) in key:
            return column
    return None


def controls_on_page(form):
    visible = [c for c in form.descendants()
               if c.class_name() == "TTabSheet" and c.is_visible()
               and c.rectangle().top > form.rectangle().top + form.rectangle().height() // 2]
    if len(visible) != 1:
        raise RuntimeError(f"Aba de filtro visível: {len(visible)}")
    return [c for c in visible[0].descendants()
            if c.class_name() in ("TEdit", "TComboBox") and c.is_visible()]


def select_history(form, index, label):
    def selected():
        return any(c.class_name() == "TTabSheet" and c.is_visible()
                   and c.window_text() == label
                   and c.rectangle().top < form.rectangle().top + form.rectangle().height() // 2
                   for c in form.descendants())

    if selected():
        return
    for _ in range(3):
        form.set_focus()
        click_tab(tabs(form.handle, upper=True)[index])
        try:
            wait_until(3, 0.1, selected)
            return
        except WaitTimeoutError:
            continue
    raise RuntimeError(f"Histórico {label!r} não ficou visível")


def button(form, prefix):
    found = [c for c in form.descendants() if c.class_name() == "THoverSpeedButton"
             and normalized(c.window_text()).startswith(normalized(prefix))]
    if len(found) != 1:
        raise RuntimeError(f"Botão {prefix}: encontrados {len(found)}")
    return found[0]


def count_from(messages):
    for dialog in messages:
        for message in dialog["mensagens"]:
            match = re.search(r"Possui\s+(\d+)\s+registros?", message)
            if match:
                return int(match.group(1))
    return None


def application_error(messages):
    return any(any(marker in message for marker in ("[FireDAC]", "[ODBC]", "Exception", "Exceção", "Access violation"))
               for dialog in messages for message in dialog["mensagens"])


def execute(form, pid, moment, label, subindex, value, case):
    dialogs(pid, dismiss=True)
    form.set_focus()
    button(form, "Limpar Filtros").click()
    before = dialogs(pid, dismiss=True)
    period = set_period(form, moment, case if label == "Período" else 0)
    entered = None
    if label != "Período":
        lower = tabs(form.handle, upper=False)
        selected = [t for t in lower if t.window_text() == label]
        if len(selected) != 1:
            raise RuntimeError(f"Filtro {label}: encontrados {len(selected)}")
        click_tab(selected[0])
        wait_until(5, 0.1, lambda: any(c.class_name() == "TTabSheet" and c.is_visible()
                                        and c.window_text() == label
                                        for c in form.descendants()))
        controls = controls_on_page(form)
        control = controls[subindex]
        if control.class_name() == "TEdit":
            control.set_edit_text(value)
        else:
            options = control.item_texts()
            control.select(value)
            value = options[value]
        entered = control.window_text()
    form.set_focus()
    button(form, "Consultar").click()
    consult_messages = dialogs(pid, dismiss=True)
    button(form, "Contar Registros").click()
    count_messages = dialogs(pid, dismiss=True)
    return {"periodo": period, "valor_entrada": value, "valor_exibido": entered,
            "mensagens_limpeza": before, "mensagens_consulta": consult_messages,
            "mensagens_contagem": count_messages,
            "contagem": count_from(count_messages)}


def run(pid, module, skip=()):
    if module not in TABLES:
        raise ValueError("Módulo desconhecido")
    db = SqlServer(replace(Settings.load(), sql_database="acessofagundes"))
    db.assert_database()
    main = [w for w in Desktop(backend="win32").windows(process=pid)
            if w.class_name().endswith("Principal") and w.is_visible()]
    if len(main) != 1:
        raise RuntimeError("Janela principal não encontrada de forma única")
    forms = [c for c in main[0].descendants()
             if "AuditoriaHistorico" in c.class_name() and c.is_visible()]
    if len(forms) != 1:
        raise RuntimeError("Auditorias/Históricos não encontrada de forma única")
    form = forms[0]
    output = ROOT / "resultados" / f"auditorias-filtros-{datetime.now():%Y%m%d-%H%M%S}" / module
    output.mkdir(parents=True, exist_ok=False)
    path = output / "tentativas.jsonl"
    histories = tabs(form.handle, upper=True) or [None]
    for history_index, history in enumerate(histories):
        if history_index in skip:
            continue
        form.set_focus()
        if history is not None:
            select_history(form, history_index, history.window_text())
        history_name = history.window_text() if history is not None else form.window_text()
        table, datecol = TABLES[module][history_index]
        moment = date_for(db, table, datecol)
        filters = tabs(form.handle, upper=False)
        for filter_index, filter_item in enumerate(filters):
            label = filter_item.window_text()
            form.set_focus()
            click_tab(tabs(form.handle, upper=False)[filter_index])
            if normalized(label).startswith("periodo"):
                fields = [("Período", 0, "TMaskEdit", [])]
            else:
                fields = []
                for subindex, control in enumerate(controls_on_page(form)):
                    column = filter_column(label, subindex, module)
                    samples = sample_values(db, table, column, datecol, moment) if column else []
                    fields.append((label, subindex, control.class_name(), samples))
            for field_label, subindex, kind, samples in fields:
                if kind == "TComboBox":
                    opts = controls_on_page(form)[subindex].item_texts()
                    values = [i % len(opts) for i in range(10)]
                elif kind == "TMaskEdit":
                    values = [None] * 10
                else:
                    values = (samples + ["", "0", "1", "999999999", "-1", "abc", "áç", "  ", "0001", "999999"])[0:10]
                for case, value in enumerate(values):
                    record = {"modulo": module, "historico": history_name,
                              "tabela_referencia": table, "coluna_data": datecol,
                              "data_referencia": moment.isoformat(), "filtro": field_label,
                              "subcampo": subindex, "tipo": kind, "tentativa": case + 1,
                              "amostra_banco": value in samples if isinstance(value, str) else False,
                              "iniciado_em": datetime.now().isoformat()}
                    try:
                        record.update(execute(form, pid, moment, field_label, subindex, value, case))
                        if application_error(record["mensagens_consulta"]):
                            record["status"] = "ERRO_APLICACAO"
                        else:
                            record["status"] = "CONSULTADO" if record["contagem"] is not None else "SEM_CONTAGEM"
                    except Exception as exc:
                        record["status"] = "ERRO"
                        record["erro"] = f"{type(exc).__name__}: {exc}"
                        try:
                            form.capture_as_image().save(output / f"erro-{history_index+1:02d}-{filter_index+1:02d}-{subindex}-{case+1:02d}.png")
                            dialogs(pid, dismiss=True)
                        except Exception:
                            pass
                    with path.open("a", encoding="utf-8") as stream:
                        stream.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
                    print(json.dumps({k: record.get(k) for k in ("historico", "filtro", "subcampo", "tentativa", "status", "contagem", "erro")}, ensure_ascii=False), flush=True)
    print(json.dumps({"saida": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    run(int(sys.argv[1]), sys.argv[2], {int(value) for value in sys.argv[3:]})
