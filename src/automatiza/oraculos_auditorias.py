"""Contagens opcionais definidas apenas em regras de negócio confirmadas."""
import re
from pathlib import Path

import yaml

from automatiza.config import ROOT


def carregar(folder=None):
    folder = Path(folder or ROOT / "docs/cenarios")
    rules = []
    for path in folder.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            continue
        try:
            meta = yaml.safe_load(content.split("---", 2)[1]) or {}
        except yaml.YAMLError:
            continue
        if meta.get("status") == "CONFIRMADA":
            for rule in meta.get("auditorias_contagens", []):
                if all(k in rule for k in ("modulo", "historico", "filtro", "sql")):
                    rules.append(rule)
    return rules


def verificar(db, record, rules=None):
    """Retorna None quando não há regra confirmada; nunca inventa expectativa."""
    rules = carregar() if rules is None else rules
    for rule in rules:
        if all(str(record.get(k, "")).casefold() == str(rule[k]).casefold()
               for k in ("modulo", "historico", "filtro")):
            sql = rule["sql"].strip()
            if not re.fullmatch(r"(?is)SELECT\s+COUNT\s*\(\s*\*\s*\)\s+FROM\s+\[[a-z0-9_]+\]"
                                r"(?:\s+WHERE\s+\[[a-z0-9_]+\]\s*=\s*\?)?", sql):
                raise ValueError("Oráculo de contagem exige SELECT COUNT(*) simples e parametrizado.")
            parameters = (record.get("valor_exibido"),) if "?" in sql else ()
            expected = db.scalar(sql, parameters)
            actual = record.get("contagem")
            return {"status": "PASSOU" if actual == expected else "FALHOU",
                    "esperado": expected, "obtido": actual, "regra": rule.get("id", "")}
    return None
