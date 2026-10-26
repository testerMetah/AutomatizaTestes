"""Complementa a auditoria existente sem alterar cadastros ou configuração."""
import hashlib
import json
import os
import re
import ssl
import urllib.request
from datetime import datetime
from pathlib import Path

from automatiza.config import Settings
from automatiza.database import SqlServer

OUT = Path("reports/integracao-api/20261020/auditoria-103518")
def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

def record(action, expected, observed, status):
    e = dict(horario=datetime.now().astimezone().isoformat(), acao=action,
             esperado=expected, observado=observed, resultado=status)
    with (OUT / "diario-testes.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False, default=str) + "\n")
    with (OUT / "diario-testes.txt").open("a", encoding="utf-8") as f:
        f.write(f"[{e['horario']}] {status} | {action}\n  Esperado: {expected}\n"
                f"  Observado: {observed}\n\n")
    print(json.dumps(e, ensure_ascii=True, default=str), flush=True)

record("Retomar investigação das pendências", "Preservar os cadastros existentes",
       "Somente consultas: catálogo autenticado, binário instalado e destino.", "INICIADO")
ctx = ssl._create_unverified_context()
base = "https://apimetadados.metahequipamentos.com.br"
request = urllib.request.Request(base + "/login",
    data=json.dumps(dict(email="metahdev02@gmail.com", senha=os.environ["SIRH_TEST_PASSWORD"])).encode(),
    headers={"Content-Type": "application/json"})
with urllib.request.urlopen(request, context=ctx, timeout=40) as response:
    token = json.load(response)["accessToken"]
record("Autenticar para consultar catálogo gerenciável", "HTTP 200",
       "Token obtido; não persistido. Mesma exceção TLS restrita ao diagnóstico anterior.", "PASSOU")
request = urllib.request.Request(base + "/endpoint", headers={"Authorization": "Bearer " + token})
try:
    with urllib.request.urlopen(request, context=ctx, timeout=40) as response:
        data = json.load(response)
        if not isinstance(data, list):
            raise ValueError("Catálogo fora do formato esperado")
        names = [str(row.get("nome", "")) for row in data]
        save("catalogo-endpoints-autenticado.json", names)
        matches = [n for n in names if any(k in n.lower() for k in ("reserv", "refei", "consumo"))]
        record("Procurar reservas no catálogo autenticado /endpoint",
               "Identificar endpoint para reservas, refeições ou consumo",
               dict(http=response.status, endpoints=len(names), correspondencias=matches),
               "ROTA_NAO_ENCONTRADA" if not matches else "EXAMINAR_ROTA")
except urllib.error.HTTPError as exc:
    record("Consultar /endpoint", "Acesso ao catálogo autenticado",
           dict(http=exc.code, observacao="Sem exportar corpo da resposta"), "BLOQUEADO")

binary = Path("C:/acesso/AcessusSyncImportacao.exe").read_bytes()
strings = [s.decode("utf-16le") for s in re.findall(rb"(?:[\x20-\x7e\xa0-\xff]\x00){5,}", binary)]
filters = sorted(set(s for s in strings if
    "GERAAFASTAMENTO = 'S'" in s or ":Hoje BETWEEN" in s or
    "TERMINOGOZOFERIAS >= :Hoje" in s))
bad_label = "F\u00c3\u00a9rias"
routes = sorted(set(s for s in strings if re.fullmatch(r"(?:cadastro|frequencia)/[A-Za-z]+", s)))
evidence = dict(arquivo="C:/acesso/AcessusSyncImportacao.exe",
               sha256=hashlib.sha256(binary).hexdigest(), filtros_sql_embutidos=filters,
               rotas_literais=routes, literal_ferias_incorreto_presente=bad_label in strings,
               limite="Strings embutidas são evidência estática; não provam fluxo executado nem requisito de negócio.")
save("evidencia-estatica-importador.json", evidence)
record("Inspecionar filtros embutidos no importador instalado",
       "Encontrar evidência que explique as exclusões observadas",
       dict(filtros=filters, limite=evidence["limite"]), "EVIDENCIA_ESTATICA")
record("Investigar origem do texto incorreto de férias",
       "Literal legível no importador e no destino",
       dict(literal_incorreto_no_binario=bad_label in strings,
            inferencia="Se presente, o executável é uma origem provável do defeito; não foi alterado."),
       "DEFEITO_LOCALIZADO" if bad_label in strings else "INCONCLUSIVO")

db = SqlServer(Settings.load())
rows = db.query("""SELECT Id,IdPessoa,DataInicio,DataTermino,Causa,IdFreq FROM Afastamentos
 WHERE IdPessoa=5 ORDER BY Id""")
codes = db.query("""SELECT Id,UNICODE(SUBSTRING(Causa,2,1)) AS Codigo2,
 UNICODE(SUBSTRING(Causa,3,1)) AS Codigo3 FROM Afastamentos
 WHERE IdPessoa=5 AND IdFreq LIKE 'AFAST_F_%' ORDER BY Id""")
save("destino-pendencias.json", dict(afastamentos=rows, codigos_causa=codes,
                                   reservas=db.scalar("SELECT COUNT(*) FROM RefeicoesReservas")))
cases = json.loads((OUT / "casos-conferidos.json").read_text(encoding="utf-8"))
date = datetime(2026, 10, 20)
classifications = []
for case in cases:
    if not case["caso"].startswith("O"):
        continue
    start = datetime.fromisoformat(case["inicio"])
    end = datetime.fromisoformat(case["termino"]) if case["termino"] else date
    eligible = case["gera_afastamento"] == "S" and start <= date <= end
    present = any(r["Id"] == case["id_destino"] for r in rows)
    classifications.append(dict(caso=case["caso"],
        criterio="gera_afastamento=S e início<=20/10/2026<=término (ou aberto)",
        elegivel=eligible, presente=present, corresponde=eligible == present))
save("comparacao-filtro-vigencia.json", classifications)
record("Comparar os 20 casos com o filtro encontrado",
       "Presença/ausência compatível com gera-afastamento e vigência em 20/10/2026",
       dict(casos=len(classifications), correspondentes=sum(x["corresponde"] for x in classifications),
            limite="Compatibilidade técnica com filtro estático; aprovação do requisito funcional permanece separada."),
       "COMPATIVEL" if all(x["corresponde"] for x in classifications) else "DIVERGENTE")
record("Revalidar causa das férias", "Segundo caractere 233, equivalente a é",
       codes, "FALHOU_TEXTO" if any(r["Codigo2"] != 233 for r in codes) else "PASSOU")
record("Concluir investigação sem novos cadastros", "Preservar estado de negócio",
       "Nenhum INSERT/UPDATE/DELETE executado; nenhuma importação SQL substituiu a API.", "CONCLUIDO")
