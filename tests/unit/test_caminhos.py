from automatiza import caminhos


def test_raiz_sobrescrita(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTOMATIZA_RAIZ", str(tmp_path))
    assert caminhos.raiz() == tmp_path
    assert caminhos.logs_permanentes() == tmp_path / "saidas/logs-permanentes"
    pasta = caminhos.nova_rodada("Auditorias", "Refeitório")
    assert pasta.parent == tmp_path / "saidas/rodadas"
    assert pasta.name.startswith("20")


def test_manifesto_indice_e_migracao(monkeypatch, tmp_path):
    from automatiza.organizacao import iniciar, finalizar, indice
    from automatiza.manutencao_saidas import organizar, digest, verificar
    monkeypatch.setenv("AUTOMATIZA_RAIZ", str(tmp_path))
    old = tmp_path / "resultados/auditorias-20261026-123000"
    old.mkdir(parents=True)
    (old / "tentativas.jsonl").write_text('{"status":"CONSULTADO"}\n', encoding="utf-8")
    hash_antigo = digest(old / "tentativas.jsonl")
    assert len(organizar()) == 1
    assert old.exists()
    organizar(aplicar=True)
    assert not old.exists()
    assert digest(tmp_path / "saidas/arquivo-legado/resultados" / old.name / "tentativas.jsonl") == hash_antigo
    assert len(organizar()) == 0
    assert len(indice()) == 1
    assert not verificar()
    folder = caminhos.nova_rodada("auditorias", "refeitorio")
    manifest = iniciar(folder, "auditorias", "refeitorio", banco_efetivo="BancoTeste")
    assert set(manifest) >= {"id", "estado_final", "links_relativos", "pausas"}
    finalizar(folder, "CONCLUIDO", {"CONSULTADO": 1})
    assert len(indice()) == 2


def test_verificar_detecta_rodada_sem_manifesto(monkeypatch, tmp_path):
    from automatiza.manutencao_saidas import verificar
    monkeypatch.setenv("AUTOMATIZA_RAIZ", str(tmp_path))
    (tmp_path / "saidas/rodadas/incompleta").mkdir(parents=True)
    assert any("sem manifesto" in erro for erro in verificar())
