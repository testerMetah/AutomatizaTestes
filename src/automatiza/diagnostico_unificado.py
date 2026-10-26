"""Pré-checagem somente leitura, consumida pela CLI e pelo painel."""
import json
import struct
import subprocess
from pathlib import Path

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer
from automatiza.perfis_teste import carregar, configuracao


def _item(items, nome, estado, detalhe):
    items.append({"item": nome, "estado": estado, "detalhe": str(detalhe)})


def executar(nome_perfil="auditorias"):
    items = []
    bits = struct.calcsize("P") * 8
    _item(items, "Python", "OK" if bits == 32 else "ERRO", f"{bits} bits; obrigatório 32")
    try:
        import pyodbc
        drivers = pyodbc.drivers()
        wanted = Settings.load().sql_driver
        _item(items, "Driver ODBC", "OK" if wanted in drivers else "ERRO",
              f"{wanted}: {'instalado' if wanted in drivers else 'ausente'}")
    except Exception as exc:
        _item(items, "Driver ODBC", "ERRO", f"{type(exc).__name__}: {exc}")
    names = ["auditorias", "sequencias"]
    if nome_perfil not in names:
        names.append(nome_perfil)
    for name in names:
        try:
            profile = carregar(name)
            folder = Path(profile["pasta_executaveis"])
            exe = folder / "Acessus.exe"
            if not exe.exists():
                exe = folder / "Acessus.Modulo.exe"
            if exe.exists():
                try:
                    import win32api
                    raw = win32api.GetFileVersionInfo(str(exe), "\\")
                    version = ".".join(str(n) for n in
                                       (raw["FileVersionMS"] >> 16, raw["FileVersionMS"] & 0xffff,
                                        raw["FileVersionLS"] >> 16, raw["FileVersionLS"] & 0xffff))
                except Exception:
                    version = "versão não legível"
                _item(items, f"{name}: executável", "OK", f"{exe} ({version})")
            else:
                _item(items, f"{name}: executável", "ERRO", f"Ausente em {folder}")
            for filename in ("ConexaoConfig.ini", "AccessusComConfig.ini"):
                ini = folder / filename
                if not ini.is_file():
                    _item(items, f"{name}: {filename}", "ALERTA", "Arquivo ausente")
                    continue
                content = ini.read_text(encoding="cp1252", errors="replace")
                values = {}
                for line in content.splitlines():
                    if "=" in line:
                        key, value = line.split("=", 1)
                        if key.strip().casefold() in {"server", "database"}:
                            values[key.strip().casefold()] = value.strip()
                db = values.get("database", "?")
                server = values.get("server", "?")
                state = ("OK" if db.casefold() == profile["banco"].casefold()
                         and server.casefold() == profile["servidor"].casefold() else "ALERTA")
                _item(items, f"{name}: {filename}", state, f"Server={server}; Database={db}")
            try:
                settings = configuracao(name)
                actual = SqlServer(settings).assert_database()
                one = SqlServer(settings).scalar("SELECT 1")
                _item(items, f"{name}: SQL", "OK" if one == 1 else "ERRO",
                      f"{settings.sql_server}/{actual}; SELECT 1={one}")
            except Exception as exc:
                _item(items, f"{name}: SQL", "ERRO", f"{type(exc).__name__}: {exc}")
        except Exception as exc:
            _item(items, f"perfil {name}", "ERRO", f"{type(exc).__name__}: {exc}")
    config = json.loads((ROOT / "config/ambiente-teste.json").read_text(encoding="utf-8"))
    for key in ("sql_origem",):
        data = config[key]
        try:
            from dataclasses import replace
            settings = replace(Settings.load(), sql_server=data["servidor"], sql_database=data["banco"])
            actual = SqlServer(settings).assert_database()
            _item(items, f"{key}: SQL", "OK", f"{settings.sql_server}/{actual}; SELECT 1={SqlServer(settings).scalar('SELECT 1')}")
        except Exception as exc:
            _item(items, f"{key}: SQL", "ERRO", f"{type(exc).__name__}: {exc}")
    for name, service in config.get("servicos", {}).items():
        try:
            result = subprocess.run(["sc.exe", "query", service["nome_windows"]],
                                    capture_output=True, text=True, timeout=10)
            status = "RUNNING" if "RUNNING" in result.stdout else (
                "STOPPED" if "STOPPED" in result.stdout else "não identificado")
            _item(items, f"serviço {name}", "OK" if status == "RUNNING" else "ALERTA", status)
        except Exception as exc:
            _item(items, f"serviço {name}", "ALERTA", f"{type(exc).__name__}: {exc}")
    return items
