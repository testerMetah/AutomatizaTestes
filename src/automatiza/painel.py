"""Painel HTTP local; executa a CLI na sessão interativa do usuário."""
import html
import json
import os
import secrets
import shutil
import socket
import subprocess
import sys
import threading
import time
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from automatiza.catalogo_comandos import COMANDOS, POWERSHELL
from automatiza.config import ROOT
from automatiza.perfis_teste import carregar, configuracao, validar_escrita

STATIC = Path(__file__).with_name("painel.html")
ROOTS = (ROOT / "resultados", ROOT / "reports")
UI_COMMANDS = {"auditorias", "robot", "sequencias", "ciclos", "testes-unitarios"}


class Estado:
    def __init__(self):
        self.lock = threading.RLock()
        self.token = secrets.token_urlsafe(24)
        self.process = None
        self.job = None
        self.lines = []
        self.next_id = 1

    def start(self, args, *, ui=False):
        with self.lock:
            if self.process and self.process.poll() is None:
                raise ValueError("Já existe uma execução em andamento; aguarde ou use PARAR.")
            env = os.environ.copy()
            env["PYTHONUNBUFFERED"] = "1"
            cmd = [sys.executable, "-u", "-m", "automatiza.nova_cli", *args]
            self.process = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                                            errors="replace", bufsize=1,
                                            creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0))
            self.lines = []
            self.job = {"id": self.next_id, "comando": "automatiza " + " ".join(args),
                        "inicio": datetime.now().isoformat(), "ui": ui, "estado": "rodando"}
            self.next_id += 1
            thread = threading.Thread(target=self._collect, args=(self.process,), daemon=True)
            thread.start()
            return dict(self.job)

    def _collect(self, proc):
        try:
            for line in proc.stdout:
                with self.lock:
                    self.lines.append(line.rstrip("\r\n"))
                    if len(self.lines) > 10000:
                        self.lines = self.lines[-10000:]
            code = proc.wait()
        except Exception as exc:
            code = 1
            with self.lock:
                self.lines.append(f"Falha ao ler a execução: {type(exc).__name__}")
        with self.lock:
            if self.process is proc and self.job:
                self.job["estado"] = "concluído" if code == 0 else "falhou"
                self.job["codigo"] = code
                self.job["fim"] = datetime.now().isoformat()

    def stop(self):
        with self.lock:
            proc = self.process
            if not proc or proc.poll() is not None:
                raise ValueError("Nenhuma execução em andamento.")
            subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                           capture_output=True, timeout=15)
            self.job["estado"] = "interrompido"
            return dict(self.job)

    def snapshot(self, from_line=0):
        with self.lock:
            return {"job": dict(self.job) if self.job else None,
                    "linhas": self.lines[max(0, from_line):], "total": len(self.lines)}


def _arquivo_seguro(name):
    path = (ROOT / name).resolve()
    if not any(path == root.resolve() or root.resolve() in path.parents for root in ROOTS):
        raise ValueError("Arquivo fora das pastas de evidência.")
    if not path.is_file():
        raise ValueError("Arquivo não encontrado.")
    return path


def _rodadas():
    rows = []
    for root in ROOTS:
        if not root.exists():
            continue
        for folder in root.iterdir():
            if not folder.is_dir():
                continue
            summary = folder / "resumo.json"
            report = folder / "RELATORIO.html"
            data = {}
            if summary.is_file():
                try:
                    data = json.loads(summary.read_text(encoding="utf-8"))
                except (ValueError, OSError):
                    pass
            if report.exists() or summary.exists() or list(folder.glob("**/tentativas.jsonl")):
                rows.append({"pasta": str(folder.relative_to(ROOT)), "data": datetime.fromtimestamp(
                    folder.stat().st_mtime).isoformat(timespec="seconds"), "resumo": data.get("modulos", {}),
                    "relatorio": str(report.relative_to(ROOT)) if report.exists() else None})
    return sorted(rows, key=lambda x: x["data"], reverse=True)[:100]


def _comando(data):
    kind = data.get("tipo")
    if kind == "auditorias":
        module = data.get("modulo")
        if module not in {"acesso", "refeitorio", "portaria", "estacionamento", "escola", "administracao", "todos"}:
            raise ValueError("Módulo inválido.")
        profile = data.get("perfil") or "auditorias"
        carregar(profile)
        args = ["auditorias", "--modulo", module, "--perfil", profile]
        if data.get("extremo"):
            args.append("--extremo")
        for name in ("filtro", "pular"):
            if data.get(name):
                args += ["--" + name, str(data[name])]
        return args
    if kind == "ambiente":
        return ["ambiente", "--perfil", data.get("perfil") or "auditorias"]
    if kind == "robot":
        return ["robot", "--tag", data.get("tag") or "smoke"]
    if kind == "sequencias":
        args = ["sequencias"]
        if data.get("arquivo"):
            path = (ROOT / str(data["arquivo"])).resolve()
            if ROOT not in path.parents or not path.is_file() or path.suffix != ".yaml":
                raise ValueError("Arquivo YAML deve existir dentro do projeto.")
            args += ["--arquivo", str(path.relative_to(ROOT))]
        elif data.get("seed") not in (None, ""):
            args += ["--seed", str(int(data["seed"])), "--passos", str(int(data.get("passos") or 8)),
                     "--massa", str(int(data.get("massa") or 5))]
        else:
            raise ValueError("Escolha YAML ou semente.")
        return args
    if kind == "observar":
        action = data.get("acao")
        if action not in {"iniciar", "anotar", "status", "parar"}:
            raise ValueError("Ação de observação inválida.")
        args = ["observar", action]
        if action == "iniciar":
            args += ["--duracao", str(float(data.get("duracao") or 7200)),
                     "--intervalo", str(float(data.get("intervalo") or 15))]
        if action == "anotar":
            args += ["--nota", str(data.get("nota") or "")]
        return args
    if kind == "conferir":
        action = data.get("acao")
        if action not in {"consultar", "comparar"}:
            raise ValueError("Ação de comparação inválida.")
        args = ["conferir", action]
        for name in ("filtros", "antes", "depois", "saida"):
            if data.get(name):
                args += ["--" + name, str(data[name])]
        return args
    if kind == "ciclos":
        action = data.get("acao")
        if action not in {"planejar", "executar", "suite"}:
            raise ValueError("Ação de ciclo inválida.")
        args = ["ciclos", action, "--arquivo", str(data.get("arquivo") or ""),
                "--saida", str(data.get("saida") or ""), "--perfil", str(data.get("perfil") or "sequencias")]
        if action in {"executar", "suite"}:
            if data.get("confirmacao") != "Entendo que isto altera dados":
                raise ValueError("Confirmação de escrita ausente.")
            actual = validar_escrita(configuracao(data.get("perfil") or "sequencias"))
            if data.get("banco_confirmado", "").casefold() != actual.casefold():
                raise ValueError(f"Confirme o banco efetivo {actual} antes de executar.")
            args.append("--confirmo-escrita")
        return args
    if kind == "comparar-rodadas":
        return ["comparar-rodadas", str(data.get("anterior") or ""), str(data.get("atual") or "")]
    if kind == "testes-unitarios":
        return ["testes-unitarios"]
    raise ValueError("Comando desconhecido.")


def criar_servidor(porta=8765):
    state = Estado()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            return

        def _json(self, data, status=200):
            body = json.dumps(data, ensure_ascii=False, default=str).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def _body(self):
            length = int(self.headers.get("Content-Length", "0"))
            if length > 1_000_000:
                raise ValueError("Pedido grande demais.")
            return json.loads(self.rfile.read(length) or b"{}")

        def _check(self):
            if self.client_address[0] not in {"127.0.0.1", "::1"}:
                raise ValueError("Acesso permitido apenas neste computador.")
            if self.headers.get("X-Painel-Token") != state.token:
                raise ValueError("Token do painel inválido.")
            origin = self.headers.get("Origin")
            if origin and origin != f"http://127.0.0.1:{self.server.server_port}":
                raise ValueError("Origem inválida.")

        def do_GET(self):
            try:
                url = urlparse(self.path)
                if self.client_address[0] not in {"127.0.0.1", "::1"}:
                    raise ValueError("Acesso permitido apenas neste computador.")
                if url.path in {"/", "/index.html"}:
                    page = STATIC.read_text(encoding="utf-8").replace("__TOKEN__", state.token)
                    body = page.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(body)
                    return
                if not url.path.startswith("/evidencia/"):
                    self._check()
                qs = parse_qs(url.query)
                if url.path.startswith("/evidencia/"):
                    path = _arquivo_seguro(url.path[len("/evidencia/"):])
                    mime = {".html": "text/html", ".png": "image/png"}.get(path.suffix.lower())
                    if not mime:
                        raise ValueError("Tipo de evidência não permitido.")
                    body = path.read_bytes()
                    self.send_response(200)
                    self.send_header("Content-Type", mime + ("; charset=utf-8" if mime == "text/html" else ""))
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; img-src 'self'; frame-ancestors 'none'")
                    self.end_headers()
                    self.wfile.write(body)
                    return
                if url.path == "/api/ambiente":
                    from automatiza.diagnostico_unificado import executar
                    return self._json(executar())
                if url.path == "/api/config":
                    return self._json({"perfis": [carregar(n) for n in ("auditorias", "sequencias")],
                                       "env": {key: ("••••" if key in {"TESTE_SENHA", "SQL_PASSWORD", "RH_PASSWORD"}
                                                     and os.getenv(key) else os.getenv(key, ""))
                                               for key in ("TESTE_USUARIO", "TESTE_SENHA", "SQL_SERVER",
                                                           "SQL_DATABASE", "SQL_USER", "SQL_PASSWORD",
                                                           "RH_USER", "RH_PASSWORD")}})
                if url.path == "/api/catalogo":
                    return self._json(COMANDOS + POWERSHELL)
                if url.path == "/api/job":
                    return self._json(state.snapshot(int(qs.get("de", ["0"])[0])))
                if url.path == "/api/resultados":
                    return self._json(_rodadas())
                if url.path == "/api/perfis":
                    return self._json([{"nome": n, "banco": carregar(n)["banco"],
                                        "pasta_executaveis": carregar(n)["pasta_executaveis"]}
                                       for n in ("auditorias", "sequencias")])
                if url.path == "/api/banco":
                    from automatiza.database import SqlServer
                    settings = configuracao(qs.get("perfil", ["sequencias"])[0])
                    actual = SqlServer(settings).assert_database()
                    return self._json({"servidor": settings.sql_server, "banco": actual})
                if url.path == "/api/arquivos":
                    base = qs.get("pasta", [""])[0]
                    folder = (ROOT / base).resolve()
                    if not any(folder == x.resolve() or x.resolve() in folder.parents for x in ROOTS):
                        raise ValueError("Pasta fora das evidências.")
                    return self._json([str(p.relative_to(ROOT)) for p in folder.glob("**/*")
                                       if p.is_file() and p.suffix.lower() in {".png", ".html", ".jsonl", ".log"}][:500])
                if url.path == "/api/log":
                    name = qs.get("arquivo", [""])[0]
                    path = _arquivo_seguro(name)
                    if path.suffix not in {".log", ".jsonl", ".txt"}:
                        raise ValueError("Este arquivo não é um log.")
                    filtro = qs.get("estado", [""])[0]
                    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[-2000:]
                    if filtro:
                        lines = [x for x in lines if filtro.casefold() in x.casefold()]
                    return self._json({"linhas": lines})
                if url.path == "/api/arquivo":
                    path = _arquivo_seguro(qs.get("nome", [""])[0])
                    mime = {".html": "text/html", ".png": "image/png", ".json": "application/json",
                            ".jsonl": "text/plain", ".log": "text/plain"}.get(path.suffix.lower())
                    if not mime:
                        raise ValueError("Tipo de arquivo não permitido.")
                    body = path.read_bytes()
                    self.send_response(200)
                    self.send_header("Content-Type", mime + ("; charset=utf-8" if mime.startswith("text") else ""))
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; img-src 'self'")
                    self.end_headers()
                    self.wfile.write(body)
                    return
                if url.path == "/api/build":
                    return self._json(_build_info())
                self._json({"erro": "Rota não encontrada."}, 404)
            except Exception as exc:
                self._json({"erro": str(exc)}, 400)

        def do_POST(self):
            try:
                self._check()
                url = urlparse(self.path)
                data = self._body()
                if url.path == "/api/iniciar":
                    args = _comando(data)
                    return self._json(state.start(args, ui=args[0] in UI_COMMANDS))
                if url.path == "/api/parar":
                    return self._json(state.stop())
                if url.path == "/api/perfil":
                    name = data.get("nome")
                    profile = carregar(name)
                    for key in ("pasta_executaveis", "servidor", "banco"):
                        if key in data:
                            profile[key] = str(data[key]).strip()
                    if not all(profile.get(k) for k in ("pasta_executaveis", "servidor", "banco")):
                        raise ValueError("Caminho, servidor e banco são obrigatórios.")
                    if profile["banco"].casefold() != carregar(name)["banco"].casefold():
                        profile["confirmado_como_teste"] = False
                    target = ROOT / "profiles" / (name + ".json")
                    target.write_text(json.dumps(profile, ensure_ascii=False, indent=2), encoding="utf-8")
                    return self._json({"perfil": name, "banco": profile["banco"],
                                       "confirmado_como_teste": profile["confirmado_como_teste"]})
                if url.path == "/api/build":
                    if data.get("confirmacao") != "COPIAR BUILD":
                        raise ValueError("Confirme a substituição digitando COPIAR BUILD.")
                    return self._json(_copiar_build())
                self._json({"erro": "Rota não encontrada."}, 404)
            except Exception as exc:
                self._json({"erro": str(exc)}, 400)

    server = ThreadingHTTPServer(("127.0.0.1", porta), Handler)
    server.daemon_threads = True
    return server


def _versao(path):
    if not path.is_file():
        return "ausente"
    try:
        import win32api
        raw = win32api.GetFileVersionInfo(str(path), "\\")
        return ".".join(map(str, (raw["FileVersionMS"] >> 16, raw["FileVersionMS"] & 0xffff,
                                  raw["FileVersionLS"] >> 16, raw["FileVersionLS"] & 0xffff)))
    except Exception:
        return "não legível"


def _build_info():
    src = Path(r"\\VBOXSVR\OrigemAcessus")
    dst = Path(carregar("auditorias")["pasta_executaveis"])
    return {"origem": str(src), "destino": str(dst),
            "versao_origem": _versao(src / "Acessus.exe"),
            "versao_destino": _versao(dst / "Acessus.exe"),
            "product_key_origem": (src / "product.key").exists(),
            "product_key_destino": (dst / "product.key").exists(),
            "inis_destino": {name: (dst / name).exists() for name in
                            ("ConexaoConfig.ini", "AccessusComConfig.ini")}}


def _copiar_build():
    from automatiza.processos_auditorias import descobrir
    from automatiza.seletores_auditorias import MODULOS, PAINEL
    src = Path(r"\\VBOXSVR\OrigemAcessus")
    dst = Path(carregar("auditorias")["pasta_executaveis"])
    if not src.is_dir() or not (src / "Acessus.exe").is_file() or not (src / "product.key").is_file():
        raise ValueError("Origem incompleta: faltam Acessus.exe ou product.key.")
    for name in [PAINEL, *(x[0] for x in MODULOS.values())]:
        if dst.exists() and descobrir(dst / name):
            raise ValueError(f"Feche {name} antes de substituir a build.")
    if dst.exists():
        backup = dst.with_name(dst.name + "_backup_" + datetime.now().strftime("%Y%m%d-%H%M%S"))
        shutil.copytree(dst, backup)
    else:
        backup = None
    shutil.copytree(src, dst, dirs_exist_ok=True)
    for required in ("Acessus.exe", "Acessus.Modulo.exe", "product.key", "ConexaoConfig.ini"):
        if not (dst / required).is_file():
            raise RuntimeError(f"Cópia incompleta: {required}. Backup: {backup}")
    return {"backup": str(backup) if backup else None, "resultado": _build_info()}


def iniciar():
    from automatiza.nova_cli import require_32
    require_32()
    port = int(os.getenv("PAINEL_PORTA", "8765"))
    for candidate in range(port, port + 20):
        try:
            server = criar_servidor(candidate)
            break
        except OSError:
            continue
    else:
        raise RuntimeError("Nenhuma porta local disponível.")
    url = f"http://127.0.0.1:{server.server_port}/"
    print(f"Painel: {url}\nFeche esta janela para encerrar.", flush=True)
    webbrowser.open(url)
    try:
        server.serve_forever()
    finally:
        server.server_close()
