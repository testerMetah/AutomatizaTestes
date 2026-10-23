import json
import random
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from automatiza.acoes import Actions


class BlockedBackend:
    def supports(self, action, entity): return False
    def mutate(self, action, step): raise RuntimeError("Backend sem implementação real")


@dataclass
class Oracle:
    rules: dict = field(default_factory=dict)
    expected: dict = field(default_factory=dict)

    @classmethod
    def from_docs(cls, folder="docs/cenarios"):
        rules = {}
        for path in Path(folder).glob("*.md"):
            body = path.read_text(encoding="utf-8")
            if not body.startswith("---\n"): continue
            header = yaml.safe_load(body.split("---", 2)[1]) or {}
            if header.get("status") == "CONFIRMADA":
                for action in header.get("acoes", []):
                    rules[(header.get("entidade"), action)] = header
        return cls(rules=rules)

    def apply(self, step, report):
        key = (step.get("entidade"), step["acao"])
        if key not in self.rules:
            report.emit("AVISO", regra=f"{key[0]}/{key[1]}", motivo="REGRA NÃO CONFIRMADA; nenhum resultado esperado afirmado")
            return
        data = step.get("dados", {})
        identity = (step.get("entidade"), step.get("id"))
        if step["acao"] in {"cadastrar", "recriar_igual", "alterar"}:
            self.expected[identity] = {**self.expected.get(identity, {}), **data}
        elif step["acao"] == "deletar": self.expected.pop(identity, None)


def generate(seed, *, count=8, max_steps=20, max_mass=5):
    if seed is None: raise ValueError("SEED obrigatória")
    if not 1 <= count <= max_steps: raise ValueError("Quantidade fora do limite")
    rng = random.Random(int(seed))
    entities = ["pessoa", "cracha", "ocorrencia", "ferias", "unidade"]
    actions = ["cadastrar", "alterar", "deletar", "recriar_igual", "cadastrar_em_massa", "importar", "fechar_e_reabrir_acessus"]
    steps = []
    for i in range(count):
        action = rng.choice(actions)
        steps.append({"acao": action, "entidade": rng.choice(entities), "id": f"AUTOTEST_{seed}_{i}_",
                      "quantidade": rng.randint(1, max_mass) if action == "cadastrar_em_massa" else 1,
                      "limite_massa": max_mass})
    return {"nome": f"aleatoria-{seed}", "seed": int(seed), "passos": steps}


def load_yaml(path):
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("passos"), list):
        raise ValueError("Sequência YAML precisa de nome e passos")
    return data


def run_case(case, report, backend=None, *, stop_on_failure=True, shrink=True):
    backend = backend or BlockedBackend()
    actions, oracle = Actions(backend, report), Oracle.from_docs()
    report.context = {"sequencia": case["nome"], "seed": case.get("seed")}
    state, error = "PASSOU", None
    for number, step in enumerate(case["passos"], 1):
        report.context["passo"] = number
        result = actions.execute(step)
        if result.state == "PASSOU" and step.get("entidade"):
            oracle.apply(step, report)
        elif result.state == "FALHOU":
            state, error = "FALHOU", result.details.get("erro")
            if stop_on_failure: break
        elif result.state == "BLOQUEADO" and state == "PASSOU": state = "BLOQUEADO"
    item = {"nome": case["nome"], "seed": case.get("seed"), "estado": state,
            "passos": len(case["passos"]), "erro": error}
    safe = {"verificar_banco", "observar_acessus", "mapear_tela"}
    if state == "FALHOU" and shrink and all(s["acao"] in safe for s in case["passos"]):
        class ReplayReport:
            context = {}
            cases = []
            def emit(self, *args, **kwargs): return None
        def replay(steps):
            trial = {**case, "passos": steps}
            return run_case(trial, ReplayReport(), backend=BlockedBackend(), shrink=False)["estado"] == "FALHOU"
        reduced = reduce_failure(case, replay)
        if reduced:
            folder = Path("tests/sequencias/regressao")
            folder.mkdir(parents=True, exist_ok=True)
            path = folder / ("falha-" + str(case.get("seed", "sem-seed")) + ".yaml")
            path.write_text(yaml.safe_dump(reduced, allow_unicode=True, sort_keys=False), encoding="utf-8")
            item["reduzida"] = str(path)
            report.emit("REDUCAO", caminho=str(path), passos_originais=len(case["passos"]), passos_reduzidos=len(reduced["passos"]))
    elif state == "FALHOU" and shrink:
        report.emit("AVISO", regra="redução automática", motivo="Sequência contém ação potencialmente mutável; replay isolado não configurado")
    report.cases.append(item)
    report.emit("CASO", resultado=state, erro=error)
    return item


def reduce_failure(case, replay):
    """ddmin só para backends descartáveis; replay cria ambiente isolado por tentativa."""
    steps = list(case["passos"])
    if not replay(steps): return None
    chunks = 2
    while len(steps) >= 2:
        size = (len(steps) + chunks - 1) // chunks
        reduced = False
        for start in range(0, len(steps), size):
            candidate = steps[:start] + steps[start+size:]
            if candidate and replay(candidate):
                steps, chunks, reduced = candidate, max(2, chunks-1), True
                break
        if not reduced:
            if chunks >= len(steps): break
            chunks = min(len(steps), chunks*2)
    return {**case, "nome": case["nome"] + "-reduzida", "passos": steps}
