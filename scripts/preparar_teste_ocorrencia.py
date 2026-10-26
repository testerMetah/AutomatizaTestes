"""Leituras pontuais para selecionar pessoa de teste e preservar pré-condições."""
import json
from datetime import datetime
from pathlib import Path
from automatiza.config import Settings
from automatiza.database import SqlServer

settings = Settings.load()
db = SqlServer(settings)
db.assert_database()
folder = Path('reports/teste-real') / datetime.now().strftime('%Y%m%d-%H%M%S')
folder.mkdir(parents=True, exist_ok=False)
queries = {
    'colunas': ("SELECT OBJECT_NAME(c.object_id) AS tabela,c.name AS coluna,t.name AS tipo "
                "FROM sys.columns c JOIN sys.types t ON t.user_type_id=c.user_type_id "
                "WHERE c.object_id IN (OBJECT_ID('dbo.Pessoas'),OBJECT_ID('dbo.Ocorrencias')) "
                "ORDER BY tabela,c.column_id", ()),
    'pessoas_teste': ('SELECT TOP (30) id,nome,IdExportacao,ContratoExportacao,idempresa '
                     'FROM dbo.Pessoas WHERE nome LIKE ? ORDER BY id', ('%TEST%',)),
}
for name, (sql, params) in queries.items():
    rows = db.query('SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; ' + sql, params)
    (folder / (name + '.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2, default=str), encoding='utf-8')
    print(name, json.dumps(rows, ensure_ascii=True, default=str))
print('PASTA', folder)
