import json
import threading
from pathlib import Path
from unittest.mock import patch

import pytest

from automatiza.lotes import load_suite, run_suite


def make_suite(tmp_path):
    for name in ('a', 'b'):
        (tmp_path / (name + '.json')).write_text(json.dumps({
            'versao': 1, 'id': name, 'preparado': True,
            'etapas': [{'acao': 'sql_estrutura'}]}), encoding='utf-8')
    suite = tmp_path / 'lote.json'
    suite.write_text(json.dumps({'versao': 1, 'id': 'lote', 'cenarios': ['a.json', 'b.json']}), encoding='utf-8')
    return suite


@pytest.mark.parametrize('states,expected,calls', [(['PASSOU', 'PASSOU'], 'PASSOU', 2),
                                                (['FALHOU'], 'FALHOU', 1),
                                                (['EXECUTADO_SEM_VERIFICACAO_NEGOCIO'], 'FALHOU', 1)])
def test_lote_exige_aprovacao_de_todos_e_para_na_falha(tmp_path, states, expected, calls):
    suite = make_suite(tmp_path)
    def runner(profile, scenario, **kwargs):
        folder = kwargs['base'] / Path(scenario).stem
        folder.mkdir(parents=True)
        (folder / 'relatorio.html').write_text('Detalhes', encoding='utf-8')
        return {'estado': states.pop(0), 'pasta': str(folder)}
    with patch('automatiza.lotes.load_profile'), patch('automatiza.lotes.ROOT', tmp_path), patch('automatiza.lotes.run_scenario', side_effect=runner) as execute:
        result = run_suite('perfil.json', suite, base=tmp_path / 'reports', runner=execute)
    summary = json.loads((Path(result['pasta']) / 'resumo.json').read_text(encoding='utf-8'))
    assert result['estado'] == expected
    assert execute.call_count == calls
    assert len(summary['cenarios']) == 2
    if calls == 1:
        assert summary['cenarios'][1]['estado'] == 'NAO_EXECUTADO'
    manifest = json.loads((Path(result['pasta']) / 'manifesto-sha256.json').read_text(encoding='utf-8'))
    assert 'indice.html' in manifest


def test_lote_valida_todos_antes_da_primeira_acao(tmp_path):
    suite = make_suite(tmp_path)
    (tmp_path / 'b.json').write_text('{}', encoding='utf-8')
    with patch('automatiza.lotes.load_profile'), patch('automatiza.lotes.run_scenario') as execute:
        with pytest.raises(ValueError):
            run_suite('perfil.json', suite, base=tmp_path / 'reports')
    execute.assert_not_called()


def test_lote_cancelado_nao_inicia_cenario(tmp_path):
    suite = make_suite(tmp_path)
    stop = threading.Event()
    stop.set()
    with patch('automatiza.lotes.load_profile'), patch('automatiza.lotes.ROOT', tmp_path), patch('automatiza.lotes.run_scenario') as execute:
        result = run_suite('perfil.json', suite, base=tmp_path / 'reports', cancel_event=stop, runner=execute)
    assert result['estado'] == 'INTERROMPIDO'
    execute.assert_not_called()


def test_lote_recusa_caminho_fora_da_pasta(tmp_path):
    suite = tmp_path / 'lote.json'
    suite.write_text(json.dumps({'versao': 1, 'id': 'lote', 'cenarios': ['../fora.json']}), encoding='utf-8')
    with pytest.raises(ValueError, match='subpasta'):
        load_suite(suite)
