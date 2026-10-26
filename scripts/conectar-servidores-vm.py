"""Configura somente a VM e valida conexoes remotas com consultas de leitura."""
from __future__ import annotations

import argparse
from contextlib import closing
from dataclasses import replace
from datetime import datetime
import json
import os
from pathlib import Path
import platform
import re
import shutil
import socket
import subprocess
import sys

from dotenv import dotenv_values, set_key
import pyodbc

from automatiza.config import Settings


SQL_TARGETS = (
    ("Acessus", "tcp:desk-tec,1433", "bras1"),
    ("RH Fagundes", "tcp:desk-tec,1433", "RHFagundes"),
    ("RH Braslux", "tcp:desk-tec,1435", "RHBraslux"),
)

# Enderecos verificados pela maquina principal em 16/10/2026.
REMOTE_HOSTS = {
    "desk-tec": {"ip": "192.168.50.61", "ports": (1433, 1435)},
    "dexter": {"ip": "192.168.50.220", "ports": (1521,)},
}


def tcp_check(host: str, port: int) -> dict:
    try:
        with socket.create_connection((host, port), timeout=3):
            return {"acessivel": True}
    except OSError as error:
        return {"acessivel": False, "tipo": type(error).__name__, "codigo": error.errno}


def repair_resolution(updates: dict[str, str], backup: Path) -> None:
    if platform.node().split(".")[0].casefold() != "testesvm":
        raise RuntimeError("A resolucao de nomes so pode ser ajustada na VM.")
    hosts = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32/drivers/etc/hosts"
    raw = hosts.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
        encoding = "utf-8-sig" if raw.startswith(b"\xef\xbb\xbf") else "utf-8"
    except UnicodeDecodeError:
        text, encoding = raw.decode("cp1252"), "cp1252"
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(hosts, backup)
    # Modifique somente os aliases confirmados, preservando os demais aliases e comentarios.
    lines = []
    for line in text.splitlines():
        address_part, separator, comment = line.partition("#")
        fields = address_part.split()
        if len(fields) > 1 and any(alias.casefold() in updates for alias in fields[1:]):
            others = [alias for alias in fields[1:] if alias.casefold() not in updates]
            if others:
                lines.append(fields[0] + "\t" + " ".join(others) + ((" #" + comment) if separator else ""))
            elif separator:
                lines.append("#" + comment)
        else:
            lines.append(line)
    lines += [f"{ip}\t{host}\t# AutomatizaTestes: servidor verificado" for host, ip in updates.items()]
    hosts.write_bytes(("\r\n".join(lines).rstrip("\r\n") + "\r\n").encode(encoding))
    subprocess.run([str(Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32/ipconfig.exe"), "/flushdns"], capture_output=True, check=True)


def check_network(report_path: Path) -> dict:
    result = {}
    updates = {}
    for host, expected in REMOTE_HOSTS.items():
        print(f"Verificando rede: {host} ({expected['ip']})...", flush=True)
        item = {"ip_confirmado_na_origem": expected["ip"], "portas": {}}
        try:
            item["dns"] = sorted({entry[4][0] for entry in socket.getaddrinfo(host, None, socket.AF_INET)})
        except OSError as error:
            item.update(dns=[], erro_dns=type(error).__name__, codigo_dns=error.errno)
        for port in expected["ports"]:
            item["portas"][str(port)] = {"por_nome": tcp_check(host, port), "por_ip": tcp_check(expected["ip"], port)}
        reachable_by_ip = any(value["por_ip"]["acessivel"] for value in item["portas"].values())
        if expected["ip"] not in item["dns"] and reachable_by_ip:
            updates[host] = expected["ip"]
        result[host] = item
    if updates:
        repair_resolution(updates, report_path.parent / "config-backups" / (report_path.stem + ".hosts.backup"))
        print("Resolucao ajustada SOMENTE na VM: " + ", ".join(sorted(updates)), flush=True)
    for host, item in result.items():
        item["resolucao_ajustada"] = host in updates
        item["portas_apos_ajuste"] = {str(port): tcp_check(host, port) for port in REMOTE_HOSTS[host]["ports"]}
    return result


def configure_vm(source: Path, project: Path, backup: Path) -> Settings:
    if platform.node().split(".")[0].casefold() != "testesvm":
        raise RuntimeError("Execute somente dentro da VM TESTESVM.")
    if project.resolve() != Path(r"C:\AutomatizaTestes").resolve():
        raise RuntimeError("Destino inesperado para a configuracao da VM.")
    values = dotenv_values(source, interpolate=False)
    if not source.is_file():
        raise RuntimeError("Configuracao de origem indisponivel na pasta compartilhada.")
    auth = values.get("SQL_AUTH") or "windows"
    if auth == "sql" and not (values.get("SQL_USER") and values.get("SQL_PASSWORD")):
        raise RuntimeError("A configuracao de origem nao contem credenciais SQL completas.")
    settings = Settings(
        sql_server="tcp:desk-tec,1433", sql_database="bras1",
        sql_driver="ODBC Driver 17 for SQL Server", sql_auth=auth,
        sql_user=values.get("SQL_USER") or "",
        sql_password=values.get("SQL_PASSWORD") or "",
        sql_encrypt=values.get("SQL_ENCRYPT") or "yes",
        sql_trust_certificate=values.get("SQL_TRUST_CERTIFICATE") or "no",
        sql_timeout=10,
    )
    # Valide a estrutura antes de salvar, sem abrir conexao.
    settings.connection_string()
    destination = project / ".env"
    if source.resolve() == destination.resolve():
        raise RuntimeError("Origem e destino da configuracao nao podem ser o mesmo arquivo.")
    if destination.exists():
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(destination, backup)
    else:
        shutil.copy2(project / ".env.example", destination)
    updates = {
        "APP_PATH": r"C:\acesso\Acessus.exe",
        "APP_WORK_DIR": r"C:\acesso",
        "RH_PATH": r"C:\meta\rhsis\rh.exe",
        "RH_WORK_DIR": r"C:\meta\rhsis",
        "SQL_SERVER": settings.sql_server,
        "SQL_DATABASE": settings.sql_database,
        "SQL_DRIVER": settings.sql_driver,
        "SQL_AUTH": settings.sql_auth,
        "SQL_USER": settings.sql_user,
        "SQL_PASSWORD": settings.sql_password,
        "SQL_ENCRYPT": settings.sql_encrypt,
        "SQL_TRUST_CERTIFICATE": settings.sql_trust_certificate,
        "SQL_TIMEOUT": str(settings.sql_timeout),
    }
    for key, value in updates.items():
        set_key(destination, key, value, quote_mode="always", encoding="utf-8")
    return settings


def check_sql(settings: Settings, label: str, server: str, database: str) -> dict:
    print(f"Validando {label}: {server} / {database}...", flush=True)
    target = replace(settings, sql_server=server, sql_database=database)
    result = {"ambiente": label, "servidor": server, "base": database}
    try:
        with closing(pyodbc.connect(target.connection_string(), timeout=10)) as connection:
            connection.timeout = 10
            cursor = connection.cursor()
            cursor.execute("SELECT DB_NAME(), CAST(SERVERPROPERTY('ServerName') AS nvarchar(128))")
            actual_database, actual_server = cursor.fetchone()
            if actual_database.casefold() != database.casefold():
                raise RuntimeError("A conexao retornou uma base diferente da esperada.")
            result.update(estado="conectado", base_confirmada=actual_database, instancia_confirmada=actual_server)
        print(f"OK: {label}; banco confirmado: {actual_database}.", flush=True)
    except Exception as error:
        # Nao grave connection strings, usuario nem senha nos relatórios.
        result.update(estado="falha", tipo=type(error).__name__)
        if isinstance(error, pyodbc.Error) and error.args:
            result["sqlstate"] = str(error.args[0])
            message = " ".join(str(value) for value in error.args[1:])
            for secret in (settings.sql_password, settings.sql_user):
                if secret:
                    message = message.replace(secret, "<omitido>")
            result["detalhe"] = message[:1600]
        print(f"FALHA: {label}; tipo={result['tipo']}; SQLSTATE={result.get('sqlstate', 'nao aplicavel')}.", flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "computador": platform.node(), "data": datetime.now().astimezone().isoformat(),
        "metodo": "Consultas SQL de leitura; sistemas e integracoes nao iniciados.",
        "bancos_locais_criados": False, "sql": [],
    }
    try:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        settings = configure_vm(
            Path(r"\\VBOXSVR\OrigemAutomatiza\.env"), Path(r"C:\AutomatizaTestes"),
            args.saida.parent / "config-backups" / (args.saida.stem + ".env-anterior.backup"),
        )
        result["driver"] = settings.sql_driver
        result["rede"] = check_network(args.saida)
        result["sql"] = [check_sql(settings, *target) for target in SQL_TARGETS]
        oracle = {
            "ambiente": "oracle-braslux", "servidor": "dexter", "porta": 1521,
            "usuario": "rhtimegprevisao", "login_validado": False,
            "pendente": "Confirmar servico/SID e configurar a conexao Oracle do RH.",
            "biblioteca_gerenciada_copiada": Path(r"C:\meta\rhsis\Oracle.ManagedDataAccess.dll").is_file(),
        }
        try:
            with socket.create_connection(("dexter", 1521), timeout=5):
                oracle["porta_acessivel"] = True
        except OSError:
            oracle["porta_acessivel"] = False
        result["oracle"] = oracle
        print("Oracle dexter:1521: " + ("porta acessivel" if oracle["porta_acessivel"] else "porta inacessivel"), flush=True)
        print("O login Oracle ainda nao foi validado; falta o servico/SID.", flush=True)
        result["estado"] = "sql_validado_oracle_pendente" if all(item["estado"] == "conectado" for item in result["sql"]) else "falha_conexao_sql"
    except Exception as error:
        result.update(estado="falha_preparacao", tipo=type(error).__name__)
        print(f"Falha de preparacao: {type(error).__name__}. Nenhuma senha foi registrada.", flush=True)
    args.saida.write_text(json.dumps(result, ensure_ascii=True, indent=2), encoding="utf-8")
    return 0 if result["estado"] == "sql_validado_oracle_pendente" else 1


if __name__ == "__main__":
    sys.exit(main())
