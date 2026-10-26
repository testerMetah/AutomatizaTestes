"""Perfis independentes de origem RH/destino Acessus, sem guardar senhas."""
import configparser
import json
import os
from dataclasses import replace
from pathlib import Path

from automatiza.config import ROOT


def read_ini(path):
    data = Path(path).read_bytes()
    try:
        text = data.decode('utf-16') if data[:2] in (b'\xff\xfe', b'\xfe\xff') else data.decode('utf-8-sig')
    except UnicodeError:
        text = data.decode('cp1252')
    parser = configparser.ConfigParser(interpolation=None, strict=False)
    parser.read_string(text)
    return parser


def discover_aliases(paths=None):
    if paths is None:
        local = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / 'AppData/Local')))
        paths = [Path(os.environ.get('WINDIR', r'C:\Windows')) / 'MDE.ini',
                 local / 'VirtualStore/Windows/MDE.ini']
    found = {}
    for path in paths:
        if not Path(path).is_file():
            continue
        parser = read_ini(path)
        for section in parser.sections():
            values = parser[section]
            found[section] = {'alias': section, 'servidor': values.get('hostname', ''),
                              'banco': values.get('database', ''), 'driver': values.get('drivername', ''),
                              'arquivo_mde': str(Path(path).resolve())}
    return sorted(found.values(), key=lambda x: x['alias'].casefold())


def import_destination(path):
    parser = read_ini(path)
    section = next((s for s in parser.sections() if s.casefold() == 'configuracoes'), None)
    if section is None:
        raise ValueError('Configuração do importador sem seção Configuracoes.')
    return {'servidor': parser[section].get('server', ''), 'banco': parser[section].get('database', '')}


def destinations_match(first, second):
    def server(value):
        value = value.strip().casefold()
        if value.startswith('tcp:'):
            value = value[4:]
        if ',' not in value and '\\' not in value:
            value += ',1433'
        return value
    return (bool(first.get('servidor')) and bool(first.get('banco'))
            and server(first['servidor']) == server(second['servidor'])
            and first['banco'].strip().casefold() == second['banco'].strip().casefold())


def validate_profile(profile):
    if not isinstance(profile, dict) or profile.get('versao') != 1:
        raise ValueError('Perfil precisa usar versao 1.')
    if set(profile) - {'versao', 'nome', 'origem_rh', 'destino_sql'}:
        raise ValueError('Propriedade desconhecida no perfil.')
    origin, destination = profile.get('origem_rh', {}), profile.get('destino_sql', {})
    if not isinstance(origin, dict) or not isinstance(destination, dict):
        raise ValueError('Origem e destino devem ser objetos.')
    if set(origin) - {'alias', 'servidor', 'banco', 'driver', 'arquivo_mde'}:
        raise ValueError('Propriedade desconhecida na origem; não inclua credenciais.')
    if set(destination) - {'servidor', 'banco', 'driver', 'auth', 'encrypt', 'trust_certificate', 'user_env', 'password_env'}:
        raise ValueError('Propriedade desconhecida no destino; use referências de ambiente para credenciais.')
    if not all(isinstance(origin.get(k), str) and origin[k].strip() for k in ('alias', 'banco')):
        raise ValueError('Escolha alias e banco de origem do RH.')
    if not all(isinstance(destination.get(k), str) and destination[k].strip() for k in ('servidor', 'banco')):
        raise ValueError('Escolha servidor e banco de destino SQL.')
    # Credenciais só podem ser referenciadas pelo nome da variável de ambiente.
    forbidden = {'senha', 'password', 'sql_password', 'rh_password', 'token', 'connection_string'}
    def scan(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k.casefold() in forbidden:
                    raise ValueError('Não grave credenciais no perfil; use o .env local.')
                scan(v)
        elif isinstance(obj, list):
            for value in obj:
                scan(value)
    scan(profile)
    return profile


def load_profile(path):
    return validate_profile(json.loads(Path(path).read_text(encoding='utf-8-sig')))


def save_profile(path, profile):
    validate_profile(profile)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as output:
        json.dump(profile, output, ensure_ascii=False, indent=2)


def profile_settings(settings, profile):
    validate_profile(profile)
    dest = profile['destino_sql']
    overrides = {'sql_server': dest['servidor'], 'sql_database': dest['banco']}
    for key in ('driver', 'auth', 'encrypt', 'trust_certificate'):
        if key in dest:
            overrides['sql_' + key] = dest[key]
    for key in ('user', 'password'):
        env = dest.get(key + '_env')
        if env:
            if env not in os.environ:
                raise ValueError('Variável de credencial não configurada: ' + env)
            overrides['sql_' + key] = os.environ[env]
    return replace(settings, **overrides)


def check_origin_definition(profile):
    origin = profile['origem_rh']
    paths = [origin['arquivo_mde']] if origin.get('arquivo_mde') else None
    aliases = [a for a in discover_aliases(paths) if a['alias'] == origin['alias']]
    if len(aliases) != 1:
        raise ValueError('Alias de origem não encontrado de forma única na configuração local.')
    actual = aliases[0]
    for key in ('servidor', 'banco'):
        if actual.get(key, '').casefold() != origin.get(key, '').casefold():
            raise ValueError('A definição do alias mudou. Revise o perfil antes de executar.')
    return actual
