"""Empacota somente os artefatos locais explicitamente selecionados."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def main():
    base = ROOT / 'reports/levantamento-20261015'
    selected = set()
    for relative in ('docs/mapeamentos/rh-completo',
                     'docs/mapeamentos/acessus-completo/estatico-20261015-ampliado',
                     'reports/banco/20261015-095741', 'reports/integracao-config/20261015-100206',
                     'reports/levantamento-20261015'):
        for path in (ROOT / relative).rglob('*'):
            if path.is_file() and path.suffix in {'.json', '.md', '.html'} and path.name not in {'manifesto-levantamento.json', 'verificacao-pacote.json'}:
                selected.add(path)
    for relative in ('docs/LEVANTAMENTO-ACESSUS-RH-SQL.md', 'docs/BASES-DE-TESTE.md',
                     'docs/DICIONARIO-BRAS1-HISTORICO.md', 'docs/PISTAS-SQL-INTEGRACAO.md',
                     'README.md', 'CONTEXTO-PARA-CONTINUAR.md', 'pyproject.toml'):
        selected.add(ROOT / relative)
    for relative in ('scripts', 'src/automatiza', 'tests/unit'):
        selected.update(p for p in (ROOT / relative).rglob('*') if p.is_file() and p.suffix in {'.py', '.ps1'})
    manifest = {}
    for path in sorted(selected):
        if not path.resolve().is_relative_to(ROOT) or '.env' in path.parts:
            raise ValueError('Arquivo fora da seleção permitida')
        manifest[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest_file = base / 'manifesto-levantamento.json'
    manifest_file.write_text(json.dumps({'metodo': 'Artefatos estáticos e evidências históricas/atuais identificadas nos documentos.',
                                       'sha256': manifest}, ensure_ascii=False, indent=2), encoding='utf-8')
    bundle_path = base / 'levantamento-acessus-rh-sql.zip'
    with ZipFile(bundle_path, 'w', ZIP_DEFLATED) as bundle:
        for path in sorted(selected):
            bundle.write(path, path.relative_to(ROOT).as_posix())
        bundle.write(manifest_file, manifest_file.relative_to(ROOT).as_posix())
    with ZipFile(bundle_path) as bundle:
        for name, expected in manifest.items():
            if hashlib.sha256(bundle.read(name)).hexdigest() != expected:
                raise RuntimeError('Hash divergente no pacote')
        if any(Path(name).name == '.env' for name in bundle.namelist()):
            raise RuntimeError('Arquivo de credenciais incluído')
    result = {'arquivos_verificados': len(manifest), 'bytes_zip': bundle_path.stat().st_size,
              'sha256_zip': hashlib.sha256(bundle_path.read_bytes()).hexdigest(), 'hashes_consistentes': True,
              'inclui_env': False}
    (base / 'verificacao-pacote.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
