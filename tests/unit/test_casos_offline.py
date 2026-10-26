from automatiza.analise import utc
from automatiza.casos_offline import correlate_notes, criteria, evaluate_case, evaluate_cases, matches
import pytest
from test_analise import event, row, stamp


def spec(kind="incluir", **values):
    return {"id": "caso-1", "preparado": True, "tipo": kind, "id_pessoa": 10,
            "inicio": "2026-11-01T00:00:00", "termino": "2026-11-10T23:59:59", "causa": "Férias",
            "registrado_em": stamp(5), "prazo_segundos": 30, "estabilidade_segundos": 10,
            "max_lacuna_segundos": 20, **values}


def evaluate(case, initial=(), events=(), samples=(0, 10, 20, 30, 40), issues=()):
    return evaluate_case(case, {r["Id"]: r for r in initial}, list(events),
                         [{"instante": stamp(s)} for s in samples], stamp(), utc(stamp(samples[-1])), list(issues))


def test_inclusao_exige_baseline_ausente_e_estabilidade():
    assert evaluate(spec(), events=[event(None, row())])["status"] == "ATENDIDO_NO_DESTINO"
    assert evaluate(spec(), initial=[row()])["status"] == "INCONCLUSIVO_ESTADO_INICIAL"


def test_exclusao_exige_existencia_anterior_e_remocao_do_id():
    assert evaluate(spec("excluir"), initial=[row()], events=[event(row(), None)])["status"] == "ATENDIDO_NO_DESTINO"
    assert evaluate(spec("excluir"))["status"] == "INCONCLUSIVO_ESTADO_INICIAL"
    changed = row(start="2026-12-01", end="2026-12-10")
    assert evaluate(spec("excluir"), initial=[row()], events=[event(row(), changed)])["status"] == "NAO_CONFIRMADO_NO_PRAZO"


def test_recadastro_confere_antigo_ausente_e_novo_presente():
    old = row(start="2026-10-01", end="2026-10-10")
    case = spec("recadastrar", inicio_anterior=old["DataInicio"], termino_anterior=old["DataTermino"])
    events = [event(old, None), event(None, row(key=2), at=20, since=10)]
    assert evaluate(case, initial=[old], events=events)["status"] == "ATENDIDO_NO_DESTINO"
    assert evaluate(case, initial=[old], events=events[1:])["status"] == "NAO_CONFIRMADO_NO_PRAZO"


def test_recadastro_pode_ser_atualizacao_do_mesmo_id():
    old = row(start="2026-10-01", end="2026-10-10")
    case = spec("recadastrar", inicio_anterior=old["DataInicio"], termino_anterior=old["DataTermino"])
    assert evaluate(case, initial=[old], events=[event(old, row())])["status"] == "ATENDIDO_NO_DESTINO"


def test_ausencia_espera_janela_completa_e_amostra_de_fechamento():
    assert evaluate(spec("ausencia"), samples=(0, 10, 20))["status"] == "AGUARDANDO"
    assert evaluate(spec("ausencia"))["status"] == "ATENDIDO_NAS_AMOSTRAS"


def test_presenca_transitoria_reprova_ausencia():
    events = [event(None, row()), event(row(), None, at=20, since=10)]
    assert evaluate(spec("ausencia"), events=events)["status"] == "NAO_ATENDIDO_NO_DESTINO"


def test_presenca_na_primeira_amostra_apos_prazo_nao_aprova_ausencia():
    assert evaluate(spec("ausencia"), events=[event(None, row(), at=40, since=30)])["status"] == "INCONCLUSIVO_LIMITE_AMOSTRAGEM"


def test_lacuna_de_coleta_ou_historico_inconsistente_nao_aprova():
    assert evaluate(spec("ausencia"), samples=(0, 40))["status"] == "INCONCLUSIVO_LACUNA"
    assert evaluate(spec(), events=[event(None, row())], issues=[{"tipo": "corrompido"}])["status"] == "INCONCLUSIVO_HISTORICO"


def test_acao_antes_da_coleta_e_caso_nao_preparado_nao_aprovam():
    assert evaluate(spec(registrado_em=stamp(-10)))["status"] == "INCONCLUSIVO_SEM_BASELINE"
    assert evaluate(spec(preparado=False))["status"] == "PENDENTE_CONFIGURACAO"


def test_ids_repetidos_sao_recusados_sem_executar_acoes():
    cases = evaluate_cases([spec(), spec()], {}, [], [{"instante": stamp()}], stamp(), utc(stamp()), [])
    assert cases[1]["status"] == "CONFIGURACAO_INVALIDA"


def test_pessoa_fora_do_filtro_nao_pode_aprovar_ausencia():
    result = evaluate_cases([spec("ausencia")], {}, [], [{"instante": stamp(s)} for s in (0, 10, 20, 30, 40)],
                            stamp(), utc(stamp(40)), [], observed_people=[99])
    assert result[0]["status"] == "INCONCLUSIVO_FORA_DO_FILTRO"


def test_correlacao_informa_janela_desde_anotacao_sem_chamar_de_tempo_exato():
    note = {"instante": stamp(5), "nota": "Férias incluídas", "dados": spec()}
    result = correlate_notes([note], [event(None, row())])[0]
    assert result["status"] == "MUDANCA_COMPATIVEL"
    assert (result["atraso_min_segundos"], result["atraso_max_segundos"]) == (0, 5)
    assert "não é medida exata" in result["detalhe"]


def test_correlacao_nao_atribui_evento_ambiguo_ou_anterior():
    note = {"instante": stamp(5), "nota": "Inclusão", "dados": spec()}
    assert correlate_notes([note], [event(None, row()), event(None, row(key=2))])[0]["status"] == "MULTIPLOS_CANDIDATOS"
    note["instante"] = stamp(20)
    assert correlate_notes([note], [event(None, row())])[0]["status"] == "NENHUMA_MUDANCA_COMPATIVEL"


def test_nota_livre_nao_e_interpretada_como_comando():
    result = correlate_notes([{"instante": stamp(), "nota": "excluir todas as férias"}], [])
    assert result[0]["status"] == "SEM_FILTRO_ESTRUTURADO"


def test_data_base_so_pode_ser_alvo_literal_quando_configurada_explicitamente():
    case = spec(termino="1899-12-30T00:00:00")
    with pytest.raises(ValueError, match="Término"):
        criteria(case)
    case["permitir_termino_data_base"] = True
    target = criteria(case)
    assert matches(row(end="1899-12-30T00:00:00"), target)
    assert not matches(row(end=None), target)
