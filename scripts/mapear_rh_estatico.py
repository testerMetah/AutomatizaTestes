"""Inventaria recursos Delphi do RH instalado sem executar rotinas de negócio."""
import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

from automatiza.delphi_resources import Reader, flatten, resource_index, menu_paths
from mapear_modulos_estatico import routes


def extract(origin, output, *, complement=False):
    output.mkdir(parents=True, exist_ok=False)
    (output / 'formularios').mkdir()
    catalog = {'data': datetime.now().astimezone().isoformat(),
               'metodo': 'Leitura estática TPF0; não comprova telas disponíveis nem regras de negócio.',
               'arquivos': [], 'formularios': {}}
    sources = sorted(p for p in origin.iterdir()
                     if p.is_file() and p.name.lower().startswith('rh') != complement
                     and p.suffix.lower() in {'.exe', '.bpl', '.dll'})
    for source in sources:
        record = {'arquivo': source.name, 'formularios': [], 'falhas': []}
        catalog['arquivos'].append(record)
        try:
            data = source.read_bytes()
            record['sha256'] = hashlib.sha256(data).hexdigest()
            for resource in resource_index(data):
                cls = resource['classe']
                if not any(t in cls.lower() for t in ('frm', 'form', 'frame', 'dialog')):
                    continue
                try:
                    reader = Reader(data, resource['offset'] + 4)
                    root = reader.component()
                    encoded = json.dumps(root, sort_keys=True, ensure_ascii=False).encode('utf-8')
                    key = cls + '-' + hashlib.sha256(encoded).hexdigest()[:20]
                    record['formularios'].append({'chave': key, 'offset': resource['offset']})
                    if key not in catalog['formularios']:
                        nodes = list(flatten(root))
                        catalog['formularios'][key] = {
                            'classe': cls, 'caption': root['propriedades'].get('Caption', ''),
                            'componentes': len(nodes), 'origens': [],
                            'mapa': 'formularios/' + key + '.json',
                            'menus': list(menu_paths(root)), 'rotas_actionbars': routes(root),
                            'validado_em_execucao': False}
                        (output / 'formularios' / (key + '.json')).write_text(
                            json.dumps(root, ensure_ascii=False, indent=2), encoding='utf-8')
                    if source.name not in catalog['formularios'][key]['origens']:
                        catalog['formularios'][key]['origens'].append(source.name)
                except Exception as exc:
                    record['falhas'].append({'classe': cls, 'offset': resource['offset'],
                                              'erro': type(exc).__name__ + ': ' + str(exc)})
        except OSError as exc:
            record['erro'] = type(exc).__name__
        if source.name.lower() in {'rh.exe', 'rhid.exe', 'rhpa.exe'}:
            print(json.dumps({'arquivo': source.name, 'recursos': len(record['formularios'])}), flush=True)
    (output / 'catalogo.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding='utf-8')
    frequency = {k: v for k, v in catalog['formularios'].items()
                 if 'RHPA.exe' in v['origens'] or v['classe'].startswith('TFrm_RHPA')}
    (output / 'frequencia.json').write_text(json.dumps(frequency, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Inventário estático do RH', '',
             'Recursos declarados nos arquivos instalados. Não valida navegação, login ou regras.',
             'Valores de campos, SQL, conexões e imagens binárias são omitidos pelo leitor.',
             'Componentes herdados podem exigir consulta a outros formulários.', '',
             '| Formulário | Legenda | Componentes | Origens |', '|---|---|---|---|']
    for k, v in catalog['formularios'].items():
        cells = [f"[{v['classe']}]({v['mapa']})", v['caption'], str(v['componentes']), ', '.join(v['origens'])]
        lines.append('| ' + ' | '.join(c.replace('|', '\\|').replace('\n', ' ').replace('\r', ' ') for c in cells) + ' |')
    (output / 'INDICE.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'arquivos': len(sources), 'formularios_distintos': len(catalog['formularios']),
                      'componentes': sum(v['componentes'] for v in catalog['formularios'].values()),
                      'falhas': sum(len(r['falhas']) + int('erro' in r) for r in catalog['arquivos']),
                      'frequencia_candidatos': len(frequency)}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--origem', type=Path, default=Path(r'C:\meta\rhsis'))
    parser.add_argument('--saida', type=Path, required=True)
    parser.add_argument('--complementar', action='store_true', help='Lê binários sem prefixo RH da mesma pasta')
    args = parser.parse_args()
    extract(args.origem, args.saida, complement=args.complementar)
