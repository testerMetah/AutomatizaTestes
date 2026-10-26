"""Entrada única. Comandos antigos continuam disponíveis via automatiza.cli."""
import argparse
import json
import os
import struct
import subprocess
import sys
import tempfile
import time
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
    sub.add_parser("pausa-teste", help="Testar sentinela e atalhos globais")
    a = sub.add_parser("aviso-teste", help="Visualizar aviso sem executar teste")
    a.add_argument("tipo", choices=("inicio", "fim", "cancelado"))
    sub.add_parser("indice", help="Recriar índice das rodadas")
    a = sub.add_parser("organizar", help="Migrar saídas antigas com preservação")
    g = a.add_mutually_exclusive_group()
    g.add_argument("--simular", action="store_true", default=True)
    g.add_argument("--aplicar", action="store_true")
    sub.add_parser("verificar-estrutura", help="Verificar pastas e manifestos")
    a = sub.add_parser("limpar", help="Compactar rodadas antigas sem apagar")
    a.add_argument("--aplicar", action="store_true")
    a.add_argument("--simular", action="store_true", default=True)
    a.add_argument("--dias", type=int, default=60)
    a = sub.add_parser("marcar", help="Marcar rodada importante ou adicionar nota")
    a.add_argument("id")
    a.add_argument("--manter", action="store_true")
    a.add_argument("--nota")
    a = sub.add_parser("resumo-para-ia", help="Resumo compacto de uma rodada")
    a.add_argument("id", nargs="?", default="ultima")
    a = sub.add_parser("exportar", help="Pacote sem segredos para compartilhar")
    a.add_argument("id")
    a.add_argument("--com-evidencias", action="store_true")
    return p


def require_32():
    if struct.calcsize("P") * 8 != 32:
        raise RuntimeError("O painel não abriu porque este Python não é 32 bits. O Acessus exige a versão 32 bits. Use Abrir-Painel.bat ou C:\\python32b\\venv32\\Scripts\\automatiza.exe.")


def _exec(args, *, env=None):
    return subprocess.call([sys.executable, *map(str, args)], cwd=ROOT, env=env)


def executar(ns):
    if ns.comando == "indice":
        from automatiza.organizacao import indice
        print(f"Índice gerado: {len(indice())} rodadas")
        return 0
    if ns.comando == "organizar":
        from automatiza.manutencao_saidas import organizar
        plano = organizar(aplicar=ns.aplicar)
        for origem, destino, arquivo, tamanho in plano:
            print(f"{origem} -> {destino} | arquivo: {arquivo} | {tamanho} bytes")
        print(f"{len(plano)} itens {'migrados' if ns.aplicar else 'planejados; use --aplicar para executar'}")
        return 0
    if ns.comando == "verificar-estrutura":
        from automatiza.manutencao_saidas import verificar
        erros = verificar()
        for erro in erros: print("ERRO:", erro)
        print("Estrutura íntegra." if not erros else f"{len(erros)} problemas encontrados.")
        return 1 if erros else 0
    if ns.comando == "limpar":
        from automatiza.manutencao_saidas import limpar
        itens = limpar(aplicar=ns.aplicar, dias=ns.dias)
        for item in itens: print(item["id"])
        print(f"{len(itens)} rodadas {'compactadas' if ns.aplicar else 'candidatas'}; originais preservados.")
        return 0
    if ns.comando == "marcar":
        from automatiza.manutencao_saidas import marcar
        marcar(ns.id, ns.manter, ns.nota)
        print(f"Rodada {ns.id} atualizada.")
        return 0
    if ns.comando == "resumo-para-ia":
        from automatiza.resumo_ia import gerar
        print(gerar(ns.id))
        return 0
    if ns.comando == "exportar":
        from automatiza.resumo_ia import exportar
        print(exportar(ns.id, ns.com_evidencias))
        return 0
    if ns.comando in {"pausa-teste", "aviso-teste"}:
        from automatiza.sentinela.autoteste import executar as testar
        return testar(ns)
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
            if os.environ.get("AUTOMATIZA_OBSERVADOR_WORKER") == "1":
                state = run_observer(Settings.load(), base, duration=ns.duracao,
                                     interval=ns.intervalo, people=())
                print(json.dumps(state, ensure_ascii=False, default=str))
            else:
                base.mkdir(parents=True, exist_ok=True)
                stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                log = (base / f"processo-{stamp}.log").open("w", encoding="utf-8")
                env = os.environ.copy()
                env["AUTOMATIZA_OBSERVADOR_WORKER"] = "1"
                proc = subprocess.Popen([sys.executable, "-u", "-m", "automatiza.nova_cli",
                                         "observar", "iniciar", "--duracao", str(ns.duracao),
                                         "--intervalo", str(ns.intervalo)],
                                        cwd=ROOT, env=env, stdin=subprocess.DEVNULL,
                                        stdout=log, stderr=subprocess.STDOUT,
                                        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                log.close()
                print(f"Observação iniciada em segundo plano: PID {proc.pid}; log {base / ('processo-' + stamp + '.log')}")
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
        ambiente_ciclo = None
        if ns.acao in {"executar", "suite"}:
            if not ns.confirmo_escrita:
                raise ValueError("Escrita recusada: informe --confirmo-escrita após conferir o banco de teste.")
            from dataclasses import replace
            from automatiza.database import SqlServer
            from automatiza.perfis_teste import permitidos
            manifest = json.loads(Path(ns.arquivo).read_text(encoding="utf-8-sig"))
            target = manifest.get("configuracao", manifest)
            profile_settings = configuracao(ns.perfil)
            if target.get("destino", "").casefold() != profile_settings.sql_database.casefold():
                raise ValueError("Escrita recusada: destino do manifesto/plano difere do perfil.")
            if target.get("origem", "").casefold() not in permitidos():
                raise ValueError("Escrita recusada: origem do manifesto não é banco de teste permitido.")
            SqlServer(replace(profile_settings, sql_database=target["origem"])).assert_database()
            actual = validar_escrita(profile_settings)
            print(f"Banco efetivo autorizado: {actual}", flush=True)
            ambiente_ciclo = os.environ.copy()
            ambiente_ciclo["SQL_SERVER"] = profile_settings.sql_server
            ambiente_ciclo["SQL_DATABASE"] = profile_settings.sql_database
        args = ["-m", "automatiza.ciclos_cli", ns.acao, "--arquivo", ns.arquivo,
                "--saida", ns.saida, "--semente", ns.semente, "--rodadas", ns.rodadas]
        if ns.acao == "suite":
            args += ["--sementes", ns.sementes]
        return _exec(args, env=ambiente_ciclo)
    if ns.comando == "comparar-rodadas":
        from automatiza.relatorio_auditorias import comparar
        print(json.dumps(comparar(ns.anterior, ns.atual), ensure_ascii=False, indent=2))
        return 0
    if ns.comando == "testes-unitarios":
        temp = ROOT / "resultados" / f"pytest-cli-{datetime.now():%Y%m%d-%H%M%S}"
        return _exec(["-m", "pytest", "tests/unit", "-q", f"--basetemp={temp}",
                      "-p", "no:cacheprovider"])
    if ns.comando == "painel":
        from automatiza.painel import iniciar
        iniciar()
        return 0
    raise ValueError(f"Comando desconhecido: {ns.comando}")


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    argv = list(sys.argv[1:] if argv is None else argv)
    legacy = {"diagnostico", "banco", "inspecionar", "consulta", "abrir", "acompanhar",
              "rh", "iniciar", "observar-status", "parar-observacao", "anotar", "mapear-delphi",
              "analisar", "seguir-analise", "analise-status", "parar-analise",
              "registrar-caso", "exportar-evidencias", "atualizar-referencias"}
    try:
        require_32()
        if argv and argv[0] in legacy:
            return _exec(["-m", "automatiza.cli", *argv])
        ns = parser_cli().parse_args(argv)
        testes = {"auditorias", "sequencias", "robot", "ciclos", "conferir", "observar", "testes-unitarios"}
        if ns.comando in testes and not (ns.comando == "observar" and ns.acao in {"status", "anotar", "parar"}):
            from automatiza.pausa import TesteCancelado, gravar, ler
            from automatiza.config import ROOT
            from automatiza.sessao import Rodada
            nome = ("Auditorias — " + ns.modulo) if ns.comando == "auditorias" else ns.comando.capitalize()
            perfil = getattr(ns, "perfil", "auditorias" if ns.comando == "auditorias" else "sequencias")
            try:
                from automatiza.perfis_teste import carregar, configuracao as perfil_config
                from automatiza.database import SqlServer
                perfil_dados = carregar(perfil)
                ajustes = perfil_config(perfil)
                banco = SqlServer(ajustes).assert_database()
                servidor = ajustes.sql_server
                executavel = perfil_dados.get("pasta_executaveis")
            except Exception:
                banco, servidor, executavel = None, None, None
            alvo = getattr(ns, "modulo", None) or getattr(ns, "tag", None) or getattr(ns, "acao", None) or "geral"
            rodada = Rodada(ns.comando, alvo, perfil, banco, servidor,
                            opcoes={k: v for k, v in vars(ns).items() if k not in {"comando", "saida"}},
                            executavel=executavel)
            base = Path(os.environ.get("AUTOMATIZA_PAUSA_DIR") or tempfile.mkdtemp(prefix="automatiza-pausa-"))
            base.mkdir(parents=True, exist_ok=True)
            os.environ["AUTOMATIZA_PAUSA_DIR"] = str(base)
            gravar(base / "meta.json", {"nome": nome, "perfil": perfil, "banco": banco,
                                        "pid": os.getpid(), "inicio_monotonico": time.monotonic()})
            gravar(base / "controle.json", {"estado": "RODANDO", "instante": time.time()})
            sentinela = None
            try:
                exe = Path(sys.executable).with_name("pythonw.exe")
                if not exe.exists():
                    exe = Path(sys.executable)
                log_sentinela = (base / "sentinela-erro.log").open("w", encoding="utf-8")
                sentinela = subprocess.Popen([str(exe), "-m", "automatiza.sentinela.runtime", str(base)],
                                             cwd=ROOT, stdin=subprocess.DEVNULL, stdout=log_sentinela,
                                             stderr=subprocess.STDOUT, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                log_sentinela.close()
                limite = time.monotonic() + 1.5
                while time.monotonic() < limite and not (base / "sentinela.json").exists() and sentinela.poll() is None:
                    time.sleep(0.03)
                if sentinela.poll() is not None:
                    print("AVISO: sentinela não iniciou; teste continuará sem pausa.", flush=True)
                else:
                    print(f"Sentinela: {ler(base / 'sentinela.json').get('atalho') or 'aguardando registro'}; controle: {base}", flush=True)
            except OSError as exc:
                print(f"AVISO: sentinela indisponível ({type(exc).__name__}); teste continuará.", flush=True)
            try:
                with rodada:
                    try:
                        codigo = executar(ns)
                        final = "CANCELADO" if ler(base / "controle.json").get("estado") == "CANCELANDO" or codigo == 2 else ("CONCLUIDO" if codigo == 0 else "FALHOU")
                        return codigo
                    except TesteCancelado:
                        final = "CANCELADO"
                        print("Teste cancelado pelo usuário.", flush=True)
                        return 2
                    except BaseException:
                        final = "FALHOU"
                        raise
            finally:
                eventos = []
                if (base / "eventos.jsonl").is_file():
                    for line in (base / "eventos.jsonl").read_text(encoding="utf-8").splitlines():
                        try: eventos.append(json.loads(line))
                        except ValueError: continue
                pausas = {"quantidade": sum(e.get("tipo") == "PAUSA_INICIADA" for e in eventos),
                          "tempo_total_s": round(sum(e.get("duracao_ms", 0) for e in eventos if e.get("tipo") == "PAUSA_RETOMADA") / 1000, 3)}
                rodada.concluir(final, pausas)
                gravar(base / "final.json", {"estado": final, "resumo": f"Duração: {int(time.monotonic()-ler(base/'meta.json')['inicio_monotonico'])} s",
                                              "pasta": str(rodada.pasta)})
        return executar(ns)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
