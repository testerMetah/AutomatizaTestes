import json
import os
import re
from collections import Counter
from datetime import datetime
from html import escape
from pathlib import Path
from uuid import uuid4


SENSITIVE = re.compile(r"senha|password|secret|token|cpf|documento|matricula|connection|email|telefone|fone", re.I)


def mask(value, key=""):
    if SENSITIVE.search(str(key)):
        return "****"
    if re.search(r"^(nome|name)$", str(key), re.I) and isinstance(value, str) and not value.startswith("AUTOTEST_"):
        return "****"
    if isinstance(value, dict):
        return {k: mask(v, k) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [mask(v, key) for v in value]
    return value


class Report:
    def __init__(self, root="reports"):
        self.folder = Path(root) / (datetime.now().strftime("%Y%m%d-%H%M%S-%f") + "-" + uuid4().hex[:6])
        self.folder.mkdir(parents=True, exist_ok=False)
        self.events = []
        self.cases = []
        self.context = {}

    def emit(self, kind, **fields):
        event = mask({"hora": datetime.now().astimezone().isoformat(timespec="milliseconds"),
                      "numero": len(self.events) + 1, "tipo": kind, **self.context, **fields})
        with (self.folder / "eventos.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, ensure_ascii=False, default=str) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        self.events.append(event)
        return event

    def finish(self):
        counts = Counter(c["estado"] for c in self.cases)
        acts = Counter(e.get("acao") for e in self.events if e.get("tipo") == "INTERACAO")
        screens = {e.get("tela", {}).get("titulo") for e in self.events if isinstance(e.get("tela"), dict)} - {None}
        metrics = {
            "Telas visitadas": len(screens), "Cliques": acts["clique"] + acts["duplo_clique"],
            "Campos preenchidos": acts["digitar"] + acts["selecionar"],
            "Registros criados": sum(e.get("quantidade", 0) for e in self.events if e.get("acao") in ("cadastrar", "cadastrar_em_massa") and e.get("resultado") == "PASSOU"),
            "Registros alterados": sum(e.get("resultado") == "PASSOU" for e in self.events if e.get("acao") == "alterar"),
            "Registros deletados": sum(e.get("resultado") == "PASSOU" for e in self.events if e.get("acao") == "deletar"),
            "Importações": sum(e.get("acao") == "importar" and e.get("resultado") == "PASSOU" for e in self.events),
            "Verificações no banco": sum(e.get("tipo") == "BANCO" for e in self.events),
            "Maior sequência": max((c.get("passos", 0) for c in self.cases), default=0),
            "Combinações cobertas": len({(e.get("entidade"), e.get("acao")) for e in self.events if e.get("tipo") == "ACAO"}),
        }
        rows = lambda entries: "".join("<tr>" + "".join(f"<td>{escape(str(v))}</td>" for v in row) + "</tr>" for row in entries)
        timeline = rows((e.get("hora"), e.get("sequencia"), e.get("passo"), e.get("tipo"), e.get("acao", ""), e.get("resultado", ""), e.get("erro", "")) for e in self.events)
        fields = rows((e.get("tela", {}).get("titulo", ""), e.get("controle", {}).get("nome", ""), e.get("acao"), e.get("valor"), e.get("valor_anterior")) for e in self.events if e.get("tipo") == "INTERACAO")
        failures = rows((c.get("nome"), c.get("seed"), c.get("erro"), c.get("reduzida")) for c in self.cases if c["estado"] == "FALHOU")
        blocked = rows((e.get("sequencia"), e.get("passo"), e.get("acao"), e.get("motivo")) for e in self.events if e.get("resultado") == "BLOQUEADO")
        warnings = rows((e.get("sequencia"), e.get("regra"), e.get("motivo")) for e in self.events if e.get("tipo") == "AVISO")
        html = f"""<!doctype html><html lang=pt-BR><meta charset=utf-8><title>Relatório de sequências</title><style>body{{font:15px system-ui;margin:2rem;color:#17212b}}table{{border-collapse:collapse;width:100%;margin-bottom:2rem}}td,th{{border:1px solid #ccd;padding:.35rem;vertical-align:top}}th{{background:#eef}}h2{{margin-top:2rem}}code{{white-space:pre-wrap}}</style><h1>Relatório de sequências</h1><p>PASSOU: {counts['PASSOU']} · FALHOU: {counts['FALHOU']} · BLOQUEADO: {counts['BLOQUEADO']} · avisos: {sum(e['tipo']=='AVISO' for e in self.events)}</p><h2>Métricas de complexidade</h2><table>{rows(metrics.items())}</table><h2>Linha do tempo</h2><table><tr><th>Hora</th><th>Sequência</th><th>Passo</th><th>Tipo</th><th>Ação</th><th>Resultado</th><th>Erro</th></tr>{timeline}</table><h2>Campos por tela</h2><table><tr><th>Tela</th><th>Campo</th><th>Ação</th><th>Valor</th><th>Anterior</th></tr>{fields}</table><h2>Falhas e sequência reduzida</h2><table>{failures}</table><h2>Bloqueados e desbloqueio</h2><table>{blocked}</table><h2>Regras não confirmadas</h2><table>{warnings}</table></html>"""
        html = html.replace("· avisos:", f"· CANCELADO: {counts['CANCELADO']} · avisos:")
        (self.folder / "RELATORIO.html").write_text(html, encoding="utf-8")
        (self.folder / "resumo.json").write_text(json.dumps({"casos": self.cases, "metricas": metrics}, ensure_ascii=False, indent=2), encoding="utf-8")
        return self.folder / "RELATORIO.html"
