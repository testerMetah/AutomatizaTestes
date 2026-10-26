import json

from automatiza.diario_auditorias import DiarioAuditorias


def test_diarios_centrais_acrescentam_acoes_e_tentativas_sem_apagar(tmp_path):
    for numero in (1, 2):
        with DiarioAuditorias(tmp_path, {"banco_sql_confirmado": "TESTE"}) as diario:
            registro = {"inicio": "2026-10-26T10:00:00-03:00", "status": "CONSULTADO",
                        "valor_planejado": str(numero), "periodo": ["26/10/2026", "10:00"]}
            diario.iniciar_tentativa(registro)
            diario.acao("acesso", "Pessoas", "Pessoa", f"Preencheu com: {numero}")
            diario.finalizar_tentativa(registro)

    linhas = (tmp_path / "passo-a-passo.log").read_text(encoding="utf-8").splitlines()
    eventos = [json.loads(linha) for linha in
              (tmp_path / "passo-a-passo-detalhado.jsonl").read_text(encoding="utf-8").splitlines()]
    acoes = [evento for evento in eventos if evento["tipo"] == "acao"]
    tentativas = [evento for evento in eventos if evento["tipo"] == "tentativa_finalizada"]

    assert len(linhas) == len(acoes) == len(tentativas) == 2
    assert [evento["linha_passo_a_passo"] for evento in acoes] == linhas
    assert acoes[0]["execucao_id"] != acoes[1]["execucao_id"]
    assert [evento["registro_completo"]["valor_planejado"] for evento in tentativas] == ["1", "2"]
    assert all(evento["registro_completo"]["duracao_ms"] >= 0 for evento in tentativas)
    assert len([evento for evento in eventos if evento["tipo"] == "fim_execucao"]) == 2
