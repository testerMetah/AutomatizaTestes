"""Confere a massa multiempresa do Frequência sem modificar os bancos."""

import json
import sys
from dataclasses import replace
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from automatiza.config import Settings
from automatiza.database import SqlServer


def main() -> int:
    db = SqlServer(replace(Settings.load(), sql_database="RHFagundes"))
    companies = db.query("SELECT EMPRESA,ATIVADESATIVADA FROM RHEMPRESAS WHERE EMPRESA IN ('9001','9002','9003')")
    units = db.query("SELECT UNIDADE,EMPRESA,ATIVADESATIVADA FROM RHUNIDADES WHERE UNIDADE IN ('9101','9102','9201','9202','9301','9302')")
    establishments = db.query("SELECT EMPRESA,ESTABELECIMENTO,ATIVADESATIVADA FROM RHESTABELECIMENTOS WHERE EMPRESA IN ('9001','9002','9003')")
    people = db.query("SELECT EMPRESA,PESSOA FROM RHPESSOAS WHERE EMPRESA IN ('9001','9002','9003') AND PESSOA IN (990001,910101,910201,920101,920201,930101,930201)")
    contracts = db.query("SELECT EMPRESA,UNIDADE,CONTRATO,PESSOA,SITUACAO FROM RHCONTRATOS WHERE UNIDADE IN ('9101','9102','9201','9202','9301','9302')")

    expected_units = {('9101','9001'),('9102','9001'),('9201','9002'),('9202','9002'),('9301','9003'),('9302','9003')}
    expected_people = {(company,990001) for company in ('9001','9002','9003')} | {(company,person) for company,person in [('9001',910101),('9001',910201),('9002',920101),('9002',920201),('9003',930101),('9003',930201)]}
    expected_contracts = {(unit,number,person) for unit,number,person in [('9101',910101,990001),('9101',910102,910101),('9102',910201,990001),('9102',910202,910201),('9201',920101,990001),('9201',920102,920101),('9202',920201,990001),('9202',920202,920201),('9301',930101,990001),('9301',930102,930101),('9302',930201,990001),('9302',930202,930201)]}
    checks = {
        'empresas_ausentes': sorted({'9001','9002','9003'} - {r['EMPRESA'] for r in companies}),
        'empresas_inativas': sorted(r['EMPRESA'] for r in companies if r['ATIVADESATIVADA'] != '1'),
        'unidades_ausentes': sorted(expected_units - {(r['UNIDADE'],r['EMPRESA']) for r in units}),
        'unidades_inativas': sorted(r['UNIDADE'] for r in units if r['ATIVADESATIVADA'] != '1'),
        'estabelecimentos_ausentes': sorted({'9001','9002','9003'} - {r['EMPRESA'] for r in establishments}),
        'estabelecimentos_inativos': sorted(r['ESTABELECIMENTO'] for r in establishments if r['ATIVADESATIVADA'] != '1'),
        'pessoas_ausentes': sorted(expected_people - {(r['EMPRESA'],r['PESSOA']) for r in people}),
        'contratos_ausentes': sorted(expected_contracts - {(r['UNIDADE'],r['CONTRATO'],r['PESSOA']) for r in contracts}),
        'contratos_inesperados': sorted((r['UNIDADE'],r['CONTRATO'],r['PESSOA']) for r in contracts if (r['UNIDADE'],r['CONTRATO'],r['PESSOA']) not in expected_contracts),
        'contratos_nao_ativos': sorted((r['UNIDADE'],r['CONTRATO'],r['SITUACAO']) for r in contracts if (r['UNIDADE'],r['CONTRATO'],r['PESSOA']) in expected_contracts and r['SITUACAO'] != '1'),
    }
    report = {'data': datetime.now().isoformat(timespec='seconds'), 'banco': 'RHFagundes', 'resultado': 'APROVADO' if all(not value for value in checks.values()) else 'PENDENTE', 'verificacoes': checks}
    output = Path(__file__).resolve().parents[1] / 'reports' / 'frequencia_fixtures_validacao.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f'Relatório: {output}')
    return 0 if report['resultado'] == 'APROVADO' else 1


if __name__ == '__main__':
    sys.exit(main())
