"""Relatório local, triagem e comparação; não consulta nem modifica o banco."""
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


def ler(rodada):
    folder = Path(rodada)
    files = list(folder.glob("**/tentativas.jsonl"))
    records = []
    for path in files:
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def mensagem(record):
    for field in ("mensagens_consulta", "mensagens_contagem"):
        for dialog in record.get(field, []) or []:
            for value in dialog.get("mensagens", []) or []:
                if value:
                    return value
    return record.get("erro", "") or record.get("status", "")


def normalizar(value):
    value = unicodedata.normalize("NFKD", str(value or "").casefold())
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"0x[0-9a-f]+|\b\d+\b", "#", value)
    return re.sub(r"\s+", " ", value).strip()


def agrupar_erros(records):
    groups = defaultdict(list)
    for record in records:
        if record.get("oraculo_contagem", {}).get("status") == "FALHOU":
            key = "contagem divergente: esperado " + str(record["oraculo_contagem"]["esperado"])
            groups[normalizar(key)].append(record)
        if record.get("status") in {"ERRO_APLICACAO", "ERRO_AUTOMACAO", "FALHOU"}:
            groups[normalizar(mensagem(record))].append(record)
    return [{"mensagem_normalizada": key, "quantidade": len(items),
             "ocorrencias": [{"modulo": x.get("modulo"), "historico": x.get("historico"),
                              "filtro": x.get("filtro"), "status": x.get("status"),
                              "screenshot": x.get("screenshot") or next(
                                  (d.get("screenshot") for d in x.get("mensagens_consulta", [])
                                   if d.get("screenshot")), None)}
                             for x in items]}
            for key, items in sorted(groups.items(), key=lambda x: -len(x[1]))]


def _chaves(records):
    return {(x.get("modulo"), x.get("historico"), x.get("filtro"), x.get("status"))
            for x in records}


def comparar(anterior, atual):
    before = _chaves(ler(anterior))
    after = _chaves(ler(atual))
    failure = {"ERRO_APLICACAO", "ERRO_AUTOMACAO", "SEM_CONTAGEM", "FALHOU"}
    old_errors = {x for x in before if x[3] in failure}
    new_errors = {x for x in after if x[3] in failure}
    old_keys = {x[:3] for x in old_errors}
    new_keys = {x[:3] for x in new_errors}
    def ordered(values):
        return [dict(zip(("modulo", "historico", "filtro", "estado"), x)) for x in sorted(values)]
    return {"novos": ordered({x for x in new_errors if x[:3] not in old_keys}),
            "corrigidos": ordered({x for x in old_errors if x[:3] not in new_keys}),
            "regredidos": ordered({x for x in new_errors if x[:3] in old_keys and x not in old_errors}),
            "persistentes": ordered(old_errors & new_errors)}


def exportar_passo_a_passo(folder, records):
    """Copia para a rodada as ações dos IDs registrados nas tentativas."""
    ids = {x.get("execucao_id") for x in records if x.get("execucao_id")}
    from automatiza.caminhos import logs_permanentes
    origem = logs_permanentes() / "passo-a-passo-detalhado.jsonl"
    if not ids or not origem.exists():
        return None
    destino = folder / "passo-a-passo.log"
    detalhado = folder / "passo-a-passo-detalhado.jsonl"
    total = 0
    with origem.open(encoding="utf-8") as entrada, destino.open("w", encoding="utf-8") as legivel, detalhado.open("w", encoding="utf-8") as jsonl:
        for linha in entrada:
            try:
                evento = json.loads(linha)
            except json.JSONDecodeError:
                continue
            if evento.get("execucao_id") not in ids:
                continue
            jsonl.write(linha)
            if evento.get("linha_passo_a_passo"):
                legivel.write(evento["linha_passo_a_passo"] + "\n")
                total += 1
    return total


def gerar(rodada):
    folder = Path(rodada)
    records = ler(folder)
    passos = exportar_passo_a_passo(folder, records)
    import os
    origem_pausa = os.environ.get("AUTOMATIZA_PAUSA_DIR")
    if origem_pausa and (Path(origem_pausa) / "eventos.jsonl").exists():
        (folder / "pausas.jsonl").write_bytes((Path(origem_pausa) / "eventos.jsonl").read_bytes())
    pausas = []
    if (folder / "pausas.jsonl").exists():
        for line in (folder / "pausas.jsonl").read_text(encoding="utf-8").splitlines():
            try:
                pausas.append(json.loads(line))
            except ValueError:
                continue
    numero_pausas = sum(x.get("tipo") == "PAUSA_INICIADA" for x in pausas)
    tempo_pausado_ms = sum(x.get("duracao_ms", 0) for x in pausas if x.get("tipo") == "PAUSA_RETOMADA")
    cancelada = any(x.get("tipo") == "CANCELADO_PELO_USUARIO" for x in pausas) or any(x.get("status") == "CANCELADO" for x in records)
    counts = defaultdict(Counter)
    for record in records:
        counts[record.get("modulo", "?")][record.get("status", "?")] += 1
        oracle = record.get("oraculo_contagem")
        if oracle:
            counts[record.get("modulo", "?")]["ORACULO_" + oracle["status"]] += 1
    findings = agrupar_erros(records)
    from automatiza.log import json_seguro
    (folder / "achados.json").write_text(json_seguro([
        {"mensagem": item["mensagem_normalizada"], "contagem": item["quantidade"],
         "exemplos": item["ocorrencias"][:1]} for item in findings
    ]), encoding="utf-8")
    def esc(value):
        return html.escape(str(value if value is not None else ""))
    rows = "".join("<tr><td>" + esc(mod) + "</td>" +
                   "".join("<td>" + str(c[status]) + "</td>" for status in
                           ("CONSULTADO", "SEM_CONTAGEM", "ERRO_APLICACAO", "ERRO_AUTOMACAO", "CANCELADO",
                            "ORACULO_PASSOU", "ORACULO_FALHOU")) +
                   "</tr>" for mod, c in sorted(counts.items()))
    errors = []
    for group in findings:
        occurrences = []
        for item in group["ocorrencias"]:
            link = ""
            if item["screenshot"]:
                try:
                    relative = Path(item["screenshot"]).resolve().relative_to(folder.resolve())
                    link = f' <a href="{esc(relative.as_posix())}">captura</a>'
                except ValueError:
                    link = " (captura fora da rodada)"
            occurrences.append(f"<li>{esc(item['modulo'])} / {esc(item['historico'])} / "
                               f"{esc(item['filtro'])} — {esc(item['status'])}{link}</li>")
        errors.append(f"<details><summary>{esc(group['mensagem_normalizada'])} "
                      f"({group['quantidade']})</summary><ul>{''.join(occurrences)}</ul></details>")
    body = f"""<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<title>Auditorias — {esc(folder.name)}</title>
<style>body{{font:16px system-ui;max-width:1100px;margin:32px auto;color:#182533}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ccd5dd;padding:9px;text-align:left}}
th{{background:#e9f2f8}}details{{border:1px solid #ccd5dd;padding:12px;margin:8px 0}}
a{{color:#065a9c}}</style>
<h1>Auditorias/Históricos</h1><p>Rodada: {esc(folder.name)} · Tentativas: {len(records)}</p>
<p>Pausas: {numero_pausas} · Tempo pausado: {round(tempo_pausado_ms / 1000, 1)} s · Cancelada pelo usuário: {'sim' if cancelada else 'não'}</p>
{f'<p><a href="passo-a-passo.log">Log passo a passo</a> ({passos} ações) · <a href="passo-a-passo-detalhado.jsonl">Log detalhado JSONL</a></p>' if passos is not None else ''}
<table><tr><th>Módulo</th><th>Consultado</th><th>Sem contagem</th>
<th>Erro da aplicação</th><th>Erro da automação</th><th>Cancelado</th>
<th>Oráculo passou</th><th>Oráculo falhou</th></tr>{rows}</table>
<h2>Achados agrupados</h2>{''.join(errors) or '<p>Nenhum erro registrado.</p>'}
<p>As contagens são exploratórias quando não há regra CONFIRMADA para o filtro.</p></html>"""
    output = folder / "RELATORIO.html"
    output.write_text(body, encoding="utf-8")
    (folder / "resumo.json").write_text(json.dumps({
        "rodada": folder.name, "tentativas": len(records), "pausas": numero_pausas,
        "tempo_pausado_ms": tempo_pausado_ms, "cancelada_pelo_usuario": cancelada,
        "modulos": {name: dict(c) for name, c in counts.items()},
        "achados": findings}, ensure_ascii=False, indent=2), encoding="utf-8")
    return output
