"""Abre a cópia, executa a suíte e retoma tentativas após falha da UI."""
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from automatiza.config import ROOT
from automatiza.perfis_teste import carregar
from automatiza.processos_auditorias import descobrir, validar_pid
from automatiza.seletores_auditorias import (BOTAO_LOGIN, CLASSE_AUDITORIA,
    CLASSE_JANELA_PRINCIPAL, CLASSE_LOGIN, CLASSE_PAINEL, MENU_AUDITORIAS,
    MENU_CONSULTAS, MENU_MODULOS, MODULOS, PAINEL)


def _esperar(func, timeout, descricao):
    from automatiza.pausa import esperar
    try:
        esperar(lambda: bool(func()), timeout)
    except Exception as exc:
        raise RuntimeError(f"Tempo esgotado aguardando {descricao} ({timeout}s).") from exc


def _janela(pid, classe):
    from pywinauto import Desktop
    windows = [w for w in Desktop(backend="win32").windows(process=pid)
               if classe in w.class_name() and w.is_visible()]
    return windows[0] if len(windows) == 1 else None


def _menu(parent, top, prefix):
    from pywinauto import Desktop
    from automatiza.pausa import ponto
    ponto({"acao": "abrir menu", "menu": prefix})
    parent.set_focus()
    menu = Desktop(backend="uia").window(handle=parent.handle)
    def matches():
        return [i for i in menu.descendants(control_type="MenuItem")
                if i.is_visible() and i.window_text().startswith(prefix)]
    items = matches()
    if not items:
        ponto({"acao": "abrir menu", "menu": top})
        menu.child_window(title=top, control_type="MenuItem", visible_only=True).click_input()
        items = matches()
    if len(items) != 1:
        raise RuntimeError(f"Menu {prefix!r}: encontrados {len(items)} itens; remapeie a tela.")
    ponto({"acao": "clicar menu", "menu": prefix})
    items[0].click_input()


def abrir(modulo, pasta, *, pid=None, timeout=45, evidencias=None):
    """Reutiliza módulo correto ou abre pelo painel da mesma instalação."""
    from pywinauto import Desktop
    from automatiza.pausa import ponto
    ponto({"modulo": modulo, "acao": "abrir modulo"})
    exe = pasta / MODULOS[modulo][0]
    if not exe.is_file():
        raise ValueError(f"Executável ausente: {exe}")
    if pid is not None:
        validar_pid(pid, exe)
    else:
        pid = descobrir(exe)
    if pid is None:
        panel_exe = pasta / PAINEL
        if not panel_exe.is_file():
            raise ValueError(f"Painel ausente: {panel_exe}")
        panel_pid = descobrir(panel_exe)
        if panel_pid is None:
            subprocess.Popen([str(panel_exe)], cwd=pasta)
            _esperar(lambda: descobrir(panel_exe) is not None, timeout, "processo do painel")
            panel_pid = descobrir(panel_exe)
        panel = _janela(panel_pid, CLASSE_PAINEL)
        if panel is None:
            login = _janela(panel_pid, CLASSE_LOGIN)
            _esperar(lambda: _janela(panel_pid, CLASSE_LOGIN) or _janela(panel_pid, CLASSE_PAINEL),
                     timeout, "login ou painel")
            login = _janela(panel_pid, CLASSE_LOGIN)
            if login:
                user = os.getenv("TESTE_USUARIO")
                password = os.getenv("TESTE_SENHA")
                if not user or not password:
                    raise ValueError("Login automático requer TESTE_USUARIO e TESTE_SENHA no .env.")
                edits = sorted([x for x in login.descendants() if x.class_name() == "TEdit" and x.is_visible()],
                               key=lambda x: x.rectangle().top)
                if len(edits) != 2:
                    raise RuntimeError(f"Login: encontrados {len(edits)} campos TEdit; remapeie.")
                ponto({"acao": "digitar usuario"})
                edits[0].set_edit_text(user)
                ponto({"acao": "digitar senha"})
                edits[1].set_edit_text(password)
                buttons = [x for x in login.descendants() if x.window_text() == BOTAO_LOGIN]
                if len(buttons) != 1:
                    raise RuntimeError("Botão Login não identificado; remapeie.")
                ponto({"acao": "entrar"})
                buttons[0].click_input()
            _esperar(lambda: _janela(panel_pid, CLASSE_PAINEL), timeout, "painel autenticado")
            panel = _janela(panel_pid, CLASSE_PAINEL)
        _menu(panel, MENU_MODULOS, MODULOS[modulo][1])
        _esperar(lambda: descobrir(exe) is not None, timeout, f"módulo {modulo}")
        pid = descobrir(exe)
    # Um aviso modal deixado por uma tentativa anterior desabilita a janela MDI.
    # Registre a evidência antes de liberar apenas avisos com botão OK.
    from pywinauto import Desktop
    for dialog in Desktop(backend="win32").windows(process=pid):
        if dialog.class_name() != "#32770" or not dialog.is_visible():
            continue
        buttons = [item for item in dialog.descendants()
                   if item.class_name() == "Button" and item.window_text() == "OK"]
        if len(buttons) != 1:
            raise RuntimeError(f"Diálogo modal não reconhecido em {modulo}: {dialog.window_text()}")
        message = " | ".join(item.window_text() for item in dialog.descendants()
                             if item.class_name() == "Static" and item.window_text())
        if evidencias:
            image = Path(evidencias) / f"dialogo-inicial-{datetime.now():%Y%m%d-%H%M%S}.png"
            dialog.capture_as_image().save(image)
        print(f"{modulo}: aviso modal existente: {message or dialog.window_text()}", flush=True)
        ponto({"modulo": modulo, "acao": "fechar aviso modal"})
        buttons[0].click_input()
    _esperar(lambda: _janela(pid, CLASSE_JANELA_PRINCIPAL), timeout, "janela principal")
    main = _janela(pid, CLASSE_JANELA_PRINCIPAL)
    if not any(CLASSE_AUDITORIA in c.class_name() and c.is_visible() for c in main.descendants()):
        _menu(main, MENU_CONSULTAS, MENU_AUDITORIAS)
    _esperar(lambda: any(CLASSE_AUDITORIA in c.class_name() and c.is_visible()
                         for c in _janela(pid, CLASSE_JANELA_PRINCIPAL).descendants()),
             timeout, "Auditorias/Históricos")
    return pid


def _tail(path, start):
    if not path.is_file():
        return []
    with path.open(encoding="utf-8") as f:
        f.seek(start)
        return [json.loads(line) for line in f if line.strip()]


def _capturar(pid, output):
    from pywinauto import Desktop
    try:
        windows = Desktop(backend="win32").windows(process=pid)
        if windows:
            path = output / f"travamento-{datetime.now():%Y%m%d-%H%M%S}.png"
            windows[0].capture_as_image().save(path)
            return str(path)
    except Exception:
        pass
    return None


def _executar_monitorado(args, *, env, pid, timeout, diario):
    """Interrompe automação quando a janela morre, trava ou deixa de progredir."""
    from automatiza.processos_auditorias import caminho_processo
    from pywinauto import Desktop
    import pywintypes
    proc = subprocess.Popen(args, cwd=ROOT, env=env)
    ultimo = time.monotonic()
    tamanho = diario.stat().st_size if diario.exists() else 0
    try:
        while True:
            from automatiza.pausa import ler, pasta, gravar
            base = pasta()
            if base and ler(base / "controle.json").get("estado") == "PAUSADO":
                if time.time() - ler(base / "heartbeat.json").get("instante", 0) > 2:
                    import ctypes
                    handle = ctypes.windll.kernel32.OpenProcess(0x0800, False, proc.pid)
                    if handle:
                        ctypes.windll.ntdll.NtResumeProcess(handle)
                        ctypes.windll.kernel32.CloseHandle(handle)
                    gravar(base / "controle.json", {"estado": "RODANDO", "instante": time.time()})
                    print("AVISO: sentinela parou; automação retomada sem pausa.", flush=True)
                    continue
                ultimo = time.monotonic()
                try:
                    return proc.wait(timeout=0.1)
                except subprocess.TimeoutExpired:
                    continue
            try:
                return proc.wait(timeout=0.1)
            except subprocess.TimeoutExpired:
                pass
            try:
                caminho_processo(pid)
            except (OSError, PermissionError, pywintypes.error):
                raise RuntimeError("O processo do Acessus encerrou durante o teste.")
            windows = Desktop(backend="win32").windows(process=pid)
            if windows:
                import ctypes
                if ctypes.windll.user32.IsHungAppWindow(windows[0].handle):
                    raise RuntimeError("A janela do Acessus não está respondendo.")
            atual = diario.stat().st_size if diario.exists() else 0
            if atual > tamanho:
                tamanho, ultimo = atual, time.monotonic()
            if time.monotonic() - ultimo > timeout:
                raise RuntimeError(f"Sem novo passo no diário por {timeout}s.")
    finally:
        if proc.poll() is None:
            subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                           capture_output=True, timeout=15)


def _marcar_restante(module, module_output, reason, *, only_filter=None, skip="", status="ERRO_AUTOMACAO"):
    """Usa o mapa da tela para registrar os filtros que ficaram sem execução."""
    from automatiza.diario_auditorias import DiarioAuditorias
    from automatiza.caminhos import mapas
    maps = list(mapas().glob(f"*/{module}/*/resultado.json"))
    maps += sorted((ROOT / "resultados").glob(f"auditorias-runtime-*/{module}/resultado.json"))
    maps.sort(key=lambda p: p.stat().st_mtime)
    completed = set()
    file = module_output / "tentativas.jsonl"
    if file.exists():
        for line in file.read_text(encoding="utf-8").splitlines():
            try:
                item = json.loads(line)
                completed.add((item.get("historico"), item.get("filtro"),
                               item.get("subcampo"), item.get("tentativa")))
            except ValueError:
                continue
    remaining = []
    if maps:
        data = json.loads(maps[-1].read_text(encoding="utf-8"))
        skipped = {int(item) for item in skip.split(",") if item.strip().isdigit()}
        for index, history in enumerate(data.get("historicos", [])):
            if index in skipped:
                continue
            for filt in history.get("filtros", []):
                if only_filter and not filt.get("nome", "").startswith(only_filter):
                    continue
                name = "Período" if filt.get("nome", "").startswith("Per") else filt.get("nome")
                fields = 2 if "Coletor/Fun" in name else 1
                for subcampo in range(fields):
                    for tentativa in range(1, 6):
                        key = (history.get("historico"), name, subcampo, tentativa)
                        if key not in completed:
                            remaining.append(key)
    if not remaining:
        remaining = [("(módulo)", "(restante não mapeado)", 0, 0)]
    from automatiza.caminhos import logs_permanentes
    with DiarioAuditorias(logs_permanentes(), {"modulo": module,
                                                "motivo_interrupcao": reason,
                                                "pasta_evidencias": str(module_output)}) as diary:
        for history, filt, subcampo, tentativa in remaining:
            record = {"modulo": module, "historico": history, "filtro": filt,
                      "status": status, "erro": reason,
                      "subcampo": subcampo, "tentativa": tentativa, "nao_executado": True}
            diary.iniciar_tentativa(record)
            diary.acao(module, history, filt, f"Não executado: {reason}")
            diary.finalizar_tentativa(record)
            with file.open("a", encoding="utf-8") as out:
                out.write(json.dumps(record, ensure_ascii=False) + "\n")


def executar(ns):
    from dotenv import load_dotenv
    from automatiza.relatorio_auditorias import gerar
    load_dotenv(ROOT / ".env", override=False)
    profile = carregar(ns.perfil)
    folder = Path(profile["pasta_executaveis"])
    from automatiza.caminhos import rodadas, nova_rodada, logs_permanentes
    output = Path(ns.saida) if ns.saida else Path(os.environ.get("AUTOMATIZA_RODADA_DIR") or nova_rodada("auditorias", ns.modulo))
    output.mkdir(parents=True, exist_ok=True)
    os.environ["AUTOMATIZA_RESULTADO_DIR"] = str(output)
    modules = list(MODULOS) if ns.modulo == "todos" else [ns.modulo]
    (output / "opcoes.json").write_text(json.dumps({
        "perfil": ns.perfil, "modulos": modules, "extremo": ns.extremo,
        "filtro": ns.filtro, "pular": ns.pular, "timeout": ns.timeout,
        "reinicios": ns.reinicios}, ensure_ascii=False, indent=2), encoding="utf-8")
    had_error = False
    cancelada = False
    for module in modules:
        from automatiza.pausa import TesteCancelado, ler, pasta, ponto
        base = pasta()
        if base and ler(base / "controle.json").get("estado") == "CANCELANDO":
            cancelada = True
            module_output = output / module
            module_output.mkdir(exist_ok=True)
            _marcar_restante(module, module_output, "Cancelado pelo usuário",
                            only_filter=ns.filtro, skip=ns.pular, status="CANCELADO")
            continue
        module_output = output / module
        module_output.mkdir(exist_ok=True)
        pid = ns.pid if ns.modulo != "todos" else None
        for restart in range(ns.reinicios + 1):
            try:
                ponto({"modulo": module, "acao": "iniciar ou retomar"})
                pid = abrir(module, folder, pid=pid, timeout=ns.timeout,
                            evidencias=module_output)
                print(f"{module}: PID {pid}, levantamento da tela", flush=True)
                survey = subprocess.run([sys.executable, str(ROOT / "scripts/levantar_auditorias_runtime.py"),
                                         str(pid), module], cwd=ROOT, timeout=ns.timeout * 5)
                if survey.returncode == 2:
                    cancelada = True
                    _marcar_restante(module, module_output, "Cancelado pelo usuário",
                                    only_filter=ns.filtro, skip=ns.pular, status="CANCELADO")
                    break
                if survey.returncode:
                    raise RuntimeError(f"Levantamento falhou com código {survey.returncode}.")
                path = module_output / "tentativas.jsonl"
                start = path.stat().st_size if path.exists() else 0
                env = os.environ.copy()
                env["AUTOMATIZA_PERFIL"] = ns.perfil
                env["AUDITORIA_EXTREME"] = "1" if ns.extremo else "0"
                env["AUDITORIA_STOP_ON_AV"] = "1"
                env["AUDITORIA_RESUME"] = "1"
                if ns.filtro:
                    env["AUDITORIA_ONLY_FILTER"] = ns.filtro
                else:
                    env.pop("AUDITORIA_ONLY_FILTER", None)
                args = [sys.executable, str(ROOT / "scripts/testar_auditorias_cronologico.py"),
                        str(pid), module, str(module_output)]
                args += [x.strip() for x in ns.pular.split(",") if x.strip()]
                result_code = _executar_monitorado(
                    args, env=env, pid=pid, timeout=ns.timeout,
                    diario=logs_permanentes() / "passo-a-passo-detalhado.jsonl")
                if result_code == 2 or (base and ler(base / "controle.json").get("estado") == "CANCELANDO"):
                    cancelada = True
                    _marcar_restante(module, module_output, "Cancelado pelo usuário",
                                    only_filter=ns.filtro, skip=ns.pular, status="CANCELADO")
                    break
                recent = _tail(path, start)
                av = any("Access violation" in str(x.get("mensagens_consulta", "")) for x in recent)
                if result_code == 0 and not av:
                    print(f"{module}: concluído ({len(recent)} novas tentativas)", flush=True)
                    break
                if result_code != 75 and not av:
                    raise RuntimeError(f"Suíte encerrada com código {result_code}.")
                print(f"{module}: Access violation; retomada após reinício {restart + 1}", flush=True)
                _capturar(pid, module_output)
                subprocess.run(["taskkill", "/PID", str(pid), "/F", "/T"], capture_output=True, timeout=10)
                pid = None
            except TesteCancelado:
                cancelada = True
                _marcar_restante(module, module_output, "Cancelado pelo usuário",
                                only_filter=ns.filtro, skip=ns.pular, status="CANCELADO")
                break
            except (RuntimeError, ValueError, subprocess.TimeoutExpired, OSError) as exc:
                print(f"{module}: {type(exc).__name__}: {exc}", flush=True)
                if pid:
                    _capturar(pid, module_output)
                    try:
                        validar_pid(pid, folder / MODULOS[module][0])
                        subprocess.run(["taskkill", "/PID", str(pid), "/F", "/T"],
                                       capture_output=True, timeout=10)
                    except (ValueError, OSError, subprocess.TimeoutExpired):
                        pass
                pid = None
                if restart == ns.reinicios:
                    had_error = True
                    (module_output / "supervisor-erro.txt").write_text(str(exc), encoding="utf-8")
                    _marcar_restante(module, module_output, str(exc),
                                    only_filter=ns.filtro, skip=ns.pular)
                else:
                    continue
            if restart == ns.reinicios:
                had_error = True
                if not (module_output / "supervisor-erro.txt").exists():
                    _marcar_restante(module, module_output,
                                    f"Limite de {ns.reinicios} reinícios após erro da aplicação",
                                    only_filter=ns.filtro, skip=ns.pular)
                print(f"{module}: limite de {ns.reinicios} reinícios; restante ERRO_AUTOMACAO", flush=True)
    report = gerar(output)
    print(f"Relatório: {report}", flush=True)
    return 2 if cancelada else (1 if had_error else 0)
