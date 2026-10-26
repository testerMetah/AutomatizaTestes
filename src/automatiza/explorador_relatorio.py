"""Resumo de cobertura e validação observado no diário do explorador."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


def write_report(config: dict, folder: Path) -> dict:
    folder = Path(folder)
    names = [route["modulo"] + ":" + " > ".join(route["menu"])
             for route in config["rotas"]]
    routes = {name: Counter() for name in names}
    for line in (folder / "passos.jsonl").open(encoding="utf-8"):
        event = json.loads(line)
        name = event.get("rota")
        if name in routes:
            routes[name][event["resultado"]] += 1
    rows = []
    for name, counts in routes.items():
        rows.append({"rota": name, "abertura": counts["INVENTARIO"] > 0,
                     "sequencias_concluidas": counts["FIM_SEQUENCIA"],
                     "validacoes_aprovadas": counts["VALIDACAO_APROVADO"],
                     "validacoes_falhas": counts["VALIDACAO_FALHOU"],
                     "sem_validacao": counts["VALIDACAO_NAO_VERIFICADO"],
                     "erros_execucao": sum(value for key, value in counts.items()
                                          if key.startswith("ERRO")),
                     "controles_ignorados": counts["IGNORADO"] + counts["IGNORADO_LIMITE"]})
    summary = {"rotas_planejadas": len(rows),
               "rotas_abertas": sum(row["abertura"] for row in rows),
               "sequencias_concluidas": sum(row["sequencias_concluidas"] for row in rows),
               "validacoes_aprovadas": sum(row["validacoes_aprovadas"] for row in rows),
               "validacoes_falhas": sum(row["validacoes_falhas"] for row in rows),
               "sem_validacao": sum(row["sem_validacao"] for row in rows),
               "erros_execucao": sum(row["erros_execucao"] for row in rows),
               "rotas": rows}
    (folder / "validacao-resumo.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    header = "| Rota | Aberta | Sequências | Aprovadas | Falhas | Sem validação | Erros | Ignorados |"
    lines = ["# Resultado da validação", "",
             f"Rotas abertas: {summary['rotas_abertas']}/{summary['rotas_planejadas']}.",
             f"Sequências concluídas: {summary['sequencias_concluidas']}.",
             f"Validações: {summary['validacoes_aprovadas']} aprovadas, "
             f"{summary['validacoes_falhas']} falhas, {summary['sem_validacao']} sem verificação.",
             f"Erros de execução: {summary['erros_execucao']}.", "",
             "A aprovação compara o estado visível do controle com o valor esperado. "
             "Ela não comprova gravação no banco nem regra de negócio sem um cenário específico.", "",
             header, "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for row in rows:
        lines.append(f"| {row['rota'].replace('|', '/') } | {'Sim' if row['abertura'] else 'Não'} | "
                     f"{row['sequencias_concluidas']} | {row['validacoes_aprovadas']} | "
                     f"{row['validacoes_falhas']} | {row['sem_validacao']} | "
                     f"{row['erros_execucao']} | {row['controles_ignorados']} |")
    (folder / "validacao-resumo.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary
