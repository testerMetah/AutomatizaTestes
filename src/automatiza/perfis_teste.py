"""Perfis declarativos e trava do banco de teste."""
import json
from dataclasses import replace
from pathlib import Path

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer

PROFILE_DIR = ROOT / "profiles"


def carregar(nome: str) -> dict:
    if not nome or Path(nome).name != nome or not nome.replace("-", "").replace("_", "").isalnum():
        raise ValueError("Nome de perfil inválido.")
    path = PROFILE_DIR / f"{nome}.json"
    if not path.is_file():
        raise ValueError(f"Perfil {nome!r} não encontrado em profiles/.")
    data = json.loads(path.read_text(encoding="utf-8"))
    for field in ("nome", "pasta_executaveis", "servidor", "banco", "confirmado_como_teste"):
        if field not in data:
            raise ValueError(f"Perfil {nome}: falta {field}.")
    return data


def permitidos() -> set[str]:
    databases = set()
    for path in PROFILE_DIR.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("confirmado_como_teste") is True:
                databases.add(data["banco"].casefold())
        except (ValueError, KeyError, TypeError):
            continue
    config = ROOT / "config" / "ambiente-teste.json"
    if config.exists():
        data = json.loads(config.read_text(encoding="utf-8"))
        for key in ("sql_origem", "sql_destino"):
            item = data.get(key, {})
            if item.get("confirmado_como_teste") is True:
                databases.add(item["banco"].casefold())
    return databases


def configuracao(nome: str) -> Settings:
    data = carregar(nome)
    if data["confirmado_como_teste"] is not True:
        raise ValueError("Perfil sem confirmação de banco de teste.")
    return replace(Settings.load(), sql_server=data["servidor"], sql_database=data["banco"])


def validar_escrita(settings: Settings) -> str:
    """A escrita só pode começar após validar DB_NAME contra a lista permitida."""
    if settings.sql_database.casefold() not in permitidos():
        raise ValueError("Escrita recusada: banco configurado fora da lista de teste.")
    actual = SqlServer(settings).assert_database()
    if actual.casefold() not in permitidos():
        raise ValueError(f"Escrita recusada: banco efetivo {actual!r} fora da lista de teste.")
    return actual
