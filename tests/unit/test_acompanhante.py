import json
from unittest.mock import MagicMock

import pytest

from automatiza.acompanhante import follow_analysis, save_case
from automatiza.observador import annotate, observer_lock
from automatiza.servicos import service_changes
from test_analise import row, stamp, write_session
from test_casos_offline import spec


class Clock:
    time = 0

    def now(self):
        return self.time

    def sleep(self, seconds):
        self.time += seconds


def session(tmp_path):
    folder = tmp_path / "sessao"
    write_session(folder, [row()], [row()], [])
    (tmp_path / "ativo.json").write_text(json.dumps({"pasta": str(folder)}), encoding="utf-8")
    return folder


def test_acompanhante_registra_servico_e_encerra_com_coleta_sem_consultar_sql(tmp_path, monkeypatch):
    folder = session(tmp_path)
    clock = Clock()
    query = MagicMock(side_effect=AssertionError("Não deve haver SQL no acompanhante"))
    monkeypatch.setattr("automatiza.database.SqlServer.query", query)
    services = MagicMock(side_effect=[[{"nome": "api", "descricao": "API", "estado": "EXECUTANDO", "processo_id": 1}],
                                     [{"nome": "api", "descricao": "API", "estado": "PARADO", "processo_id": 0}]])
    def status(base):
        alive = clock.time < 35
        return folder, {"status": "OBSERVANDO" if alive else "FINALIZADO", "processo_ativo": alive}
    result = follow_analysis(tmp_path, interval=5, service_interval=30, duration=60,
                             clock=clock.now, sleep=clock.sleep, service_reader=services, source_status=status)
    assert result["status"] == "FINALIZADO_COM_COLETA"
    assert result["atualizacoes"] >= 3
    assert services.call_count == 2
    query.assert_not_called()
    events = [json.loads(line) for line in (folder / "eventos-servicos.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(events) == 1
    assert events[0]["antes"]["estado"] == "EXECUTANDO"
    assert events[0]["depois"]["estado"] == "PARADO"
    assert json.loads((folder / "analise.json").read_text(encoding="utf-8"))["estado_coleta"] == "FINALIZADO"


def test_acompanhante_nao_duplica_processamento_da_mesma_sessao(tmp_path):
    folder = session(tmp_path)
    with observer_lock(folder / "controle-analise"):
        with pytest.raises(RuntimeError, match="Já existe"):
            follow_analysis(tmp_path)


def test_sinal_para_analise_nao_para_a_coleta(tmp_path):
    folder = session(tmp_path)
    (folder / "parar-analise.sinal").touch()
    result = follow_analysis(tmp_path, service_reader=lambda: [],
                             source_status=lambda base: (folder, {"processo_ativo": True, "status": "OBSERVANDO"}))
    assert result["status"] == "PARADO"
    assert not (folder / "parar.sinal").exists()


def test_registro_de_caso_e_local_imutavel_e_tem_horario(tmp_path):
    folder = session(tmp_path)
    case = spec()
    saved = save_case(tmp_path, case)
    assert saved["registrado_em"] == stamp(5)
    with pytest.raises(ValueError, match="Já existe"):
        save_case(tmp_path, case)
    assert len(json.loads((folder / "casos.json").read_text(encoding="utf-8"))["casos"]) == 1


def test_caso_com_prazo_invalido_nao_e_salvo(tmp_path):
    folder = session(tmp_path)
    with pytest.raises(ValueError, match="Prazo"):
        save_case(tmp_path, spec(prazo_segundos=-1))
    assert not (folder / "casos.json").exists()


def test_nota_estruturada_e_salva_sem_acionar_cadastro(tmp_path):
    folder = session(tmp_path)
    annotate(tmp_path, "Vou incluir férias", metadata=spec())
    note = json.loads((folder / "anotacoes.jsonl").read_text(encoding="utf-8"))
    assert note["dados"]["id_pessoa"] == 10
    assert note["nota"] == "Vou incluir férias"
    assert not (folder / "casos.json").exists()


def test_mudanca_de_pid_e_registrada_sem_afirmar_instante_do_restart():
    before = [{"nome": "api", "estado": "EXECUTANDO", "processo_id": 1}]
    after = [{"nome": "api", "estado": "EXECUTANDO", "processo_id": 2}]
    result = service_changes(before, after)
    assert len(result) == 1
    assert result[0]["depois"]["processo_id"] == 2


def test_caso_fora_do_filtro_nao_e_registrado(tmp_path):
    folder = session(tmp_path)
    (folder / "resumo.json").write_text(json.dumps({"pessoas": [99]}), encoding="utf-8")
    with pytest.raises(ValueError, match="fora do filtro"):
        save_case(tmp_path, spec())
    assert not (folder / "casos.json").exists()


def test_inicio_explicito_reutiliza_sessao_e_limpa_so_sinal_da_analise(tmp_path):
    folder = session(tmp_path)
    (folder / "parar-analise.sinal").touch()
    (folder / "parar.sinal").touch()
    result = follow_analysis(tmp_path, reset_stop=True, service_reader=lambda: [],
                             source_status=lambda base: (folder, {"processo_ativo": False, "status": "PARADO"}))
    assert result["status"] == "FINALIZADO_COM_COLETA"
    assert not (folder / "parar-analise.sinal").exists()
    assert (folder / "parar.sinal").exists()
