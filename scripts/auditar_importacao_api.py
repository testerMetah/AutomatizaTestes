"""Auditoria somente leitura, com diário próprio; nenhuma inserção de negócio."""
import json
import os
import ssl
import time
import urllib.request
from collections import Counter
from dataclasses import replace
from datetime import datetime
from pathlib import Path

from automatiza.config import Settings
from automatiza.database import SqlServer

OUT = Path("reports/integracao-api/20261020") / datetime.now().strftime("auditoria-%H%M%S")
OUT.mkdir(parents=True, exist_ok=False)
events = []


def event(action, expected, observed, status="OBSERVADO"):
    row = dict(horario=datetime.now().astimezone().isoformat(), acao=action,
               esperado=expected, observado=observed, resultado=status)
    events.append(row)
    with (OUT / "diario-testes.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
    with (OUT / "diario-testes.txt").open("a", encoding="utf-8") as f:
        f.write(f"[{row['horario']}] {status} | {action}\n"
                f"  Esperado: {expected}\n  Observado: {observed}\n\n")
    print(json.dumps(row, ensure_ascii=True, default=str), flush=True)


def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str),
                           encoding="utf-8")


settings = Settings.load()
source = SqlServer(replace(settings, sql_database="RHFagundes"))
dest = SqlServer(settings)
service_log = Path("C:/acesso/Logs/AcessusSyncProcessoService.log")
log_position = service_log.stat().st_size
event("Iniciar auditoria dos cadastros existentes",
      "Nenhum novo cadastro; acompanhar importador API e conferir origem/API/destino",
      "Unidade 0004, contrato 4, pessoa Acessus 5. Diário próprio iniciado agora; "
      "não reconstrói horários de ações anteriores.")
occ = source.query("""SELECT R.OCORRENCIA,R.DATAINICIOOCORRENCIA,
 R.DATATERMINOOCORRENCIA,R.NROHORASOCORRENCIA,C.DESCRICAO40,
 C.GERAAFASTAMENTO,C.GERAAFASTAMENTOPONTO
 FROM RHREGOCORRENCIAS R JOIN RHOCORRENCIAS C ON C.OCORRENCIA=R.OCORRENCIA
 WHERE R.UNIDADE='0004' AND R.CONTRATO=4 ORDER BY R.DATAINICIOOCORRENCIA""")
hol = source.query("""SELECT INICIOGOZOFERIAS,TERMINOGOZOFERIAS FROM RHFERIASCEDIDASPA
 WHERE UNIDADE='0004' AND CONTRATO=4 ORDER BY INICIOGOZOFERIAS""")
res = source.query("""SELECT NROORDEM,DATAINICIO,DATATERMINO,REFEICAO,CARDAPIO,
 TIPOREFEICAO,QUANTIDADECONSUMIDA,REFEITORIO FROM RHPROGRESERVACONSUMO
 WHERE UNIDADE='0004' AND CONTRATO=4 ORDER BY NROORDEM""")
save("origem.json", dict(ocorrencias=occ, ferias=hol, reservas_consumos=res))
event("Ler registros efetivamente salvos no SIRH",
      "Usar dados persistidos, sem considerar rascunhos como cadastros",
      f"{len(occ)} ocorrências; {len(hol)} férias; {len(res)} reservas/consumos", "CONFERIDO")

base = "https://apimetadados.metahequipamentos.com.br"
ctx = ssl._create_unverified_context()
event("Preparar consulta diagnóstica HTTPS",
      "Usar a API configurada sem alterar Windows ou Acessus",
      "Exceção de certificado restrita a este processo diagnóstico, pois o certificado "
      "do servidor não é confiável nesta máquina. Credenciais e token não serão registrados.")
req = urllib.request.Request(base + "/login",
    data=json.dumps({"email": "metahdev02@gmail.com",
                     "senha": os.environ["SIRH_TEST_PASSWORD"]}).encode(),
    headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, context=ctx, timeout=45) as response:
    token = json.load(response)["accessToken"]
    event("Autenticar na API", "HTTP 200 e token utilizável",
          f"HTTP {response.status}; token mantido apenas em memória", "PASSOU")


def api_pages(route, query, fields):
    result = []
    previous = None
    for page in range(1, 21):
        url = base + route + "?" + query + ("&" if query else "") + f"pagina={page}"
        request = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
        with urllib.request.urlopen(request, context=ctx, timeout=45) as response:
            data = json.load(response)
            if not isinstance(data, list):
                raise RuntimeError("Formato de API inesperado: " + route)
            event(f"Consultar {route}, página {page}", "HTTP 200 e lista de registros",
                  f"HTTP {response.status}; {len(data)} registros", "PASSOU")
        if not data:
            break
        projected = [{k: row.get(k) for k in fields} for row in data]
        if projected == previous:
            raise RuntimeError("Paginação repetida: " + route)
        result.extend(projected)
        previous = projected
    else:
        raise RuntimeError("Paginação não terminou")
    return result


api_occ = api_pages("/cadastro/registrosOcorrencias", "unidade=0004&contrato=4",
                    ["unidade", "contrato", "ocorrencia", "dataInicioOcorrencia",
                     "dataTerminoOcorrencia", "nroHorasOcorrecia"])
api_hol = api_pages("/frequencia/feriasCedidas", "unidade=0004&contrato=4",
                    ["unidade", "contrato", "inicioGozoFerias", "terminoGozoFerias"])
save("api.json", dict(ocorrencias=api_occ, ferias=api_hol))
with urllib.request.urlopen(base + "/swagger/v1/swagger.json", context=ctx, timeout=45) as response:
    spec = json.load(response)
paths = list(spec["paths"])
reservation_paths = [p for p in paths if any(k in p.lower() for k in ("reserv", "refeic", "consumo"))]
save("rotas-api.json", paths)
event("Verificar rota API para reservas/consumos",
      "Uma rota publicada que entregue reservas ao importador",
      f"Rotas compatíveis encontradas no Swagger atual: {reservation_paths}",
      "BLOQUEADO" if not reservation_paths else "CONFERIR")


def snapshot():
    return dict(afastamentos=dest.query("""SELECT Id,IdPessoa,DataInicio,DataTermino,Causa,IdFreq
        FROM Afastamentos WHERE IdPessoa=5 ORDER BY Id"""),
        reservas_total=dest.scalar("SELECT COUNT(*) FROM RefeicoesReservas"),
        refeitorios_total=dest.scalar("SELECT COUNT(*) FROM Refeitorios"))


before = snapshot()
save("destino-antes.json", before)
event("Fotografar destino antes dos próximos ciclos",
      "Estabelecer quantidade e IDs para verificar repetição",
      f"{len(before['afastamentos'])} afastamentos; "
      f"{before['reservas_total']} reservas no banco; {before['refeitorios_total']} refeitórios")
cycles = Counter()
deadline = time.monotonic() + 210
while time.monotonic() < deadline:
    time.sleep(15)
    with service_log.open("rb") as f:
        f.seek(log_position)
        chunk = f.read()
        log_position = f.tell()
    # Somente marcadores de conclusão; nunca exportar conteúdo bruto do log.
    for operation in ("GetFeriasCedidas", "GetAfastamentos"):
        n = chunk.count(("Finalizou " + operation + " com sucesso.").encode())
        if n:
            cycles[operation] += n
            current = snapshot()
            event("Observar conclusão de " + operation,
                  "Ciclo automático finalizar e manter dados coerentes",
                  f"{n} conclusão(ões) desde a leitura anterior; "
                  f"{len(current['afastamentos'])} afastamentos e "
                  f"{current['reservas_total']} reservas no destino", "CICLO_CONCLUIDO")
    if all(cycles[k] >= 2 for k in ("GetFeriasCedidas", "GetAfastamentos")):
        break
after = snapshot()
save("destino-depois.json", after)
event("Conferir repetição dos ciclos", "Dois ciclos de férias e afastamentos sem duplicação",
      f"Ciclos: {dict(cycles)}; estado anterior igual ao posterior: {before == after}",
      "PASSOU" if before == after and all(cycles[k] >= 2 for k in
      ("GetFeriasCedidas", "GetAfastamentos")) else "CONFERIR")


def norm(value):
    if value is None:
        return None
    return datetime.fromisoformat(str(value)).replace(tzinfo=None).isoformat(timespec="seconds")


cases = []
for i, row in enumerate(occ, 1):
    start, end = row["DATAINICIOOCORRENCIA"], row["DATATERMINOOCORRENCIA"]
    aid = f"AFAST_O_0004_4_{row['OCORRENCIA']}_{(start-datetime(1899,12,30)).days}"
    api_match = [a for a in api_occ if a["ocorrencia"] == row["OCORRENCIA"]
                 and norm(a["dataInicioOcorrencia"]) == norm(start)]
    api_equal = len(api_match) == 1 and norm(api_match[0]["dataTerminoOcorrencia"]) == norm(end) \
        and api_match[0]["nroHorasOcorrecia"] == row["NROHORASOCORRENCIA"]
    target = [d for d in after["afastamentos"] if d["IdFreq"] == aid]
    exact = len(target) == 1 and norm(target[0]["DataInicio"]) == norm(start) \
        and norm(target[0]["DataTermino"]) == norm(end)
    status = "IMPORTADO_EXATO" if exact else ("NAO_IMPORTADO" if not target else "DIVERGENTE")
    case = dict(caso=f"O{i:02}", tipo=row["OCORRENCIA"], descricao=row["DESCRICAO40"],
                inicio=norm(start), termino=norm(end), horas=row["NROHORASOCORRENCIA"],
                gera_afastamento=row["GERAAFASTAMENTO"], gera_ponto=row["GERAAFASTAMENTOPONTO"],
                api_exata=api_equal, destino=status, id_destino=target[0]["Id"] if target else None)
    cases.append(case)
    event(f"Conferir {case['caso']} ocorrência {case['tipo']}",
          f"API preservar início={norm(start)}, término={norm(end)}, horas={row['NROHORASOCORRENCIA']}; "
          "conferir elegibilidade e correspondência no destino",
          f"API exata={api_equal}; destino={status}; gera afastamento={row['GERAAFASTAMENTO']}; "
          f"gera ponto={row['GERAAFASTAMENTOPONTO']}",
          status if api_equal else "DIVERGENCIA_API")
for i, row in enumerate(hol, 1):
    start, end = row["INICIOGOZOFERIAS"], row["TERMINOGOZOFERIAS"]
    aid = f"AFAST_F_0004_4_{(start-datetime(1899,12,30)).days}"
    matches = [a for a in api_hol if norm(a["inicioGozoFerias"]) == norm(start)]
    api_equal = len(matches) == 1 and norm(matches[0]["terminoGozoFerias"]) == norm(end)
    target = [d for d in after["afastamentos"] if d["IdFreq"] == aid]
    exact = len(target) == 1 and norm(target[0]["DataInicio"]) == norm(start) \
        and norm(target[0]["DataTermino"]) == norm(end)
    status = "IMPORTADO_EXATO" if exact else ("NAO_IMPORTADO" if not target else "DIVERGENTE")
    case = dict(caso=f"F{i:02}", inicio=norm(start), termino=norm(end),
                api_exata=api_equal, destino=status, id_destino=target[0]["Id"] if target else None)
    cases.append(case)
    event(f"Conferir {case['caso']} férias",
          f"Preservar período {norm(start)} até {norm(end)}",
          f"API exata={api_equal}; destino={status}",
          status if api_equal else "DIVERGENCIA_API")
for row in res:
    case = dict(caso=f"R{row['NROORDEM']:02}", inicio=norm(row["DATAINICIO"]),
                termino=norm(row["DATATERMINO"]), refeicao=row["REFEICAO"],
                tipo=row["TIPOREFEICAO"], api_exata=None, destino="BLOQUEADO_SEM_ROTA_API")
    cases.append(case)
    event("Conferir " + case["caso"] + " reserva/consumo",
          "API fornecer registro e importador persistir reserva com período/refeição corretos",
          f"Origem: {case['inicio']} até {case['termino']}, refeição {case['refeicao']}, "
          f"tipo {case['tipo']}; sem rota publicada; destino com {after['reservas_total']} reservas",
          "BLOQUEADO")
save("casos-conferidos.json", cases)
duplicates = [key for key, n in Counter(d["IdFreq"] for d in after["afastamentos"]).items() if n > 1]
event("Verificar chaves duplicadas da pessoa de teste", "Nenhum IdFreq repetido",
      f"{len(duplicates)} chaves repetidas", "PASSOU" if not duplicates else "FALHOU")
event("Encerrar conferência", "Relatório por caso e diário próprio disponíveis",
      f"{len(cases)} casos conferidos; registros não importados não são aprovação automática de regra.")
lines = ["# Conferência da importação pela API", "",
         f"Executado em {datetime.now().astimezone().isoformat()}.", "",
         "Diário próprio: [diario-testes.txt](diario-testes.txt). Eventos estruturados: "
         "[diario-testes.jsonl](diario-testes.jsonl).", "",
         "Os cadastros são anteriores a esta auditoria. Os horários do diário indicam quando "
         "cada conferência foi feita. O importador automático existente foi acompanhado; "
         "este script não grava diretamente no destino.", "",
         "| Caso | Tipo | Início | Término | API preservou dados | Acessus |",
         "|---|---|---|---|---|---|"]
for c in cases:
    lines.append(f"| {c['caso']} | {c.get('tipo','férias')} | {c['inicio']} | {c['termino']} | "
                 f"{c['api_exata']} | {c['destino']} |")
lines += ["", "## Limites da conclusão", "",
          "- Ausência no destino exige conferir regra de vigência e gera-afastamento. "
          "Não foi presumido que toda ocorrência futura ou apenas de ponto deva virar afastamento.",
          "- Reservas: não foi encontrada rota publicada no Swagger atual; importação API não comprovada.",
          "- Férias e reservas cadastradas têm datas, sem campo de horário nesse fluxo. "
          "Ocorrências incluem faixa horária, passagem de meia-noite e horas por dia.",
          "- O diagnóstico HTTPS usou exceção local de certificado; não alterou a configuração do importador.",
          "- Diário sem senha, token, CPF ou cópia do log bruto do sistema.", ""]
(OUT / "RELATORIO.md").write_text("\n".join(lines), encoding="utf-8")
print("RELATORIO=" + str(OUT.resolve()), flush=True)
