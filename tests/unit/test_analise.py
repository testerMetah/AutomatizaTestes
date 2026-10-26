import csv
import hashlib
import json
import random
from datetime import datetime, timedelta, timezone
from zipfile import ZipFile

from automatiza.analise import analyze_session, data_alerts, export_bundle, history_integrity, journal, origin_reappearances, service_statistics
from automatiza.observador import changes


def stamp(seconds=0):
    return (datetime(2026, 10, 15, 12, tzinfo=timezone.utc) + timedelta(seconds=seconds)).isoformat()


def row(key=1, person=10, start="2026-11-01T00:00:00", end="2026-11-10T23:59:59", cause="Férias", origin="RH-1"):
    return {"Id": key, "IdPessoa": person, "DataInicio": start, "DataTermino": end, "Causa": cause, "IdFreq": origin}


def event(old, new, at=10, since=0):
    before = {old["Id"]: old} if old else {}
    after = {new["Id"]: new} if new else {}
    result = changes(before, after)[0]
    result.update(observado_em=stamp(at), desde=stamp(since))
    return result


def write_session(folder, initial, current, events, *, at=20, samples=(0, 10, 20)):
    folder.mkdir(parents=True, exist_ok=True)
    for name, value in {"inicial.json": {"instante": stamp(), "linhas": initial},
                        "atual.json": {"instante": stamp(at), "linhas": current},
                        "resumo.json": {"status": "OBSERVANDO", "falhas_coleta": 0}}.items():
        (folder / name).write_text(json.dumps(value), encoding="utf-8")
    (folder / "eventos.jsonl").write_text("".join(json.dumps(e) + "\n" for e in events), encoding="utf-8")
    (folder / "amostras.jsonl").write_text("".join(json.dumps({"instante": stamp(s)}) + "\n" for s in samples), encoding="utf-8")


def test_datas_repetidas_sobrepostas_e_invertidas_sao_alertas_distintos():
    rows = [row(), row(key=2, origin="RH-2"),
            row(key=3, person=11, start="2026-12-10", end="2026-12-01"),
            row(key=4, person=12, end=None, origin=None)]
    alerts = data_alerts(rows)
    kinds = {a["tipo"] for a in alerts}
    assert {"POSSIVEL_REPETICAO_DE_PERIODO_E_CAUSA", "SOBREPOSICAO_DE_PERIODOS", "PERIODO_INVERTIDO", "SEM_IDFREQ"} <= kinds
    assert not any(a["tipo"] == "DATA_AUSENTE_OU_INVALIDA" and a["ids"] == [4] for a in alerts)


def test_fim_aberto_sobrepoe_periodo_posterior_sem_inventar_data():
    alerts = data_alerts([row(end=None), row(key=2, start="2030-01-01", end="2030-01-03", origin="RH-2")])
    assert any(a["tipo"] == "SOBREPOSICAO_DE_PERIODOS" for a in alerts)


def test_data_zero_delphi_nao_e_chamada_de_periodo_invertido_comum():
    alerts = data_alerts([row(end="1899-12-30T00:00:00"), row(key=2, origin="RH-2")])
    assert any(a["tipo"] == "TERMINO_DATA_BASE_DELPHI" for a in alerts)
    assert not any(a["tipo"] in {"PERIODO_INVERTIDO", "SOBREPOSICAO_DE_PERIODOS"} for a in alerts)


def test_periodos_separados_e_pessoas_diferentes_nao_geram_sobreposicao():
    alerts = data_alerts([row(), row(key=2, person=11, origin="RH-2"),
                          row(key=3, start="2026-12-01", end="2026-12-10", origin="RH-3")])
    assert not any(a["tipo"] == "SOBREPOSICAO_DE_PERIODOS" for a in alerts)


def test_alertas_de_sobreposicao_sao_limitados():
    alerts = data_alerts([row(key=k, origin=str(k)) for k in range(20)], limit=10)
    assert alerts[-1]["tipo"] == "LIMITE_DE_ALERTAS"
    assert len(alerts) <= 11


def test_historico_reconstroi_estado_e_identifica_antes_incompativel():
    old, new = row(), row(end="2026-11-15T23:59:59")
    ev = event(old, new)
    assert history_integrity({1: old}, {1: new}, [ev]) == []
    assert history_integrity({}, {1: new}, [ev])[0]["tipo"] == "ESTADO_ANTERIOR_DIVERGENTE"


def test_eventos_futuros_e_linha_parcial_nao_entram_na_amostra_atual(tmp_path):
    write_session(tmp_path, [], [], [event(None, row(), at=30)], at=20)
    with (tmp_path / "eventos.jsonl").open("ab") as f:
        f.write(b'{"tipo":"linha-parcial')
    result = analyze_session(tmp_path)
    assert result["totais"]["INCLUIDO"] == 0
    assert result["problemas_historico"] == []


def test_relatorio_por_pessoa_preserva_antes_depois_e_csv_seguro(tmp_path):
    new = row(cause="=HYPERLINK(1)")
    write_session(tmp_path, [], [new], [event(None, new)])
    result = analyze_session(tmp_path)
    assert result["pessoas"][0]["id_pessoa"] == 10
    assert result["pessoas"][0]["eventos"][0]["depois"] == new
    assert result["problemas_historico"] == []
    with (tmp_path / "afastamentos-atuais.csv").open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f, delimiter=";"))
    assert rows[1][4].startswith("'=")


def test_html_escapa_legendas_e_nao_carrega_recursos_externos(tmp_path):
    new = row(cause='<img src=x onerror="alert(1)">')
    write_session(tmp_path, [], [new], [event(None, new)])
    analyze_session(tmp_path)
    html = (tmp_path / "analise.html").read_text(encoding="utf-8")
    assert "<img src=x" not in html
    assert "&lt;img" in html
    assert "https://" not in html


def test_base_da_sessao_aparece_na_analise_e_no_pacote(tmp_path):
    session = tmp_path / 'sessao'
    write_session(session, [], [], [])
    state_file = session / 'resumo.json'
    state = json.loads(state_file.read_text(encoding='utf-8'))
    state.update(banco='teste-ferias', servidor='servidor-teste')
    state_file.write_text(json.dumps(state), encoding='utf-8')
    result = analyze_session(session)
    assert result['banco'] == 'teste-ferias'
    assert 'Base teste-ferias' in (session / 'analise.html').read_text(encoding='utf-8')
    bundle = export_bundle(session, tmp_path / 'pacotes')
    with ZipFile(bundle) as zipped:
        assert 'SQL teste-ferias' in zipped.read('LEIA-ME.txt').decode('utf-8')
        assert json.loads(zipped.read('analise.json'))['servidor'] == 'servidor-teste'


def test_troca_de_pessoa_aparece_nos_dois_historicos(tmp_path):
    old, new = row(), row(person=11)
    write_session(tmp_path, [old], [new], [event(old, new)])
    result = analyze_session(tmp_path)
    assert {p["id_pessoa"] for p in result["pessoas"]} == {10, 11}
    assert all(len(p["eventos"]) == 1 for p in result["pessoas"])
    assert result["totais"]["ALTERADO"] == 1


def test_mesmo_idfreq_reaparece_sem_confundir_com_outro_cadastro():
    events = [event(row(), None), event(None, row(key=2), at=20, since=10),
              event(row(key=3, origin="RH-3"), None, at=30, since=20),
              event(None, row(key=4, origin="RH-4"), at=40, since=30)]
    result = origin_reappearances(events)
    assert len(result) == 1
    assert (result[0]["id_anterior"], result[0]["id_posterior"]) == (1, 2)


def test_linha_completa_corrompida_e_informada(tmp_path):
    file = tmp_path / "eventos.jsonl"
    file.write_bytes(b"not-json\n")
    values, issues = journal(file)
    assert values == []
    assert issues[0]["linha"] == 1


def test_replay_resiste_a_sequencias_mistas_de_varias_pessoas():
    rng = random.Random(42)
    initial = {key: row(key=key, person=10 + key % 3, origin=str(key)) for key in range(1, 10)}
    current, history, next_id = dict(initial), [], 10
    for second in range(1, 251):
        before = dict(current)
        operation = rng.choice(["incluir", "alterar", "excluir"])
        if operation == "incluir" or not current:
            current[next_id] = row(key=next_id, person=rng.randrange(10, 13), origin=str(next_id))
            next_id += 1
        elif operation == "excluir":
            current.pop(rng.choice(list(current)))
        else:
            key = rng.choice(list(current))
            current[key] = {**current[key], "Causa": "Alterada " + str(second)}
        for ev in changes(before, current):
            ev.update(observado_em=stamp(second), desde=stamp(second - 1))
            history.append(ev)
    assert history_integrity(initial, current, history) == []


def test_reaparecimento_na_mesma_amostra_funciona_com_id_menor():
    old, new = row(key=30), row(key=2)
    result = origin_reappearances([event(None, new), event(old, None)])
    assert len(result) == 1
    assert result[0]["mesmos_dados_exceto_id"] is True
    changed = row(key=2, end="2026-11-20")
    result = origin_reappearances([event(None, changed), event(old, None)])
    assert result[0]["campos_diferentes"] == ["DataTermino"]


def test_estatisticas_servicos_preservam_estado_desconhecido():
    result = service_statistics([{"instante": stamp(n), "servicos": [{"nome": "api", "estado": state}]}
                                 for n, state in enumerate(["EXECUTANDO", "PARADO", "INDISPONIVEL"])])
    assert result[0]["amostras"] == 3
    assert result[0]["estados"] == {"EXECUTANDO": 1, "PARADO": 1, "INDISPONIVEL": 1}


def test_pacote_de_evidencias_e_coerente_verificavel_e_nao_inclui_env(tmp_path):
    session = tmp_path / "sessao"
    write_session(session, [], [row()], [event(None, row())])
    (session / ".env").write_text("SQL_PASSWORD=segredo-nao-exportar", encoding="utf-8")
    bundle_path = export_bundle(session, tmp_path / "pacotes")
    with ZipFile(bundle_path) as bundle:
        assert ".env" not in bundle.namelist()
        manifest = json.loads(bundle.read("manifesto.json"))
        for name, digest in manifest["sha256"].items():
            assert hashlib.sha256(bundle.read(name)).hexdigest() == digest
        assert all(b"segredo-nao-exportar" not in bundle.read(name) for name in bundle.namelist())
        frozen = json.loads(bundle.read("analise.json"))
        assert frozen["estado_coleta"] == "PACOTE_CONGELADO"
        assert b'href="relatorio.html"' not in bundle.read("analise.html")
        destination = tmp_path / "replay"
        bundle.extractall(destination)
    replayed = analyze_session(destination)
    assert replayed["problemas_historico"] == []
    assert replayed["totais"] == frozen["totais"]
