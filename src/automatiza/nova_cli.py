"""Entrada única. Comandos antigos continuam disponíveis via automatiza.cli."""
import argparse
import json
import os
import struct
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from automatiza.catalogo_comandos import COMANDOS
from automatiza.config import ROOT


def parser_cli():
    p = argparse.ArgumentParser(prog="automatiza", description="Testes do Acessus em português")
    sub = p.add_subparsers(dest="comando", required=True)
    a = sub.add_parser("ambiente", help="Pré-checagem somente leitura")
    a.add_argument("--perfil", default="auditorias")
    a = sub.add_parser("auditorias", help="Testar históricos e filtros")
    a.add_argument("--modulo", required=True, choices=("acesso", "refeitorio", "portaria", "estacionamento", "escola", "administracao", "todos"))
    a.add_argument("--perfil", default="auditorias")
    a.add_argument("--pid", type=int)
    a.add_argument("--extremo", action="store_true")
    a.add_argument("--filtro")
    a.add_argument("--pular", default="")
    a.add_argument("--saida")
    a.add_argument("--timeout", type=int, default=45)
    a.add_argument("--reinicios", type=int, default=3)
    a = sub.add_parser("sequencias", help="Rodar cenário YAML ou semente")
    g = a.add_mutually_exclusive_group()
    g.add_argument("--arquivo")
    g.add_argument("--seed", type=int)
    a.add_argument("--passos", type=int, default=8)
    a.add_argument("--massa", type=int, default=5)
    a = sub.add_parser("robot", help="Rodar suíte Robot")
    a.add_argument("--tag", default="smoke")
    a = sub.add_parser("observar", help="Observação SQL")
    a.add_argument("acao", choices=("iniciar", "anotar", "status", "parar"))
    a.add_argument("--nota")
    a.add_argument("--duracao", type=float, default=7200)
    a.add_argument("--intervalo", type=float, default=15)
    a = sub.add_parser("conferir", help="Retratos de consultas")
    a.add_argument("acao", choices=("consultar", "comparar"))
    a.add_argument("--filtros")
    a.add_argument("--antes")
    a.add_argument("--depois")
    a.add_argument("--saida")
    a.add_argument("--base")
    a = sub.add_parser("ciclos", help="Ciclos RH/SIRH")
    a.add_argument("acao", choices=("planejar", "executar", "suite"))
    a.add_argument("--arquivo", required=True)
    a.add_argument("--saida", required=True)
    a.add_argument("--semente", type=int, default=211)
    a.add_argument("--rodadas", type=int, default=1)
    a.add_argument("--sementes", type=int, default=3)
    a.add_argument("--perfil", default="sequencias")
    a.add_argument("--confirmo-escrita", action="store_true")
    a = sub.add_parser("comparar-rodadas", help="Comparar falhas de duas rodadas")
    a.add_argument("anterior")
    a.add_argument("atual")
    sub.add_parser("testes-unitarios", help="pytest tests/unit -q")
    sub.add_parser("comandos", help="Catálogo didático")
    sub.add_parser("painel", help="Servidor local")
    return p


def require_32():
    if struct.calcsize("P") * 8 != 32:
        raise RuntimeError("Python 32 bits obrigatório. Execute C:\\python32b\\venv32\\Scripts\\automatiza.exe.")


def _exec(args, *, env=None):
    return subprocess.call([sys.executable, *map(str, args)], cwd=ROOT, env=env)


def executar(ns):
    if ns.comando == "comandos":
        for item in COMANDOS:
            print(f"\n[{item['tema']}] automatiza {item['comando']} — {item['descricao']}")
            print(f"  Quando usar: {item['descricao']}")
            print(f"  Exemplo: {item['exemplo']}")
            print(f"  Opções: {item['opcoes']}")
        return 0
    if ns.comando == "ambiente":
        from automatiza.diagnostico_unificado import executar as diagnosticar
        items = diagnosticar(ns.perfil)
        for item in items:
            print(f"{item['estado']:6} | {item['item']}: {item['detalhe']}")
        return 1 if any(x["estado"] == "ERRO" for x in items) else 0
    if ns.comando == "auditorias":
        from automatiza.supervisor_auditorias import executar as auditar
        return auditar(ns)
    if ns.comando == "sequencias":
        args = ["-m", "automatiza.sequencias.cli"]
        if ns.arquivo:
            args += ["--arquivo", ns.arquivo]
        if ns.seed is not None:
            args += ["--seed", ns.seed]
        args += ["--passos", ns.passos, "--massa", ns.massa]
        return _exec(args)
    if ns.comando == "robot":
        return _exec(["-m", "robot", "--outputdir", str(ROOT / "reports/robot"),
                      "--include", ns.tag, str(ROOT / "tests/sequencias/suites.robot")])
    if ns.comando == "observar":
        from automatiza.observador import annotate, observer_status, run_observer, stop_observer
        from automatiza.config import Settings
        base = ROOT / "reports/observacao"
        if ns.acao == "iniciar":
            state = run_observer(Settings.load(), base, duration=ns.duracao, interval=ns.intervalo, people=())
            print(json.dumps(state, ensure_ascii=False, default=str))
        elif ns.acao == "status":
            folder, state = observer_status(base)
            print(json.dumps(state, ensure_ascii=False, default=str))
        elif ns.acao == "parar":
            print(stop_observer(base))
        else:
            if not ns.nota:
                raise ValueError("Informe --nota para anotar.")
            print(annotate(base, ns.nota))
        return 0
    if ns.comando == "conferir":
        args = [str(ROOT / "scripts/conferir.py"), ns.acao]
        for name in ("filtros", "antes", "depois", "saida", "base"):
            value = getattr(ns, name)
            if value:
                args += [f"--{name}", value]
        return _exec(args)
    if ns.comando == "ciclos":
        from automatiza.perfis_teste import configuracao, validar_escrita
        if ns.acao in {"executar", "suite"}:
            if not ns.confirmo_escrita:
                raise ValueError("Escrita recusada: informe --confirmo-escrita após conferir o banco de teste.")
            actual = validar_escrita(configuracao(ns.perfil))
            print(f"Banco efetivo autorizado: {actual}", flush=True)
        args = ["-m", "automatiza.ciclos_cli", ns.acao, "--arquivo", ns.arquivo,
                "--saida", ns.saida, "--semente", ns.semente, "--rodadas", ns.rodadas]
        if ns.acao == "suite":
            args += ["--sementes", ns.sementes]
        return _exec(args)
    if ns.comando == "comparar-rodadas":
        from automatiza.relatorio_auditorias import comparar
        print(json.dumps(comparar(ns.anterior, ns.atual), ensure_ascii=False, indent=2))
        return 0
    if ns.comando == "testes-unitarios":
        return _exec(["-m", "pytest", "tests/unit", "-q"])
    if ns.comando == "painel":
        from automatiza.painel import iniciar
        iniciar()
        return 0
    raise ValueError(f"Comando desconhecido: {ns.comando}")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    legacy = {"diagnostico", "banco", "inspecionar", "consulta", "abrir", "acompanhar",
              "rh", "iniciar", "observar-status", "parar-observacao", "anotar", "mapear-delphi",
              "analisar", "seguir-analise", "analise-status", "parar-analise",
              "registrar-caso", "exportar-evidencias", "atualizar-referencias"}
    if argv and argv[0] in legacy:
        require_32()
        return _exec(["-m", "automatiza.cli", *argv])
    ns = parser_cli().parse_args(argv)
    require_32()
    try:
        return executar(ns)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
