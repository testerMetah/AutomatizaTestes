"""Sequências reproduzíveis de CRUD + importação, com diário e retomada."""
import hashlib
import json
import random
from datetime import datetime
from html import escape
from pathlib import Path


class Blocked(RuntimeError):
    pass


def atomic(path, value):
    path = Path(path)
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)


def validate(config):
    if config.get("versao") != 1 or not config.get("casos"):
        raise ValueError("Informe versao=1 e casos.")
    def no_secrets(value):
        if isinstance(value, dict):
            if any(k.lower() in {"senha", "password", "token", "sql_password", "rh_password",
                                 "senha_api", "access_token", "accesstoken"} for k in value):
                raise ValueError("Credenciais não podem estar no plano; use ambiente/cofre Windows.")
            for item in value.values():
                no_secrets(item)
        elif isinstance(value, list):
            for item in value:
                no_secrets(item)
    no_secrets(config)
    ids = set()
    for c in config["casos"]:
        if c["id"] in ids or c["tipo"] not in {"ferias", "ocorrencia", "reserva"}:
            raise ValueError("Identificador duplicado ou tipo desconhecido.")
        ids.add(c["id"])
        if not isinstance(c["presente"], bool):
            raise ValueError("presente deve ser booleano.")
        for key in ("inicio", "termino", "termino_alterado"):
            datetime.fromisoformat(c[key])
        if c["termino"] == c["termino_alterado"]:
            raise ValueError("Alteração precisa mudar o término.")
        if any(datetime.fromisoformat(c[k]) < datetime.fromisoformat(c["inicio"])
               for k in ("termino", "termino_alterado")):
            raise ValueError("Término anterior ao início.")
    return config


def plan(config, seed, rounds=1):
    """Intercala casos, preservando a ordem causal dentro de cada um."""
    validate(config)
    if type(rounds) is not int or not 1 <= rounds <= 50:
        raise ValueError("Use entre 1 e 50 rodadas.")
    rng = random.Random(seed)
    queues = {}
    patterns = [
        ["alterar", "importar", "importar", "excluir", "importar", "criar", "importar"],
        ["excluir", "importar", "criar", "importar", "alterar", "importar",
         "restaurar", "importar"],
        ["alterar", "importar", "restaurar", "importar", "excluir", "importar",
         "criar", "importar", "importar"],
    ]
    for c in config["casos"]:
        actions = ["importar"] if c["presente"] else ["criar", "importar"]
        for _ in range(rounds):
            actions += list(rng.choice(patterns))
        current = c["termino"] if c["presente"] else None
        queue = []
        for action in actions:
            target = (None if action == "excluir" else c["termino_alterado"]
                      if action == "alterar" else c["termino"]
                      if action in {"criar", "restaurar"} else current)
            queue.append(dict(caso=c["id"], acao=action, antes=current, depois=target))
            current = target
        queues[c["id"]] = queue
    steps = []
    while queues:
        name = rng.choice(sorted(queues))
        step = queues[name].pop(0)
        steps.append(dict(numero=len(steps) + 1, **step))
        if not queues[name]:
            del queues[name]
    return dict(versao=1, semente=seed, rodadas=rounds, configuracao=config, etapas=steps)


def validate_plan(execution_plan):
    if execution_plan.get("versao") != 1:
        raise ValueError("Versão de plano desconhecida.")
    config = validate(execution_plan["configuracao"])
    cases = {case["id"] for case in config["casos"]}
    last = {}
    steps = execution_plan.get("etapas")
    if not isinstance(steps, list) or not steps:
        raise ValueError("Plano vazio.")
    for number, step in enumerate(steps, 1):
        if step.get("numero") != number or step.get("caso") not in cases:
            raise ValueError("Etapa sem número sequencial ou caso válido.")
        action, before, after = step.get("acao"), step.get("antes"), step.get("depois")
        if action not in {"criar", "alterar", "restaurar", "excluir", "importar"}:
            raise ValueError("Ação não suportada no plano.")
        if before is not None:
            datetime.fromisoformat(before)
        if after is not None:
            datetime.fromisoformat(after)
        if step["caso"] in last and before != last[step["caso"]]:
            raise ValueError("Cadeia de estado inconsistente no plano.")
        if (action == "criar" and (before is not None or after is None)
                or action == "excluir" and (before is None or after is not None)
                or action in {"alterar", "restaurar"} and
                (before is None or after is None or before == after)
                or action == "importar" and before != after):
            raise ValueError("Transição inválida no plano.")
        last[step["caso"]] = after
    return execution_plan


class Runner:
    """backend: preflight, source, mutate, observe; dados já sanitizados."""
    def __init__(self, execution_plan, backend, directory):
        self.plan = validate_plan(execution_plan)
        self.backend = backend
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "estado.json"
        self.digest = hashlib.sha256(json.dumps(execution_plan, sort_keys=True).encode()).hexdigest()
        if self.path.exists():
            self.state = json.loads(self.path.read_text(encoding="utf-8"))
            if self.state["plano_sha256"] != self.digest:
                raise ValueError("O plano difere da execução a retomar.")
        else:
            self.state = dict(plano_sha256=self.digest, proxima=0, pendente=None,
                              bloqueados={}, falhas=0, status="PREPARADO")
            atomic(self.directory / "plano.json", execution_plan)
            self.persist()
        self.cases = {c["id"]: c for c in self.plan["configuracao"]["casos"]}

    def persist(self):
        atomic(self.path, self.state)

    def log(self, step, status, expected, observed):
        event = dict(horario=datetime.now().astimezone().isoformat(),
                     etapa=step.get("numero"), caso=step.get("caso"),
                     acao=step["acao"], resultado=status, esperado=expected, observado=observed)
        with (self.directory / "diario.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False, default=str) + "\n")
        with (self.directory / "diario.txt").open("a", encoding="utf-8") as f:
            f.write(f"[{event['horario']}] #{event['etapa']} {event['caso']} "
                    f"{event['acao']} — {status}\n"
                    f"  Esperado: {expected}\n  Observado: {observed}\n\n")
        self.report()

    def report(self):
        rows = [json.loads(s) for s in (self.directory / "diario.jsonl").read_text(encoding="utf-8").splitlines()]
        html = ('<!doctype html><meta charset="utf-8"><title>Ciclos de importação</title>'
                '<style>body{font:15px system-ui;margin:2rem}td,th{padding:.6rem;border:1px solid #ccc}'
                'table{border-collapse:collapse}td{white-space:pre-wrap}</style>'
                '<h1>Diário dos ciclos de importação</h1>'
                '<p>Logs produzidos pelo executor de testes. Não são logs do sistema.</p>'
                '<table><tr><th>Horário</th><th>Etapa/caso</th><th>Ação</th>'
                '<th>Resultado</th><th>Esperado</th><th>Observado</th></tr>')
        for r in rows:
            values = [r["horario"], f'{r["etapa"]}/{r["caso"]}', r["acao"],
                      r["resultado"], r["esperado"], r["observado"]]
            html += "<tr>" + "".join("<td>" + escape(str(v)) + "</td>" for v in values) + "</tr>"
        (self.directory / "relatorio.html").write_text(html + "</table>", encoding="utf-8")

    def run(self):
        preflight = dict(acao="precondicoes")
        self.log(preflight, "INICIO", "Origem, destino, pessoa e autenticação correspondentes",
                 "Conferir ambiente antes de qualquer alteração.")
        try:
            self.backend.preflight()
        except Exception as exc:
            self.state["status"] = "INTERROMPIDO"
            self.persist()
            self.log(preflight, "INTERROMPIDO", "Ambiente válido", type(exc).__name__)
            raise
        self.log(preflight, "PASSOU", "Ambiente válido", "Precondições conferidas.")
        self.state["status"] = "EXECUTANDO"
        self.persist()
        for index in range(self.state["proxima"], len(self.plan["etapas"])):
            step = self.plan["etapas"][index]
            case = self.cases[step["caso"]]
            if case["id"] in self.state["bloqueados"]:
                self.log(step, "BLOQUEADO", step["depois"], self.state["bloqueados"][case["id"]])
                self.state["proxima"] = index + 1
                self.persist()
                continue
            mutating = False
            try:
                self.backend.available(case)
                actual = self.backend.source(case)
                pending = self.state["pendente"]
                if step["acao"] != "importar" and pending == index and actual == step["depois"]:
                    self.log(step, "RECUPERADO", step["depois"],
                             "Efeito anterior confirmado na origem; operação não repetida.")
                else:
                    if actual != step["antes"]:
                        raise Blocked("Origem diverge do estado previsto; interromper caso para reconciliação.")
                    self.log(step, "INICIO", step["depois"], dict(origem_antes=actual))
                    self.state["pendente"] = index
                    self.persist()  # Intenção durável ANTES da ação.
                    if step["acao"] == "importar":
                        result = self.backend.observe(case, step["depois"], self.directory,
                                                      lambda expected, observed:
                                                      self.log(step, "AMOSTRA", expected, observed))
                        if result["status"] != "PASSOU":
                            self.state["falhas"] += 1
                        self.log(step, result["status"], step["depois"], result)
                    else:
                        mutating = True
                        self.backend.mutate(case, step["acao"], step["depois"], self.directory, step["numero"])
                        actual = self.backend.source(case)
                        if actual != step["depois"]:
                            raise Blocked("Efeito da ação não confirmado na origem.")
                        self.log(step, "PASSOU", step["depois"], dict(origem_depois=actual))
                self.state.update(proxima=index + 1, pendente=None)
                self.persist()
            except Blocked as exc:
                if mutating:
                    self.state["status"] = "INTERROMPIDO"
                    self.persist()
                    self.log(step, "INTERROMPIDO", step["depois"], str(exc))
                    raise
                self.state["bloqueados"][case["id"]] = str(exc)
                self.log(step, "BLOQUEADO", step["depois"], str(exc))
                self.state.update(proxima=index + 1, pendente=None)
                self.persist()
            except BaseException as exc:
                self.state["status"] = "INTERROMPIDO"
                self.persist()
                self.log(step, "INTERROMPIDO", step["depois"],
                         type(exc).__name__ + "; conferir estado antes de retomar.")
                raise
        self.state["status"] = ("CONCLUIDO_COM_RESSALVAS" if self.state["falhas"] or
                                self.state["bloqueados"] else "PASSOU")
        self.persist()
        self.log(dict(acao="encerrar"), self.state["status"], "Todas as etapas verificadas",
                 dict(falhas=self.state["falhas"], bloqueados=self.state["bloqueados"]))
        return self.state
