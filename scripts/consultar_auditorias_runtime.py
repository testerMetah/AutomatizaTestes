"""Consulta e conta cada histórico aberto, em intervalo curto e sem escrita.

Os resultados são evidência exploratória. Regras de negócio e filtros específicos
precisam de casos confirmados antes de virar asserções de regressão.
"""

import json
import re
import sys
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from pywinauto import Desktop

from automatiza.config import Settings
from automatiza.database import SqlServer

from levantar_auditorias_runtime import ROOT, click_tab, tabs


PROGRAMS = {
    "acesso": "Acessus",
    "refeitorio": "Acessus.Refeitorio",
    "portaria": "Acessus.Portaria",
    "estacionamento": "Acessus.Estacionamento",
    "escola": "Acessus.Escola",
    "administracao": "Acessus.Administracao",
}


def dialogs(pid, *, dismiss):
    found = []
    for _ in range(8):
        windows = [w for w in Desktop(backend="win32").windows(process=pid)
                   if w.class_name() == "#32770" and w.is_visible()]
        if not windows:
            break
        for window in windows:
            uia = Desktop(backend="uia").window(handle=window.handle)
            messages = [c.window_text() for c in uia.descendants(control_type="Text") if c.window_text()]
            found.append({"titulo": window.window_text(), "mensagens": messages})
            if dismiss:
                buttons = [c for c in window.descendants()
                           if c.class_name() == "Button" and c.window_text() == "OK"]
                if len(buttons) == 1:
                    buttons[0].click()
                else:
                    raise RuntimeError("Diálogo inesperado sem botão OK único")
        if not dismiss:
            break
    return found


def last_sql(db, program):
    rows = db.query(
        "SELECT s.session_id, DB_NAME(s.database_id) AS banco, t.text AS sql "
        "FROM sys.dm_exec_sessions s "
        "JOIN sys.dm_exec_connections c ON c.session_id=s.session_id "
        "CROSS APPLY sys.dm_exec_sql_text(c.most_recent_sql_handle) t "
        "WHERE s.host_name=HOST_NAME() AND s.program_name=?",
        (program,),
    )
    if len(rows) != 1:
        raise RuntimeError(f"Sessão SQL de {program}: encontradas {len(rows)}")
    if rows[0]["banco"].casefold() != "acessofagundes":
        raise RuntimeError("Módulo conectado a banco diferente de AcessoFagundes")
    return rows[0]["sql"]


def run(pid, module):
    if module not in PROGRAMS:
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
        raise RuntimeError("Janela Auditorias/Históricos não encontrada de forma única")
    form = forms[0]
    output = ROOT / "resultados" / f"auditorias-consultas-{datetime.now():%Y%m%d-%H%M%S}" / module
    output.mkdir(parents=True, exist_ok=False)
    results = {"modulo": module, "periodo": "21/10/2026 09:30 a 09:33",
               "banco": "desk-tec/AcessoFagundes", "historicos": []}
    originals = tabs(form.handle, upper=True) or [None]
    for index, original in enumerate(originals):
        entry = {"historico": original.window_text() if original is not None else form.window_text()}
        results["historicos"].append(entry)
        try:
            dialogs(pid, dismiss=True)
            form.set_focus()
            if original is not None:
                click_tab(tabs(form.handle, upper=True)[index])
            period = [item for item in tabs(form.handle, upper=False)
                      if item.window_text().startswith("Per")]
            if len(period) != 1:
                raise RuntimeError(f"Filtro Período: encontrados {len(period)}")
            click_tab(period[0])
            edits = sorted([c for c in form.descendants()
                            if c.class_name() == "TMaskEdit" and c.is_visible()],
                           key=lambda c: c.rectangle().left)
            if len(edits) != 4:
                raise RuntimeError(f"Período: esperados 4 campos, encontrados {len(edits)}")
            for control, value in zip(edits, ("21/10/2026", "09:30", "21/10/2026", "09:33")):
                control.set_edit_text(value)
            form.set_focus()
            consult = [c for c in form.descendants()
                       if c.class_name() == "THoverSpeedButton"
                       and c.window_text().startswith("Consultar")]
            if len(consult) != 1:
                raise RuntimeError("Botão Consultar não encontrado de forma única")
            consult[0].click()
            entry["sql"] = last_sql(db, PROGRAMS[module])
            entry["dialogos_consulta"] = dialogs(pid, dismiss=True)
            count = [c for c in form.descendants()
                     if c.class_name() == "THoverSpeedButton"
                     and c.window_text().startswith("Contar Registros")]
            if len(count) != 1:
                raise RuntimeError("Botão Contar Registros não encontrado de forma única")
            count[0].click()
            entry["dialogos_contagem"] = dialogs(pid, dismiss=True)
            counts = [int(m.group(1)) for dialog in entry["dialogos_contagem"]
                      for message in dialog["mensagens"]
                      if (m := re.search(r"Possui\s+(\d+)\s+registros?", message))]
            entry["contagem_tela"] = counts[-1] if counts else None
            form.set_focus()
            form.capture_as_image().save(output / f"historico-{index+1:02d}.png")
            entry["status"] = "CONSULTADO" if counts else "SEM_CONTAGEM"
        except Exception as exc:
            entry["status"] = "FALHA"
            entry["erro"] = f"{type(exc).__name__}: {exc}"
            try:
                form.set_focus()
                form.capture_as_image().save(output / f"falha-{index+1:02d}.png")
            except Exception:
                pass
            dialogs(pid, dismiss=True)
    (output / "resultado.json").write_text(json.dumps(results, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    summary = {"saida": str(output), "consultados": sum(x["status"] == "CONSULTADO" for x in results["historicos"]),
               "falhas": [{"historico": x["historico"], "erro": x.get("erro")}
                           for x in results["historicos"] if x["status"] == "FALHA"]}
    print(json.dumps(summary, ensure_ascii=False))
    return 1 if summary["falhas"] else 0


if __name__ == "__main__":
    raise SystemExit(run(int(sys.argv[1]), sys.argv[2]))
