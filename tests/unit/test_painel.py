import json
import threading
import urllib.request

from automatiza.painel import _comando, criar_servidor


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
    finally:
        server.shutdown()
        server.server_close()
