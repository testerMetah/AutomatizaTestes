"""Atualiza a análise lendo arquivos locais e consultando somente estados de serviços."""

import json
import math
import os
import time
from pathlib import Path

from automatiza.analise import analyze_session
from automatiza.observador import active_folder, append_json, atomic_json, observer_lock, observer_status, utc_now
from automatiza.servicos import service_changes, snapshot_services

WATCHED = ("inicial.json", "atual.json", "eventos.jsonl", "amostras.jsonl", "anotacoes.jsonl", "casos.json", "servicos-atual.json", "pessoas-referencia.json")


def signature(folder):
    result = []
    for name in WATCHED:
        file = folder / name
        try:
            stat = file.stat()
            result.append((name, stat.st_mtime_ns, stat.st_size))
        except FileNotFoundError:
            result.append((name, None, None))
    return tuple(result)


def follow_analysis(base, *, interval=10, service_interval=60, duration=7200,
                    clock=time.monotonic, sleep=time.sleep, service_reader=None, source_status=None, reset_stop=False):
    for number, minimum, label in ((interval, 5, "Intervalo"), (service_interval, 30, "Intervalo de serviços"), (duration, 1, "Duração")):
        if isinstance(number, bool) or not isinstance(number, (int, float)) or not math.isfinite(number) or number < minimum:
            raise ValueError(f"{label} precisa ser finito e de pelo menos {minimum} segundos.")
    folder = active_folder(base)
    service_reader = service_reader or snapshot_services
    source_status = source_status or observer_status
    control = folder / "controle-analise"
    with observer_lock(control, label="uma análise contínua"):
        if reset_stop:
            (folder / "parar-analise.sinal").unlink(missing_ok=True)
        status = {"status": "ANALISANDO", "pid": os.getpid(), "inicio": utc_now(), "atualizacoes": 0,
                  "falhas_analise": 0, "pasta": str(folder)}
        atomic_json(folder / "analista.json", status)
        start, next_services, previous_signature = clock(), 0, None
        previous_services, errors = None, 0
        while True:
            stop = (folder / "parar-analise.sinal").exists()
            current_folder, source = source_status(base)
            source_alive = source.get("processo_ativo", False) and Path(current_folder) == folder
            if Path(current_folder) != folder:
                source = {"status": "SESSAO_SUBSTITUIDA"}
            if clock() >= next_services:
                try:
                    services = service_reader()
                    instant = utc_now()
                    atomic_json(folder / "servicos-atual.json", {"instante": instant, "servicos": services})
                    append_json(folder / "amostras-servicos.jsonl", {"instante": instant, "servicos": services})
                    if previous_services is not None:
                        for event in service_changes(previous_services, services):
                            append_json(folder / "eventos-servicos.jsonl", {"instante": instant, **event})
                    previous_services = services
                    status["ultima_consulta_servicos"] = instant
                except Exception as exc:
                    append_json(folder / "erros-analise.jsonl", {"instante": utc_now(), "etapa": "servicos", "tipo": type(exc).__name__})
                next_services = clock() + service_interval
            current_signature = signature(folder)
            if current_signature != previous_signature or not source_alive or stop:
                try:
                    analyze_session(folder, source_state=source)
                    status["atualizacoes"] += 1
                    status["ultima_analise"] = utc_now()
                    errors = 0
                    previous_signature = current_signature
                except Exception as exc:
                    errors += 1
                    status["falhas_analise"] += 1
                    append_json(folder / "erros-analise.jsonl", {"instante": utc_now(), "etapa": "analise", "tipo": type(exc).__name__})
            if errors >= 5:
                status["status"] = "ERRO"
            elif stop:
                status["status"] = "PARADO"
            elif not source_alive:
                status["status"] = "ERRO" if errors else "FINALIZADO_COM_COLETA"
            elif clock() - start >= duration:
                status["status"] = "FINALIZADO_POR_TEMPO"
            atomic_json(folder / "analista.json", status)
            if status["status"] != "ANALISANDO":
                break
            next_update = min(clock() + interval, start + duration)
            while clock() < next_update and not (folder / "parar-analise.sinal").exists():
                sleep(min(1, next_update - clock()))
        return status


def save_case(base, case):
    """Registra expectativa local; não executa ação alguma no RH ou no SQL."""
    from automatiza.analise import utc
    from automatiza.casos_offline import criteria
    if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"].strip():
        raise ValueError("O caso precisa de um identificador textual.")
    if case.get("preparado") is not True:
        raise ValueError("Configure o caso e marque preparado=true antes de registrá-lo.")
    criteria(case)
    if case.get("tipo") not in {"incluir", "excluir", "recadastrar", "ausencia"}:
        raise ValueError("Tipo de caso inválido.")
    if case["tipo"] == "recadastrar":
        criteria(case, previous=True)
    registered = dict(case)
    registered.setdefault("registrado_em", utc_now())
    utc(registered["registrado_em"])
    from automatiza.casos_offline import evaluate_case
    validation = evaluate_case(registered, {}, [], [], registered["registrado_em"], utc(registered["registrado_em"]), [])
    if validation["status"] == "CONFIGURACAO_INVALIDA":
        raise ValueError(validation["detalhe"])
    folder = active_folder(base)
    source = json.loads((folder / "resumo.json").read_text(encoding="utf-8"))
    if source.get("pessoas") and registered["id_pessoa"] not in source["pessoas"]:
        raise ValueError("Esta pessoa está fora do filtro da coleta; o caso não pode ser acompanhado nesta sessão.")
    with observer_lock(folder / "controle-casos", label="uma edição dos casos"):
        path = folder / "casos.json"
        content = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"casos": []}
        if any(item["id"] == registered["id"] for item in content["casos"]):
            raise ValueError("Já existe um caso com esse identificador nesta sessão. Use outro identificador para uma nova ação.")
        if len(content["casos"]) >= 100:
            raise ValueError("Limite de 100 casos por sessão.")
        content["casos"].append(registered)
        atomic_json(path, content)
        if registered["tipo"] != "ausencia":
            fields = ("tipo", "id_pessoa", "inicio", "termino", "causa", "id_freq", "prazo_segundos", "permitir_termino_data_base")
            append_json(folder / "anotacoes.jsonl", {"instante": registered["registrado_em"],
                        "nota": "Expectativa registrada: " + registered["id"] + ". A operação manual não está comprovada por esta anotação.",
                        "dados": {key: registered[key] for key in fields if key in registered}})
    return registered


def analysis_status(base):
    folder = active_folder(base)
    state = json.loads((folder / "analista.json").read_text(encoding="utf-8"))
    try:
        with observer_lock(folder / "controle-analise"):
            running = False
    except RuntimeError:
        running = True
    state["processo_ativo"] = running
    if not running and state["status"] == "ANALISANDO":
        state["status"] = "ENCERRADO_SEM_FINALIZACAO"
    return folder, state
