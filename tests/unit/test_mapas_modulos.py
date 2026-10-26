import importlib
from pathlib import Path

import pytest


@pytest.fixture
def renderer(monkeypatch, tmp_path):
    scripts = Path(__file__).resolve().parents[2] / 'scripts'
    monkeypatch.syspath_prepend(str(scripts))
    module = importlib.import_module('inspecionar_modulos_vm')
    monkeypatch.setattr(module, 'STATIC', tmp_path / 'static')
    monkeypatch.setattr(module, 'ROOT', tmp_path)
    (module.STATIC / 'formularios').mkdir(parents=True)
    return module


def test_markdown_preserva_estado_e_omite_valores_de_dados(renderer, tmp_path):
    def node(cls, text, hidden=False):
        return {'classe': cls, 'texto': text, 'valor_omitido': hidden,
                'visivel': False, 'habilitado': True, 'caminho_estrutural': [cls], 'filhos': []}
    root = node('TFrmTesteMapa', 'Tela | teste')
    root['filhos'] = [node('TEdit', 'segredo-unitario', True)]
    record = {'janela': root, 'modulo': 'teste', 'rota': 'Menu > Tela', 'capturado_em': 'data-unitaria'}
    path = tmp_path / 'mapa.json'
    renderer.write_markdown(record, path)
    result = path.with_suffix('.md').read_text(encoding='utf-8')
    assert 'segredo-unitario' not in result
    assert '[valor omitido]' in result
    assert 'False' in result
    assert 'Tela \\| teste' in result
    assert 'Menu > Tela' in result


def test_estado_estatico_nao_e_publicado_como_controle_confirmado(renderer, tmp_path):
    import json
    static = {'classe': 'TFrmTesteMapa', 'nome': 'Frm', 'propriedades': {}, 'filhos': [
        {'classe': 'TEdit', 'nome': 'edSenha', 'propriedades': {'Text': 'nao-publicar'}, 'filhos': []},
        {'classe': 'TButton', 'nome': 'btnSalvar', 'propriedades': {'Caption': 'Salvar'}, 'filhos': []}]}
    (renderer.STATIC / 'formularios/TFrmTesteMapa-unit.json').write_text(json.dumps(static), encoding='utf-8')
    root = {'classe': 'TFrmTesteMapa', 'texto': 'Tela', 'valor_omitido': False,
            'visivel': True, 'habilitado': True, 'caminho_estrutural': ['Tela'], 'filhos': []}
    record = {'janela': root, 'modulo': 'teste', 'rota': 'Menu > Tela', 'capturado_em': 'data-unitaria'}
    path = tmp_path / 'mapa.json'
    renderer.write_markdown(record, path)
    result = path.with_suffix('.md').read_text(encoding='utf-8')
    assert 'nao-publicar' not in result
    assert 'recurso estático' in result
    assert 'não são automation_id confirmados' in result
    assert 'btnSalvar' in result
