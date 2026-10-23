from dataclasses import replace
import re

from automatiza.config import Settings
from automatiza.database import SqlServer


SELECT_ONLY = re.compile(r"^\s*SELECT\b", re.I)


def compare_fields(expected, actual):
    return [{"campo": k, "esperado": v, "obtido": actual.get(k), "igual": actual.get(k) == v}
            for k, v in expected.items()]


def check_database(report, *, server, database, sql, params=(), expected=None):
    if not SELECT_ONLY.match(sql) or ";" in sql or "--" in sql:
        raise ValueError("Checkpoint aceita apenas SELECT simples parametrizado")
    settings = replace(Settings.load(), sql_server=server, sql_database=database)
    db = SqlServer(settings)
    db.assert_database()
    rows = db.query(sql, params)
    comparison = compare_fields(expected, rows[0]) if expected is not None and len(rows) == 1 else None
    ok = comparison is None or all(x["igual"] for x in comparison)
    report.emit("BANCO", sql=sql, parametros=params, linhas=rows, esperado=expected, obtido=rows,
                comparacao=comparison, resultado="PASSOU" if ok else "FALHOU")
    if not ok: raise AssertionError(f"Banco: esperado {expected}; obtido {rows}")
    return rows


def check_screen(report, gateway, selector, expected):
    actual = gateway.read(selector)
    comparison = compare_fields({"valor": expected}, {"valor": actual})
    report.emit("TELA_VERIFICACAO", tela={"titulo": gateway.window.window_text(), "classe": gateway.window.class_name(), "menu": gateway.menu_path},
                controle=selector, esperado=expected, obtido=actual, comparacao=comparison,
                resultado="PASSOU" if comparison[0]["igual"] else "FALHOU")
    return comparison[0]["igual"]
