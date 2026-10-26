"""Manifestos, índices e manutenção segura das saídas."""
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import zipfile
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

from automatiza import caminhos
from automatiza.log import json_seguro, mascarar

ESTADOS = {"EM_ANDAMENTO", "CONCLUIDO", "FALHOU", "CANCELADO", "INTERROMPIDO"}
CAMPOS = ("id", "tipo", "alvo", "perfil", "servidor", "banco_efetivo", "build", "versao_do_executavel",
          "caminho_executavel", "comando_cli_equivalente", "opcoes", "maquina", "usuario_windows",
          "inicio", "fim", "duracao_s", "estado_final", "totais", "pausas", "versao_do_projeto",
          "pasta", "links_relativos", "observacoes")


def _agora():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _escrever(path, dados):
    from automatiza.pausa import gravar
    gravar(path, mascarar(dados))


def _git():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=caminhos.raiz(),
                                       stderr=subprocess.DEVNULL, timeout=2, text=True).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def iniciar(pasta, tipo, alvo, **dados):
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    manifesto = {chave: None for chave in CAMPOS}
    manifesto.update({"id": pasta.name, "tipo": tipo, "alvo": alvo, "inicio": _agora(),
                      "estado_final": "EM_ANDAMENTO", "totais": {}, "pausas": {"quantidade": 0, "tempo_total_s": 0},
                      "pasta": pasta.relative_to(caminhos.raiz()).as_posix() if pasta.is_relative_to(caminhos.raiz()) else str(pasta),
                      "maquina": socket.gethostname(), "usuario_windows": None, "versao_do_projeto": _git(),
                      "links_relativos": {"relatorio": "RELATORIO.html", "tentativas": "tentativas.jsonl",
                                           "evidencias": "evidencias", "log_permanente_trecho": None}})
    manifesto.update({k: v for k, v in dados.items() if k in CAMPOS})
    _escrever(pasta / "manifesto.json", manifesto)
    (pasta / "LEIA-ME.md").write_text(
        f"# Rodada {pasta.name}\n\nTipo: {tipo}; alvo: {alvo}.\nComece por manifesto.json e resumo.json.\n"
        "Leia achados.json e RELATORIO.html para os resultados.\nEvidências ficam em evidencias/.\n", encoding="utf-8")
    return manifesto


def carregar(pasta):
    return json.loads((Path(pasta) / "manifesto.json").read_text(encoding="utf-8"))


def atualizar(pasta, **dados):
    manifesto = carregar(pasta)
    manifesto.update({k: v for k, v in dados.items() if k in CAMPOS or k in {"manter", "origem", "nota"}})
    _escrever(Path(pasta) / "manifesto.json", manifesto)
    return manifesto


def finalizar(pasta, estado, totais=None, **dados):
    if estado not in ESTADOS - {"EM_ANDAMENTO"}:
        raise ValueError("Estado final inválido")
    manifesto = carregar(pasta)
    inicio = datetime.fromisoformat(manifesto["inicio"])
    fim = datetime.now().astimezone()
    dados.update(estado_final=estado, fim=fim.isoformat(timespec="seconds"),
                 duracao_s=round((fim - inicio).total_seconds(), 2), totais=totais or {})
    atualizado = atualizar(pasta, **dados)
    indice()
    return atualizado


def _manifestos():
    for path in caminhos.rodadas().glob("*/manifesto.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("id") == path.parent.name:
                yield data
        except (OSError, json.JSONDecodeError):
            continue


def _estado(m):
    if m.get("estado_final") == "EM_ANDAMENTO":
        try:
            idade = datetime.now().astimezone() - datetime.fromisoformat(m["inicio"])
            if idade.total_seconds() > 86400:
                return "INTERROMPIDO"
        except (TypeError, ValueError):
            return "INTERROMPIDO"
    return m.get("estado_final")


def indice():
    caminhos.saidas().mkdir(parents=True, exist_ok=True)
    rows = sorted(_manifestos(), key=lambda x: x.get("id", ""), reverse=True)
    payload = [{**m, "estado_final": _estado(m)} for m in rows]
    _escrever(caminhos.saidas() / "INDICE.json", payload)
    lines = ["# Índice de rodadas", "", "| ID | Tipo | Alvo | Build | Banco | Início | Duração | Estado | Totais | Relatório |",
             "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |"]
    for m in payload[:50]:
        ident = m["id"]
        rel = f"rodadas/{ident}/RELATORIO.html"
        vals = [ident, m.get("tipo"), m.get("alvo"), m.get("build"), m.get("banco_efetivo"),
                m.get("inicio"), m.get("duracao_s"), m.get("estado_final"), m.get("totais")]
        lines.append("| " + " | ".join(str(mascarar(x) if x is not None else "—").replace("|", "/") for x in vals)
                     + f" | [Abrir]({rel}) |")
    lines += ["", "## Última rodada de cada tipo/módulo", ""]
    vistos = set()
    for m in payload:
        chave = (m.get("tipo"), m.get("alvo"))
        if chave not in vistos:
            lines.append(f"- {chave[0]} / {chave[1]}: {m['id']} ({m['estado_final']})")
            vistos.add(chave)
    achados = Counter()
    for m in payload[:10]:
        path = caminhos.rodadas() / m["id"] / "achados.json"
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                for a in data if isinstance(data, list) else data.get("achados", []):
                    achados[a.get("mensagem", "erro")] += int(a.get("contagem", 1))
            except (OSError, ValueError, TypeError):
                continue
    lines += ["", "## Achados mais frequentes (últimas 10 rodadas)", ""]
    lines += [f"- {mascarar(msg)}: {n}" for msg, n in achados.most_common(10)] or ["- Nenhum achado registrado."]
    for nome in ("passo-a-passo.log", "passo-a-passo-detalhado.jsonl"):
        path = caminhos.logs_permanentes() / nome
        if path.exists() and path.stat().st_size > 200 * 1024 * 1024:
            lines.append(f"\nAviso: {nome} passou de 200 MB. Não foi rotacionado.")
    (caminhos.saidas() / "INDICE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload
