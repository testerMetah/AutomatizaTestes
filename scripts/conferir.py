"""CLI sem desktop: capturar consulta filtrada ou comparar arquivos locais."""
import argparse
import json
from dataclasses import replace
from automatiza.config import Settings
from automatiza.conferencia import capture, compare_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="acao", required=True)
    query = sub.add_parser("consultar")
    query.add_argument("--filtros", required=True)
    query.add_argument("--saida", required=True)
    query.add_argument("--base", help="Base SQL desta consulta; não altera o .env")
    compare = sub.add_parser("comparar")
    compare.add_argument("--antes", required=True)
    compare.add_argument("--depois", required=True)
    compare.add_argument("--saida", required=True)
    args = parser.parse_args()
    try:
        if args.acao == "consultar":
            from pathlib import Path
            spec = json.loads(Path(args.filtros).read_text(encoding="utf-8-sig"))
            settings = Settings.load()
            if args.base is not None:
                settings = replace(settings, sql_database=args.base)
            result = capture(settings, spec, args.saida)
            print(f"Amostra salva: {len(result['linhas'])} registros. Nenhum dado alterado.")
        else:
            result = compare_files(args.antes, args.depois, args.saida)
            print(f"Comparação salva: {len(result['eventos'])} diferenças entre amostras.")
    except ValueError as exc:
        parser.exit(1, str(exc) + "\n")
    except Exception as exc:
        parser.exit(1, f"Operação não concluída ({type(exc).__name__}); verifique os arquivos/configuração.\n")
