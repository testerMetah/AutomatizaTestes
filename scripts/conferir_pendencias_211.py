"""Confer?ncia das pend?ncias de inspe??o ap?s atualiza??o autorizada para 2.11."""
import json
from pathlib import Path
import inspecionar_modulos_vm as inspect
from automatiza.ambiente import require_interactive_desktop

ROOT = Path(__file__).resolve().parents[1]

def main():
    require_interactive_desktop()
    inspect.STATIC = ROOT / 'docs/mapeamentos/acessus-211/estatico-20261020'
    inspect.walk.CATALOG = inspect.STATIC / 'catalogo.json'
    folder = inspect.configure(ROOT / 'reports/inspecao-telas/vm-211-20261020')
    groups = [('acesso', 10, 10), ('acesso', 13, 13), ('acesso', 19, 19),
              ('refeitorio', 2, 3), ('refeitorio', 7, 7),
              ('estacionamento', 7, 7), ('estacionamento', 9, 9),
              ('escola', 8, 8), ('escola', 12, 12),
              ('administracao', 1, 1), ('administracao', 3, 3)]
    for module, first, last in groups:
        inspect.walk.run(module, first, last)
        inspect.consolidate(folder)
        rows = [json.loads(line) for line in (folder / (module + '-percurso.jsonl')).read_text(encoding='utf-8').splitlines()]
        if rows[-1]['situacao'] == 'FALHA_INSPECAO':
            raise RuntimeError('Inspe??o interrompida; conferir ?ltimo registro antes de continuar.')

if __name__ == '__main__':
    main()
