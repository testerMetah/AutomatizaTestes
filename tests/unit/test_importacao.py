import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from automatiza.importacao import load_case, monitor


class Clock:
    def __init__(self):
        self.time = 0

    def now(self):
        return self.time

    def sleep(self, seconds):
        self.time += seconds


def case(expected=1, mode="convergencia"):
    return {"id": "caso", "descricao": "Teste", "pessoa": "123", "acao_origem": "Ação de teste",
            "timeout_segundos": 5, "intervalo_segundos": 1, "estabilidade_segundos": 2,
            "verificacoes": [{"nome": "afastamento", "sql": "SELECT COUNT(*) FROM teste WHERE id=?",
                                "parametros": [123], "quantidade_esperada": expected, "modo": mode}]}


def run(tmp_path, spec, values):
    db = MagicMock()
    db.scalar.side_effect = values
    clock = Clock()
    result = monitor(db, spec, tmp_path, clock=clock.now, sleep=clock.sleep)
    return result, clock, db


def test_importacao_precisa_estabilizar_depois_de_oscilacao(tmp_path):
    result, clock, db = run(tmp_path, case(), [0, 1, 0, 1, 1, 1])
    assert result["status"] == "PASSOU"
    assert clock.time == 5
    assert len(result["amostras"]) == 6
    db.scalar.assert_called_with("SELECT COUNT(*) FROM teste WHERE id=?", (123,))


def test_exclusao_pode_demorar_para_propagacao(tmp_path):
    result, clock, _ = run(tmp_path, case(0), [1, 1, 0, 0, 0])
    assert result["status"] == "PASSOU"
    assert clock.time == 4
    assert result["amostras"][0]["observado"] == 1


def test_ausencia_na_janela_nao_aprova_antes_do_limite(tmp_path):
    result, clock, _ = run(tmp_path, case(0, "na_janela"), [0] * 6)
    assert result["status"] == "PASSOU"
    assert clock.time == 5


def test_presenca_transitoria_reprova_ausencia_na_janela(tmp_path):
    result, _, _ = run(tmp_path, case(0, "na_janela"), [0, 1, 0, 0, 0, 0])
    assert result["status"] == "FALHOU"


def test_timeout_sem_importacao_preserva_amostras(tmp_path):
    result, _, _ = run(tmp_path, case(), [0] * 6)
    assert result["status"] == "FALHOU"
    directory = Path(result["report"]).parent
    assert len((directory / "amostras.jsonl").read_text(encoding="utf-8").splitlines()) == 6
    assert json.loads((directory / "resultado.json").read_text(encoding="utf-8"))["status"] == "FALHOU"


def test_erro_sql_e_distinto_de_falha_de_negocio_e_nao_expoe_detalhes(tmp_path):
    result, _, _ = run(tmp_path, case(), [0, RuntimeError("senha-na-mensagem")])
    assert result["status"] == "ERRO"
    assert len(result["amostras"]) == 1
    assert "senha-na-mensagem" not in Path(result["report"]).read_text(encoding="utf-8")


def test_modelo_nao_preparado_nao_executa_verificacoes():
    with pytest.raises(ValueError, match="preparado=true"):
        load_case(Path(__file__).resolve().parents[2] / "examples" / "integracao-rh.modelo.json", "ferias-incluir")


def test_contagem_invalida_nao_aprova_caso(tmp_path):
    result, _, _ = run(tmp_path, case(), [None])
    assert result["status"] == "ERRO"


def test_relatorio_escapa_texto_do_cenario(tmp_path):
    spec = case()
    spec["pessoa"] = "<script>alert(1)</script>"
    result, _, _ = run(tmp_path, spec, [1, 1, 1])
    html = Path(result["report"]).read_text(encoding="utf-8")
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_caso_nao_preparado_continua_bloqueado_quando_outro_foi_configurado(tmp_path):
    spec = case(0, "na_janela")
    spec["preparado"] = False
    path = tmp_path / "casos.json"
    path.write_text(json.dumps({"preparado": True, "casos": [spec]}), encoding="utf-8")
    with pytest.raises(ValueError, match="caso ainda"):
        load_case(path, "caso")


@pytest.mark.parametrize("id_pessoa", [0, -1, True])
def test_identificador_ilustrativo_nao_aprova_ausencia_por_engano(tmp_path, id_pessoa):
    spec = case(0, "na_janela")
    spec["id_pessoa"] = id_pessoa
    path = tmp_path / "casos.json"
    path.write_text(json.dumps({"preparado": True, "casos": [spec]}), encoding="utf-8")
    with pytest.raises(ValueError, match="id_pessoa"):
        load_case(path, "caso")


def test_parametro_referencia_id_pessoa_do_caso_sem_duplicar_configuracao(tmp_path):
    spec = case()
    spec["id_pessoa"] = 123
    check = spec["verificacoes"][0]
    check["parametros"] = [{"campo_caso": "id_pessoa"}]
    check["arquivo_sql"] = "consulta.sql"
    (tmp_path / "consulta.sql").write_text(check["sql"], encoding="utf-8")
    path = tmp_path / "casos.json"
    path.write_text(json.dumps({"preparado": True, "casos": [spec]}), encoding="utf-8")
    loaded = load_case(path, "caso")
    assert loaded["verificacoes"][0]["parametros"] == [123]
