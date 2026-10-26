import argparse
import platform
import json
from dataclasses import replace
from pathlib import Path

import pyodbc

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer


def main():
    parser = argparse.ArgumentParser(description="Diagnóstico da automação")
    parser.add_argument("command", choices=["diagnostico", "banco", "inspecionar", "consulta", "abrir", "acompanhar", "rh", "iniciar",
                                           "observar", "observar-status", "parar-observacao", "anotar", "mapear-delphi",
                                           "analisar", "seguir-analise", "analise-status", "parar-analise", "registrar-caso", "exportar-evidencias", "atualizar-referencias"])
    parser.add_argument("--arquivo", help="Arquivo de entrada SQL, JSON ou binário, conforme o comando")
    parser.add_argument("--base", help="Base SQL deste teste; substitui SQL_DATABASE apenas nesta execução")
    parser.add_argument("--parametros", default="[]", help='Parâmetros como lista JSON, por exemplo [123]')
    parser.add_argument("--saida", help="Arquivo JSON opcional para salvar o resultado")
    parser.add_argument("--abrir", action="store_true", help="Inicia o executável na inspeção")
    parser.add_argument("--cenario", help="Arquivo JSON das verificações de importação")
    parser.add_argument("--caso", help="Identificador do caso a acompanhar após a ação no RH")
    parser.add_argument("--duracao", type=float, default=7200, help="Duração da observação SQL em segundos")
    parser.add_argument("--intervalo", type=float, default=15, help="Intervalo entre amostras SQL em segundos")
    parser.add_argument("--pessoas", nargs="+", type=int, help="IdPessoa internos do Acessus para filtrar a observação")
    parser.add_argument("--nota", help="Anotação de ação manual para correlacionar com o banco")
    parser.add_argument("--classe", help="Classe do formulário Delphi para leitura estática do binário")
    parser.add_argument("--dados", help="JSON opcional com pessoa, tipo, causa e datas de uma anotação")
    args = parser.parse_args()
    settings = Settings.load()
    if args.base is not None:
        settings = replace(settings, sql_database=args.base)
    if args.command in {"analisar", "seguir-analise", "analise-status", "parar-analise", "registrar-caso", "exportar-evidencias", "atualizar-referencias"}:
        from automatiza.acompanhante import analysis_status, follow_analysis, save_case
        from automatiza.analise import analyze_session, export_bundle
        from automatiza.observador import active_folder, observer_status, utc_now
        base = ROOT / "reports" / "observacao"
        try:
            folder = active_folder(base)
            if args.command == "analisar":
                folder, state = observer_status(base)
                result = analyze_session(folder, source_state=state)
                print(f"Análise gerada: {len(result['pessoas'])} pessoas; {len(result['alertas'])} alertas para conferir.")
            elif args.command == "seguir-analise":
                result = follow_analysis(base, interval=args.intervalo, duration=args.duracao, reset_stop=True)
                print("Análise contínua encerrada: " + result["status"])
                if result["status"] == "ERRO":
                    raise SystemExit(1)
            elif args.command == "analise-status":
                folder, state = analysis_status(base)
                print(json.dumps(state, ensure_ascii=False, indent=2))
            elif args.command == "parar-analise":
                (folder / "parar-analise.sinal").write_text(utc_now(), encoding="utf-8")
                print("Parada da análise solicitada; a coleta SQL continua independente.")
            elif args.command == "exportar-evidencias":
                path = export_bundle(folder, ROOT / "reports" / "evidencias")
                print("Pacote de evidências local: " + str(path))
            elif args.command == "atualizar-referencias":
                from automatiza.referencias import update_references
                result = update_references(settings, folder, args.pessoas)
                print(f"Referências consultadas: {len(result['ids_consultados'])}; não localizadas: {len(result['ids_nao_localizados'])}. Nenhum dado alterado.")
            else:
                if not args.arquivo:
                    parser.error("registrar-caso exige --arquivo com um caso JSON")
                case = json.loads(Path(args.arquivo).read_text(encoding="utf-8-sig"))
                saved = save_case(base, case)
                print("Expectativa registrada (nenhuma ação no RH executada): " + saved["id"])
            print("Relatório: " + str(folder / "analise.html"))
        except (ValueError, FileNotFoundError, RuntimeError) as exc:
            print(str(exc))
            raise SystemExit(1) from None
        except Exception as exc:
            print(f"Falha na análise local ({type(exc).__name__}). Confira os arquivos da sessão.")
            raise SystemExit(1) from None
    elif args.command == "mapear-delphi":
        from automatiza.delphi_resources import flatten, map_resource
        if not args.arquivo or not args.classe or not args.saida:
            parser.error("mapear-delphi exige --arquivo, --classe e --saida (JSON)")
        result = map_resource(args.arquivo, args.classe, args.saida)
        print(f"Recurso mapeado sem abrir o sistema: {args.classe}; {len(list(flatten(result['arvore'])))} componentes.")
        print("Mapa salvo em: " + args.saida)
    elif args.command in {"observar", "observar-status", "parar-observacao", "anotar"}:
        from automatiza.observador import annotate, observer_status, run_observer, stop_observer
        base = ROOT / "reports" / "observacao"
        try:
            if args.command == "observar":
                state = run_observer(settings, base, duration=args.duracao, interval=args.intervalo,
                                     people=args.pessoas or ())
                print("Observação SQL encerrada: " + state["status"])
                if state["status"] in {"ERRO", "FINALIZADO_COM_ERROS"}:
                    raise SystemExit(1)
            elif args.command == "observar-status":
                folder, state = observer_status(base)
                print(json.dumps({key: state.get(key) for key in
                                  ("status", "processo_ativo", "pid", "inicio", "fim", "ultima_amostra", "linhas_atuais",
                                   "amostras_validas", "falhas_coleta", "totais")}, ensure_ascii=False, indent=2))
                print("Relatório: " + str(folder / "relatorio.html"))
            elif args.command == "parar-observacao":
                folder = stop_observer(base)
                print("Parada solicitada; o observador encerra após a consulta atual. " + str(folder))
            else:
                if not args.nota:
                    parser.error("anotar exige --nota")
                if args.dados and args.arquivo:
                    parser.error("Use --dados ou --arquivo para os dados da anotação, não ambos.")
                metadata = (json.loads(Path(args.arquivo).read_text(encoding="utf-8-sig")) if args.arquivo else
                            json.loads(args.dados) if args.dados else None)
                folder = annotate(base, args.nota, metadata=metadata)
                print("Anotação salva em: " + str(folder))
        except (FileNotFoundError, ValueError, RuntimeError) as exc:
            print(str(exc))
            raise SystemExit(1) from None
        except Exception as exc:
            print(f"Erro na observação SQL ({type(exc).__name__}). Confira a configuração e os arquivos locais.")
            raise SystemExit(1) from None
    elif args.command == "diagnostico":
        drivers = pyodbc.drivers()
        print(f"Python: {platform.python_version()} ({platform.architecture()[0]})")
        print(f"Configuração .env: {'encontrada' if (ROOT / '.env').exists() else 'pendente'}")
        print("Drivers ODBC: " + (", ".join(drivers) or "nenhum instalado"))
        status = "instalado" if settings.sql_driver in drivers else "instalação pendente"
        print(f"Driver configurado: {settings.sql_driver} ({status})")
        print(f"Aplicação: {'configurada' if settings.app_path else 'pendente'}")
        print(f"Banco: {'configurado' if settings.sql_server and settings.sql_database else 'pendente'}")
    elif args.command == "banco":
        value = SqlServer(settings).scalar("SELECT CAST(1 AS int) AS conexao_ok")
        print(f"Conexão SQL Server validada: {value}")
    elif args.command == "consulta":
        from automatiza.queries import read_query, run_query
        params = json.loads(args.parametros)
        if not isinstance(params, list):
            parser.error("--parametros precisa ser uma lista JSON.")
        sql = read_query(args.arquivo)
        if sql:
            run_query(SqlServer(settings), sql, tuple(params), args.saida)
    elif args.command == "acompanhar":
        from automatiza.importacao import load_case, monitor
        if not args.cenario or not args.caso:
            parser.error("acompanhar exige --cenario e --caso")
        case = load_case(args.cenario, args.caso)
        result = monitor(SqlServer(settings), case, ROOT / "reports" / "importacao")
        print(f"Resultado: {result['status']}. Relatório: {result['report']}")
        if result["status"] != "PASSOU":
            raise SystemExit(1)
    elif args.command in {"rh", "iniciar"}:
        if args.command == "iniciar":
            from automatiza.desktop import DesktopApp
            DesktopApp(settings).start()
            print("Módulo de Acesso disponível.")
        from automatiza.rh import RhApp
        rh = RhApp(settings).start()
        for warning in rh.warnings:
            print("Aviso: " + warning)
        print("RH autenticado; Módulo de Frequência disponível.")
    elif args.command == "abrir":
        from automatiza.desktop import DesktopApp
        app = DesktopApp(settings).start()
        print("Módulo conectado: " + app.window.window_text())
    else:
        from automatiza.desktop import DesktopApp
        app = DesktopApp(settings)
        app.start() if args.abrir else app.connect()
        directory = ROOT / "artifacts"
        directory.mkdir(exist_ok=True)
        path = directory / f"controles-{settings.app_backend}.txt"
        app.window.print_control_identifiers(filename=str(path))
        app.screenshot(directory / f"janela-{settings.app_backend}.png")
        print(f"Inspeção salva em: {path}")


if __name__ == "__main__":
    main()
