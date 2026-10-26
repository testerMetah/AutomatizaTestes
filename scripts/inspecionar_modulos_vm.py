"""Inspeção autorizada das telas Acessus; salva JSON e Markdown a cada captura.

Reutiliza a navegação de inspeção sem salvar cadastros nem executar operações.
Executar somente com a VM livre para controle de janelas.
"""
import argparse
import ctypes
import hashlib
import json
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

import inspecionar_telas as capture
import navegar_inspecao as nav
import percorrer_telas as walk
from automatiza.ambiente import require_interactive_desktop
from pywinauto import Desktop

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / 'docs/mapeamentos/acessus-completo/estatico-20261015-v2'


def flatten(node):
    yield node
    for child in node.get('filhos', []):
        yield from flatten(child)


def escape(value):
    return str('' if value is None else value).replace('|', '\\|').replace('\r', ' ').replace('\n', ' ')


def write_markdown(result, path):
    module, route = result['modulo'], result['rota']
    title = result['janela']['texto'] or result['janela']['classe']
    lines = ['# ' + escape(title), '', '**Módulo:** ' + module,
             '', '**Rota:** ' + escape(route), '', '**Captura real:** ' + result['capturado_em'],
             '', 'Árvore estruturada: [' + path.name + '](' + path.name + ').',
             '', 'Valores dos campos, grades e listas omitidos. IDs, handles e coordenadas são desta sessão.',
             '', '| Caminho estrutural | Classe | Legenda observada | Visível | Habilitado |',
             '|---|---|---|---|---|']
    for node in flatten(result['janela']):
        lines.append('| ' + ' | '.join(escape(x) for x in (
            '/'.join(node['caminho_estrutural']), node['classe'],
            '[valor omitido]' if node['valor_omitido'] else node['texto'],
            node['visivel'], node['habilitado'])) + ' |')
    # Recursos históricos complementam os rótulos não expostos pelo Delphi.
    # São identificados explicitamente como estáticos, nunca como seletores UIA.
    matches = list((STATIC / 'formularios').glob(result['janela']['classe'] + '-*.json'))
    if matches:
        lines += ['', '## Campos e ações declarados no recurso estático', '',
                  'Referência de 15/10; nomes Delphi não são automation_id confirmados.']
        seen = set()
        for source in matches:
            lines += ['', 'Recurso: [' + source.name + '](../../../' + source.relative_to(ROOT).as_posix() + ').', '',
                      '| Nome Delphi | Classe | Legenda | DataField | Evento |', '|---|---|---|---|---|']
            data = json.loads(source.read_text(encoding='utf-8'))
            root = data.get('formulario', data.get('raiz', data))
            for node in flatten(root):
                props = node.get('propriedades', {})
                values = (node.get('nome', ''), node.get('classe', ''), props.get('Caption', ''),
                          props.get('DataField', ''), props.get('OnClick', props.get('OnExit', '')))
                if values in seen or not any(values[2:]):
                    continue
                seen.add(values)
                lines.append('| ' + ' | '.join(escape(x) for x in values) + ' |')
            options = []
            for node in flatten(root):
                props = node.get('propriedades', {})
                choices = props.get('Items.Strings', props.get('Items'))
                if choices:
                    options.append('- `' + escape(node.get('nome', '')) + '`: ' + escape(choices))
            if options:
                lines += ['', 'Opções fixas declaradas (não são dados consultados):', '', *options, '']
    path.with_suffix('.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def configure(folder):
    folder = Path(folder).resolve()
    if not folder.is_relative_to(ROOT / 'reports/inspecao-telas'):
        raise ValueError('Sessão deve ficar em reports/inspecao-telas.')
    folder.mkdir(parents=True, exist_ok=True)
    nav.FOLDER = walk.FOLDER = folder
    original = capture.snapshot

    def snapshot(handle, target, slug, module, route, **kwargs):
        base = slug
        attempt = 1
        while (Path(target) / (slug + '.json')).exists():
            attempt += 1
            slug = base + '-tentativa-' + str(attempt)
        result, path = original(handle, target, slug, module, route, **kwargs)
        write_markdown(result, path)
        return result, path

    nav.snapshot = walk.snapshot = snapshot
    return folder


def close_readonly(entry):
    for window in reversed(list(walk.visible_screens(entry).values())):
        if not window.is_enabled():
            continue
        if window.class_name() in {'#32770', 'TMessageForm'}:
            buttons = walk.safe_buttons(window, 'OK') or walk.safe_buttons(window, '&OK')
            if len(buttons) == 1:
                next(iter(buttons.values())).click_input()
            else:
                window.close()
        else:
            cancel = walk.safe_buttons(window, 'Cancelar (Ctrl+D)')
            if len(cancel) == 1:
                next(iter(cancel.values())).click_input()
            if ctypes.windll.user32.IsWindow(window.handle):
                try:
                    window.close()
                except Exception:
                    time.sleep(.3)
                    if ctypes.windll.user32.IsWindow(window.handle) and window.is_visible():
                        raise
        time.sleep(.15)
    if walk.visible_screens(entry):
        raise RuntimeError('Formulário ainda aberto; conferir manualmente antes de continuar.')


def consolidate(folder):
    for path in folder.glob('*.json'):
        data = json.loads(path.read_text(encoding='utf-8'))
        if isinstance(data, dict) and 'janela' in data:
            write_markdown(data, path)
    registry = json.loads((folder / 'modulos.json').read_text(encoding='utf-8'))
    catalog = json.loads(walk.CATALOG.read_text(encoding='utf-8'))
    docs = ROOT / 'docs/mapeamentos' / folder.name
    docs.mkdir(parents=True, exist_ok=True)
    summary = {'sessao': str(folder.relative_to(ROOT)), 'gerado_em': datetime.now().astimezone().isoformat(),
               'limite': 'Inspeção de telas; não comprova regras de negócio ou importação.', 'modulos': {}}
    code = {'observacao': 'Rotas e janelas observadas; controles são candidatos, exigir unicidade antes de usar.', 'modulos': {}}
    index = ['# Inspeção real dos módulos na VM', '', 'Sessão: ' + folder.name, '',
             'Uma tela é aberta, inspecionada e salva antes da próxima. Sem gravação de dados de negócio.', '',
             '| Módulo | Rotas previstas | Inspecionadas | Outras situações |', '|---|---:|---:|---:|']
    for module, (caption, cls) in nav.MODULES.items():
        expected = next(m['rotas'] for m in catalog['modulos'][module]['menus'] if m['formulario'] == cls)
        log = folder / (module + '-percurso.jsonl')
        observed = {}
        if log.exists():
            for line in log.read_text(encoding='utf-8').splitlines():
                row = json.loads(line)
                observed[row['indice']] = row
        records = [observed.get(i, {'indice': i, **route, 'situacao': 'PENDENTE', 'mapas': []})
                   for i, route in enumerate(expected, 1)]
        counts = Counter(r['situacao'] for r in records)
        summary['modulos'][module] = {'janela': registry.get(module), 'totais': dict(counts), 'rotas': records}
        binary = Path(catalog['modulos'][module]['arquivo'])
        if binary.is_file():
            digest = hashlib.sha256(binary.read_bytes()).hexdigest()
            summary['modulos'][module]['binario'] = {'arquivo': str(binary), 'sha256_atual': digest,
                'igual_ao_catalogo_estatico': digest == catalog['modulos'][module].get('sha256')}
        code['modulos'][module] = {'painel': ['Modulos', caption], 'principal_classe': cls, 'telas': []}
        index.append(f'| [{caption}]({module}.md) | {len(records)} | {counts["INSPECIONADA"]} | {len(records)-counts["INSPECIONADA"]} |')
        lines = ['# ' + caption, '', '| Rota | Situação | Telas e mapas | Observações |', '|---|---|---|---|']
        for row in records:
            maps = []
            for item in row.get('mapas', []) + [a['mapa'] for a in row.get('abas', []) + row.get('abas_inclusao', [])]:
                path = Path(item).with_suffix('.md')
                maps.append('[' + path.stem + '](../../../' + path.as_posix() + ')')
            selectors = []
            for item in row.get('mapas', []):
                data = json.loads((ROOT / item).read_text(encoding='utf-8'))
                controls = [n for n in flatten(data['janela']) if n['visivel']]
                frequencies = Counter((n['classe'], n['texto']) for n in controls if n['texto'])
                selectors.append({'janela_classe': data['janela']['classe'], 'titulo': data['janela']['texto'],
                    'mapa': item, 'controles_unicos_visiveis': [
                        {'classe': n['classe'], 'titulo': n['texto'], 'habilitado': n['habilitado']}
                        for n in controls if n['texto'] and frequencies[(n['classe'], n['texto'])] == 1
                        and ('button' in n['classe'].lower() or n['classe'] == 'TBitBtn')]})
            code['modulos'][module]['telas'].append({'rota': row['rota_declarada'], 'situacao': row['situacao'], 'formularios': selectors})
            lines.append('| ' + ' | '.join((escape(' → '.join(row['rota_declarada'])), escape(row['situacao']),
                         ' '.join(maps), escape(row.get('erro', row.get('motivo', row.get('inclusao', '')))))) + ' |')
        lines += ['', 'Os links apontam para mapas Markdown por tela/aba, acompanhados de JSON.',
                  'As operações de gravação, exclusão, importação, impressão e equipamentos não foram executadas.',
                  'Rotas de saída são inventariadas sem acionamento. Campos ocultos são candidatos; não são controles utilizáveis confirmados.']
        (docs / (module + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    records = [r for module in summary['modulos'].values() for r in module['rotas']]
    summary['totais'] = {
        'rotas_previstas': len(records), 'situacoes': dict(Counter(r['situacao'] for r in records)),
        'variacoes_abas': sum(len(r.get('abas', [])) + len(r.get('abas_inclusao', [])) for r in records),
        'inclusoes_canceladas': sum('cancelado sem salvar' in r.get('inclusao', '') for r in records),
        'mapas_markdown': len(list(folder.glob('*.md')))}
    index += ['', '## Material para reutilizar', '',
              '- [Catálogo de telas e cobertura](catalogo-telas.json).',
              '- [Rotas, janelas e botões candidatos para código](rotas-para-codigo.json).',
              '- [Painel de Módulos](../../../' + folder.relative_to(ROOT).as_posix() + '/painel-corrigido.md).',
              '', 'Cada mapa registra a captura real e a referência estática separadamente. Valores de dados são omitidos.',
              'Nomes Delphi não são automation_id. Handles e IDs de sessão não são seletores permanentes.',
              '', 'As rotas indisponíveis ou não acionadas permanecem identificadas no catálogo; não são aprovações.',
              '', 'Totais desta sessão:', '', '```json', json.dumps(summary['totais'], ensure_ascii=False, indent=2), '```']
    (docs / 'LEIA-ME.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    (docs / 'catalogo-telas.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    (docs / 'rotas-para-codigo.json').write_text(json.dumps(code, ensure_ascii=False, indent=2), encoding='utf-8')
    manifest = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for directory in (folder, docs) for p in directory.rglob('*')
                if p.is_file() and p.name != 'manifesto-sha256.json'}
    (folder / 'manifesto-sha256.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('acao', choices=['iniciar', 'modulo', 'consolidar', 'fechar-leitura'])
    parser.add_argument('--sessao', type=Path, required=True)
    parser.add_argument('--catalogo', type=Path, help='Cat?logo est?tico da vers?o instalada')
    parser.add_argument('--modulo', choices=nav.MODULES)
    parser.add_argument('--inicio', type=int, default=1)
    parser.add_argument('--fim', type=int)
    args = parser.parse_args()
    global STATIC
    if args.catalogo:
        walk.CATALOG = args.catalogo.resolve()
        STATIC = walk.CATALOG.parent
    folder = configure(args.sessao)
    if args.acao == 'consolidar':
        result = consolidate(folder)
        print(json.dumps({m: d['totais'] for m, d in result['modulos'].items()}))
        return
    require_interactive_desktop()
    if args.acao == 'iniciar':
        nav.open_modules()
    else:
        if not args.modulo:
            parser.error('Informe --modulo.')
        registry = json.loads((folder / 'modulos.json').read_text(encoding='utf-8'))
        if args.acao == 'fechar-leitura':
            close_readonly(registry[args.modulo])
        else:
            walk.run(args.modulo, args.inicio, args.fim)
        consolidate(folder)


if __name__ == '__main__':
    main()
