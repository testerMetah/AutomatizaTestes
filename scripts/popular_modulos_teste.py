"""Amplia a fixture AUTOTEST para acessos, refeitório, escola e visitas."""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pyodbc

from automatiza.config import Settings
from popular_base_teste import PREFIX, TARGET, insert

MARK = PREFIX + "MODULOS_"


def main():
    manifest = json.loads((ROOT / "config/ambiente-teste.json").read_text(encoding="utf-8"))
    target = manifest["sql_destino"]
    settings = Settings.load()
    if not target["confirmado_como_teste"] or target["banco"] != TARGET or settings.sql_database != TARGET:
        raise SystemExit("Destino AUTOTEST nao confirmado")
    counts = {}
    connection = pyodbc.connect(settings.connection_string(), autocommit=False)
    try:
        c = connection.cursor()
        c.execute("SELECT DB_NAME()")
        if c.fetchone()[0] != TARGET:
            raise RuntimeError("DB_NAME() incorreto")
        c.execute("SELECT COUNT(*) FROM AcessosAutorizados WHERE IdFreq LIKE ?", MARK + "%")
        if c.fetchone()[0]:
            raise RuntimeError("Carga de modulos ja existe")

        def add(table, **values):
            result = insert(c, table, **values)
            counts[table] = counts.get(table, 0) + 1
            return result

        def link(table, columns, values):
            sql = f"INSERT INTO dbo.[{table}] ({','.join('[' + x + ']' for x in columns)}) VALUES ({','.join('?' for _ in values)})"
            c.execute(sql, values)
            counts[table] = counts.get(table, 0) + 1

        c.execute("SELECT id FROM Coletores WHERE nome=?", PREFIX + "COLETOR_LOOPBACK")
        collector = c.fetchone()[0]
        c.execute("SELECT id,id_empresa,IdRefeitorio FROM cardapios WHERE nome LIKE ? ORDER BY id", PREFIX + "%")
        menus = c.fetchall()
        c.execute("SELECT id,id_empresa FROM Refeitorios WHERE nome LIKE ? ORDER BY id", PREFIX + "%")
        refectories = c.fetchall()
        c.execute("SELECT id,nome,idempresa FROM Pessoas WHERE nome LIKE ? ORDER BY id", PREFIX + "%")
        people = c.fetchall()
        c.execute("SELECT IdPessoa,Codigo FROM RegCrachas WHERE Codigo LIKE 'AUTOTEST-%'")
        badges = {int(row[0]): row[1] for row in c.fetchall()}
        c.execute("SELECT id,id_empresa FROM ALUNOS WHERE nome LIKE ?", PREFIX + "%")
        students = c.fetchall()
        c.execute("SELECT id,id_empresa FROM RESPONSAVEIS WHERE nome LIKE ?", PREFIX + "%")
        responsible = {int(row[1]): int(row[0]) for row in c.fetchall()}

        for index, row in enumerate(menus):
            link("cardapios_refeitorios", ("CardapiosId", "RefeitoriosId"), (row[0], row[2]))
        for row in students:
            link("ALUNOS_RESPONSAVEIS", ("id_aluno", "id_responsavel"),
                 (row[0], responsible[int(row[1])]))
        for n in range(1, 6):
            add("MensagemColetores", nome=MARK + f"MENSAGEM_{n}")
        c.execute("SELECT id FROM GrupoAcesso WHERE nome LIKE ? ORDER BY id", PREFIX + "%")
        for n, row in enumerate(c.fetchall(), 1):
            add("GrupoAcessoRegras", idgrupoacesso=row[0], ordem=1,
                inicio=datetime(2026, 1, 1), termino=datetime(2030, 1, 1), regra=0)

        for i, row in enumerate(people[:80], 1):
            person, _, company = int(row[0]), row[1], int(row[2])
            badge = badges[person]
            menu = menus[(company - 2) * 2] if 2 <= company <= 4 else menus[0]
            refectory = refectories[company - 2][0] if 2 <= company <= 4 else refectories[0][0]
            day = datetime(2026, 11, 1) + timedelta(days=i % 20)
            add("AcessosAutorizados", IdPessoa=person, DataHoraInicio=day,
                DataHoraFim=day + timedelta(days=1), Autorizado=1,
                IdFreq=MARK + f"ACESSO_{i:04d}", importado="N")
            add("FaixaAcessoColetores", idcoletor=collector, funcaocoletor=0,
                nrocracha=badge, status=0, qtdeacesso=2, origem="GA",
                datahorainicio=day, datahoratermino=day + timedelta(days=1))
            add("MarcacoesOnline", datahora=day + timedelta(hours=8), idCracha=badge,
                funcao=0, idcoletor=collector, sentido=0, tipocoleta=0, situacao=0,
                msg="AUTOTEST", idpessoa=person)
            if i <= 40:
                add("RefeicoesReservas", situacao=0, datahora=day, credencial=badge,
                    refeicoes=str(menu[0]), id_refeitorio=refectory,
                    IdExportacao=MARK + f"RESERVA_{i:04d}", datahoraini=day,
                    datahorafim=day + timedelta(hours=1), id_empresa=company,
                    id_pessoa=person, tipo_pessoa=0)
                add("Refeicoes", IdColetor=collector, IdCardapio=menu[0], Funcao=0,
                    tipoRefeicao=0, DataHora=day + timedelta(hours=12), IdPessoa=person,
                    refeitorio=refectory, id_empresa=company)
                add("Creditos", IdColetor=collector, IdCardapio=menu[0],
                    IdRefeitorio=refectory, IdPessoa=person, Qtde=10)
                add("CreditosPessoa", IdColetor=collector, IdCardapio=menu[0],
                    IdRefeitorio=refectory, IdPessoa=person, saldo=10)

        c.execute("SELECT id FROM VisitantesTerceiros WHERE Nome LIKE ? ORDER BY id", PREFIX + "%")
        visitors = [int(row[0]) for row in c.fetchall()]
        for i, visitor in enumerate(visitors, 1):
            visit = add("VisitantesTerceirosHistoricos", idVisitantes=visitor,
                NrCracha=f"AUTOTEST-VIS-{i}", Observacao=MARK + "VISITA",
                Cardapios=str(menus[0][0]), Status=0,
                DataHoraInicio=datetime(2026, 11, i),
                DataHoraTermino=datetime(2026, 11, i, 18))
            add("EstadoVisita", estado=0, datahora=datetime(2026, 11, i), idvisita=visit)
            add("registroTransportadora", transportadora=MARK + f"TRANSPORTADORA_{i}",
                nome_motorista=MARK + f"MOTORISTA_{i}",
                data_entrada=datetime(2026, 11, i, 9))
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    print(json.dumps({"banco": TARGET, "tabelas": counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
