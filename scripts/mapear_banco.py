"""Inventário pontual de metadados SQL; não lê registros das tabelas de negócio."""
import json
import argparse
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer, configured_database

QUERIES = {
    "servidor_base": """SELECT DB_NAME() AS banco, CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(100)) AS versao,
        CAST(SERVERPROPERTY('ProductLevel') AS nvarchar(100)) AS nivel,
        CAST(SERVERPROPERTY('Edition') AS nvarchar(100)) AS edicao,
        d.compatibility_level AS compatibilidade, d.collation_name AS collation,
        d.recovery_model_desc AS recuperacao, d.state_desc AS estado, d.is_read_only AS somente_leitura,
        d.snapshot_isolation_state_desc AS isolamento_snapshot,
        d.is_read_committed_snapshot_on AS read_committed_snapshot,
        d.is_broker_enabled AS broker, d.is_cdc_enabled AS cdc
        FROM sys.databases d WHERE d.name=DB_NAME()""",
    "objetos": """SELECT s.name AS esquema, o.name AS objeto, o.type_desc AS tipo
        FROM sys.objects o JOIN sys.schemas s ON s.schema_id=o.schema_id
        WHERE o.is_ms_shipped=0 AND o.type IN ('U','V','P','FN','IF','TF','TR') ORDER BY s.name,o.name""",
    "colunas": """SELECT s.name AS esquema, o.name AS objeto, c.column_id AS ordem,
        c.name AS coluna, t.name AS tipo, c.max_length AS bytes_maximos,
        c.precision AS precisao, c.scale AS escala, c.is_nullable AS aceita_nulo,
        c.is_identity AS identidade, c.is_computed AS calculada
        FROM sys.columns c JOIN sys.objects o ON o.object_id=c.object_id
        JOIN sys.schemas s ON s.schema_id=o.schema_id JOIN sys.types t ON t.user_type_id=c.user_type_id
        WHERE o.is_ms_shipped=0 AND o.type IN ('U','V') ORDER BY s.name,o.name,c.column_id""",
    "indices": """SELECT s.name AS esquema, tb.name AS tabela, i.name AS indice,
        i.type_desc AS tipo, i.is_unique AS unico, i.is_primary_key AS chave_primaria,
        c.name AS coluna, ic.key_ordinal AS ordem, ic.is_included_column AS incluida
        FROM sys.indexes i JOIN sys.tables tb ON tb.object_id=i.object_id
        JOIN sys.schemas s ON s.schema_id=tb.schema_id
        JOIN sys.index_columns ic ON ic.object_id=i.object_id AND ic.index_id=i.index_id
        JOIN sys.columns c ON c.object_id=ic.object_id AND c.column_id=ic.column_id
        WHERE tb.is_ms_shipped=0 AND i.is_hypothetical=0 ORDER BY s.name,tb.name,i.name,ic.index_column_id""",
    "relacionamentos": """SELECT fk.name AS chave, ps.name AS esquema_origem, pt.name AS tabela_origem,
        pc.name AS coluna_origem, rs.name AS esquema_destino, rt.name AS tabela_destino,
        rc.name AS coluna_destino, fk.is_disabled AS desabilitada, fk.is_not_trusted AS nao_validada,
        fk.delete_referential_action_desc AS ao_excluir
        FROM sys.foreign_keys fk JOIN sys.foreign_key_columns fkc ON fkc.constraint_object_id=fk.object_id
        JOIN sys.tables pt ON pt.object_id=fkc.parent_object_id JOIN sys.schemas ps ON ps.schema_id=pt.schema_id
        JOIN sys.columns pc ON pc.object_id=pt.object_id AND pc.column_id=fkc.parent_column_id
        JOIN sys.tables rt ON rt.object_id=fkc.referenced_object_id JOIN sys.schemas rs ON rs.schema_id=rt.schema_id
        JOIN sys.columns rc ON rc.object_id=rt.object_id AND rc.column_id=fkc.referenced_column_id
        ORDER BY ps.name,pt.name,fk.name,fkc.constraint_column_id""",
    "gatilhos": """SELECT s.name AS esquema, o.name AS tabela, tr.name AS gatilho,
        tr.is_disabled AS desabilitado, tr.is_instead_of_trigger AS substitui_operacao
        FROM sys.triggers tr JOIN sys.objects o ON o.object_id=tr.parent_id
        JOIN sys.schemas s ON s.schema_id=o.schema_id WHERE tr.is_ms_shipped=0 ORDER BY s.name,o.name,tr.name""",
    "tabelas_estimativas": """SELECT s.name AS esquema,t.name AS tabela,
        SUM(p.rows) AS linhas_estimadas,t.temporal_type_desc AS temporal,t.is_tracked_by_cdc AS cdc,
        t.is_memory_optimized AS em_memoria
        FROM sys.tables t JOIN sys.schemas s ON s.schema_id=t.schema_id
        LEFT JOIN sys.partitions p ON p.object_id=t.object_id AND p.index_id IN (0,1)
        WHERE t.is_ms_shipped=0 GROUP BY s.name,t.name,t.temporal_type_desc,t.is_tracked_by_cdc,t.is_memory_optimized
        ORDER BY s.name,t.name""",
    "restricoes": """SELECT s.name AS esquema,t.name AS tabela,o.name AS restricao,o.type_desc AS tipo,
        c.name AS coluna FROM sys.objects o JOIN sys.tables t ON t.object_id=o.parent_object_id
        JOIN sys.schemas s ON s.schema_id=t.schema_id
        LEFT JOIN sys.columns c ON c.object_id=o.parent_object_id AND c.column_id=
        COALESCE((SELECT parent_column_id FROM sys.default_constraints WHERE object_id=o.object_id),
                 (SELECT parent_column_id FROM sys.check_constraints WHERE object_id=o.object_id))
        WHERE t.is_ms_shipped=0 AND o.type IN ('PK','UQ','F','C','D') ORDER BY s.name,t.name,o.name""",
    "dependencias": """SELECT s.name AS esquema_origem,o.name AS objeto_origem,
        d.referenced_server_name AS servidor_destino,d.referenced_database_name AS banco_destino,
        d.referenced_schema_name AS esquema_destino,d.referenced_entity_name AS objeto_destino,
        d.is_schema_bound_reference AS schema_bound
        FROM sys.sql_expression_dependencies d JOIN sys.objects o ON o.object_id=d.referencing_id
        JOIN sys.schemas s ON s.schema_id=o.schema_id WHERE o.is_ms_shipped=0
        ORDER BY s.name,o.name,d.referenced_entity_name""",
    "parametros": """SELECT s.name AS esquema,o.name AS objeto,p.parameter_id AS ordem,p.name AS parametro,
        t.name AS tipo,p.max_length AS bytes_maximos,p.precision AS precisao,p.scale AS escala,p.is_output AS saida
        FROM sys.parameters p JOIN sys.objects o ON o.object_id=p.object_id
        JOIN sys.schemas s ON s.schema_id=o.schema_id JOIN sys.types t ON t.user_type_id=p.user_type_id
        WHERE o.is_ms_shipped=0 ORDER BY s.name,o.name,p.parameter_id""",
    "sinonimos": """SELECT s.name AS esquema,sy.name AS sinonimo,sy.base_object_name AS objeto_destino
        FROM sys.synonyms sy JOIN sys.schemas s ON s.schema_id=sy.schema_id ORDER BY s.name,sy.name""",
    "arquivos_base": """SELECT name AS nome_logico,type_desc AS tipo,size*8.0/1024 AS tamanho_mb,
        max_size AS maximo_paginas,growth AS crescimento,is_percent_growth AS percentual
        FROM sys.database_files ORDER BY file_id""",
}


def inspect_schema(settings, output, *, db=None):
    database = configured_database(settings)
    db = db or SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
    db.assert_database()
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    result = {"base": database, "servidor": settings.sql_server,
              "observado_em": datetime.now(timezone.utc).isoformat(), "falhas": {},
              "limites": "Metadados visíveis ao login; linhas são estimativas de catálogo, sem varrer dados ou exportar definições SQL."}
    for name, sql in QUERIES.items():
        try:
            result[name] = db.query("SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; " + sql)
        except Exception as exc:
            result["falhas"][name] = type(exc).__name__
            result[name] = None
        (output / (name + ".json")).write_text(json.dumps(result[name], ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    (output / "inventario.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    lines = ["# Estrutura SQL Server — " + database, "", "Somente metadados; inventário pontual, sem alterações de dados.", "",
             "A nomenclatura sugere funções; não comprova a regra de importação nem relacionamentos sem FK.", "",
             "## Estruturas relacionadas aos testes", ""]
    terms = ("afast", "feria", "ocorr", "pessoa", "import", "integra", "freq", "contrat", "empresa", "log", "sincr", "servic")
    for obj in result["objetos"] or []:
        if any(term in obj["objeto"].casefold() for term in terms):
            name = obj["esquema"] + "." + obj["objeto"]
            cols = [c for c in result["colunas"] or [] if c["esquema"] == obj["esquema"] and c["objeto"] == obj["objeto"]]
            lines.extend([f"### {name} ({obj['tipo']})", "", ", ".join(f"`{c['coluna']}` ({c['tipo']})" for c in cols) or "Sem colunas de tabela/view.", ""])
    lines.extend(["## Chaves estrangeiras declaradas", ""])
    for fk in result["relacionamentos"] or []:
        lines.append(f"- {fk['esquema_origem']}.{fk['tabela_origem']}.{fk['coluna_origem']} → {fk['esquema_destino']}.{fk['tabela_destino']}.{fk['coluna_destino']} ({fk['chave']})")
    (output / "LEIA-ME.md").write_text("\n".join(lines), encoding="utf-8")
    if result["falhas"]:
        lines.extend(["", "## Consultas não concluídas", "", json.dumps(result["falhas"], ensure_ascii=False)])
        (output / "LEIA-ME.md").write_text("\n".join(lines), encoding="utf-8")
    return {name: len(result[name]) if result[name] is not None else None for name in QUERIES}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Base SQL deste levantamento; substitui SQL_DATABASE apenas nesta execução')
    parser.add_argument('--saida', type=Path)
    args = parser.parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    settings = Settings.load()
    if args.base is not None:
        settings = replace(settings, sql_database=args.base)
    folder = args.saida or ROOT / "reports" / "banco" / stamp
    print(inspect_schema(settings, folder))
    print("Inventário salvo em: " + str(folder))
