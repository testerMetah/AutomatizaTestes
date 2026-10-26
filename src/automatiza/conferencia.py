"""Consultas delimitadas e comparação local de afastamentos."""
import json
from dataclasses import replace
from datetime import datetime
from html import escape
from pathlib import Path

from automatiza.database import SqlServer, configured_database
from automatiza.observador import atomic_json, changes, normalize_snapshot, utc_now


def query_spec(spec):
    allowed = {"pessoas", "contrato", "causa", "inicio_de", "inicio_ate", "limite"}
    if not isinstance(spec, dict) or set(spec) - allowed:
        raise ValueError("Filtros desconhecidos. Use o modelo de consulta.")
    people = spec.get("pessoas", [])
    if not isinstance(people, list) or len(people) > 100 or any(type(p) is not int or p <= 0 for p in people):
        raise ValueError("Informe até 100 IdPessoa positivos.")
    limit = spec.get("limite", 1000)
    if type(limit) is not int or not 1 <= limit <= 10000:
        raise ValueError("Limite precisa estar entre 1 e 10000.")
    clauses, params = [], [limit + 1]
    if people:
        clauses.append("a.IdPessoa IN (" + ",".join("?" for _ in set(people)) + ")")
        params.extend(sorted(set(people)))
    if spec.get("contrato") is not None:
        if type(spec["contrato"]) is not int or spec["contrato"] <= 0:
            raise ValueError("Contrato precisa ser inteiro positivo.")
        clauses.append("p.ContratoExportacao = ?")
        params.append(spec["contrato"])
    if spec.get("causa") is not None:
        if not isinstance(spec["causa"], str) or not spec["causa"].strip():
            raise ValueError("Causa precisa ser texto não vazio.")
        clauses.append("a.Causa = ?")
        params.append(spec["causa"])
    dates = {}
    for key, operator in (("inicio_de", ">="), ("inicio_ate", "<")):
        if spec.get(key) is not None:
            dates[key] = datetime.fromisoformat(spec[key])
            if dates[key].tzinfo is not None:
                raise ValueError("Datas SQL devem ser locais, sem fuso.")
            clauses.append(f"a.DataInicio {operator} ?")
            params.append(dates[key])
    if len(dates) == 2 and dates["inicio_de"] >= dates["inicio_ate"]:
        raise ValueError("Intervalo de início vazio ou invertido.")
    if not clauses:
        raise ValueError("Informe pelo menos um filtro para limitar a consulta.")
    sql = ("SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; SELECT TOP (?) "
           "a.Id, a.IdPessoa, a.DataInicio, a.DataTermino, a.Causa, a.IdFreq "
           "FROM dbo.Afastamentos a JOIN dbo.Pessoas p ON p.id=a.IdPessoa WHERE "
           + " AND ".join(clauses) + " ORDER BY a.Id")
    return sql, tuple(params), limit


def capture(settings, spec, output, *, db=None):
    database = configured_database(settings)
    sql, params, limit = query_spec(spec)
    output = Path(output)
    if output.exists():
        raise ValueError("A amostra já existe; escolha outro nome para preservar o histórico.")
    db = db or SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
    db.assert_database()
    started = utc_now()
    rows = db.query(sql, params)
    if len(rows) > limit:
        raise ValueError("Limite excedido; refine os filtros. Nenhuma amostra truncada foi salva.")
    result = {"banco": database, "servidor": settings.sql_server, "filtros": spec,
              "inicio_consulta": started, "observado_em": utc_now(),
              "linhas": list(normalize_snapshot(rows).values())}
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise ValueError("A amostra já existe; escolha outro nome para preservar o histórico.")
    atomic_json(output, result)
    return result


def compare_files(before_file, after_file, output):
    before, after = [json.loads(Path(p).read_text(encoding="utf-8-sig")) for p in (before_file, after_file)]
    for key in ("banco", "servidor", "filtros"):
        if key not in before or before[key] != after.get(key):
            raise ValueError("Compare amostras da mesma origem e com filtros idênticos.")
    if datetime.fromisoformat(before["observado_em"]) > datetime.fromisoformat(after["observado_em"]):
        raise ValueError("A amostra anterior é posterior à final.")
    events = changes(normalize_snapshot(before["linhas"]), normalize_snapshot(after["linhas"]))
    totals = {kind: sum(e["tipo"] == kind for e in events) for kind in ("INCLUIDO", "REMOVIDO", "ALTERADO")}
    result = {"gerado_em": utc_now(), "antes_em": before["observado_em"], "depois_em": after["observado_em"], "totais": totals,
              "banco": before["banco"], "servidor": before["servidor"],
              "filtros": before["filtros"], "eventos": events,
              "limite_interpretacao": "Diferenças entre duas amostras; não revela mudanças transitórias nem comprova a ação no RH."}
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    atomic_json(output / "comparacao.json", result)
    rows = "".join("<tr>" + "".join("<td>" + escape(str(v)) + "</td>" for v in
                   (e["tipo"], e["id"], ", ".join(e["campos_alterados"]),
                    json.dumps(e["antes"], ensure_ascii=False), json.dumps(e["depois"], ensure_ascii=False))) + "</tr>" for e in events)
    (output / "comparacao.html").write_text('<!doctype html><meta charset="utf-8"><title>Comparação</title>'
        '<style>body{font:16px sans-serif;margin:24px}td,th{border:1px solid #ccc;padding:8px}table{border-collapse:collapse}</style>'
        '<h1>Comparação de afastamentos</h1><p>' + escape(result["limite_interpretacao"]) + '</p><p>'
        + escape(result["antes_em"] + " → " + result["depois_em"]) + '</p><p>' + escape(str(totals))
        + '</p><table><tr><th>Evento</th><th>Id</th>'
        '<th>Campos alterados</th><th>Antes</th><th>Depois</th></tr>' + rows + '</table>', encoding="utf-8")
    return result
