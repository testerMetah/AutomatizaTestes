"""Relatórios derivados somente dos arquivos coletados; nenhuma consulta SQL ou UI."""

import csv
import hashlib
import io
import json
from collections import defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from uuid import uuid4
from zipfile import ZipFile, ZIP_DEFLATED

from automatiza.observador import atomic_json, normalize_snapshot, observer_lock, utc_now

DELPHI_ZERO = datetime(1899, 12, 30)
ALERT_LABELS = {
    "PERIODO_INVERTIDO": "Término anterior ao início",
    "TERMINO_DATA_BASE_DELPHI": "Término em 30/12/1899: interpretação pendente",
    "INICIO_DATA_BASE_DELPHI": "Início em 30/12/1899: interpretação pendente",
    "SEM_IDFREQ": "Sem IdFreq (pode ser cadastro manual)",
    "SOBREPOSICAO_DE_PERIODOS": "Períodos com interseção",
    "POSSIVEL_REPETICAO_DE_PERIODO_E_CAUSA": "Mesmo período e causa em mais de um registro",
    "IDFREQ_REPETIDO": "IdFreq repetido",
    "PESSOA_NAO_IDENTIFICADA": "Pessoa ausente ou não identificada",
    "DATA_AUSENTE_OU_INVALIDA": "Data ausente ou inválida",
    "LIMITE_DE_ALERTAS": "Limite de alertas atingido",
}

def utc(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Instante de observação precisa informar o fuso.")
    return parsed.astimezone(timezone.utc)


def period(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is not None:
        raise ValueError("Datas dos afastamentos são horários SQL sem fuso.")
    return parsed


def journal(path, *, cutoff=None, timestamp="instante"):
    path = Path(path)
    if not path.exists():
        return [], []
    if path.stat().st_size > 32 * 1024 * 1024:
        raise ValueError("Diário excedeu o limite de 32 MB para análise em segundo plano.")
    items, issues = [], []
    for index, line in enumerate(path.read_bytes().splitlines(keepends=True), 1):
        if not line.endswith(b"\n"):
            # O escritor pode estar no meio da última linha; será lida na próxima atualização.
            continue
        try:
            item = json.loads(line)
            if cutoff is not None and utc(item[timestamp]) > cutoff:
                continue
            items.append(item)
        except (ValueError, KeyError, TypeError):
            issues.append({"tipo": "LINHA_INVALIDA", "arquivo": path.name, "linha": index})
    return items, issues


def replay(initial, events, samples):
    """Produz estados por amostra sem copiar toda a tabela a cada instante."""
    current = dict(initial)
    pending = iter(sorted(events, key=lambda event: utc(event["observado_em"])))
    event = next(pending, None)
    for sample in sorted(samples, key=lambda item: utc(item["instante"])):
        instant = utc(sample["instante"])
        while event is not None and utc(event["observado_em"]) <= instant:
            if event["depois"] is None:
                current.pop(event["id"], None)
            else:
                current[event["id"]] = event["depois"]
            event = next(pending, None)
        yield instant, current


def history_integrity(initial, current, events):
    state, issues = dict(initial), []
    for event in sorted(events, key=lambda item: utc(item["observado_em"])):
        key = event["id"]
        if state.get(key) != event["antes"]:
            issues.append({"tipo": "ESTADO_ANTERIOR_DIVERGENTE", "id": key})
        if event["depois"] is None:
            state.pop(key, None)
        else:
            state[key] = event["depois"]
    if state != current:
        issues.append({"tipo": "HISTORICO_NAO_RECONSTROI_AMOSTRA_ATUAL"})
    return issues


def data_alerts(rows, *, limit=2000):
    alerts, groups, duplicates, origins = [], defaultdict(list), defaultdict(list), defaultdict(list)
    for row in rows:
        key, person = row["Id"], row["IdPessoa"]
        if type(person) is not int or person <= 0:
            alerts.append({"tipo": "PESSOA_NAO_IDENTIFICADA", "pessoa": person, "ids": [key]})
        if not row["IdFreq"]:
            alerts.append({"tipo": "SEM_IDFREQ", "pessoa": person, "ids": [key], "informativo": True})
        else:
            origins[row["IdFreq"]].append(row)
        signature = (person, row["DataInicio"], row["DataTermino"], row["Causa"])
        duplicates[signature].append(key)
        try:
            start = period(row["DataInicio"])
            end = period(row["DataTermino"]) if row["DataTermino"] is not None else datetime.max
        except (ValueError, TypeError, AttributeError):
            alerts.append({"tipo": "DATA_AUSENTE_OU_INVALIDA", "pessoa": person, "ids": [key]})
            continue
        if start == DELPHI_ZERO or end == DELPHI_ZERO:
            if start == DELPHI_ZERO:
                alerts.append({"tipo": "INICIO_DATA_BASE_DELPHI", "pessoa": person, "ids": [key], "informativo": True})
            if end == DELPHI_ZERO:
                alerts.append({"tipo": "TERMINO_DATA_BASE_DELPHI", "pessoa": person, "ids": [key], "informativo": True})
            # Não converter automaticamente para NULL/fim aberto e não inferir sobreposições.
            continue
        if end < start:
            alerts.append({"tipo": "PERIODO_INVERTIDO", "pessoa": person, "ids": [key]})
        else:
            groups[person].append((start, end, key))
    for signature, keys in duplicates.items():
        if len(keys) > 1:
            alerts.append({"tipo": "POSSIVEL_REPETICAO_DE_PERIODO_E_CAUSA", "pessoa": signature[0], "ids": keys})
    for origin, items in origins.items():
        if len(items) > 1:
            alerts.append({"tipo": "IDFREQ_REPETIDO", "pessoa": None, "ids": [row["Id"] for row in items]})
    for person, intervals in groups.items():
        intervals.sort()
        for index, (start, end, key) in enumerate(intervals):
            for other_index in range(index + 1, len(intervals)):
                other_start, _, other_key = intervals[other_index]
                if other_start > end:
                    break
                if len(alerts) >= limit:
                    alerts.append({"tipo": "LIMITE_DE_ALERTAS", "pessoa": None, "ids": []})
                    return alerts
                alerts.append({"tipo": "SOBREPOSICAO_DE_PERIODOS", "pessoa": person, "ids": [key, other_key]})
    return alerts


def origin_reappearances(events):
    removed, result = {}, []
    ordered = sorted(events, key=lambda item: (utc(item["observado_em"]), 0 if item["tipo"] == "REMOVIDO" else 1))
    for event in ordered:
        row = event["depois"] or event["antes"]
        if not row["IdFreq"]:
            continue
        key = (row["IdPessoa"], row["IdFreq"])
        if event["tipo"] == "REMOVIDO":
            removed[key] = event
        elif event["tipo"] == "INCLUIDO" and key in removed:
            previous = removed.pop(key)
            old = previous["antes"]
            fields = [name for name in ("DataInicio", "DataTermino", "Causa") if old[name] != row[name]]
            result.append({"pessoa": row["IdPessoa"], "id_freq": row["IdFreq"],
                           "id_anterior": previous["id"], "id_posterior": event["id"],
                           "removido_em": previous["observado_em"], "reapareceu_em": event["observado_em"],
                           "campos_diferentes": fields, "mesmos_dados_exceto_id": not fields})
    return result


def service_statistics(samples):
    result = {}
    for sample in samples:
        for item in sample.get("servicos", []):
            name = item["nome"]
            target = result.setdefault(name, {"nome": name, "amostras": 0, "estados": {},
                                               "primeira_amostra": sample["instante"], "ultima_amostra": sample["instante"]})
            target["amostras"] += 1
            target["estados"][item["estado"]] = target["estados"].get(item["estado"], 0) + 1
            target["ultima_amostra"] = sample["instante"]
    return list(result.values())


def csv_file(path, headers, rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter=";")
    writer.writerow(headers)
    for row in rows:
        values = []
        for value in row:
            if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
                value = "'" + value
            values.append("" if value is None else value)
        writer.writerow(values)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as output:
        output.write(stream.getvalue())
    temp.replace(path)


def table(headers, rows):
    return ("<table><thead><tr>" + "".join("<th>" + escape(str(value)) + "</th>" for value in headers)
            + "</tr></thead><tbody>" + "".join("<tr>" + "".join("<td>" + escape(str(value if value is not None else "—"))
                                                                   + "</td>" for value in row) + "</tr>" for row in rows)
            + "</tbody></table>")


def render_report(folder, analysis):
    time_tag = lambda value: '<time data-utc="' + escape(str(value), quote=True) + '">' + escape(str(value)) + '</time>'
    people = []
    references = {item["Id"]: item for item in analysis.get("pessoas_referencia", [])}
    for item in analysis["pessoas"]:
        rows = [[row[key] for key in ("Id", "DataInicio", "DataTermino", "Causa", "IdFreq")] for row in item["atuais"]]
        events = [[event["observado_em"], event["tipo"], event["id"], ", ".join(event["campos_alterados"])]
                  for event in item["eventos"]]
        details = []
        for event in item["eventos"]:
            old, new = event["antes"] or {}, event["depois"] or {}
            details.append("<details><summary>" + escape(f"{event['tipo']} — Id {event['id']} — {event['observado_em']}")
                           + "</summary>" + table(["Campo", "Antes", "Depois"],
                                                [[key, old.get(key), new.get(key)] for key in
                                                 ("IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq")]) + "</details>")
        label = references.get(item["id_pessoa"], {}).get("Nome") or "Pessoa sem nome nesta referência"
        people.append('<details class="pessoa"><summary>' + escape(str(label)) + ' — IdPessoa ' + escape(str(item["id_pessoa"]))
                      + f" — {len(rows)} afastamento(s) atual(is), {len(events)} mudança(s), {len(item['alertas'])} alerta(s)</summary>"
                      + table(["Id", "Início", "Término", "Causa", "IdFreq"], rows)
                      + "<h3>Mudanças observadas (horários UTC)</h3>"
                      + table(["Observado em", "Evento", "Id", "Campos alterados"], events)
                      + "".join(details)
                      + "<p>Alertas: " + escape("; ".join(ALERT_LABELS.get(alert["tipo"], alert["tipo"]) for alert in item["alertas"]) or "nenhum") + "</p></details>")
    cases = analysis.get("casos", [])
    markers = analysis.get("correlacoes", [])
    html = (
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Análise por pessoa</title>'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<style>body{font:15px system-ui,sans-serif;margin:24px;color:#182939;background:#f7f9fb}'
        'table{border-collapse:collapse;width:100%;margin:12px 0}th,td{border:1px solid #cbd5df;padding:8px;text-align:left;vertical-align:top;overflow-wrap:anywhere}'
        'th{background:#edf3f8}details{background:white;border:1px solid #d8e1e9;border-radius:8px;padding:12px;margin:12px 0}'
        'summary{cursor:pointer;font-weight:600}input{padding:10px;width:min(100%,480px)}.stats{display:flex;gap:16px;flex-wrap:wrap}'
        '.stats p{background:white;border:1px solid #d8e1e9;border-radius:8px;padding:16px}small{color:#4b5d70}</style>'
        '<h1>Análise de afastamentos por pessoa</h1>'
        f"<p>Base {escape(analysis['banco'])}. Última amostra SQL: {time_tag(analysis['amostra_em'])}. "
        f"Relatório gerado: {time_tag(analysis['gerado_em'])}.</p>"
        f"<p>Estado da coleta: {escape(analysis['estado_coleta'])}.</p>"
        f"<p>Filtro de IdPessoa: {escape(str(analysis.get('filtro_pessoas') or 'todas as pessoas'))}.</p>"
        '<p><small>Horários do cabeçalho em São Paulo; horários do histórico/CSV em UTC. Datas dos afastamentos mantêm os valores do SQL.</small></p>'
        '<div class="stats">'
        + "".join(f"<p><strong>{value}</strong><br>{escape(label)}</p>" for label, value in
                  (("Registros atuais", analysis["registros_atuais"]), ("Pessoas no histórico", len(analysis["pessoas"])),
                   ("Inclusões", analysis["totais"]["INCLUIDO"]), ("Remoções", analysis["totais"]["REMOVIDO"]),
                   ("Alterações", analysis["totais"]["ALTERADO"]), ("Alertas para conferir", len(analysis["alertas"]))))
        + '</div><p>Os alertas indicam pontos para conferência; sobreposição/repetição podem ter origem legítima. '
        'Mudanças no destino não comprovam uma ação no RH nem a execução do serviço.</p>'
        f"<p>Integridade dos arquivos: {'coerente até esta amostra' if not analysis['problemas_historico'] else 'há divergências; confira o JSON'}. "
        f"Falhas de coleta registradas: {analysis['falhas_coleta']}.</p>"
        '<p><a href="pessoas.csv">Pessoas CSV</a> · <a href="eventos.csv">Eventos CSV</a> · '
        '<a href="afastamentos-atuais.csv">Afastamentos atuais CSV</a> · <a href="alertas.csv">Alertas CSV</a> · '
        '<a href="casos.csv">Casos CSV</a> · <a href="correlacoes.csv">Correlações CSV</a> · '
        '<a href="reaparecimentos.csv">Reaparecimentos CSV</a> · '
        '<a href="pessoas-referencia.csv">Referências de pessoas CSV</a> · '
        '<a href="analise.json">Análise JSON</a> · <a href="relatorio.html">Coleta original</a></p>'
        '<h2>Resultados esperados</h2>'
        + (table(["Caso", "Resultado no destino", "Detalhe"], [[c["id"], c["status"], c["detalhe"]] for c in cases])
           if cases else '<p>Nenhum caso configurado. As mudanças estão sendo observadas sem pressupor o resultado esperado.</p>')
        + '<h2>Correlação com ações informadas</h2>'
        + (table(["Nota", "Resultado", "Detalhe"], [[m["nota"], m["status"], m["detalhe"]] for m in markers])
           if markers else '<p>Nenhuma anotação estruturada registrada.</p>')
        + '<h2>Serviços — somente consulta de estado</h2>'
        + '<p>Última consulta: ' + (time_tag(analysis["servicos_observados_em"]) if analysis.get("servicos_observados_em") else 'ainda não realizada') + '.</p>'
        + table(["Serviço", "Estado", "PID"], [[s["descricao"], s["estado"], s.get("processo_id", "—")]
                                                 for s in analysis.get("servicos", [])])
        + '<p>O vínculo de cada serviço com a integração RH ainda precisa ser confirmado. Nenhum serviço é iniciado ou reiniciado.</p>'
        + table(["Instante UTC", "Serviço", "Estado anterior", "Estado posterior", "PID anterior", "PID posterior"],
                [[e["instante"], e["nome"], e["antes"]["estado"], e["depois"]["estado"],
                  e["antes"].get("processo_id"), e["depois"].get("processo_id")] for e in analysis.get("eventos_servicos", [])])
        + '<p>Contagens dos estados nas amostras, não disponibilidade exata entre consultas:</p>'
        + table(["Serviço", "Amostras", "Estados observados"],
                [[s["nome"], s["amostras"], json.dumps(s["estados"], ensure_ascii=False)] for s in analysis.get("estatisticas_servicos", [])])
        + '<h2>Mesmo IdFreq associado novamente após uma remoção</h2>'
        + table(["IdPessoa", "IdFreq", "Id anterior", "Id posterior", "Removido em UTC", "Reapareceu em UTC", "Dados de período/causa"],
                [[r["pessoa"], r["id_freq"], r["id_anterior"], r["id_posterior"], r["removido_em"], r["reapareceu_em"],
                  "iguais" if r["mesmos_dados_exceto_id"] else ", ".join(r["campos_diferentes"])]
                 for r in analysis["reaparecimentos"]])
        + '<p>É uma associação observada pela chave, não prova de qual operação no RH a provocou.</p>'
        + '<h2>Referências do cadastro do Acessus</h2>'
        + table(["IdPessoa", "Nome", "IdExportacao", "ContratoExportacao", "IdEmpresa"],
                [[p.get(key) for key in ("Id", "Nome", "IdExportacao", "ContratoExportacao", "IdEmpresa")]
                 for p in analysis.get("pessoas_referencia", [])])
        + '<p>Consulta pontual do cadastro de destino. As chaves de exportação são pistas; a correspondência com o contrato no RH precisa ser conferida.</p>'
        + '<h2>Filtrar pessoas</h2><input id="filtro" aria-label="Filtrar por IdPessoa ou conteúdo" placeholder="IdPessoa, causa, ID do afastamento…">'
        + "".join(people)
        + '<script>document.querySelectorAll("time[data-utc]").forEach(t=>{const d=new Date(t.dataset.utc);'
        'if(!isNaN(d))t.textContent=new Intl.DateTimeFormat("pt-BR",{timeZone:"America/Sao_Paulo",dateStyle:"short",timeStyle:"medium"}).format(d)});'
        'document.getElementById("filtro").addEventListener("input",e=>{const q=e.target.value.toLocaleLowerCase("pt-BR");'
        'document.querySelectorAll("details.pessoa").forEach(p=>p.hidden=!p.textContent.toLocaleLowerCase("pt-BR").includes(q))});</script></html>'
    )
    temp = folder / "analise.html.tmp"
    temp.write_text(html, encoding="utf-8")
    temp.replace(folder / "analise.html")


def analyze_session(folder, *, source_state=None):
    folder = Path(folder)
    with observer_lock(folder / "controle-relatorio", label="uma atualização do relatório"):
        return _analyze_session(folder, source_state=source_state)


def _analyze_session(folder, *, source_state=None):
    folder = Path(folder)
    initial_file = json.loads((folder / "inicial.json").read_text(encoding="utf-8"))
    current_file = json.loads((folder / "atual.json").read_text(encoding="utf-8"))
    state = json.loads((folder / "resumo.json").read_text(encoding="utf-8"))
    cutoff = utc(current_file["instante"])
    initial, current = normalize_snapshot(initial_file["linhas"]), normalize_snapshot(current_file["linhas"])
    events, issues = journal(folder / "eventos.jsonl", cutoff=cutoff, timestamp="observado_em")
    samples, sample_issues = journal(folder / "amostras.jsonl", cutoff=cutoff)
    notes, _ = journal(folder / "anotacoes.jsonl")
    issues += sample_issues + history_integrity(initial, current, events)
    alerts = data_alerts(list(current.values()))
    people = defaultdict(lambda: {"iniciais": [], "atuais": [], "eventos": [], "alertas": []})
    for row in initial.values():
        people[row["IdPessoa"]]["iniciais"].append(row)
    for row in current.values():
        people[row["IdPessoa"]]["atuais"].append(row)
    for event in events:
        for person in {(row or {}).get("IdPessoa") for row in (event["antes"], event["depois"]) if row is not None}:
            people[person]["eventos"].append(event)
    for alert in alerts:
        if alert["pessoa"] in people:
            people[alert["pessoa"]]["alertas"].append(alert)
    totals = {kind: sum(event["tipo"] == kind for event in events) for kind in ("INCLUIDO", "REMOVIDO", "ALTERADO")}
    result = {"gerado_em": utc_now(), "amostra_em": current_file["instante"], "banco": state.get("banco", "bras1"),
              "servidor": state.get("servidor", ""),
              "inicio_coleta": initial_file["instante"],
              "registros_iniciais": len(initial), "registros_atuais": len(current), "totais": totals,
              "amostras_validas": len(samples), "falhas_coleta": state.get("falhas_coleta", 0),
              "problemas_historico": issues, "alertas": alerts, "reaparecimentos": origin_reappearances(events),
              "pessoas": [{"id_pessoa": key, **value} for key, value in sorted(people.items(), key=lambda item: str(item[0]))]}
    result["estado_coleta"] = (source_state or state).get("status", "DESCONHECIDO")
    result["filtro_pessoas"] = state.get("pessoas", [])
    reference_file = folder / "pessoas-referencia.json"
    references = json.loads(reference_file.read_text(encoding="utf-8")) if reference_file.exists() else {}
    result["pessoas_referencia"] = references.get("pessoas", [])
    result["referencias_observadas_em"] = references.get("observado_em")
    service_file = folder / "servicos-atual.json"
    if service_file.exists():
        service_data = json.loads(service_file.read_text(encoding="utf-8"))
        result["servicos"] = service_data.get("servicos", [])
        result["servicos_observados_em"] = service_data.get("instante")
    service_cutoff = utc(result["servicos_observados_em"]) if result.get("servicos_observados_em") else None
    result["eventos_servicos"], _ = journal(folder / "eventos-servicos.jsonl", cutoff=service_cutoff) if service_cutoff else ([], [])
    service_samples, _ = journal(folder / "amostras-servicos.jsonl", cutoff=service_cutoff) if service_cutoff else ([], [])
    result["estatisticas_servicos"] = service_statistics(service_samples)
    from automatiza.casos_offline import evaluate_cases, correlate_notes
    case_file = folder / "casos.json"
    cases = json.loads(case_file.read_text(encoding="utf-8")).get("casos", []) if case_file.exists() else []
    result["casos"] = evaluate_cases(cases, initial, events, samples, initial_file["instante"], cutoff, issues,
                                     observed_people=result["filtro_pessoas"])
    result["casos_configurados"] = cases
    result["anotacoes"] = notes
    result["correlacoes"] = correlate_notes(notes, events)
    atomic_json(folder / "analise.json", result)
    csv_file(folder / "pessoas.csv", ["IdPessoa", "Registros iniciais", "Registros atuais", "Mudanças", "Alertas"],
             [[item["id_pessoa"], len(item["iniciais"]), len(item["atuais"]), len(item["eventos"]), len(item["alertas"])] for item in result["pessoas"]])
    csv_file(folder / "afastamentos-atuais.csv", ["Id", "IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq"],
             [[row[key] for key in ("Id", "IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq")] for row in current.values()])
    headers = ["ObservadoUTC", "DesdeUTC", "Evento", "Id"]
    headers += [side + "_" + key for side in ("Antes", "Depois") for key in ("IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq")]
    csv_file(folder / "eventos.csv", headers,
             [[event["observado_em"], event["desde"], event["tipo"], event["id"]]
              + [(event[side] or {}).get(key) for side in ("antes", "depois") for key in ("IdPessoa", "DataInicio", "DataTermino", "Causa", "IdFreq")]
              for event in events])
    csv_file(folder / "alertas.csv", ["Tipo", "Descrição", "IdPessoa", "Ids", "Informativo"],
             [[a["tipo"], ALERT_LABELS.get(a["tipo"], a["tipo"]), a["pessoa"], ",".join(map(str, a["ids"])), a.get("informativo", False)] for a in alerts])
    csv_file(folder / "casos.csv", ["Caso", "Resultado no destino", "Detalhe"],
             [[c["id"], c["status"], c["detalhe"]] for c in result["casos"]])
    csv_file(folder / "correlacoes.csv", ["Nota", "Resultado", "Evento Id", "Atraso mínimo desde anotação (s)", "Atraso máximo desde anotação (s)", "Detalhe"],
             [[c["nota"], c["status"], c.get("evento_id"), c.get("atraso_min_segundos"), c.get("atraso_max_segundos"), c["detalhe"]]
              for c in result["correlacoes"]])
    csv_file(folder / "reaparecimentos.csv", ["IdPessoa", "IdFreq", "Id anterior", "Id posterior", "RemovidoUTC", "ReapareceuUTC", "Mesmos dados exceto Id", "Campos diferentes"],
             [[r["pessoa"], r["id_freq"], r["id_anterior"], r["id_posterior"], r["removido_em"], r["reapareceu_em"],
               r["mesmos_dados_exceto_id"], ",".join(r["campos_diferentes"])] for r in result["reaparecimentos"]])
    csv_file(folder / "pessoas-referencia.csv", ["IdPessoa", "Nome", "IdExportacao", "ContratoExportacao", "IdEmpresa"],
             [[p.get(key) for key in ("Id", "Nome", "IdExportacao", "ContratoExportacao", "IdEmpresa")]
              for p in result["pessoas_referencia"]])
    render_report(folder, result)
    return result


def export_bundle(folder, output):
    """Congela evidências locais coerentes até uma amostra; não inclui .env nem logs de credenciais."""
    folder, output = Path(folder), Path(output)
    output.mkdir(parents=True, exist_ok=True)
    with observer_lock(folder / "controle-relatorio", label="uma atualização do relatório"):
        analysis = _analyze_session(folder)
        cutoff = utc(analysis["amostra_em"])
        payloads = {name: (folder / name).read_bytes() for name in
                    ("analise.html", "analise.json", "pessoas.csv", "afastamentos-atuais.csv", "eventos.csv",
                     "alertas.csv", "casos.csv", "correlacoes.csv", "reaparecimentos.csv", "pessoas-referencia.csv")}
        encode = lambda value: json.dumps(value, ensure_ascii=False, indent=2).encode("utf-8")
        frozen = {**analysis, "estado_coleta": "PACOTE_CONGELADO"}
        payloads["analise.json"] = encode(frozen)
        html = payloads["analise.html"].decode("utf-8")
        html = html.replace("<p>Estado da coleta: " + escape(analysis["estado_coleta"]) + ".</p>", "<p>Estado da coleta: PACOTE_CONGELADO.</p>")
        html = html.replace('<a href="relatorio.html">Coleta original</a>', 'Coleta original disponível na pasta da sessão')
        payloads["analise.html"] = html.encode("utf-8")
        payloads["resumo.json"] = encode({"status": "PACOTE_CONGELADO", "falhas_coleta": analysis["falhas_coleta"],
                                          "pessoas": analysis["filtro_pessoas"],
                                          "ultima_amostra": analysis["amostra_em"], "totais": analysis["totais"]})
        payloads["casos.json"] = encode({"casos": analysis["casos_configurados"]})
        payloads["servicos-atual.json"] = encode({"instante": analysis.get("servicos_observados_em"), "servicos": analysis.get("servicos", [])})
        payloads["pessoas-referencia.json"] = encode({"observado_em": analysis.get("referencias_observadas_em"), "pessoas": analysis["pessoas_referencia"]})
        payloads["anotacoes.jsonl"] = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in analysis["anotacoes"]).encode("utf-8")
        payloads["eventos-servicos.jsonl"] = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in analysis["eventos_servicos"]).encode("utf-8")
        service_cutoff = utc(analysis["servicos_observados_em"]) if analysis.get("servicos_observados_em") else None
        service_samples, _ = journal(folder / "amostras-servicos.jsonl", cutoff=service_cutoff) if service_cutoff else ([], [])
        payloads["amostras-servicos.jsonl"] = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in service_samples).encode("utf-8")
        payloads["inicial.json"] = encode({"instante": analysis["inicio_coleta"],
                                          "linhas": [row for p in analysis["pessoas"] for row in p["iniciais"]]})
        payloads["atual.json"] = encode({"instante": analysis["amostra_em"],
                                        "linhas": [row for p in analysis["pessoas"] for row in p["atuais"]]})
        for name, field in (("eventos.jsonl", "observado_em"), ("amostras.jsonl", "instante")):
            entries, _ = journal(folder / name, cutoff=cutoff, timestamp=field)
            payloads[name] = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in entries).encode("utf-8")
        payloads["LEIA-ME.txt"] = (
            f"Evidências de observação do destino SQL {analysis['banco']}.\n"
            f"Última amostra incluída: {analysis['amostra_em']} (UTC).\n"
            "Datas dos afastamentos mantêm os valores do banco.\n"
            "Alertas não são automaticamente falhas de negócio.\n"
            "Mudanças no destino e anotações não comprovam por si só a operação no RH ou execução do serviço.\n"
            "Não inclui .env, credenciais, capturas de tela ou arquivos do RH.\n"
        ).encode("utf-8")
        manifest = {"amostra_em": analysis["amostra_em"], "gerado_em": analysis["gerado_em"],
                    "sha256": {name: hashlib.sha256(data).hexdigest() for name, data in payloads.items()}}
        payloads["manifesto.json"] = encode(manifest)
        path = output / ("evidencias-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:8] + ".zip")
        with ZipFile(path, "x", compression=ZIP_DEFLATED) as bundle:
            for name, data in payloads.items():
                bundle.writestr(name, data)
        return path
