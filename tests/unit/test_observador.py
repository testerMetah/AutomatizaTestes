import json
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from automatiza.config import Settings
from automatiza.observador import (AfastamentoSource, active_folder, annotate, changes,
                                  normalize_snapshot, observe, observer_lock, observer_status, run_observer,
                                  stop_observer)


def row(key=1, person=10, start="2026-10-20T00:00:00", end="2026-10-25T23:59:59"):
    return {"Id": key, "IdPessoa": person, "DataInicio": start, "DataTermino": end,
            "Causa": "Férias", "IdFreq": "origem-1"}


class Clock:
    time = 0

    def now(self):
        return self.time

    def sleep(self, seconds):
        self.time += seconds


def run(tmp_path, snapshots, duration, **kwargs):
    source = MagicMock()
    source.fetch.side_effect = snapshots
    clock = Clock()
    result = observe(source, tmp_path, server="teste", duration=duration, interval=1,
                     clock=clock.now, sleep=clock.sleep, now=lambda: str(clock.time), **kwargs)
    return result


def test_baseline_nao_e_reportada_como_inclusao(tmp_path):
    state = run(tmp_path, [[row()], [row()]], 1)
    assert state["status"] == "FINALIZADO"
    assert state["amostras_validas"] == 2
    assert sum(state["totais"].values()) == 0
    assert json.loads((tmp_path / "inicial.json").read_text(encoding="utf-8"))["linhas"] == [row()]


def test_cadastro_alteracao_exclusao_e_novo_id_sao_preservados(tmp_path):
    original, modified, new_id = row(), row(start="2026-11-01T00:00:00"), row(key=2)
    state = run(tmp_path, [[], [original], [modified], [], [new_id]], 4)
    assert state["totais"] == {"INCLUIDO": 2, "REMOVIDO": 1, "ALTERADO": 1}
    events = [json.loads(line) for line in (tmp_path / "eventos.jsonl").read_text(encoding="utf-8").splitlines()]
    assert events[1]["campos_alterados"] == ["DataInicio"]
    assert events[2]["antes"] == modified
    assert events[3]["id"] == 2


def test_erro_de_coleta_nao_vira_falsa_remocao_e_nao_expoe_senha(tmp_path):
    state = run(tmp_path, [[row()], RuntimeError("senha-na-excecao"), [row()]], 2)
    assert state["status"] == "FINALIZADO"
    assert state["falhas_coleta"] == 1
    assert sum(state["totais"].values()) == 0
    assert "senha-na-excecao" not in (tmp_path / "relatorio.html").read_text(encoding="utf-8")


def test_mudanca_depois_da_falha_mantem_limites_da_ultima_amostra_valida(tmp_path):
    state = run(tmp_path, [[row()], RuntimeError(), []], 2)
    event = state["eventos_recentes"][0]
    assert event["tipo"] == "REMOVIDO"
    assert event["desde"] == "0"
    assert event["observado_em"] == "2"


def test_erros_consecutivos_encerram_sem_chamar_isso_de_falha_de_negocio(tmp_path):
    state = run(tmp_path, [RuntimeError(), RuntimeError()], 10, max_errors=2)
    assert state["status"] == "ERRO"
    assert state["falhas_coleta"] == 2
    assert state["amostras_validas"] == 0


def test_sinal_de_parada_nao_toca_banco(tmp_path):
    (tmp_path / "parar.sinal").touch()
    source = MagicMock()
    state = observe(source, tmp_path, server="teste")
    assert state["status"] == "PARADO"
    source.fetch.assert_not_called()


def test_consulta_e_fixa_parametrizada_e_recusa_amostra_truncada():
    db = MagicMock()
    db.query.return_value = [row(), row(key=2)]
    source = AfastamentoSource(db, people=[11, 10, 10], row_limit=1)
    with pytest.raises(ValueError, match="Limite de linhas"):
        source.fetch()
    sql, params = db.query.call_args.args
    assert "SET LOCK_TIMEOUT 1000" in sql
    assert "IdPessoa IN (?,?)" in sql
    assert params == (2, 10, 11)
    assert "NOLOCK" not in sql


def test_identificadores_repetidos_ou_colunas_incompletas_recusados():
    with pytest.raises(ValueError, match="repetido"):
        normalize_snapshot([row(), row()])
    with pytest.raises(ValueError, match="colunas"):
        normalize_snapshot([{"Id": 1}])
    sample = row()
    sample["DataInicio"] = datetime(2026, 10, 15)
    assert normalize_snapshot([sample])[1]["DataInicio"] == "2026-10-15T00:00:00"


def test_anotacao_e_parada_nao_escrevem_fora_da_pasta_de_relatorios(tmp_path):
    (tmp_path / "ativo.json").write_text(json.dumps({"pasta": str(tmp_path.parent)}), encoding="utf-8")
    with pytest.raises(ValueError, match="fora"):
        stop_observer(tmp_path)
    with pytest.raises(ValueError, match="fora"):
        annotate(tmp_path, "teste")


def test_anotacao_fica_no_relatorio_escapada(tmp_path):
    folder = tmp_path / "sessao"
    folder.mkdir()
    run(folder, [[row()], [row()]], 1)
    (tmp_path / "ativo.json").write_text(json.dumps({"pasta": str(folder)}), encoding="utf-8")
    annotate(tmp_path, "<script>acao</script>")
    html = (folder / "relatorio.html").read_text(encoding="utf-8")
    assert "<script>" not in html
    assert "&lt;script&gt;acao" in html


def test_trava_impede_dois_observadores_ao_mesmo_tempo(tmp_path):
    with observer_lock(tmp_path):
        with pytest.raises(RuntimeError, match="Já existe"):
            with observer_lock(tmp_path):
                pytest.fail("Segunda execução não deveria obter a trava")
    with observer_lock(tmp_path):
        pass


def test_base_ausente_ou_intervalo_excessivo_sao_recusados_antes_de_conectar(tmp_path):
    with pytest.raises(ValueError, match="SQL_DATABASE"):
        run_observer(Settings(), tmp_path)
    with pytest.raises(ValueError, match="pelo menos 5"):
        run_observer(Settings(sql_database="bras1"), tmp_path, interval=0.1)


def test_base_variavel_e_gravada_na_sessao_e_repassada_ao_observador(tmp_path):
    with patch('automatiza.observador.SqlServer', autospec=True) as db_class, patch('automatiza.observador.observe') as observe_mock:
        run_observer(Settings(sql_database='teste-ferias', sql_server='servidor-teste'), tmp_path)
    db_class.return_value.assert_database.assert_called_once()
    assert observe_mock.call_args.kwargs['database'] == 'teste-ferias'
    active = json.loads((tmp_path / 'ativo.json').read_text(encoding='utf-8'))
    assert active['banco'] == 'teste-ferias'
    assert active['servidor'] == 'servidor-teste'


def test_relatorio_do_observador_usa_base_da_execucao_e_escapa_html(tmp_path):
    state = run(tmp_path, [[row()], [row()]], 1, database='teste<ferias>')
    assert state['banco'] == 'teste<ferias>'
    html = (tmp_path / 'relatorio.html').read_text(encoding='utf-8')
    assert 'teste&lt;ferias&gt;' in html
    assert 'teste<ferias>' not in html


def test_status_nao_diz_que_processo_encerrado_ainda_esta_observando(tmp_path):
    folder = tmp_path / "sessao"
    folder.mkdir()
    (tmp_path / "ativo.json").write_text(json.dumps({"pasta": str(folder)}), encoding="utf-8")
    (folder / "resumo.json").write_text(json.dumps({"status": "OBSERVANDO"}), encoding="utf-8")
    _, state = observer_status(tmp_path)
    assert state["status"] == "ENCERRADO_SEM_FINALIZACAO"
    assert state["processo_ativo"] is False
    with observer_lock(tmp_path):
        _, state = observer_status(tmp_path)
    assert state["status"] == "OBSERVANDO"
    assert state["processo_ativo"] is True
