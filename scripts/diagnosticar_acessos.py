"""Diagnóstico sem mudanças: desktop, Python, Schannel, TCP e leitura SQL."""
import argparse
import importlib.util
import json
import socket
import sys
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from automatiza.ambiente import desktop_context, schannel_probe
from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer


def diagnose(settings, *, include_sql=True):
    result = {'verificado_em': datetime.now().astimezone().isoformat(),
              'python': sys.executable, 'desktop': desktop_context(),
              'pacotes': {name: importlib.util.find_spec(name) is not None
                          for name in ('pywinauto', 'pyodbc', 'dotenv', 'PIL')},
              'servidor': settings.sql_server, 'base': settings.sql_database,
              'driver': settings.sql_driver, 'autenticacao': settings.sql_auth,
              'encrypt': settings.sql_encrypt, 'trust_server_certificate': settings.sql_trust_certificate,
              'sem_alteracoes': True}
    try:
        result['schannel'] = schannel_probe()
    except Exception as exc:
        result['schannel'] = {'disponivel': False, 'erro': type(exc).__name__}
    # Não presume a porta 1433 em instâncias nomeadas ou aliases.
    server = settings.sql_server.removeprefix('tcp:')
    if server and '\\' not in server and ':' not in server:
        host, separator, port = server.partition(',')
        try:
            with socket.create_connection((host, int(port) if separator else 1433), timeout=3):
                result['tcp'] = 'ACESSIVEL'
        except Exception as exc:
            result['tcp'] = type(exc).__name__
    else:
        result['tcp'] = 'NAO_TESTADO_ALIAS_OU_INSTANCIA'
    if include_sql:
        try:
            db = SqlServer(replace(settings, sql_timeout=min(settings.sql_timeout, 5)))
            actual = db.assert_database()
            result['sql'] = {'disponivel': True, 'base_confirmada': actual}
        except Exception as exc:
            message = str(exc).lower()
            reason = ('NEGOCIACAO_CRIPTOGRAFICA' if any(t in message for t in ('ssl', 'criptografia', 'pacote de seguran'))
                      else 'CONEXAO_NAO_CONCLUIDA')
            state = str(exc.args[0]) if exc.args and isinstance(exc.args[0], str) and len(exc.args[0]) == 5 else None
            result['sql'] = {'disponivel': False, 'tipo': type(exc).__name__, 'sqlstate': state, 'categoria': reason}
    result['pronto_para_testar_fluxo_real'] = bool(result['desktop']['disponivel'] and
                                                 all(result['pacotes'].values()) and
                                                 result.get('sql', {}).get('disponivel'))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base')
    parser.add_argument('--saida', type=Path)
    parser.add_argument('--sem-sql', action='store_true', help='Não tenta conexão SQL; diagnóstico fica incompleto')
    args = parser.parse_args()
    settings = Settings.load()
    if args.base is not None:
        settings = replace(settings, sql_database=args.base)
    result = diagnose(settings, include_sql=not args.sem_sql)
    output = args.saida or ROOT / 'reports/diagnostico-acessos' / (datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=True, indent=2))
    print('Relatorio: ' + str(output))
    return 0 if result['pronto_para_testar_fluxo_real'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
