"""Verifica a preparação sem controlar telas nem alterar dados de negócio."""
import importlib.util
import json
import platform
from datetime import datetime
from html import escape
from pathlib import Path
from uuid import uuid4

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer
from automatiza.perfis import check_origin_definition, destinations_match, import_destination, load_profile, profile_settings


REQUIRED_COLUMNS = {
    'Afastamentos': {'Id', 'IdPessoa', 'DataInicio', 'DataTermino', 'Causa', 'IdFreq'},
    'Pessoas': {'id', 'IdExportacao', 'ContratoExportacao'},
}


def check_schema(db):
    rows = db.query(
        "SET LOCK_TIMEOUT 1000; SELECT t.name AS tabela,c.name AS coluna "
        "FROM sys.tables t JOIN sys.schemas s ON s.schema_id=t.schema_id "
        "JOIN sys.columns c ON c.object_id=t.object_id "
        "WHERE s.name='dbo' AND t.name IN ('Afastamentos','Pessoas')")
    actual = {(str(r['tabela']).casefold(), str(r['coluna']).casefold()) for r in rows}
    missing = [table + '.' + column for table, columns in REQUIRED_COLUMNS.items()
               for column in sorted(columns) if (table.casefold(), column.casefold()) not in actual]
    if missing:
        raise ValueError('Colunas necessárias ausentes: ' + ', '.join(missing))
    return 'Estrutura de Pessoas e Afastamentos disponível.'


def inspect_preparation(*, root=ROOT, settings=None, sql=False, db_factory=SqlServer):
    root = Path(root)
    settings = settings or Settings.load()
    checks = []

    def check(name, operation):
        try:
            detail = operation()
            checks.append({'item': name, 'estado': 'OK', 'detalhe': detail or 'Disponível.'})
        except Exception as exc:
            # Exceções de ODBC e bibliotecas podem incluir credenciais.
            checks.append({'item': name, 'estado': 'PENDENTE', 'detalhe': type(exc).__name__})

    def required_file(path):
        if not path or not Path(path).is_file():
            raise FileNotFoundError()
        return str(path)

    check('Executável Acessus', lambda: required_file(settings.app_path))
    check('Executável RH', lambda: required_file(settings.rh_path))
    for module in ('pyodbc', 'pywinauto', 'dotenv', 'pytest', 'pytest_html', 'PIL', 'tkinter'):
        def dependency(name=module):
            if importlib.util.find_spec(name) is None:
                raise ModuleNotFoundError()
        check('Biblioteca ' + module, dependency)

    def driver():
        import pyodbc
        if settings.sql_driver not in pyodbc.drivers():
            raise ValueError()
        return settings.sql_driver
    check('Driver SQL da automação', driver)
    check('Configuração SQL', lambda: bool(settings.connection_string()) and 'Campos obrigatórios preenchidos.')
    checks.append({'item': 'Credenciais RH', 'estado': 'OK' if settings.rh_user and settings.rh_password else 'PENDENTE',
                   'detalhe': 'Presença conferida; login precisa de validação manual.'})

    profiles = sorted((root / 'profiles').glob('*.json'))
    if not profiles:
        checks.append({'item': 'Perfis de ambiente', 'estado': 'PENDENTE', 'detalhe': 'Nenhum perfil salvo.'})
    for path in profiles:
        def inspect_profile(path=path):
            profile = load_profile(path)
            check_origin_definition(profile)
            return profile['origem_rh']['alias'] + ' → ' + profile['destino_sql']['banco']
        check('Perfil ' + path.name, inspect_profile)
        if sql:
            def connect_profile(path=path):
                profile = load_profile(path)
                db = db_factory(profile_settings(settings, profile))
                db.assert_database()
                return check_schema(db)
            check('Destino SQL do perfil ' + path.name, connect_profile)

    def importer():
        actual = import_destination(Path(settings.app_work_dir) / 'ConexaoConfig.ini')
        if not actual['servidor'] or not actual['banco']:
            raise ValueError()
        return actual['servidor'] + ' / ' + actual['banco'] + ' (comparar com o perfil antes do cenário)'
    check('Destino declarado no importador', importer)
    def matching_importer():
        actual = import_destination(Path(settings.app_work_dir) / 'ConexaoConfig.ini')
        if not destinations_match(actual, {'servidor': settings.sql_server, 'banco': settings.sql_database}):
            raise ValueError()
        return 'Importador e configuração SQL usam o mesmo destino.'
    check('Destino do importador corresponde à configuração SQL', matching_importer)
    scenarios = sorted((root / 'examples/cenarios').glob('*.json'))
    if not scenarios:
        checks.append({'item': 'Cenários da Central', 'estado': 'PENDENTE', 'detalhe': 'Nenhum cenário encontrado.'})
    else:
        from automatiza.execucao import load_scenario
        for path in scenarios:
            check('Cenário ' + path.name, lambda path=path: load_scenario(path)['id'])
    if sql:
        def target():
            db = db_factory(settings)
            db.assert_database()
            return check_schema(db)
        check('Conexão e estrutura SQL selecionadas', target)

    return {'computador': platform.node(), 'gerado_em': datetime.now().astimezone().isoformat(),
            'estado': 'PREPARACAO_TECNICA_CONFERIDA' if all(c['estado'] == 'OK' for c in checks) else 'PENDENCIAS',
            'consultou_sql': sql, 'verificacoes': checks,
            'validacoes_manuais': [
                'Entrar no RH e conferir o alias ativo antes dos cenários de tela.',
                'Conferir a origem RH usada pelo importador; o perfil da Central não troca a origem do serviço.',
                'Confirmar pessoa/contrato, ocorrência que gera afastamento, causa e datas esperadas.',
                'Validar gravação, exclusão e recadastro no RH antes de habilitar cenários de negócio.',
                'Confirmar ciclo da integração, regra de datas antigas e conversão do término.',
                'Oracle exige serviço/SID e login validados quando esse ambiente for usado.',
            ], 'limite': 'Preparação técnica não aprova regras de negócio. Nenhuma janela foi controlada e nenhum dado de negócio foi alterado.'}


def save_preparation(result, base=None):
    folder = Path(base or ROOT / 'reports/preparacao') / (datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + uuid4().hex[:8])
    folder.mkdir(parents=True, exist_ok=False)
    (folder / 'preparacao.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    rows = ''.join('<tr>' + ''.join('<td>' + escape(str(c[k])) + '</td>' for k in ('item', 'estado', 'detalhe')) + '</tr>'
                   for c in result['verificacoes'])
    todo = ''.join('<li>' + escape(v) + '</li>' for v in result['validacoes_manuais'])
    (folder / 'preparacao.html').write_text(
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Preparação dos testes</title>'
        '<style>body{font:16px system-ui;margin:32px;max-width:1100px}table{border-collapse:collapse;width:100%}'
        'td,th{border:1px solid #ccd;padding:8px;text-align:left}</style><h1>Preparação dos testes</h1><p>'
        + escape(result['estado']) + ' — ' + escape(result['gerado_em']) + '</p><p>' + escape(result['limite'])
        + '</p><table><tr><th>Item</th><th>Estado</th><th>Detalhe</th></tr>' + rows
        + '</table><h2>Validações necessárias para os cenários completos</h2><ul>' + todo + '</ul></html>', encoding='utf-8')
    return folder
