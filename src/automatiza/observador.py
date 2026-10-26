"""Observação passiva de dbo.Afastamentos: sem desktop, escrita SQL ou mudança de serviço."""

import json
import math
import os
import time
from contextlib import contextmanager
from dataclasses import replace
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path
from uuid import uuid4

from automatiza.database import SqlServer, configured_database

FIELDS = ("Id", "IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq")


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path, value):
    path = Path(path)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)


def append_json(path, value):
    with Path(path).open("a", encoding="utf-8") as output:
        output.write(json.dumps(value, ensure_ascii=False) + "\n")


def normalize_snapshot(rows):
    result = {}
    for raw in rows:
        if set(raw) != set(FIELDS) or type(raw["Id"]) is not int:
            raise ValueError("Amostra de afastamentos sem as colunas/identificador esperados.")
        if raw["Id"] in result:
            raise ValueError("Amostra com identificador repetido; comparação recusada.")
        result[raw["Id"]] = {key: value.isoformat() if isinstance(value, (datetime, date)) else value
                             for key, value in raw.items()}
    return result


def changes(before, after):
    """Compara pelo Id do destino; não presume que novos IDs sejam o mesmo cadastro."""
    events = []
    for key in sorted(before.keys() | after.keys()):
        old, new = before.get(key), after.get(key)
        if old == new:
            continue
        kind = "INCLUIDO" if old is None else "REMOVIDO" if new is None else "ALTERADO"
        fields = [name for name in FIELDS if old is not None and new is not None and old[name] != new[name]]
        events.append({"tipo": kind, "id": key, "antes": old, "depois": new, "campos_alterados": fields})
    return events


class AfastamentoSource:
    def __init__(self, db, *, people=(), row_limit=10000):
        if type(row_limit) is not int or row_limit < 1:
            raise ValueError("O limite de linhas precisa ser inteiro positivo.")
        self.db = db
        if any(type(person) is not int or person <= 0 for person in people):
            raise ValueError("Use IdPessoa internos positivos no filtro de pessoas.")
        self.people = tuple(sorted(set(people)))
        self.row_limit = row_limit

    def fetch(self):
        condition = " WHERE IdPessoa IN (" + ",".join("?" for _ in self.people) + ")" if self.people else ""
        # Não usar NOLOCK: leituras sujas produziriam falsas inclusões/exclusões.
        # Espera de bloqueio curta e prioridade baixa; erro nunca vira uma amostra vazia.
        sql = ("SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; "
               "SELECT TOP (?) Id, IdPessoa, DataInicio, DataTermino, Causa, IdFreq "
               "FROM dbo.Afastamentos" + condition + " ORDER BY Id")
        rows = self.db.query(sql, (self.row_limit + 1, *self.people))
        if len(rows) > self.row_limit:
            raise ValueError("Limite de linhas excedido; filtre pessoas antes de continuar.")
        return rows


def write_report(folder, state):
    atomic_json(folder / "resumo.json", state)
    rows = []
    for event in reversed(state["eventos_recentes"]):
        old, new = event["antes"], event["depois"]
        person = (new or old)["IdPessoa"]
        display = lambda row: json.dumps(row, ensure_ascii=False) if row is not None else "—"
        cells = (event["observado_em"], event["tipo"], event["id"], person, display(old), display(new))
        rows.append("<tr>" + "".join("<td>" + escape(str(cell)) + "</td>" for cell in cells) + "</tr>")
    markers = []
    marker_file = folder / "anotacoes.jsonl"
    if marker_file.exists():
        for line in marker_file.read_text(encoding="utf-8").splitlines():
            try:
                marker = json.loads(line)
                markers.append("<li>" + escape(str(marker["instante"])) + " — " + escape(str(marker["nota"])) + "</li>")
            except (ValueError, KeyError):
                continue
    last_error = state.get("ultimo_erro")
    details = escape(json.dumps(last_error, ensure_ascii=False)) if last_error else "Nenhum"
    html = (
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Observação SQL</title>'
        '<style>body{font:15px sans-serif;margin:24px;color:#17212b}table{border-collapse:collapse;width:100%}'
        'th,td{border:1px solid #ccd3da;padding:8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}'
        'td:nth-last-child(-n+2){max-width:28em}th{background:#edf2f6}</style>'
        f"<h1>Observação de afastamentos — {escape(state['banco'])}</h1>"
        f"<p>Estado: <strong>{escape(state['status'])}</strong>. Início: {escape(state['inicio'])}. "
        f"Última amostra válida: {escape(str(state.get('ultima_amostra') or 'aguardando'))}.</p>"
        f"<p>Servidor: {escape(state['servidor'])}. Pessoas: {escape(str(state['pessoas'] or 'todas'))}. "
        f"Intervalo: {state['intervalo_segundos']}s. Duração prevista: {state['duracao_segundos']}s. Horários em UTC.</p>"
        f"<p>Registros iniciais: {state.get('linhas_iniciais', 'aguardando')}; atuais: {state.get('linhas_atuais', 'aguardando')}. "
        f"Amostras válidas: {state['amostras_validas']}; falhas de coleta: {state['falhas_coleta']}. "
        f"Incluídos: {state['totais']['INCLUIDO']}; removidos: {state['totais']['REMOVIDO']}; alterados: {state['totais']['ALTERADO']}.</p>"
        '<p>Este relatório observa apenas mudanças no destino SQL. Não confirma a ação no RH nem a execução do serviço. '
        'Uma remoção pode ter outra origem; um registro que surge e desaparece entre consultas pode não ser visto. '
        'Após falha de coleta, a próxima comparação abrange o intervalo desde a última amostra válida. '
        'Não há aprovação/reprovação automática de regras de negócio.</p>'
        f"<p>Último erro (sem mensagem sensível): {details}.</p>"
        '<h2>Anotações de ações manuais</h2><p>São declarações para correlação, não comprovação de execução.</p><ul>'
        + "".join(markers) + '</ul><h2>Últimas 200 mudanças observadas</h2>'
        '<p>O histórico completo fica em eventos.jsonl. Os estados inicial e mais recente ficam em inicial.json e atual.json.</p>'
        '<table><tr><th>Observado em UTC</th><th>Evento</th><th>Id</th><th>IdPessoa</th><th>Antes</th><th>Depois</th></tr>'
        + "".join(rows) + "</table></html>"
    )
    temp = folder / "relatorio.html.tmp"
    temp.write_text(html, encoding="utf-8")
    temp.replace(folder / "relatorio.html")


def observe(source, folder, *, server, database="bras1", people=(), duration=7200, interval=15,
            clock=time.monotonic, sleep=time.sleep, now=utc_now, max_errors=5):
    for value, label in ((duration, "duração"), (interval, "intervalo")):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"A {label} precisa ser um número positivo finito.")
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    state = {"status": "OBSERVANDO", "inicio": now(), "fim": None, "servidor": server, "banco": database,
             "pessoas": list(people), "intervalo_segundos": interval, "duracao_segundos": duration,
             "amostras_validas": 0, "falhas_coleta": 0, "eventos_recentes": [],
             "totais": {"INCLUIDO": 0, "REMOVIDO": 0, "ALTERADO": 0}, "pid": os.getpid()}
    start = clock()
    previous, previous_time = None, None
    consecutive_errors = 0
    write_report(folder, state)
    try:
        while True:
            if (folder / "parar.sinal").exists():
                state["status"] = "PARADO"
                break
            stamp, query_start = now(), clock()
            try:
                current = normalize_snapshot(source.fetch())
            except Exception as exc:
                consecutive_errors += 1
                state["falhas_coleta"] += 1
                state["status"] = "OBSERVANDO_COM_ERROS"
                error = {"instante": stamp, "tipo": type(exc).__name__}
                state["ultimo_erro"] = error
                append_json(folder / "erros.jsonl", error)
                if consecutive_errors >= max_errors:
                    state["status"] = "ERRO"
            else:
                consecutive_errors = 0
                state["status"] = "OBSERVANDO"
                state["amostras_validas"] += 1
                state["ultima_amostra"] = stamp
                state["linhas_atuais"] = len(current)
                state["ultima_consulta_ms"] = round((clock() - query_start) * 1000, 3)
                snapshot = {"instante": stamp, "linhas": list(current.values())}
                if previous is None:
                    atomic_json(folder / "inicial.json", snapshot)
                    state["linhas_iniciais"] = len(current)
                else:
                    for event in changes(previous, current):
                        event.update(observado_em=stamp, desde=previous_time)
                        append_json(folder / "eventos.jsonl", event)
                        state["totais"][event["tipo"]] += 1
                        state["eventos_recentes"].append(event)
                    state["eventos_recentes"] = state["eventos_recentes"][-200:]
                atomic_json(folder / "atual.json", snapshot)
                append_json(folder / "amostras.jsonl", {"instante": stamp, "linhas": len(current),
                                                       "consulta_ms": state["ultima_consulta_ms"]})
                previous, previous_time = current, stamp
            write_report(folder, state)
            if state["status"] == "ERRO":
                break
            if clock() - start >= duration:
                state["status"] = "FINALIZADO_COM_ERROS" if consecutive_errors else "FINALIZADO"
                break
            # Verifica o sinal de parada a cada segundo sem aumentar consultas SQL.
            next_sample = min(clock() + interval, start + duration)
            while clock() < next_sample and not (folder / "parar.sinal").exists():
                sleep(min(1, next_sample - clock()))
    except KeyboardInterrupt:
        state["status"] = "INTERROMPIDO"
    except Exception as exc:
        state["status"] = "ERRO"
        state["ultimo_erro"] = {"instante": now(), "tipo": type(exc).__name__}
    state["fim"] = now()
    write_report(folder, state)
    return state


@contextmanager
def observer_lock(base, *, label="observação SQL"):
    """Trava de processo liberada pelo Windows mesmo se o Python for encerrado."""
    import msvcrt

    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    with (base / "observador.lock").open("a+b") as lock:
        if lock.tell() == 0:
            lock.write(b"0")
            lock.flush()
        lock.seek(0)
        try:
            msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            raise RuntimeError(f"Já existe {label} em execução. Aguarde ou consulte o estado do processo.") from None
        try:
            yield
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


def run_observer(settings, base, *, duration=7200, interval=15, people=()):
    database = configured_database(settings)
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        raise ValueError("A duração precisa ser um número positivo finito.")
    if isinstance(interval, bool) or not isinstance(interval, (int, float)) or not math.isfinite(interval) or interval < 5:
        raise ValueError("Use intervalo de pelo menos 5 segundos para a observação passiva.")
    base = Path(base).resolve()
    with observer_lock(base):
        db = SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
        db.assert_database()
        source = AfastamentoSource(db, people=people)
        folder = base / (datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:8])
        folder.mkdir()
        atomic_json(base / "ativo.json", {"pid": os.getpid(), "pasta": str(folder), "inicio": utc_now(),
                                          "banco": database, "servidor": settings.sql_server})
        return observe(source, folder, server=settings.sql_server, people=source.people,
                       database=database, duration=duration, interval=interval)


def active_folder(base):
    base = Path(base).resolve()
    active = json.loads((base / "ativo.json").read_text(encoding="utf-8"))
    folder = Path(active["pasta"]).resolve()
    if not folder.is_relative_to(base) or folder == base:
        raise ValueError("Pasta de observação fora do diretório de relatórios.")
    return folder


def stop_observer(base):
    folder = active_folder(base)
    (folder / "parar.sinal").write_text(utc_now(), encoding="utf-8")
    return folder


def observer_status(base):
    folder = active_folder(base)
    state = json.loads((folder / "resumo.json").read_text(encoding="utf-8"))
    try:
        with observer_lock(base):
            running = False
    except RuntimeError:
        running = True
    state["processo_ativo"] = running
    if not running and state["status"].startswith("OBSERVANDO"):
        state["status"] = "ENCERRADO_SEM_FINALIZACAO"
    return folder, state


def annotate(base, note, *, metadata=None):
    if not note.strip():
        raise ValueError("Informe uma anotação não vazia.")
    entry = {"instante": utc_now(), "nota": note.strip()}
    if metadata is not None:
        from automatiza.casos_offline import criteria
        if not isinstance(metadata, dict) or metadata.get("tipo") not in {"incluir", "excluir", "recadastrar", "alterar"}:
            raise ValueError("Dados estruturados precisam ser um objeto com tipo de ação válido.")
        criteria(metadata)
        entry["dados"] = metadata
    folder = active_folder(base)
    append_json(folder / "anotacoes.jsonl", entry)
    state = json.loads((folder / "resumo.json").read_text(encoding="utf-8"))
    # O observador é o único escritor do resumo enquanto estiver rodando.
    if not state["status"].startswith("OBSERVANDO"):
        write_report(folder, state)
    return folder
