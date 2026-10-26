"""Conferência de expectativas usando apenas amostras e eventos já coletados."""

import math
from datetime import timedelta


def criteria(case, *, previous=False):
    from automatiza.analise import DELPHI_ZERO, period
    person = case.get("id_pessoa")
    if type(person) is not int or person <= 0:
        raise ValueError("Informe um IdPessoa interno positivo.")
    if not isinstance(case.get("causa"), str) or not case["causa"].strip() or "PREENCHER" in case["causa"].upper():
        raise ValueError("Informe a causa exata observada no destino.")
    start_key, end_key = ("inicio_anterior", "termino_anterior") if previous else ("inicio", "termino")
    start = period(case[start_key])
    end = period(case[end_key]) if case[end_key] is not None else None
    if end is not None and end < start and not (end == DELPHI_ZERO and case.get("permitir_termino_data_base") is True):
        raise ValueError("Término esperado anterior ao início.")
    return {"pessoa": person, "causa": case["causa"], "inicio": start, "termino": end,
            "id_freq": case.get("id_freq_anterior" if previous else "id_freq")}


def matches(row, target):
    from automatiza.analise import period
    try:
        return (row["IdPessoa"] == target["pessoa"] and row["Causa"] == target["causa"]
                and period(row["DataInicio"]) == target["inicio"]
                and (period(row["DataTermino"]) if row["DataTermino"] is not None else None) == target["termino"]
                and (target["id_freq"] is None or row["IdFreq"] == target["id_freq"]))
    except (ValueError, TypeError, KeyError, AttributeError):
        return False


def _positive(value, label):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{label} precisa ser positivo e finito.")
    return value


def evaluate_case(case, initial, events, samples, initial_at, cutoff, issues):
    from automatiza.analise import replay, utc
    output = {"id": str(case.get("id", "sem-identificador")), "status": "PENDENTE_CONFIGURACAO", "detalhe": ""}
    def finish(status, detail):
        output.update(status=status, detalhe=detail)
        return output
    if case.get("preparado") is not True:
        return finish("PENDENTE_CONFIGURACAO", "Dados e expectativa ainda não foram definidos para este caso.")
    try:
        kind = case["tipo"]
        if kind not in {"incluir", "excluir", "recadastrar", "ausencia"}:
            raise ValueError("Tipo precisa ser incluir, excluir, recadastrar ou ausencia.")
        target = criteria(case)
        old_target = criteria(case, previous=True) if kind == "recadastrar" else None
        if old_target is not None and (old_target["inicio"], old_target["termino"]) == (target["inicio"], target["termino"]):
            raise ValueError("O período de recadastro precisa ser diferente do anterior.")
        action = utc(case["registrado_em"])
        timeout = _positive(case.get("prazo_segundos", 180), "Prazo")
        stability = _positive(case.get("estabilidade_segundos", 15), "Estabilidade")
        max_gap = _positive(case.get("max_lacuna_segundos", 60), "Lacuna máxima")
        if stability >= timeout:
            raise ValueError("Estabilidade precisa ser menor que o prazo.")
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        return finish("CONFIGURACAO_INVALIDA", str(exc))
    if issues:
        return finish("INCONCLUSIVO_HISTORICO", "Há divergências nos arquivos coletados; não aprovar o caso com estas evidências.")
    if action < utc(initial_at):
        return finish("INCONCLUSIVO_SEM_BASELINE", "A ação foi informada antes da primeira amostra; não há estado anterior suficiente.")
    if action > cutoff:
        return finish("AGUARDANDO_AMOSTRA", "Ainda não há amostra posterior ao registro desta ação.")
    deadline = action + timedelta(seconds=timeout)
    before, after, baseline_ids, closing = None, [], set(), None
    for instant, state in replay(initial, events, samples):
        count = sum(matches(row, target) for row in state.values())
        old_count = sum(matches(row, old_target) for row in state.values()) if old_target is not None else None
        item = (instant, count, old_count)
        if instant >= deadline and closing is None:
            closing = item
        if instant <= action:
            before = item
            baseline_ids = {key for key, row in state.items() if matches(row, target)}
        elif instant <= deadline:
            after.append((*item, any(key in state for key in baseline_ids)))
    if before is None or (action - before[0]).total_seconds() > max_gap:
        return finish("INCONCLUSIVO_SEM_BASELINE", "Não há amostra anterior suficientemente próxima da ação.")
    expected_before = (1, 0) if kind == "recadastrar" else None
    baseline_ok = (before[1] == 1 if kind == "excluir" else before[1] == 0)
    if kind == "recadastrar":
        baseline_ok = (before[2], before[1]) == expected_before
    if not baseline_ok:
        return finish("INCONCLUSIVO_ESTADO_INICIAL", "O estado anterior não corresponde à pré-condição; não inferir inclusão/exclusão pela contagem final.")
    last_instant = before[0]
    stable_since, stable_samples = None, 0
    gaps, presence = False, False
    for instant, count, old_count, baseline_still_exists in after:
        gap = (instant - last_instant).total_seconds()
        if gap > max_gap:
            gaps = True
            stable_since, stable_samples = None, 0
        correct = count == (0 if kind in {"excluir", "ausencia"} else 1)
        if kind == "excluir":
            correct = correct and not baseline_still_exists
        if kind == "recadastrar":
            correct = correct and old_count == 0
        presence = presence or (kind == "ausencia" and count != 0)
        if correct:
            if stable_since is None:
                stable_since = instant
            stable_samples += 1
        else:
            stable_since, stable_samples = None, 0
        if kind != "ausencia" and stable_samples >= 2 and (instant - stable_since).total_seconds() >= stability:
            return finish("ATENDIDO_NO_DESTINO", "Estado esperado confirmado em amostras estáveis. Isso não comprova, por si só, a execução da ação no RH.")
        last_instant = instant
    if kind == "ausencia" and presence:
        return finish("NAO_ATENDIDO_NO_DESTINO", "Foi encontrada presença nas amostras de um período configurado para permanecer ausente.")
    if cutoff < deadline:
        return finish("AGUARDANDO", "Aguardando novas amostras dentro do prazo configurado.")
    if gaps or not after or (deadline - last_instant).total_seconds() > max_gap:
        return finish("INCONCLUSIVO_LACUNA", "A cobertura de coleta foi insuficiente para concluir a verificação na janela configurada.")
    if kind == "ausencia":
        if closing is None:
            return finish("INCONCLUSIVO_COLETA_FINAL", "Falta uma amostra que feche a janela de observação.")
        if closing[1] != 0:
            return finish("INCONCLUSIVO_LIMITE_AMOSTRAGEM", "Há presença na primeira amostra após o prazo; ela pode ter surgido no intervalo que atravessa o limite.")
        if (closing[0] - last_instant).total_seconds() > max_gap:
            return finish("INCONCLUSIVO_LACUNA", "A amostra que fecha a janela está distante demais da anterior.")
        return finish("ATENDIDO_NAS_AMOSTRAS", "Ausência nas amostras da janela. Não comprova que o serviço processou o evento nem ausência entre duas consultas.")
    return finish("NAO_CONFIRMADO_NO_PRAZO", "O estado esperado não ficou confirmado nas amostras até o prazo. Não equivale a afirmar o instante exato da importação.")


def evaluate_cases(cases, initial, events, samples, initial_at, cutoff, issues, observed_people=()):
    result, identifiers = [], set()
    for case in cases[:100]:
        if not isinstance(case, dict):
            result.append({"id": "inválido", "status": "CONFIGURACAO_INVALIDA", "detalhe": "O caso precisa ser um objeto JSON."})
            continue
        key = case.get("id")
        if not isinstance(key, str) or not key.strip() or key in identifiers:
            result.append({"id": str(key), "status": "CONFIGURACAO_INVALIDA", "detalhe": "Identificador vazio ou repetido."})
            continue
        identifiers.add(key)
        if observed_people and case.get("id_pessoa") not in observed_people:
            result.append({"id": key, "status": "INCONCLUSIVO_FORA_DO_FILTRO",
                           "detalhe": "Esta pessoa não faz parte do filtro da coleta; ausência de registros não pode aprovar o caso."})
            continue
        result.append(evaluate_case(case, initial, events, samples, initial_at, cutoff, issues))
    if len(cases) > 100:
        result.append({"id": "limite", "status": "CONFIGURACAO_INVALIDA", "detalhe": "Limite de 100 casos por sessão."})
    return result


def correlate_notes(notes, events):
    from automatiza.analise import utc
    result = []
    for note in notes:
        row = {"nota": str(note.get("nota", "")), "status": "SEM_FILTRO_ESTRUTURADO",
               "detalhe": "Anotação livre preservada; não foi interpretada como comando nem como caso aprovado."}
        metadata = note.get("dados")
        if not isinstance(metadata, dict):
            result.append(row)
            continue
        try:
            target = criteria(metadata)
            kinds = {"incluir": {"INCLUIDO"}, "excluir": {"REMOVIDO"}, "alterar": {"ALTERADO"},
                     "recadastrar": {"INCLUIDO", "ALTERADO"}}[metadata["tipo"]]
            recorded = utc(note["instante"])
            deadline = recorded + timedelta(seconds=_positive(metadata.get("prazo_segundos", 300), "Prazo"))
            candidates = [event for event in events if event["tipo"] in kinds
                          and recorded <= utc(event["observado_em"]) <= deadline
                          and matches(event["antes"] if event["tipo"] == "REMOVIDO" else event["depois"], target)]
        except (ValueError, KeyError, TypeError, AttributeError):
            row.update(status="FILTRO_INVALIDO", detalhe="Confira pessoa, tipo, causa, datas e horário da anotação.")
        else:
            if len(candidates) == 1:
                event = candidates[0]
                lower = max(0, (utc(event["desde"]) - recorded).total_seconds())
                upper = (utc(event["observado_em"]) - recorded).total_seconds()
                row.update(status="MUDANCA_COMPATIVEL", evento_id=event["id"],
                           atraso_min_segundos=lower, atraso_max_segundos=upper,
                           detalhe=f"Janela de {lower:g} a {upper:g}s desde a anotação; não é medida exata da importação nem prova de causalidade.")
            elif candidates:
                row.update(status="MULTIPLOS_CANDIDATOS", detalhe=f"{len(candidates)} mudanças compatíveis; não atribuir uma delas automaticamente.")
            else:
                row.update(status="NENHUMA_MUDANCA_COMPATIVEL", detalhe="Nenhum evento compatível encontrado até esta amostra; não comprova falha do serviço.")
        result.append(row)
    return result
