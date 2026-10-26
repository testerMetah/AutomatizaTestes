"""Consolida as tentativas de filtros em relatório Markdown e CSV."""

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = ("acesso", "refeitorio", "portaria", "estacionamento", "escola", "administracao")


def message_text(dialogs):
    messages = [message for dialog in dialogs for message in dialog.get("mensagens", [])]
    return " | ".join(messages) if messages else "(nenhuma mensagem)"


def main():
    results = ROOT / "resultados"
    output = results / f"relatorio-auditorias-filtros-{datetime.now():%Y%m%d-%H%M%S}"
    output.mkdir(parents=True)
    records = []
    origins = {}
    for module in MODULES:
        paths = sorted(results.glob(f"auditorias-filtros-*/{module}/tentativas.jsonl"),
                       key=lambda path: path.stat().st_mtime)
        if not paths:
            continue
        by_field = {}
        for path in paths:
            groups = defaultdict(list)
            for line in path.read_text(encoding="utf-8").splitlines():
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                groups[(record["historico"], record["filtro"], record["subcampo"])].append(record)
            for field, rows in groups.items():
                score = (sum(row.get("status") == "CONSULTADO" for row in rows), len(rows))
                previous = by_field.get(field)
                previous_score = ((sum(row.get("status") == "CONSULTADO" for row in previous[1]),
                                   len(previous[1])) if previous else (-1, -1))
                if score >= previous_score:
                    by_field[field] = (path, rows)
        origins[module] = ", ".join(str(path) for path in dict.fromkeys(
            source for source, _ in by_field.values()))
        for (history, label, subindex), (_, rows) in by_field.items():
            # O mapa da aba Pessoa em Fila/Comandos (Escola) contém um único TEdit.
            # Um segundo controle transitório foi detectado e falhou em todas as tentativas.
            if module == "escola" and history == "Fila/Comandos" and label.startswith("Pessoa") and subindex == 1:
                continue
            records.extend(rows)

    fields = ("modulo", "historico", "filtro", "subcampo", "tipo", "tentativa",
              "data_referencia", "periodo", "valor_entrada", "valor_exibido",
              "amostra_banco", "status", "contagem", "mensagens_limpeza",
              "mensagens_consulta", "mensagens_contagem", "erro")
    with (output / "todas-as-tentativas.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter=";")
        writer.writeheader()
        for record in records:
            row = {field: record.get(field) for field in fields}
            if any(marker in message_text(record.get("mensagens_consulta", []))
                   for marker in ("[FireDAC]", "[ODBC]", "Exception", "Exceção", "Access violation")):
                row["status"] = "ERRO_APLICACAO"
            row["periodo"] = " ".join(record.get("periodo", []))
            for key in ("mensagens_limpeza", "mensagens_consulta", "mensagens_contagem"):
                row[key] = message_text(record.get(key, []))
            writer.writerow(row)

    grouped = defaultdict(list)
    for record in records:
        key = (record["modulo"], record["historico"], record["filtro"], record["subcampo"])
        grouped[key].append(record)
    expected_filters = []
    for module in MODULES:
        maps = sorted(results.glob(f"auditorias-runtime-*/{module}/resultado.json"),
                      key=lambda path: path.stat().st_mtime)
        if not maps:
            continue
        survey = json.loads(maps[-1].read_text(encoding="utf-8"))
        for history in survey["historicos"]:
            for field in history["filtros"]:
                label = "Período" if field["nome"].startswith("Per") else field["nome"]
                expected_filters.append((module, history["historico"], label))
    covered_filters = {(module, history, label) for module, history, label, _ in grouped}
    missing_filters = [key for key in expected_filters if key not in covered_filters]
    incomplete_filters = [(key, len(rows)) for key, rows in grouped.items() if len(rows) < 10]
    app_errors = [record for record in records if any(
        marker in message_text(record.get("mensagens_consulta", []))
        for marker in ("[FireDAC]", "[ODBC]", "Exception", "Exceção", "Access violation"))]
    issues = [record for record in records if record["status"] != "CONSULTADO"
              or record in app_errors]
    zero_samples = [record for record in records if record.get("amostra_banco")
                    and record.get("contagem") == 0]
    messages = Counter(message_text(r.get("mensagens_consulta", [])) for r in records)
    lines = ["# Auditorias/Históricos: testes dos filtros", "",
             f"Gerado em {datetime.now():%d/%m/%Y %H:%M:%S}.", "",
             "Banco observado: `desk-tec/AcessoFagundes` (banco de teste confirmado pelo Gabriel).",
             "Execução de leitura via interface; nenhum registro foi criado, alterado ou excluído.",
             "", "## Cobertura", "",
             f"- Módulos com resultados: {len(origins)}/6",
             f"- Históricos com resultados: {len({(r['modulo'], r['historico']) for r in records})}/27",
             f"- Campos de filtro com resultados: {len(grouped)}",
             f"- Abas de filtro mapeadas: {len(expected_filters)}",
             f"- Abas de filtro sem nenhuma tentativa: {len(missing_filters)}",
             f"- Campos com menos de dez tentativas: {len(incomplete_filters)}",
             f"- Tentativas registradas: {len(records)}",
             f"- Tentativas com mensagem de contagem: {sum(r['status'] == 'CONSULTADO' for r in records)}",
             f"- Tentativas sem contagem ou com erro de automação/aplicação: {len(issues)}",
             f"- Tentativas com erro exibido pelo Acessus: {len(app_errors)}",
             f"- Amostras presentes na tabela de referência, mas com contagem zero na tela: {len(zero_samples)}",
             "", "O arquivo `todas-as-tentativas.csv` contém todas as mensagens exibidas em cada tentativa.",
             "Amostras do banco indicam valores presentes no histórico de referência na data testada;",
             "a correspondência do valor digitado com a regra do campo ainda precisa ser confirmada pela interface.",
             "Dez tentativas sobre um segundo controle transitório da aba Pessoa em Fila/Comandos da Escola",
             "foram excluídas da cobertura: o mapa da tela mostra apenas um campo real nessa aba.",
             "", "## Resultado por filtro", "",
             "| Módulo | Histórico | Filtro | Campo | Execuções | Contagens obtidas | Erros |",
             "|---|---|---|---:|---:|---|---:|"]
    for key, rows in grouped.items():
        module, history, label, subindex = key
        counts = ", ".join("?" if row.get("contagem") is None else str(row["contagem"])
                           for row in rows)
        lines.append(f"| {module} | {history} | {label} | {subindex + 1} | {len(rows)}/10 | {counts} | "
                     f"{sum(r in issues for r in rows)} |")
    lines.extend(["", "## Mensagens durante a consulta", "",
                  "| Mensagem | Ocorrências |", "|---|---:|"])
    for message, count in messages.most_common():
        lines.append(f"| {message.replace('|', '/')} | {count} |")
    lines.extend(["", "## Falhas e tentativas incompletas", ""])
    if not issues:
        lines.append("Nenhuma registrada.")
    else:
        for record in issues:
            lines.append(f"- {record['modulo']} / {record['historico']} / {record['filtro']} "
                         f"(campo {record['subcampo'] + 1}, tentativa {record['tentativa']}): "
                         f"{record.get('erro') or record['status']}; "
                         f"consulta: {message_text(record.get('mensagens_consulta', []))}; "
                         f"contagem: {message_text(record.get('mensagens_contagem', []))}")
    lines.extend(["", "## Amostras do banco com contagem zero na interface", ""])
    if not zero_samples:
        lines.append("Nenhuma registrada.")
    else:
        lines.append("Essas diferenças pedem conferência da regra do filtro; o campo pode esperar um código exibido ao usuário em vez do ID interno.")
        for record in zero_samples:
            lines.append(f"- {record['modulo']} / {record['historico']} / {record['filtro']}: "
                         f"valor {record.get('valor_entrada')!r}, minuto {record['data_referencia']}, "
                         f"tabela {record['tabela_referencia']}.")
    lines.extend(["", "## Filtros impedidos ou incompletos", ""])
    if not missing_filters and not incomplete_filters:
        lines.append("Nenhum.")
    for module, history, label in missing_filters:
        lines.append(f"- Sem tentativa: {module} / {history} / {label}.")
    for (module, history, label, subindex), count in incomplete_filters:
        lines.append(f"- {count}/10 tentativas: {module} / {history} / {label}, campo {subindex + 1}.")
    lines.extend(["", "## Arquivos de origem", ""])
    for module, path in origins.items():
        lines.append(f"- {module}: `{path}`")
    (output / "RELATORIO.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"saida": str(output), "tentativas": len(records),
                      "campos": len(grouped), "falhas": len(issues)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
