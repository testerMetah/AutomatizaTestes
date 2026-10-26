"""Cria perfis de conexao na VM; nao abre telas nem altera bancos."""
import json
import platform
from pathlib import Path
import re
import sys

from automatiza.config import ROOT, Settings
from automatiza.perfis import discover_aliases, load_profile, save_profile


def main():
    if platform.node().split('.')[0].casefold() != 'testesvm':
        raise RuntimeError('Execute somente dentro da VM TESTESVM.')
    settings = Settings.load()
    aliases = discover_aliases()
    allowed = {'rhfagundes', 'rhbraslux', 'oracle-metah', 'oracle-braslux'}
    result = {'perfis': [], 'observacao': 'Destino inicial igual ao configurado na automacao; confirme a origem ativa no RH antes de executar cenarios.'}
    for alias in aliases:
        if alias['alias'].casefold() not in allowed:
            continue
        name = re.sub(r'[^A-Za-z0-9_-]', '_', alias['alias']) + '_para_bras1'
        path = ROOT / 'profiles' / (name + '.json')
        profile = {
            'versao': 1, 'nome': name, 'origem_rh': alias,
            'destino_sql': {
                'servidor': settings.sql_server, 'banco': settings.sql_database,
                'driver': settings.sql_driver, 'auth': settings.sql_auth,
                'encrypt': settings.sql_encrypt, 'trust_certificate': settings.sql_trust_certificate,
            },
        }
        if path.exists():
            load_profile(path)
            state = 'perfil existente preservado'
        else:
            save_profile(path, profile)
            state = 'perfil criado'
        result['perfis'].append({'alias': alias['alias'], 'arquivo': str(path), 'estado': state})
        print(alias['alias'] + ': ' + state, flush=True)
    if not {'rhfagundes', 'rhbraslux'}.issubset({a['alias'].casefold() for a in aliases}):
        raise RuntimeError('Os aliases SQL do RH nao foram encontrados no MDE.ini da VM.')
    Path(sys.argv[1]).write_text(json.dumps(result, ensure_ascii=True, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
