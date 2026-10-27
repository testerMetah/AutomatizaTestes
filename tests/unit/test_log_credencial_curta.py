from automatiza.log import mascarar


def test_senha_curta_nao_corrompe_datas_e_mascara_campo(monkeypatch):
    monkeypatch.setenv("TESTE_SENHA", "1")
    assert mascarar("2026-10-27T08:49:42-03:00") == "2026-10-27T08:49:42-03:00"
    assert mascarar({"senha": "1", "inicio": "2026-10-27"}) == {
        "senha": "[oculto]", "inicio": "2026-10-27"}
    assert mascarar("senha=1") == "senha=[oculto]"
