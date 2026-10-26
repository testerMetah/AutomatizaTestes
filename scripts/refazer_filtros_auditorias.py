"""Reexecuta filtros pontuais com dez valores e guarda mensagens completas."""

import json
import sys
from dataclasses import replace
from datetime import datetime, timedelta

from pywinauto import Desktop

from automatiza.config import Settings
from automatiza.database import SqlServer
from levantar_auditorias_runtime import ROOT, tabs
from testar_filtros_auditorias import (TABLES, application_error, date_for, execute,
                                       filter_column, sample_values, select_history)


TARGETS = {
    "acesso-cracha": ("acesso", 5708, 1, "Crachá", 0),
    "acesso-credenciais-usuario": ("acesso", 5708, 1, "Usuário", 0),
    "acesso-fila-usuario": ("acesso", 5708, 2, "Usuário", 0),
    "estacionamento-veiculos-precadastro": ("estacionamento", 1472, 2, "Pré-Cadastro", 0),
    "escola-regras-pessoa": ("escola", 8432, 3, "Pessoa", 0),
}


def run(target):
    module, pid, history_index, prefix, subindex = TARGETS[target]
    db = SqlServer(replace(Settings.load(), sql_database="acessofagundes"))
    db.assert_database()
    main = [w for w in Desktop(backend="win32").windows(process=pid)
            if w.class_name().endswith("Principal") and w.is_visible()]
    if len(main) != 1:
        raise RuntimeError(f"Módulo {module} não está aberto")
    forms = [c for c in main[0].descendants()
             if "AuditoriaHistorico" in c.class_name() and c.is_visible()]
    if len(forms) != 1:
        raise RuntimeError("Janela de auditoria não está aberta")
    form = forms[0]
    histories = tabs(form.handle, upper=True)
    history = histories[history_index].window_text()
    select_history(form, history_index, history)
    stem = prefix[:2] if prefix.startswith("Pré") else prefix[:3]
    filters = [t.window_text() for t in tabs(form.handle, upper=False)
               if t.window_text().startswith(stem)]
    if len(filters) != 1:
        raise RuntimeError(f"Filtro {prefix}: encontrados {len(filters)}")
    label = filters[0]
    table, datecol = TABLES[module][history_index]
    moment = date_for(db, table, datecol)
    column = filter_column(label, subindex, module)
    samples = sample_values(db, table, column, datecol, moment) if column else []
    if target == "acesso-cracha":
        code = samples[0]
        values = [code, code, code, code[:-1], "0", "", "999999999", "abc", "  ", "0001"]
    else:
        values = (samples + ["", "0", "1", "999999999", "-1", "abc", "áç", "  ", "0001", "999999"])[0:10]
    output = ROOT / "resultados" / f"auditorias-filtros-{datetime.now():%Y%m%d-%H%M%S}" / module
    output.mkdir(parents=True)
    path = output / "tentativas.jsonl"
    for case, value in enumerate(values):
        record = {"modulo": module, "historico": history, "filtro": label,
                  "subcampo": subindex, "tipo": "TEdit", "tentativa": case + 1,
                  "tabela_referencia": table, "coluna_data": datecol,
                  "data_referencia": moment.isoformat(), "amostra_banco": value in samples,
                  "iniciado_em": datetime.now().isoformat()}
        try:
            record.update(execute(form, pid, moment, label, subindex, value, case))
            record["status"] = ("ERRO_APLICACAO" if application_error(record["mensagens_consulta"])
                                else "CONSULTADO" if record["contagem"] is not None else "SEM_CONTAGEM")
        except Exception as exc:
            record["status"] = "ERRO"
            record["erro"] = f"{type(exc).__name__}: {exc}"
            try:
                form.capture_as_image().save(output / f"falha-{case+1:02d}.png")
            except Exception:
                pass
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
        print(json.dumps({"target": target, "tentativa": case + 1,
                          "valor": value, "status": record["status"],
                          "contagem": record.get("contagem"), "erro": record.get("erro")},
                         ensure_ascii=False), flush=True)
    print(json.dumps({"saida": str(path)}, ensure_ascii=False))


if __name__ == "__main__":
    run(sys.argv[1])
