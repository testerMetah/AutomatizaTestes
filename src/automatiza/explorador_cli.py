"""CLI independente de IA para exploração reproduzível do Acessus."""

import argparse
import json
import re
from pathlib import Path

from automatiza.config import ROOT
from automatiza.explorador import Explorer, validate_config


CATALOG = ROOT / "docs/mapeamentos/vm-211-20261020/rotas-para-codigo.json"
IMMEDIATE = re.compile(r"\b(sair|excluir|gerar|importar|exportar|enviar|processar|executar|comandos)\b", re.I)


def generate(catalog: Path, *, include_pending=False) -> dict:
    data = json.loads(Path(catalog).read_text(encoding="utf-8"))
    routes = []
    for module, detail in data["modulos"].items():
        for screen in detail["telas"]:
            route = screen.get("rota", [])
            allowed_status = ({"INSPECIONADA", "PENDENTE", "DIALOGO_OBSERVADO"} if include_pending
                              else {"INSPECIONADA", "DIALOGO_OBSERVADO"})
            administrative_form = (module == "administracao" and route in
                                   (["Cadastros", "Usuários"], ["Parâmetros", "Parâmetros do Sistema"]))
            if (screen.get("situacao") not in allowed_status
                    or len(route) < 2 or not (route[-1].endswith("...") or administrative_form)
                    or IMMEDIATE.search(" ".join(route))):
                continue
            routes.append({"modulo": module, "menu": route})
    return validate_config({
        "versao": 1,
        "versao_acessus": "2.11.1.0",
        "semente": 2111,
        "destino_sql": {"servidor": "desk-tec", "banco": "novo123"},
        "rotas": routes,
        "valores": {
            "texto": ["TESTE EXPLORATORIO", "abc", "123"],
            "numero": ["0", "1", "999"],
            "data": ["21/10/2026", "01/01/2027"],
            "hora": ["08:15", "23:30"],
            "combo": [],
            "lista": [],
        },
        "politica": {
            "permitir_gravacao": False,
            "base_descartavel_confirmada": False,
            "botoes_autorizados": [],
            "capturar_erros": False,
        },
        "exploracao": {"entrar_em_cadastro": True, "combo_auto": True, "max_opcoes_combo": 5},
        "limites": {"max_acoes_por_tela": 24, "max_sequencias_por_tela": 120,
                    "sequencias_aleatorias": 40, "comprimento_aleatorio": 4},
    })


def check_environment(config):
    import win32api

    from automatiza.perfis import destinations_match, import_destination

    exe = Path("C:/acesso/Acessus.exe")
    info = win32api.GetFileVersionInfo(str(exe), "\\")
    version = ".".join(str(part) for part in (
        info["FileVersionMS"] >> 16, info["FileVersionMS"] & 0xffff,
        info["FileVersionLS"] >> 16, info["FileVersionLS"] & 0xffff,
    ))
    if version != config.get("versao_acessus"):
        raise RuntimeError(f"Versão instalada {version}; plano exige {config.get('versao_acessus')}.")
    target = config.get("destino_sql")
    if not isinstance(target, dict) or not destinations_match(
            import_destination(Path("C:/acesso/ConexaoConfig.ini")), target):
        raise RuntimeError("Destino do importador diferente do plano; execução recusada.")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Explora controles do Acessus com diário por ação.")
    command = parser.add_subparsers(dest="comando", required=True)
    create = command.add_parser("gerar-config", help="Gera rotas candidatas a partir do mapa de telas.")
    create.add_argument("--catalogo", type=Path, default=CATALOG)
    create.add_argument("--saida", type=Path, required=True)
    create.add_argument("--incluir-pendentes", action="store_true")
    run = command.add_parser("executar", help="Controla telas; requer sessão Windows interativa.")
    run.add_argument("--arquivo", type=Path, required=True)
    run.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.comando == "gerar-config":
        config = generate(args.catalogo, include_pending=args.incluir_pendentes)
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        with args.saida.open("x", encoding="utf-8") as output:
            json.dump(config, output, ensure_ascii=False, indent=2)
        print(f"{len(config['rotas'])} rotas candidatas: {args.saida}")
        return 0
    config = validate_config(json.loads(args.arquivo.read_text(encoding="utf-8-sig")))
    check_environment(config)
    from automatiza.ambiente import require_interactive_desktop
    from automatiza.explorador_windows import WindowsExplorerBackend
    from automatiza.observador import observer_lock
    from automatiza.explorador_relatorio import write_report

    require_interactive_desktop()
    with observer_lock(ROOT / "reports/controle-executor", label="exploração do Acessus"):
        try:
            result = Explorer(config, WindowsExplorerBackend(config), args.saida).run()
        finally:
            if (args.saida / "passos.jsonl").is_file():
                write_report(config, args.saida)
    print(json.dumps({"status": result["status"], "sequencias": len(result["concluidas"]),
                      "erros": result["erros"], "log": str(args.saida / "passos.log")}, ensure_ascii=False))
    return 0 if result["erros"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
