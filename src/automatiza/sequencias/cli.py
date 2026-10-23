import argparse
from pathlib import Path

from automatiza.sequencias.engine import generate, load_yaml, run_case
from automatiza.sequencias.relatorio import Report


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
    for case in cases: run_case(case, report)
    path = report.finish()
    print(path.resolve())
    return 1 if any(c["estado"] == "FALHOU" for c in report.cases) else 0


if __name__ == "__main__": raise SystemExit(main())
