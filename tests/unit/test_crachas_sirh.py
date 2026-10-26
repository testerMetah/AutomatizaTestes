import pytest

from automatiza.crachas_sirh import classify, validate_plan


def plan():
    return {"versao": 1, "origem": "RHFagundes", "destino": "novo123",
            "casos": [
                {"unidade": "0004", "contrato": 2, "pessoa_origem": 2,
                 "pessoa_destino": 3, "novo_cracha": "991022002"},
                {"unidade": "0004", "contrato": 4, "pessoa_origem": 4,
                 "pessoa_destino": 5, "novo_cracha": "991022004"}]}


def test_plan_requires_unique_numeric_badges():
    assert validate_plan(plan())["casos"][0]["novo_cracha"] == "991022002"
    invalid = plan()
    invalid["casos"][1]["novo_cracha"] = "991022002"
    with pytest.raises(ValueError, match="duplicado"):
        validate_plan(invalid)


def test_classify_distinguishes_not_imported_from_wrong_person():
    case = plan()["casos"][0]
    assert classify(case, "991022002", "991022002", [])["status"] == "NAO_IMPORTADO"
    wrong = [{"Codigo": "991022002", "IdPessoa": 99, "excluido": "N"}]
    assert classify(case, "991022002", "991022002", wrong)["status"] == "DIVERGENTE_DESTINO"
    exact = [{"Codigo": "991022002", "IdPessoa": 3, "excluido": "N"}]
    assert classify(case, "991022002", "991022002", exact)["status"] == "IMPORTADO_EXATO"
