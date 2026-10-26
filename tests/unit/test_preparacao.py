import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from automatiza.config import Settings
from automatiza.database import SqlServer
from automatiza.execucao import load_scenario, run_scenario
from automatiza.preparacao import REQUIRED_COLUMNS, check_schema, inspect_preparation, save_preparation
from automatiza.perfis import destinations_match


def complete_schema():
    return [{'tabela': t, 'coluna': c} for t, columns in REQUIRED_COLUMNS.items() for c in columns]


def test_coluna_ausente_impede_aprovar_estrutura():
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [r for r in complete_schema() if r['coluna'] != 'IdFreq']
    with pytest.raises(ValueError, match='Afastamentos.IdFreq'):
        check_schema(db)


def test_estrutura_considera_nomes_sem_diferenca_de_caixa():
    db = MagicMock(spec=SqlServer)
    db.query.return_value = [{k: v.upper() for k, v in r.items()} for r in complete_schema()]
    assert 'disponível' in check_schema(db)
    sql = db.query.call_args.args[0]
    assert 'sys.columns' in sql and 'LOCK_TIMEOUT' in sql


def test_diagnostico_sql_nao_exporta_credenciais_nem_excecoes(tmp_path):
    settings = Settings(sql_server='servidor', sql_database='banco', sql_auth='sql',
                        sql_user='usuario-privado', sql_password='senha-privada')
    db = MagicMock(spec=SqlServer)
    db.assert_database.side_effect = RuntimeError('senha-privada usuario-privado')
    factory = MagicMock(return_value=db)
    result = inspect_preparation(root=tmp_path, settings=settings, sql=True, db_factory=factory)
    text = json.dumps(result)
    assert 'senha-privada' not in text and 'usuario-privado' not in text
    assert result['estado'] == 'PENDENCIAS'
    folder = save_preparation(result, tmp_path / 'reports')
    assert (folder / 'preparacao.html').is_file()
    assert 'senha-privada' not in (folder / 'preparacao.html').read_text(encoding='utf-8')


def test_diagnostico_sem_sql_nao_conecta(tmp_path):
    factory = MagicMock()
    result = inspect_preparation(root=tmp_path, settings=Settings(), db_factory=factory)
    factory.assert_not_called()
    assert result['consultou_sql'] is False


def test_cenario_sql_disponivel_sem_telas_e_com_estrutura_real(tmp_path):
    root = Path(__file__).resolve().parents[2]
    scenario = root / 'examples/cenarios/01-conferir-estrutura-sql.json'
    profile = tmp_path / 'perfil.json'
    profile.write_text(json.dumps({'versao': 1, 'origem_rh': {'alias': 'teste', 'banco': 'origem'},
                                   'destino_sql': {'servidor': 'servidor', 'banco': 'banco'}}), encoding='utf-8')
    db = MagicMock(spec=SqlServer)
    db.query.return_value = complete_schema()
    result = run_scenario(profile, scenario, base=tmp_path / 'reports', database=db)
    assert result['estado'] == 'PASSOU'
    db.assert_database.assert_called_once()
    db.query.return_value = []
    failed = run_scenario(profile, scenario, base=tmp_path / 'reports', database=db)
    assert failed['estado'] == 'FALHOU'


def test_cenarios_de_abertura_nao_permitem_alterar_dados():
    root = Path(__file__).resolve().parents[2]
    paths = list((root / 'examples/cenarios').glob('*.json'))
    assert len(paths) == 5
    for path in paths:
        scenario = load_scenario(path)
        assert scenario['permite_alterar_dados'] is False
        assert not any(s['acao'] in {'clicar', 'preencher', 'teclas'} for s in scenario['etapas'])


def test_comparacao_importador_aceita_tcp_padrao_mas_recusa_outro_banco_ou_instancia():
    actual = {'servidor': 'DESK-TEC', 'banco': 'bras1'}
    assert destinations_match(actual, {'servidor': 'tcp:desk-tec,1433', 'banco': 'BRAS1'})
    assert not destinations_match(actual, {'servidor': 'desk-tec,1435', 'banco': 'bras1'})
    assert not destinations_match(actual, {'servidor': 'desk-tec', 'banco': 'novo123'})
    assert not destinations_match(actual, {'servidor': r'desk-tec\OUTRA', 'banco': 'bras1'})
