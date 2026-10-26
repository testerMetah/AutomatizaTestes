"""Audita por SELECT a fixture sintética e gera RELATORIO.html."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from automatiza.config import Settings
from automatiza.database import SqlServer
from automatiza.sequencias.relatorio import Report

PREFIX = "AUTOTEST_20261023_CARGA_"


def main():
    target = json.loads((ROOT / "config/ambiente-teste.json").read_text(encoding="utf-8"))["sql_destino"]
    db = SqlServer(Settings.load())
    if not target["confirmado_como_teste"] or db.assert_database() != target["banco"]:
        raise RuntimeError("Banco AUTOTEST nao confirmado")
    report = Report(root=ROOT / "reports")
    report.context = {"sequencia": "validacao-carga-sintetica", "seed": 20261023}
    checks = [
        ("empresas", "SELECT COUNT(*) FROM Empresas WHERE nome LIKE ?", (PREFIX + "%",), 3),
        ("unidades", "SELECT COUNT(*) FROM Unidades WHERE nome LIKE ?", (PREFIX + "%",), 6),
        ("pessoas", "SELECT COUNT(*) FROM Pessoas WHERE nome LIKE ?", (PREFIX + "%",), 120),
        ("crachas", "SELECT COUNT(*) FROM RegCrachas WHERE Codigo LIKE ?", ("AUTOTEST-%",), 120),
        ("refeitorios", "SELECT COUNT(*) FROM Refeitorios WHERE nome LIKE ?", (PREFIX + "%",), 3),
        ("cardapios", "SELECT COUNT(*) FROM cardapios WHERE nome LIKE ?", (PREFIX + "%",), 6),
        ("veiculos", "SELECT COUNT(*) FROM Veiculos WHERE nome LIKE ?", (PREFIX + "%",), 30),
        ("afastamentos", "SELECT COUNT(*) FROM Afastamentos WHERE IdFreq LIKE ?", (PREFIX + "%",), 18),
        ("reservas", "SELECT COUNT(*) FROM RefeicoesReservas WHERE IdExportacao LIKE ?", (PREFIX + "MODULOS_%",), 40),
        ("acessos", "SELECT COUNT(*) FROM AcessosAutorizados WHERE IdFreq LIKE ?", (PREFIX + "MODULOS_%",), 80),
        ("coletor-local", "SELECT COUNT(*) FROM Coletores WHERE nome=? AND ip='127.0.0.1' AND status=0", (PREFIX + "COLETOR_LOOPBACK",), 1),
        ("pessoas-sem-unidade", "SELECT COUNT(*) FROM Pessoas p LEFT JOIN Unidades u ON u.codigo=p.idUnidade AND u.idEmpresa=p.idempresa WHERE p.nome LIKE ? AND u.id IS NULL", (PREFIX + "%",), 0),
        ("crachas-sem-pessoa", "SELECT COUNT(*) FROM RegCrachas c LEFT JOIN Pessoas p ON p.id=c.IdPessoa WHERE c.Codigo LIKE ? AND p.id IS NULL", ("AUTOTEST-%",), 0),
        ("unidades-por-empresa", "SELECT COUNT(*) FROM (SELECT idEmpresa FROM Unidades WHERE nome LIKE ? GROUP BY idEmpresa HAVING COUNT(*)=2) x", (PREFIX + "%",), 3),
        ("pessoas-por-unidade", "SELECT COUNT(*) FROM (SELECT p.idempresa,p.idUnidade FROM Pessoas p WHERE p.nome LIKE ? GROUP BY p.idempresa,p.idUnidade HAVING COUNT(*)=20) x", (PREFIX + "%",), 6),
        ("config-api", "SELECT COUNT(*) FROM DADOS_IMPORTACAO_API WHERE id_coletores<>'' AND url_api<>'' AND senha_api<>''", (), 1),
    ]
    failed = []
    for number, (name, sql, params, expected) in enumerate(checks, 1):
        report.context["passo"] = number
        actual = db.scalar(sql, params)
        state = "PASSOU" if actual == expected else "FALHOU"
        report.emit("BANCO", acao=name, sql=sql, parametros=params, linhas=1,
                    esperado=expected, obtido=actual, resultado=state)
        if state == "FALHOU":
            failed.append(f"{name}: esperado {expected}, obtido {actual}")
    report.cases.append({"nome": "validacao-carga-sintetica", "seed": 20261023,
                         "estado": "FALHOU" if failed else "PASSOU", "passos": len(checks),
                         "erro": "; ".join(failed) if failed else None})
    path = report.finish()
    print(path)
    if failed:
        raise SystemExit("; ".join(failed))


if __name__ == "__main__":
    main()
