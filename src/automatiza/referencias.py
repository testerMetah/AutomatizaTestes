"""Consulta pontual de nomes e chaves, sem outros dados pessoais nem alterações no banco."""

import json
from dataclasses import replace
from pathlib import Path

from automatiza.database import SqlServer, configured_database
from automatiza.observador import atomic_json, utc_now


def update_references(settings, folder, people=None, *, db=None):
    database = configured_database(settings)
    folder = Path(folder)
    state_file = folder / "resumo.json"
    if state_file.exists():
        state = json.loads(state_file.read_text(encoding="utf-8"))
        if (state.get("banco", "bras1").casefold() != database.casefold()
                or state.get("servidor", settings.sql_server).casefold() != settings.sql_server.casefold()):
            raise ValueError("As referências precisam pertencer à mesma base e servidor da sessão.")
    if people is None:
        seen = []
        for name in ("inicial.json", "atual.json"):
            data = json.loads((folder / name).read_text(encoding="utf-8"))
            seen.extend(row["IdPessoa"] for row in data["linhas"])
        people = [person for person in seen if type(person) is int and person > 0]
    if any(type(person) is not int or person <= 0 for person in people):
        raise ValueError("Use apenas IdPessoa internos positivos.")
    people = sorted(set(people))
    if not people or len(people) > 100:
        raise ValueError("Informe entre 1 e 100 pessoas por consulta pontual.")
    db = db or SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
    path = folder / "pessoas-referencia.json"
    previous = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"pessoas": []}
    if previous.get("origem", database + ".dbo.Pessoas").casefold() != (database + ".dbo.Pessoas").casefold():
        raise ValueError("As referências existentes pertencem a outra base.")
    if previous.get("servidor", settings.sql_server).casefold() != settings.sql_server.casefold():
        raise ValueError("As referências existentes pertencem a outro servidor.")
    db.assert_database()
    rows = db.query("SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; "
                    "SELECT id AS Id, nome AS Nome, IdExportacao, ContratoExportacao, idempresa AS IdEmpresa "
                    "FROM dbo.Pessoas WHERE id IN (" + ",".join("?" for _ in people) + ") ORDER BY id", tuple(people))
    existing = {item["Id"]: item for item in previous["pessoas"] if item["Id"] not in people}
    existing.update({item["Id"]: item for item in rows})
    result = {"observado_em": utc_now(), "origem": database + ".dbo.Pessoas",
              "servidor": settings.sql_server, "ids_consultados": people,
              "ids_nao_localizados": sorted(set(people) - {item["Id"] for item in rows}),
              "pessoas": [existing[key] for key in sorted(existing)]}
    atomic_json(path, result)
    return result
