"""Planejamento e diário durável para exploração de formulários Acessus."""

from __future__ import annotations

import hashlib
import json
import os
import random
from datetime import datetime
from pathlib import Path


DEFAULT_LIMITS = {
    "max_acoes_por_tela": 24,
    "max_sequencias_por_tela": 120,
    "sequencias_aleatorias": 40,
    "comprimento_aleatorio": 4,
}


def validate_config(raw: dict) -> dict:
    if not isinstance(raw, dict) or raw.get("versao") != 1:
        raise ValueError("Configuração do explorador exige versao=1.")
    if not isinstance(raw.get("semente"), int) or isinstance(raw["semente"], bool):
        raise ValueError("Informe semente inteira para reproduzir a ordem.")
    routes = raw.get("rotas")
    if not isinstance(routes, list) or not routes:
        raise ValueError("Informe ao menos uma rota explícita.")
    for item in routes:
        if (not isinstance(item, dict) or item.get("modulo") not in {
            "acesso", "refeitorio", "portaria", "estacionamento", "escola", "administracao"
        } or not isinstance(item.get("menu"), list) or len(item["menu"]) < 2
                or not all(isinstance(x, str) and x.strip() for x in item["menu"])):
            raise ValueError("Rota inválida; use modulo e menu com duas ou mais legendas.")
    if not isinstance(raw.get("limites", {}), dict):
        raise ValueError("limites precisa ser um objeto.")
    limits = {**DEFAULT_LIMITS, **raw.get("limites", {})}
    bounds = {
        "max_acoes_por_tela": (1, 100),
        "max_sequencias_por_tela": (1, 2000),
        "sequencias_aleatorias": (0, 2000),
        "comprimento_aleatorio": (2, 12),
    }
    for name, (minimum, maximum) in bounds.items():
        value = limits.get(name)
        if isinstance(value, bool) or not isinstance(value, int) or not minimum <= value <= maximum:
            raise ValueError(f"{name} deve estar entre {minimum} e {maximum}.")
    if limits["max_sequencias_por_tela"] < limits["max_acoes_por_tela"]:
        raise ValueError("max_sequencias_por_tela deve cobrir cada ação elegível ao menos uma vez.")
    policy = raw.get("politica", {})
    if not isinstance(policy, dict):
        raise ValueError("politica precisa ser um objeto.")
    for key in ("permitir_gravacao", "base_descartavel_confirmada", "capturar_erros"):
        if key in policy and not isinstance(policy[key], bool):
            raise ValueError(f"{key} precisa ser booleano.")
    allow = policy.get("botoes_autorizados", [])
    if not isinstance(allow, list) or not all(isinstance(x, str) for x in allow):
        raise ValueError("botoes_autorizados precisa ser lista de legendas.")
    if policy.get("permitir_gravacao", False) and not policy.get("base_descartavel_confirmada", False):
        raise ValueError("Ações de gravação exigem base_descartavel_confirmada=true.")
    values = raw.get("valores", {})
    if not isinstance(values, dict) or not values:
        raise ValueError("Informe valores de teste para os campos.")
    for kind, entries in values.items():
        if not isinstance(kind, str) or not isinstance(entries, list) or (not entries and kind not in {"combo", "lista"}):
            raise ValueError("Cada tipo de valor precisa de lista não vazia, exceto combo e lista.")
        if not all(isinstance(x, str) and x and len(x) <= 100 and "\n" not in x and "\r" not in x
                   for x in entries):
            raise ValueError("Valores devem ser textos não vazios de até 100 caracteres.")
    rules = raw.get("regras_campos", [])
    if not isinstance(rules, list):
        raise ValueError("regras_campos precisa ser lista.")
    for rule in rules:
        if (not isinstance(rule, dict) or not set(rule) <= {"classe", "id_controle", "legenda_regex",
                                                      "rotulo_regex", "valores"}
                or not isinstance(rule.get("valores"), list) or not rule["valores"]):
            raise ValueError("Regra de campo inválida.")
        if not all(isinstance(x, str) and x and len(x) <= 100 and "\n" not in x and "\r" not in x
                   for x in rule["valores"]):
            raise ValueError("Valores de regra de campo inválidos.")
    exploration = raw.get("exploracao", {})
    if not isinstance(exploration, dict):
        raise ValueError("exploracao precisa ser um objeto.")
    for key in ("entrar_em_cadastro", "combo_auto"):
        if key in exploration and not isinstance(exploration[key], bool):
            raise ValueError(f"{key} precisa ser booleano.")
    max_options = exploration.get("max_opcoes_combo", 5)
    if isinstance(max_options, bool) or not isinstance(max_options, int) or not 1 <= max_options <= 30:
        raise ValueError("max_opcoes_combo precisa estar entre 1 e 30.")
    return {**raw, "limites": limits, "politica": policy, "valores": values}


def build_sequences(actions: list[dict], *, seed: int, limits: dict) -> list[list[str]]:
    """Cada ação, pares ordenados e caminhos aleatórios sem explodir fatorialmente."""
    ids = [a["id"] for a in actions[:limits["max_acoes_por_tela"]]]
    if len(set(ids)) != len(ids):
        raise ValueError("IDs de ações duplicados.")
    maximum = limits["max_sequencias_por_tela"]
    sequences: list[list[str]] = []
    seen = set()

    def add(sequence):
        key = tuple(sequence)
        if key and key not in seen and len(sequences) < maximum:
            sequences.append(list(sequence))
            seen.add(key)

    for action in ids:
        add([action])
    pairs = [(first, second) for first in ids for second in ids if first != second]
    rng = random.Random(seed)
    rng.shuffle(pairs)
    for pair in pairs:
        add(pair)
    for _ in range(limits["sequencias_aleatorias"]):
        if not ids or len(sequences) >= maximum:
            break
        add([rng.choice(ids) for _ in range(limits["comprimento_aleatorio"])])
    return sequences


def spread_actions(actions: list[dict], maximum: int) -> list[dict]:
    """Prioriza controles distintos antes de repetir valores no mesmo campo."""
    groups = {}
    for action in actions:
        descriptor = action.get("controle", {})
        key = (action.get("aba"), descriptor.get("classe"),
               tuple(descriptor.get("posicao", [])), descriptor.get("legenda"))
        groups.setdefault(key, []).append(action)
    selected = []
    while groups and len(selected) < maximum:
        for key in list(groups):
            selected.append(groups[key].pop(0))
            if not groups[key]:
                del groups[key]
            if len(selected) >= maximum:
                break
    return selected


def _atomic_json(path: Path, data: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


class Journal:
    def __init__(self, folder: Path, config: dict):
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.state_path = self.folder / "estado.json"
        digest = hashlib.sha256(json.dumps(config, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text(encoding="utf-8"))
            if self.state.get("config_sha256") != digest:
                raise ValueError("Configuração diferente da execução já existente.")
            if self.state.get("pendente") is not None:
                raise RuntimeError("Existe ação pendente; confira o diário e a tela antes de retomar.")
        else:
            self.state = {"config_sha256": digest, "concluidas": [], "pendente": None,
                          "erros": 0, "status": "PREPARADO"}
            _atomic_json(self.folder / "configuracao.json", config)
            self.save()

    def save(self):
        _atomic_json(self.state_path, self.state)

    def event(self, status: str, *, route: str, sequence: int | None = None,
              action: dict | None = None, detail: str = "", error: str = "", image: str = ""):
        row = {"horario": datetime.now().astimezone().isoformat(), "resultado": status,
               "rota": route, "sequencia": sequence, "acao": action, "detalhe": detail,
               "erro": error, "captura": image}
        with (self.folder / "passos.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        label = action or {}
        line = (f"[{row['horario']}] {status} rota={route} sequencia={sequence} "
                f"acao={label.get('id', '')} tipo={label.get('tipo', '')} "
                f"controle={label.get('controle', '')} valor={label.get('valor', '')} "
                f"detalhe={detail} erro={error} captura={image}\n")
        with (self.folder / "passos.log").open("a", encoding="utf-8") as stream:
            stream.write(line)
            stream.flush()
            os.fsync(stream.fileno())


class Explorer:
    """Backend: open(route), discover(config), perform(action), reset(), capture(path)."""

    def __init__(self, config: dict, backend, folder: Path):
        self.config = validate_config(config)
        self.backend = backend
        self.journal = Journal(Path(folder), self.config)
        self._route_name = ""
        self._sequence_number = None
        if hasattr(backend, "set_event_logger"):
            backend.set_event_logger(lambda status, action, detail="": self.journal.event(
                status, route=self._route_name, sequence=self._sequence_number,
                action=action, detail=detail))

    def run(self):
        state = self.journal.state
        state["status"] = "EXECUTANDO"
        self.journal.save()
        for route_index, route in enumerate(self.config["rotas"]):
            name = route["modulo"] + ":" + " > ".join(route["menu"])
            self._route_name = name
            self._sequence_number = None
            try:
                self.backend.open(route)
                found = self.backend.discover(self.config)
                actions = spread_actions(found, self.config["limites"]["max_acoes_por_tela"])
                self.journal.event("INVENTARIO", route=name,
                                   detail=f"{len(found)} elegíveis; {len(actions)} no limite")
                for skipped in getattr(self.backend, "skipped", []):
                    self.journal.event("IGNORADO", route=name, detail=str(skipped))
                chosen = {action["id"] for action in actions}
                for skipped in (action for action in found if action["id"] not in chosen):
                    self.journal.event("IGNORADO_LIMITE", route=name, action=skipped,
                                       detail="max_acoes_por_tela atingido")
                self.backend.reset()
            except Exception as exc:
                state["erros"] += 1
                self.journal.event("ERRO_ABERTURA", route=name,
                                   error=f"{type(exc).__name__}: {exc}")
                try:
                    self.backend.reset()
                except Exception:
                    state["status"] = "INTERROMPIDO_RECUPERACAO"
                    self.journal.save()
                    raise
                self.journal.save()
                continue
            by_id = {action["id"]: action for action in actions}
            sequences = build_sequences(actions, seed=self.config["semente"] + route_index,
                                        limits=self.config["limites"])
            pair_count = sum(len(sequence) == 2 for sequence in sequences)
            possible_pairs = len(actions) * max(0, len(actions) - 1)
            self.journal.event("COBERTURA_PLANEJADA", route=name,
                               detail=(f"{len(sequences)} sequências; {len(actions)} ações isoladas; "
                                       f"{pair_count}/{possible_pairs} pares ordenados"))
            for number, sequence in enumerate(sequences, 1):
                self._sequence_number = number
                key = f"{route_index}:{number}"
                if key in state["concluidas"]:
                    continue
                self.journal.event("INICIO_SEQUENCIA", route=name, sequence=number,
                                   detail=" > ".join(sequence))
                try:
                    self.backend.open(route)
                except Exception as exc:
                    state["erros"] += 1
                    self.journal.event("ERRO_ABERTURA_SEQUENCIA", route=name, sequence=number,
                                       error=f"{type(exc).__name__}: {exc}")
                    try:
                        self.backend.reset()
                    except Exception as recovery_error:
                        state["status"] = "INTERROMPIDO_RECUPERACAO"
                        self.journal.event("ERRO_RECUPERACAO", route=name, sequence=number,
                                           error=f"{type(recovery_error).__name__}: {recovery_error}")
                        self.journal.save()
                        raise
                    state["pendente"] = None
                    self.journal.save()
                    break
                try:
                    for action_id in sequence:
                        action = by_id[action_id]
                        state["pendente"] = {"rota": name, "sequencia": number, "acao": action_id}
                        self.journal.save()
                        self.journal.event("ANTES", route=name, sequence=number, action=action)
                        try:
                            observation = self.backend.perform(action)
                        except Exception as exc:
                            state["erros"] += 1
                            image = self._capture(route_index, number, action_id)
                            self.journal.event("ERRO", route=name, sequence=number, action=action,
                                               error=f"{type(exc).__name__}: {exc}", image=image)
                            break
                        else:
                            self.journal.event("DEPOIS", route=name, sequence=number,
                                               action=action, detail=str(observation))
                            validation = (observation.get("validacao") if isinstance(observation, dict)
                                          else None)
                            if not isinstance(validation, dict):
                                validation = {"status": "NAO_VERIFICADO",
                                              "motivo": "Backend não informou resultado esperado."}
                            status = validation.get("status")
                            if status not in {"APROVADO", "FALHOU", "NAO_VERIFICADO"}:
                                raise ValueError(f"Status de validação inválido: {status!r}")
                            self.journal.event("VALIDACAO_" + status, route=name, sequence=number,
                                               action=action, detail=str(validation))
                            if status == "FALHOU":
                                state["erros"] += 1
                                state["pendente"] = None
                                self.journal.save()
                                break
                            state["pendente"] = None
                            self.journal.save()
                    self.backend.reset()
                except Exception as exc:
                    state["status"] = "INTERROMPIDO_RECUPERACAO"
                    self.journal.event("ERRO_RECUPERACAO", route=name, sequence=number,
                                       error=f"{type(exc).__name__}: {exc}")
                    self.journal.save()
                    raise
                state["pendente"] = None
                state["concluidas"].append(key)
                self.journal.save()
                self.journal.event("FIM_SEQUENCIA", route=name, sequence=number)
        state["status"] = "CONCLUIDO_COM_ERROS" if state["erros"] else "CONCLUIDO"
        self.journal.save()
        self.journal.event(state["status"], route="geral",
                           detail=f"{len(state['concluidas'])} sequências, {state['erros']} erros")
        return state

    def _capture(self, route_index, number, action_id):
        name = f"erro-{route_index:03d}-{number:04d}-{action_id.replace(':', '_')}.png"
        try:
            self.backend.capture(self.journal.folder / name)
            return name
        except Exception:
            return ""
