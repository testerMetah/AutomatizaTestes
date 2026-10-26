"""Leitura pontual e limitada de configurações não secretas da integração."""
import json
import argparse
from dataclasses import replace
from datetime import datetime
from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer, configured_database

QUERIES = {
    "importacao": "SELECT TOP (101) id, intervalo_minutos, contratos_alterados, id_empresa, unidade FROM dbo.DADOS_IMPORTACAO_API ORDER BY id",
    "tarefas": "SELECT TOP (101) id, tipo, status, id_empresa FROM dbo.AcessusSyncTarefas ORDER BY id",
    "agendamentos": "SELECT TOP (101) id, id_tarefa, horarios, diassemanas, periodicamente, status, id_empresa FROM dbo.AcessusSyncAgendamento ORDER BY id",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Base SQL deste teste; não altera o .env')
    args = parser.parse_args()
    settings = Settings.load()
    if args.base is not None:
        settings = replace(settings, sql_database=args.base)
    configured_database(settings)
    db = SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
    db.assert_database()
    folder = ROOT / "reports" / "integracao-config" / datetime.now().strftime("%Y%m%d-%H%M%S")
    folder.mkdir(parents=True, exist_ok=False)
    for name, query in QUERIES.items():
        rows = db.query("SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; " + query)
        result = {"registros": rows[:100], "limite_excedido": len(rows) > 100,
                  "banco": settings.sql_database, "servidor": settings.sql_server,
                  "observado_em": datetime.now().astimezone().isoformat(),
                  "limite_interpretacao": "Configuração cadastrada não comprova execução nem regra de corte efetiva."}
        (folder / (name + ".json")).write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(name + ": " + str(min(len(rows), 100)) + " registros; limite excedido: " + str(len(rows) > 100))
    print("Configurações não secretas salvas em: " + str(folder))
