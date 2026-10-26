import argparse
from pathlib import Path

from automatiza.sequencias.engine import generate, load_yaml, run_case
from automatiza.sequencias.relatorio import Report
from automatiza.pausa import TesteCancelado


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sequências com estado; ações reais sem mapa são bloqueadas")
    parser.add_argument("--arquivo", action="append")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--passos", type=int, default=8)
    parser.add_argument("--massa", type=int, default=5)
    args = parser.parse_args(argv)
    paths = args.arquivo or ([str(p) for p in sorted(Path("tests/sequencias").glob("*.yaml"))] if args.seed is None else [])
    cases = [load_yaml(p) for p in paths]
    if args.seed is not None: cases.append(generate(args.seed, count=args.passos, max_mass=args.massa))
    report = Report()
    try:
        for case in cases: run_case(case, report)
    except TesteCancelado:
        report.cases.append({"nome": report.context.get("sequencia", "(execução)"),
                             "seed": report.context.get("seed"), "estado": "CANCELADO",
                             "passos": report.context.get("passo", 0), "erro": "Cancelado pelo usuário"})
        report.emit("CANCELADO_PELO_USUARIO", resultado="CANCELADO")
    path = report.finish()
    print(path.resolve())
    return 2 if any(c["estado"] == "CANCELADO" for c in report.cases) else (1 if any(c["estado"] == "FALHOU" for c in report.cases) else 0)


if __name__ == "__main__": raise SystemExit(main())
