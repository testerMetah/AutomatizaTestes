import json
import threading
import urllib.request

from automatiza.painel import _comando, criar_servidor


def test_resultados_incluem_rodadas_novas(monkeypatch, tmp_path):
    import automatiza.painel as painel
    monkeypatch.setattr(painel, "ROOT", tmp_path)
    monkeypatch.setattr(painel, "ROOTS", (tmp_path / "saidas" / "rodadas",))
    rodada = tmp_path / "saidas" / "rodadas" / "20261027-auditorias-acesso"
    rodada.mkdir(parents=True)
    (rodada / "RELATORIO.html").write_text("relatorio", encoding="utf-8")
    rows = painel._rodadas()
    assert rows[0]["pasta"] == "saidas/rodadas/20261027-auditorias-acesso"
    assert rows[0]["relatorio"] == "saidas/rodadas/20261027-auditorias-acesso/RELATORIO.html"


def test_comando_ciclos_escrita_exige_confirmacao():
    try:
        _comando({"tipo": "ciclos", "acao": "executar", "arquivo": "x", "saida": "y"})
    except ValueError as exc:
        assert "Confirmação" in str(exc)
    else:
        raise AssertionError("Escrita sem confirmação não foi bloqueada")


def test_rotas_basicas_do_painel():
    server = criar_servidor(0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    try:
        page = urllib.request.urlopen(base + "/", timeout=10).read().decode("utf-8")
        assert "Painel de Testes" in page
        token = page.split("const TOKEN='", 1)[1].split("'", 1)[0]
        request = urllib.request.Request(base + "/api/catalogo", headers={"X-Painel-Token": token})
        commands = json.load(urllib.request.urlopen(request, timeout=10))
        assert any(x["comando"] == "auditorias" for x in commands)
        request = urllib.request.Request(base + "/api/resultados", headers={"X-Painel-Token": token})
        assert isinstance(json.load(urllib.request.urlopen(request, timeout=10)), list)
        request = urllib.request.Request(base + "/api/ajuda", headers={"X-Painel-Token": token})
        ajuda = json.load(urllib.request.urlopen(request, timeout=10))
        assert "auditorias.extremo" in ajuda["ajudas"]
        assert len(ajuda["catalogo"]) >= 25
        request = urllib.request.Request(base + "/api/banco?perfil=auditorias", headers={"X-Painel-Token": token})
        from unittest.mock import patch
        with patch("automatiza.database.SqlServer.assert_database", return_value="AcessoFagundes"):
            banco = json.load(urllib.request.urlopen(request, timeout=10))
        assert banco["banco"] == "AcessoFagundes"
    finally:
        server.shutdown()
        server.server_close()
