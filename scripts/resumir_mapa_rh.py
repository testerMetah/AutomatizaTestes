"""Gera índice legível de Frequência e manifesto a partir dos mapas locais."""
import hashlib
import json
from pathlib import Path
from automatiza.delphi_resources import flatten


def main():
    base = Path(__file__).resolve().parents[1] / 'docs/mapeamentos/rh-completo'
    source = base / 'estatico-20261015'
    catalog = json.loads((source / 'catalogo.json').read_text(encoding='utf-8'))
    frequency = json.loads((source / 'frequencia.json').read_text(encoding='utf-8'))
    principal = next(v for v in frequency.values() if v['classe'] == 'TFrm_RHPA0010')
    paths = principal['menus']
    leaves = [p for p in paths if not any(q.startswith(p + '->') for q in paths)]
    lines = ['# Frequência — inventário estático', '',
             'Rotas declaradas em RHPA.exe. Não percorridas em execução nesta sessão.',
             f'{len(leaves)} caminhos terminais declarados; alguns podem estar ocultos ou desabilitados.',
             'Nenhuma rota desta lista foi acionada para gerar este documento.', '',
             '## Menus declarados', '']
    lines.extend('- ' + p.replace('->', ' → ') for p in leaves)
    lines += ['', '## Estruturas candidatas', '',
              'A seleção inclui recursos de RHPA.exe e classes TFrm_RHPA de bibliotecas.',
              'Não representa associação exclusiva ou validada ao módulo.', '',
              '| Classe | Legenda | Componentes |', '|---|---|---|']
    for v in frequency.values():
        caption = v['caption'].replace('|', '\\|').replace('\r', ' ').replace('\n', ' ')
        lines.append(f"| [{v['classe']}](estatico-20261015/{v['mapa']}) | {caption} | {v['componentes']} |")
    for cls in ('TFrm_RH0540RegOcorrencias', 'TFrm_RHPA5130'):
        found = [v for v in catalog['formularios'].values() if v['classe'] == cls]
        lines += ['', '## Campos e ações declarados: ' + cls, '',
                  'Nomes e eventos declarados são pistas; controles herdados podem não estar completos.', '',
                  '| Componente | Classe | Legenda | Campo | Evento |', '|---|---|---|---|---|']
        for v in found:
            root = json.loads((source / v['mapa']).read_text(encoding='utf-8'))
            for n in flatten(root):
                p = n['propriedades']
                cells = [n['nome'], n['classe'], p.get('Caption', ''), p.get('DataField', ''), p.get('OnClick', p.get('OnExit', ''))]
                lines.append('| ' + ' | '.join(str(c).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ') for c in cells) + ' |')
    (base / 'FREQUENCIA.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    missing = [v['mapa'] for v in catalog['formularios'].values() if not (source / v['mapa']).is_file()]
    if missing:
        raise RuntimeError('Mapas referenciados ausentes')
    manifest = {str(p.relative_to(base)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(base.rglob('*')) if p.is_file() and p.name != 'manifesto-sha256.json'}
    (base / 'manifesto-sha256.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'mapas_ausentes': len(missing), 'rotas_terminais_declaradas': len(leaves),
                      'arquivos_manifesto': len(manifest)}))


if __name__ == '__main__':
    main()
