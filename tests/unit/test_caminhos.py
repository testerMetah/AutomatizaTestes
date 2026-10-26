from automatiza import caminhos


def test_raiz_sobrescrita(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTOMATIZA_RAIZ", str(tmp_path))
    assert caminhos.raiz() == tmp_path
    assert caminhos.logs_permanentes() == tmp_path / "saidas/logs-permanentes"
    pasta = caminhos.nova_rodada("Auditorias", "Refeitório")
    assert pasta.parent == tmp_path / "saidas/rodadas"
    assert pasta.name.startswith("20")
