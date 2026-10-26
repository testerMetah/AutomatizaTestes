import importlib.util
import json
from pathlib import Path
from unittest.mock import MagicMock

from automatiza.config import Settings
from automatiza.database import SqlServer


def load_script(name):
    path = Path(__file__).resolve().parents[2] / 'scripts' / (name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ini_exporta_destino_sem_senhas_ou_strings_de_conexao(tmp_path):
    script = load_script('inventariar_ambiente')
    path = tmp_path / 'config.ini'
    path.write_text('[Conexao]\nServer=servidor-teste\nDatabase=base-teste\nPassword=segredo-ini\nConnectionString=Password=segredo-conexao\n')
    result = script.config_structure(path)
    text = json.dumps(result)
    assert 'servidor-teste' in text and 'base-teste' in text
    assert 'segredo-ini' not in text and 'segredo-conexao' not in text


def test_xml_nao_publica_connectionstrings_ou_valores_de_token(tmp_path):
    script = load_script('inventariar_ambiente')
    path = tmp_path / 'app.config'
    path.write_text('<configuration><connectionStrings><add name="principal" connectionString="Password=segredo-conexao"/></connectionStrings><appSettings><add key="Token" value="segredo-token"/></appSettings></configuration>')
    text = json.dumps(script.config_structure(path))
    assert 'segredo-conexao' not in text and 'segredo-token' not in text


def test_sql_estatico_omite_literais_escapados_e_incompletos():
    script = load_script('extrair_pistas_sql')
    text = script.redact("SELECT * FROM Afastamentos WHERE Causa='segredo''escapado' AND IdFreq='incompleto")
    assert 'Afastamentos' in text and 'IdFreq' in text
    assert 'segredo' not in text and 'incompleto' not in text


def test_falha_de_metadados_nao_vira_lista_vazia(tmp_path):
    script = load_script('mapear_banco')
    db = MagicMock(spec=SqlServer)

    def query(sql):
        if 'sys.sql_expression_dependencies' in sql:
            raise PermissionError('segredo-na-excecao')
        return []

    db.query.side_effect = query
    result = script.inspect_schema(Settings(sql_database='base-teste'), tmp_path / 'mapa', db=db)
    assert result['dependencias'] is None
    assert result['objetos'] == 0
    inventory = json.loads((tmp_path / 'mapa/inventario.json').read_text(encoding='utf-8'))
    assert inventory['base'] == 'base-teste'
    assert inventory['falhas']['dependencias'] == 'PermissionError'
    assert 'segredo-na-excecao' not in json.dumps(inventory)
