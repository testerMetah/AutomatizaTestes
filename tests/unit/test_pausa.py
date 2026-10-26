import json
import os
import threading
import time

import pytest

from automatiza.pausa import RelogioAtivo, TesteCancelado, gravar, ponto, tecla_reservada
from automatiza.sentinela.runtime import Antirrepique, escolher_atalho, _arvore_do_teste


def test_congelamento_inclui_supervisor_e_exclui_sentinela():
    pairs = [(10, 1), (20, 10), (30, 10), (40, 20), (50, 30)]
    assert set(_arvore_do_teste(10, pairs, {30}, 30)) == {10, 20, 40}


def test_atribuicao_de_atalho_alternativo():
    chamadas = []
    def registrar(mods, key):
        chamadas.append((mods, key))
        return len(chamadas) == 2
    assert escolher_atalho(registrar, ["Pause", "Ctrl+Shift+F9"]) == "Ctrl+Shift+F9"


def test_antirrepique():
    repeticao = Antirrepique()
    assert repeticao.aceitar(1.0)
    assert not repeticao.aceitar(1.2)
    assert repeticao.aceitar(1.41)


def test_ponto_bloqueia_e_retorna(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTOMATIZA_PAUSA_DIR", str(tmp_path))
    gravar(tmp_path / "controle.json", {"estado": "PAUSADO", "instante": time.time()})
    gravar(tmp_path / "heartbeat.json", {"instante": time.time()})
    terminou = threading.Event()
    thread = threading.Thread(target=lambda: (ponto(), terminou.set()))
    thread.start()
    assert not terminou.wait(0.12)
    gravar(tmp_path / "controle.json", {"estado": "RODANDO", "instante": time.time()})
    assert terminou.wait(0.5)
    thread.join()


def test_cancelamento_no_ponto(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTOMATIZA_PAUSA_DIR", str(tmp_path))
    gravar(tmp_path / "controle.json", {"estado": "CANCELANDO"})
    with pytest.raises(TesteCancelado):
        ponto()


def test_relogio_desconta_pausa():
    clock = RelogioAtivo()
    clock.sincronizar(True)
    time.sleep(0.06)
    assert clock.decorrido() < 0.04
    clock.sincronizar(False)
    time.sleep(0.02)
    assert clock.decorrido() >= 0.01


def test_gateway_recusa_atalho_de_pausa():
    assert tecla_reservada("{PAUSE}")
    assert tecla_reservada("^+{F9}")
    assert tecla_reservada("^+P")
    assert not tecla_reservada("{F6}")


def test_cancelado_no_relatorio(tmp_path):
    from automatiza.relatorio_auditorias import gerar
    folder = tmp_path / "rodada"
    (folder / "refeitorio").mkdir(parents=True)
    (folder / "refeitorio/tentativas.jsonl").write_text(
        json.dumps({"modulo": "refeitorio", "historico": "Fila/Comandos",
                    "filtro": "Pessoa", "status": "CANCELADO"}) + "\n", encoding="utf-8")
    gerar(folder)
    resumo = json.loads((folder / "resumo.json").read_text(encoding="utf-8"))
    assert resumo["cancelada_pelo_usuario"]
    assert resumo["modulos"]["refeitorio"]["CANCELADO"] == 1


def test_eventos_de_pausa_no_diario(monkeypatch, tmp_path):
    monkeypatch.delenv("AUTOMATIZA_PAUSA_DIR", raising=False)
    from automatiza.diario_auditorias import DiarioAuditorias
    with DiarioAuditorias(tmp_path, {"modulo": "teste"}) as diary:
        diary.acao("teste", "(pausa)", "(pausa)", "PAUSA_INICIADA")
    assert "PAUSA_INICIADA" in (tmp_path / "passo-a-passo.log").read_text(encoding="utf-8")
