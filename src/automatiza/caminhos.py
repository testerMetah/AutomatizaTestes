"""Fonte única dos caminhos gerados pelo projeto.

AUTOMATIZA_RAIZ permite testar sem tocar nos dados reais.
"""
import os
import re
from datetime import datetime
from pathlib import Path


def raiz():
    return Path(os.environ.get("AUTOMATIZA_RAIZ") or Path(__file__).resolve().parents[2]).resolve()


def saidas():
    return raiz() / "saidas"


def rodadas():
    return saidas() / "rodadas"


def logs_permanentes():
    return saidas() / "logs-permanentes"


def observacao():
    return saidas() / "observacao"


def mapas():
    return saidas() / "mapas"


def comparacoes():
    return saidas() / "comparacoes"


def exportacoes():
    return saidas() / "exportacoes"


def arquivo_legado():
    return saidas() / "arquivo-legado"


def docs():
    return raiz() / "docs"


def legado(nome):
    """Caminho de leitura dos resultados anteriores à organização."""
    if nome not in {"resultados", "reports"}:
        raise ValueError("Origem legada inválida")
    return raiz() / nome


def identificador(tipo, alvo, agora=None):
    agora = agora or datetime.now()
    def seguro(valor):
        valor = re.sub(r"[^a-z0-9]+", "-", str(valor).lower()).strip("-")
        return valor[:60] or "geral"
    return f"{agora:%Y%m%d-%H%M%S}-{seguro(tipo)}-{seguro(alvo)}"


def nova_rodada(tipo, alvo, agora=None):
    base = rodadas()
    base.mkdir(parents=True, exist_ok=True)
    stem = identificador(tipo, alvo, agora)
    path = base / stem
    numero = 2
    while path.exists():
        path = base / f"{stem}-{numero}"
        numero += 1
    path.mkdir()
    return path
