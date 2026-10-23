from automatiza.sequencias.engine import generate, reduce_failure
from automatiza.sequencias.relatorio import mask
from automatiza.sequencias.verificar import compare_fields


def test_seed_reproduz_passos_e_limita_volume():
    first = generate(42, count=20, max_mass=3)
    assert first == generate(42, count=20, max_mass=3)
    assert all(s["quantidade"] <= 3 for s in first["passos"])


def test_reducao_isola_falha_com_replay_descartavel():
    case = {"nome": "erro", "seed": 3, "passos": [{"acao": str(i)} for i in range(8)]}
    reduced = reduce_failure(case, lambda steps: any(s["acao"] == "5" for s in steps))
    assert reduced["passos"] == [{"acao": "5"}]


def test_mascara_e_comparacao_campo_a_campo():
    assert mask({"senha": "segredo", "nome": "AUTOTEST_1"}) == {"senha": "****", "nome": "AUTOTEST_1"}
    assert compare_fields({"codigo": "A"}, {"codigo": "B"}) == [{"campo": "codigo", "esperado": "A", "obtido": "B", "igual": False}]
