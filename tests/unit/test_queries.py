from unittest.mock import MagicMock, patch

import pytest

from automatiza.queries import read_query, run_query


def test_consulta_multilinha_preserva_sql():
    with patch("builtins.input", side_effect=["SELECT nome", "FROM dbo.Pessoas", "/executar"]):
        assert read_query() == "SELECT nome\nFROM dbo.Pessoas"


def test_cancelamento_nao_executa_sql():
    with patch("builtins.input", side_effect=["SELECT 1", "/cancelar"]):
        assert read_query() == ""


def test_entrada_incompleta_nao_executa():
    with patch("builtins.input", side_effect=["SELECT 1", EOFError]):
        with pytest.raises(ValueError, match="sem /executar"):
            read_query()


def test_arquivo_e_parametros_ate_resultado(tmp_path):
    source = tmp_path / "consulta.sql"
    source.write_text("SELECT nome WHERE codigo = ?", encoding="utf-8-sig")
    db = MagicMock()
    db.query.return_value = [{"nome": "João"}]
    output = tmp_path / "resultado.json"
    run_query(db, read_query(str(source)), (123,), str(output))
    db.query.assert_called_once_with("SELECT nome WHERE codigo = ?", (123,))
    assert "João" in output.read_text(encoding="utf-8")
