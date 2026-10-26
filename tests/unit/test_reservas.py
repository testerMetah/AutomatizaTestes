from datetime import datetime

import pytest

from automatiza.reservas import query_spec


def filters():
    # Dados sintéticos exclusivos de teste unitário; não são cenário real.
    return {'credencial': 'teste-unitario', 'id_refeitorio': 7, 'id_empresa': 2,
            'inicio': '2030-01-02T11:00:00', 'termino': '2030-01-02T13:00:00'}


def test_reserva_exige_empresa_e_identidade_para_evitar_falso_positivo():
    for key in filters():
        case = filters()
        del case[key]
        with pytest.raises(ValueError):
            query_spec(case)


def test_textos_de_reserva_sao_parametros_e_nao_codigo_sql():
    case = filters()
    case['credencial'] = "x'; DROP TABLE Pessoas;--"
    case['id_exportacao'] = 'chave-origem'
    sql, params, limit = query_spec(case)
    assert case['credencial'] not in sql
    assert case['credencial'] in params
    assert 'chave-origem' in params
    assert datetime(2030, 1, 2, 11) in params
    assert sql.count('?') == len(params)
    assert limit == 100 and 'TOP (101)' in sql


@pytest.mark.parametrize('key,value', [('id_empresa', True), ('id_refeitorio', 0),
    ('inicio', '2030-01-02'), ('inicio', '2030-01-02T11:00:00+00:00'),
    ('termino', '2030-01-01T13:00:00'), ('status', False)])
def test_expectativas_ambiguas_ou_invalidas_sao_recusadas(key, value):
    case = filters()
    case[key] = value
    with pytest.raises(ValueError):
        query_spec(case)
