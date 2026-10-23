import json
from pathlib import Path


def target(name):
    config = json.loads((Path(__file__).resolve().parents[3] / "config" / "ambiente-teste.json").read_text(encoding="utf-8"))
    key = {"origem": "sql_origem", "destino": "sql_destino"}.get(name)
    if key is None: raise ValueError("Banco deve ser origem ou destino")
    info = config[key]
    if info.get("confirmado_como_teste") is not True:
        raise ValueError(f"{name} não confirmado como banco de teste")
    return info
