"""python -m automatiza.ciclos_cli --help"""
import argparse
import copy
import json
from pathlib import Path

from automatiza.ciclos import Runner, atomic, plan


def main():
    p = argparse.ArgumentParser(description="Planejar/executar ciclos CRUD + API SIRH")
    p.add_argument("acao", choices=["planejar", "executar", "suite"])
    p.add_argument("--arquivo", required=True, help="Manifesto (planejar) ou plano gerado (executar)")
    p.add_argument("--saida", required=True, help="JSON do plano ou pasta de execução/retomada")
    p.add_argument("--semente", type=int, default=211)
    p.add_argument("--rodadas", type=int, default=1)
    p.add_argument("--sementes", type=int, default=3,
                   help="Quantidade de ordens diferentes para suite")
    args = p.parse_args()
    config = json.loads(Path(args.arquivo).read_text(encoding="utf-8-sig"))
    if args.acao == "planejar":
        result = plan(config, args.semente, args.rodadas)
        Path(args.saida).parent.mkdir(parents=True, exist_ok=True)
        atomic(args.saida, result)
        print(f"Plano gerado: {len(result['etapas'])} etapas; semente {args.semente}. Nenhum dado alterado.")
        return
    from automatiza.ciclos_sirh import SirhBackend
    from automatiza.config import ROOT
    from automatiza.observador import observer_lock
    if args.acao == "suite":
        if type(args.sementes) is not int or not 1 <= args.sementes <= 100:
            p.error("--sementes deve ficar entre 1 e 100")
        root = Path(args.saida)
        root.mkdir(parents=True, exist_ok=True)
        outcomes = []
        with observer_lock(ROOT / "reports/controle-executor", label="uma suite de ciclos"):
            for offset in range(args.sementes):
                current_config = copy.deepcopy(config)
                if offset:
                    for case in current_config["casos"]:
                        if not case["presente"] and case["tipo"] != "reserva":
                            case["presente"] = True
                current = plan(current_config, args.semente + offset, args.rodadas)
                folder = root / f"semente-{args.semente + offset}"
                backend = SirhBackend(current_config)
                result = Runner(current, backend, folder).run()
                outcomes.append({"semente": args.semente + offset,
                                 "status": result["status"], "pasta": str(folder)})
                # Cada ordem deve terminar no estado-base antes da próxima começar.
                for case in config["casos"]:
                    if case["tipo"] != "reserva" and backend.source(case) != case["termino"]:
                        atomic(root / "resultado.json", outcomes)
                        raise RuntimeError("Estado-base não restaurado; próxima semente não iniciada.")
                atomic(root / "resultado.json", outcomes)
        print(json.dumps(outcomes, ensure_ascii=True))
        if any(x["status"] != "PASSOU" for x in outcomes):
            raise SystemExit(1)
        return
    with observer_lock(ROOT / "reports/controle-executor", label="um ciclo de testes"):
        result = Runner(config, SirhBackend(config["configuracao"]), args.saida).run()
    print(json.dumps(result, ensure_ascii=True))
    if result["status"] != "PASSOU":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
