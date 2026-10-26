"""Carga sintetica, transacional e idempotente para a base AUTOTEST confirmada.

Nao usa dados pessoais da base antiga. O coletor aponta apenas para loopback.
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pyodbc

from automatiza.config import Settings

PREFIX = "AUTOTEST_20261023_CARGA_"
TARGET = "Acessus_AUTOTEST_20261023"


def insert(cursor, table, **values):
    columns = ", ".join("[" + key + "]" for key in values)
    marks = ", ".join("?" for _ in values)
    # OUTPUT antecede VALUES no SQL Server; retorna a identidade gerada.
    cursor.execute(
        f"INSERT INTO dbo.[{table}] ({columns}) OUTPUT INSERTED.id VALUES ({marks})",
        tuple(values.values()),
    )
    return int(cursor.fetchone()[0])


def main():
    manifest = json.loads((ROOT / "config/ambiente-teste.json").read_text(encoding="utf-8"))
    target = manifest["sql_destino"]
    if not target["confirmado_como_teste"] or target["banco"] != TARGET:
        raise SystemExit("Carga recusada: destino AUTOTEST nao confirmado.")
    settings = Settings.load()
    if settings.sql_server.casefold() != target["servidor"].casefold() or settings.sql_database != TARGET:
        raise SystemExit("Carga recusada: .env e manifesto apontam para bancos diferentes.")
    counts = {}
    connection = pyodbc.connect(settings.connection_string(), autocommit=False)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT DB_NAME()")
        if cursor.fetchone()[0] != TARGET:
            raise RuntimeError("DB_NAME() difere do alvo confirmado")
        cursor.execute("SELECT COUNT(*) FROM dbo.Empresas WHERE nome LIKE ?", PREFIX + "%")
        if cursor.fetchone()[0]:
            raise RuntimeError("Carga ja existe; operacao idempotente recusou duplicacao")

        def add(table, **values):
            row_id = insert(cursor, table, **values)
            counts[table] = counts.get(table, 0) + 1
            return row_id

        # Dados de referencia e coletor sem rede externa. Status 0 = ativo no codigo Delphi.
        model = add("ModeloColetores", idmarca="0205", nome="AUTOTEST LOCAL")
        collector = add("Coletores", nome=PREFIX + "COLETOR_LOOPBACK", status=0,
                        idmodelo=model, ip="127.0.0.1", comunicacao=0, funcacesso=0)
        sectors = [add("Setores", nome=PREFIX + f"SETOR_{n:02d}", status=0) for n in range(1, 7)]
        occurrences = [add("Ocorrencias", Nome=PREFIX + kind) for kind in
                       ("FALTA", "FERIAS", "ATRASO", "AFASTAMENTO")]
        groups = [add("GrupoAcesso", nome=PREFIX + f"GRUPO_{n:02d}", status=0) for n in range(1, 4)]
        parking = add("Estacionamento", Nome=PREFIX + "ESTACIONAMENTO", quantidade=100)
        vehicle_type = add("TipoVeiculo", Nome=PREFIX + "AUTOMOVEL")
        e_type = add("TiposDeEPIs", equipamento=PREFIX + "CAPACETE", descricao="EPI sintetico")
        add("EPIs", equipamento=e_type, aquisicao=datetime(2026, 1, 1),
            validade=datetime(2028, 1, 1), estado=0, posse=0, descricao=PREFIX + "EPI")

        for company_no in range(1, 4):
            company = add("Empresas", nome=PREFIX + f"EMPRESA_{company_no}",
                          cpf_cnpj=f"AUTOTEST-CNPJ-{company_no:03d}")
            access_company = add("EmpresaAcesso", Nome=PREFIX + f"ACESSO_{company_no}",
                                 Cnpj_Cpf=f"AUTOTEST-ACESSO-{company_no:03d}", excluido="N")
            refectory = add("Refeitorios", nome=PREFIX + f"REFEITORIO_{company_no}",
                            status=0, id_empresa=company, sentido_acesso=0,
                            IdExportacao=PREFIX + f"REF_{company_no}")
            add("cardapios", nome=PREFIX + f"CARDAPIO_{company_no}_A", status=0,
                id_empresa=company, IdRefeitorio=refectory,
                IdExportacao=PREFIX + f"CARD_{company_no}_A")
            add("cardapios", nome=PREFIX + f"CARDAPIO_{company_no}_B", status=0,
                id_empresa=company, IdRefeitorio=refectory,
                IdExportacao=PREFIX + f"CARD_{company_no}_B")
            add("RegrasAcesso", Nome=PREFIX + f"REGRA_{company_no}", TipoRegra=0,
                coletores=str(collector), TipoSelecao=0, id_empresa=company,
                DataHoraInicio=datetime(2026, 1, 1), DataHoraTermino=datetime(2030, 1, 1))
            turn = add("TURNOS", nome=PREFIX + f"TURNO_{company_no}", situacao=0, id_empresa=company)
            group = add("TURMAS", nome=PREFIX + f"TURMA_{company_no}", situacao=0,
                        id_empresa=company, id_turno=turn)
            add("RESPONSAVEIS", nome=PREFIX + f"RESPONSAVEL_{company_no}",
                situacao=0, sexo="F", id_empresa=company)
            for unit_no in range(1, 3):
                code = f"{company_no}{unit_no:03d}"
                add("Unidades", idEmpresa=company, nome=PREFIX + f"UNIDADE_{company_no}_{unit_no}",
                    status=0, codigo=code)
                for person_no in range(1, 21):
                    shared = person_no <= 5
                    label = (f"PESSOA_COMPARTILHADA_{person_no:02d}" if shared else
                             f"PESSOA_EXCLUSIVA_{company_no}_{unit_no}_{person_no:02d}")
                    person = add("Pessoas", nome=PREFIX + label, status=0, idempresa=company,
                                 idUnidade=code, idsetor=sectors[(person_no - 1) % len(sectors)],
                                 sexo="F" if person_no % 2 else "M",
                                 datacadastro=datetime(2026, 10, 23),
                                 datanascimento=datetime(1990, 1, 1) + timedelta(days=person_no * 67))
                    add("RegCrachas", Codigo=f"AUTOTEST-{company_no}{unit_no}{person_no:04d}",
                        TipoUso=0, IdPessoa=person, DataHoraRegistro=datetime(2026, 10, 23))
                    if person_no <= 5:
                        add("Veiculos", placa=f"AT{company_no}{unit_no}{person_no:03d}", idpessoa=person,
                            idtipoveiculo=vehicle_type, idestacionamento=parking,
                            nome=PREFIX + f"VEICULO_{company_no}_{unit_no}_{person_no}", situacao=0)
                    if person_no in (1, 2, 3):
                        add("Afastamentos", IdPessoa=person,
                            DataInicio=datetime(2026, 11, person_no),
                            DataTermino=datetime(2026, 11, person_no + 2),
                            Causa=PREFIX + "AFASTAMENTO",
                            IdFreq=PREFIX + f"AFAST_{company_no}_{unit_no}_{person_no}")
                    if person_no <= 2:
                        add("PreCadastros", Nome=PREFIX + f"PRE_{company_no}_{unit_no}_{person_no}",
                            Status=0, idempresa=access_company)
                add("VisitantesTerceiros", Tipo=0, Nome=PREFIX + f"VISITANTE_{company_no}_{unit_no}",
                    Cpf=f"AUTOTEST-{company_no}{unit_no}", Status=0,
                    IdEmpresaAcesso=access_company)
                add("ALUNOS", id_empresa=company, situacao=0,
                    nome=PREFIX + f"ALUNO_{company_no}_{unit_no}",
                    nascimento=datetime(2012, 1, 1), sexo="M", matricula=company_no * 100 + unit_no,
                    id_turma=group)

        cursor.execute("SELECT COUNT(*) FROM dbo.Pessoas WHERE nome LIKE ?", PREFIX + "%")
        if cursor.fetchone()[0] != counts["Pessoas"]:
            raise RuntimeError("Conferencia de pessoas falhou antes do commit")
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    print(json.dumps({"banco": TARGET, "prefixo": PREFIX, "tabelas": counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
