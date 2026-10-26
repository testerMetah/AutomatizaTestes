"""Observa uma importação já provocada no RH; não altera registros nem serviços."""

import json
import math
import time
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from uuid import uuid4


def load_case(path, case_id):
    path = Path(path).resolve()
    config = json.loads(path.read_text(encoding="utf-8-sig"))
    if config.get("preparado") is not True:
        raise ValueError("Configure as consultas e os resultados esperados; depois marque preparado=true.")
    cases = config.get("casos", [])
    matches = [case for case in cases if case.get("id") == case_id]
    if len(matches) != 1:
        raise ValueError("O identificador deve corresponder a exatamente um caso.")
    case = dict(matches[0])
    if case.get("preparado", True) is not True:
        raise ValueError("Este caso ainda não está preparado. Configure os dados e marque preparado=true no caso escolhido.")
    for field in ("descricao", "acao_origem", "pessoa"):
        value = case.get(field)
        if value is None or not str(value).strip() or "PREENCHER" in str(value).upper():
            raise ValueError(f"Informe {field} no caso.")
    if "id_pessoa" in case and (type(case["id_pessoa"]) is not int or case["id_pessoa"] <= 0):
        raise ValueError("id_pessoa deve ser o identificador interno positivo no Acessus.")
    for field, default in (("timeout_segundos", 180), ("intervalo_segundos", 5),
                           ("estabilidade_segundos", 10)):
        value = case.get(field, config.get(field, default))
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError(f"{field} precisa ser um número positivo finito.")
        case[field] = value
    if case["estabilidade_segundos"] >= case["timeout_segundos"]:
        raise ValueError("A estabilidade precisa ser menor que o tempo limite.")
    checks = case.get("verificacoes", [])
    if not checks:
        raise ValueError("O caso precisa de verificações SQL.")
    names = set()
    for check in checks:
        name = check.get("nome", "")
        if not name or name in names:
            raise ValueError("Cada verificação precisa de um nome único.")
        names.add(name)
        expected = check.get("quantidade_esperada")
        if type(expected) is not int or expected < 0:
            raise ValueError("quantidade_esperada precisa ser um inteiro não negativo.")
        check.setdefault("modo", "convergencia")
        if check["modo"] not in {"convergencia", "na_janela"}:
            raise ValueError("modo precisa ser convergencia ou na_janela.")
        if check["modo"] == "na_janela" and expected != 0:
            raise ValueError("na_janela é reservado para ausência esperada (zero registros).")
        if not isinstance(check.get("parametros", []), list):
            raise ValueError("parametros precisa ser uma lista JSON.")
        resolved = []
        for value in check.get("parametros", []):
            if isinstance(value, dict):
                if (set(value) != {"campo_caso"} or not isinstance(value["campo_caso"], str)
                        or value["campo_caso"] not in case):
                    raise ValueError("Referência campo_caso inválida ou ausente no caso.")
                value = case[value["campo_caso"]]
                if isinstance(value, (dict, list)):
                    raise ValueError("campo_caso deve referenciar um valor simples.")
            resolved.append(value)
        check["parametros"] = resolved
        if any(isinstance(value, str) and "PREENCHER" in value.upper() for value in check.get("parametros", [])):
            raise ValueError("Substitua os parâmetros PREENCHER antes de executar o caso.")
        query_path = (path.parent / check["arquivo_sql"]).resolve()
        check["sql"] = query_path.read_text(encoding="utf-8-sig")
        if not check["sql"].strip():
            raise ValueError("A consulta SQL não pode estar vazia.")
    return case


def write_report(directory, result):
    """Regrava o resumo após cada observação; JSONL conserva as amostras anteriores."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    json_path = directory / "resultado.json"
    temp = directory / "resultado.tmp"
    temp.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(json_path)
    rows = "".join(
        "<tr>" + "".join(f"<td>{escape(str(sample.get(key, '')))}</td>" for key in
                         ("instante", "decorrido_segundos", "verificacao", "esperado", "observado", "corresponde")) + "</tr>"
        for sample in result["amostras"]
    )
    body = (
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Importação RH → Acessus</title>'
        '<style>body{font:16px sans-serif;margin:32px}table{border-collapse:collapse}th,td{border:1px solid #bbb;padding:8px}</style>'
        f"<h1>Importação RH → Acessus: {escape(result['status'])}</h1>"
        f"<p>Caso: {escape(str(result['caso']))} — {escape(result['descricao'])}</p>"
        f"<p>Pessoa: {escape(str(result['pessoa']))}. IdPessoa: {escape(str(result.get('id_pessoa', 'não informado')))}. "
        f"Ação informada na origem: {escape(result['acao_origem'])}.</p>"
        f"<p>{escape(result['conclusao'])}</p>"
        "<p>Este acompanhamento começa depois da ação no RH. Ele não executa nem comprova essa ação. "
        "Ausência no banco significa ausência nas consultas e no intervalo observado, não comprova que o serviço processou o evento. "
        "O tempo contado é desde o início do acompanhamento.</p>"
        "<table><tr><th>Instante UTC</th><th>Segundos</th><th>Verificação</th><th>Esperado</th><th>Observado</th><th>Corresponde</th></tr>"
        + rows + "</table></html>"
    )
    (directory / "relatorio.html").write_text(body, encoding="utf-8")


def monitor(db, case, output, *, clock=time.monotonic, sleep=time.sleep):
    """Convergência aguarda o estado esperado; na_janela amostra ausências até o limite.

    Convergência em zero permite observar exclusões que demoram a propagar.
    Na_janela reprova qualquer presença amostrada, mesmo que depois desapareça.
    """
    directory = Path(output) / (datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:8])
    checks = case["verificacoes"]
    result = {"caso": case["id"], "descricao": case["descricao"], "pessoa": case["pessoa"],
              "acao_origem": case["acao_origem"], "status": "EM ANDAMENTO", "amostras": [],
              "conclusao": "Aguardando as verificações SQL.", "report": str(directory / "relatorio.html")}
    result["configuracao"] = {key: case[key] for key in
                              ("timeout_segundos", "intervalo_segundos", "estabilidade_segundos")}
    if "id_pessoa" in case:
        result["id_pessoa"] = case["id_pessoa"]
    result["verificacoes"] = [{"nome": check["nome"], "quantidade_esperada": check["quantidade_esperada"],
                                "modo": check.get("modo", "convergencia")}
                               for check in checks]
    start = clock()
    stable_since = None
    zero_violation = False
    has_absence = any(check.get("modo") == "na_janela" for check in checks)
    write_report(directory, result)
    try:
        while True:
            all_match = True
            for check in checks:
                value = db.scalar(check["sql"], tuple(check.get("parametros", [])))
                # COUNT(*) retorna inteiro. Não aceitar NULL, texto ou booleanos como contagem.
                if type(value) is not int or value < 0:
                    raise ValueError("A consulta deve retornar uma única contagem inteira não negativa (COUNT(*)).")
                expected = check["quantidade_esperada"]
                match = value == expected
                all_match = all_match and match
                if check.get("modo") == "na_janela" and not match:
                    zero_violation = True
                sample = {"instante": datetime.now(timezone.utc).isoformat(),
                          "decorrido_segundos": round(clock() - start, 3), "verificacao": check["nome"],
                          "esperado": expected, "observado": value, "corresponde": match}
                result["amostras"].append(sample)
                with (directory / "amostras.jsonl").open("a", encoding="utf-8") as journal:
                    journal.write(json.dumps(sample, ensure_ascii=False) + "\n")
                write_report(directory, result)
            now = clock()
            if all_match:
                if stable_since is None:
                    stable_since = now
            else:
                stable_since = None
            stable = stable_since is not None and now - stable_since >= case["estabilidade_segundos"]
            deadline = now - start >= case["timeout_segundos"]
            if not has_absence and stable:
                result.update(status="PASSOU", conclusao="Todas as contagens corresponderam nas amostras do período de estabilidade.")
                break
            if deadline:
                passed = stable and not zero_violation
                result.update(status="PASSOU" if passed else "FALHOU",
                              conclusao=("Contagens estáveis nas amostras finais; nenhuma presença encontrada nas amostras de ausência na janela."
                                         if passed else "As verificações não cumpriram o resultado esperado na janela observada."))
                break
            sleep(min(case["intervalo_segundos"], case["timeout_segundos"] - (now - start)))
    except KeyboardInterrupt:
        result.update(status="INTERROMPIDO", conclusao="Acompanhamento interrompido; evidências anteriores preservadas.")
    except Exception as exc:
        # Não persistir mensagens ODBC: podem conter SQL, servidor e credenciais.
        result.update(status="ERRO", conclusao=f"Erro ao consultar/registrar evidência ({type(exc).__name__}); não é um resultado de negócio.")
    write_report(directory, result)
    return result
