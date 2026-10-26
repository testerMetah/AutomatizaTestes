from unittest.mock import MagicMock, patch

import pytest

from automatiza.config import Settings
from automatiza.database import SqlServer


def test_parametros_separados_do_sql_e_conexao_fechada():
    connection = MagicMock()
    cursor = connection.cursor.return_value
    cursor.description = [("nome",)]
    cursor.fetchall.return_value = [("Cliente teste",)]
    db = SqlServer(Settings(sql_server="localhost", sql_database="teste"))
    with patch("automatiza.database.pyodbc.connect", return_value=connection):
        assert db.query("SELECT nome FROM clientes WHERE codigo = ?", (123,)) == [
            {"nome": "Cliente teste"}
        ]
    cursor.execute.assert_called_once_with("SELECT nome FROM clientes WHERE codigo = ?", (123,))
    connection.rollback.assert_called_once()
    connection.close.assert_called_once()
    connection.commit.assert_not_called()


def test_erro_de_consulta_tambem_libera_conexao():
    connection = MagicMock()
    connection.cursor.return_value.execute.side_effect = RuntimeError("erro simulado")
    with patch("automatiza.database.pyodbc.connect", return_value=connection):
        with pytest.raises(RuntimeError, match="erro simulado"):
            SqlServer(Settings(sql_server="s", sql_database="d")).query("SELECT 1")
    connection.rollback.assert_called_once()
    connection.close.assert_called_once()


def test_senha_com_caracteres_especiais_preservada():
    settings = Settings(sql_server="s", sql_database="d", sql_auth="sql",
                        sql_user="usuario", sql_password="abc};xyz")
    assert "PWD={abc}};xyz};" in settings.connection_string()


def test_configuracao_incompleta_recusada():
    with pytest.raises(ValueError, match="SQL_SERVER"):
        Settings().connection_string()


def test_senha_nao_aparece_na_representacao_da_configuracao():
    assert "senha_secreta" not in repr(Settings(sql_password="senha_secreta"))


def test_scalar_recusa_resultado_ambiguo():
    db = SqlServer(Settings())
    with patch.object(db, "query", return_value=[{"valor": 1}, {"valor": 2}]):
        with pytest.raises(ValueError, match="uma linha e uma coluna"):
            db.scalar("SELECT valor FROM tabela")


def test_destino_real_precisa_corresponder_a_base_configurada():
    db = SqlServer(Settings(sql_database='teste-ferias'))
    with patch.object(db, 'scalar', return_value='TESTE-FERIAS'):
        assert db.assert_database() == 'TESTE-FERIAS'
    with patch.object(db, 'scalar', return_value='bras1'):
        with pytest.raises(ValueError, match='base configurada'):
            db.assert_database()
    with patch.object(db, 'scalar', return_value=None):
        with pytest.raises(ValueError, match='base configurada'):
            db.assert_database()
