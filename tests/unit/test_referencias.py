import json
from unittest.mock import MagicMock

import pytest

from automatiza.config import Settings
from automatiza.database import SqlServer
from automatiza.referencias import update_references


def test_consulta_parametrizada_e_remove_referencia_desatualizada(tmp_path):
    path = tmp_path / "pessoas-referencia.json"
    path.write_text(json.dumps({"pessoas": [{"Id": 1}, {"Id": 2}, {"Id": 3}]}))
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [{"Id": 1, "Nome": "Pessoa teste", "IdExportacao": 10}]
    result = update_references(Settings(sql_database="bras1"), tmp_path, [2, 1, 1], db=db)
    sql, params = db.query.call_args.args
    assert params == (1, 2)
    assert "IN (?,?)" in sql
    assert "LOCK_TIMEOUT 1000" in sql
    assert "senha" not in sql.lower() and "cpf" not in sql.lower()
    assert result["ids_nao_localizados"] == [2]
    assert [person["Id"] for person in result["pessoas"]] == [1, 3]


@pytest.mark.parametrize("people", [[], [0], [-1], [True], ["1"], list(range(1, 102))])
def test_limites_antes_de_consultar(tmp_path, people):
    db = MagicMock(spec=SqlServer)
    with pytest.raises(ValueError):
        update_references(Settings(sql_database="bras1"), tmp_path, people, db=db)
    db.query.assert_not_called()


def test_rejeita_base_ausente(tmp_path):
    db = MagicMock(spec=SqlServer)
    with pytest.raises(ValueError):
        update_references(Settings(), tmp_path, [1], db=db)
    db.query.assert_not_called()


def test_base_variavel_preservada_e_sessao_de_outra_origem_recusada(tmp_path):
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [{'Id': 1, 'Nome': 'Teste'}]
    settings = Settings(sql_database='teste-ferias', sql_server='servidor-teste')
    result = update_references(settings, tmp_path, [1], db=db)
    assert result['origem'] == 'teste-ferias.dbo.Pessoas'
    assert result['servidor'] == 'servidor-teste'
    (tmp_path / 'resumo.json').write_text(json.dumps({'banco': 'bras1', 'servidor': 'servidor-teste'}))
    db.reset_mock()
    with pytest.raises(ValueError, match='mesma base'):
        update_references(settings, tmp_path, [1], db=db)
    db.query.assert_not_called()
