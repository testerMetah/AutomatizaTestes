import json

import pytest

from automatiza.explorador import Explorer, Journal, build_sequences, spread_actions, validate_config
from automatiza.explorador_cli import generate
from automatiza.explorador_windows import WindowsExplorerBackend
from automatiza.explorador_relatorio import write_report


def configuration():
    return {
        "versao": 1, "semente": 3,
        "rotas": [{"modulo": "acesso", "menu": ["Cadastros", "Pessoas..."]}],
        "valores": {"texto": ["TESTE"], "combo": []},
        "politica": {"permitir_gravacao": False},
        "limites": {"max_acoes_por_tela": 5, "max_sequencias_por_tela": 20,
                    "sequencias_aleatorias": 4, "comprimento_aleatorio": 3},
    }


def test_sequences_cover_singles_and_both_orders():
    actions = [{"id": "a"}, {"id": "b"}, {"id": "c"}]
    limits = validate_config(configuration())["limites"]
    sequences = build_sequences(actions, seed=7, limits=limits)
    assert ["a"] in sequences and ["b"] in sequences and ["c"] in sequences
    assert ["a", "b"] in sequences and ["b", "a"] in sequences
    assert sequences == build_sequences(actions, seed=7, limits=limits)
    assert len(sequences) <= limits["max_sequencias_por_tela"]


def test_action_limit_spreads_across_controls():
    actions = [
        {"id": f"field-a:{i}", "controle": {"classe": "TEdit", "posicao": [1, 1]}}
        for i in range(3)
    ] + [{"id": "field-b:0", "controle": {"classe": "TEdit", "posicao": [2, 2]}}]
    assert [action["id"] for action in spread_actions(actions, 2)] == ["field-a:0", "field-b:0"]


class FakeBackend:
    def __init__(self, fail=None):
        self.events = []
        self.fail = fail
        self.skipped = [{"motivo": "botão não autorizado"}]

    def open(self, route):
        self.events.append("open")

    def discover(self, config):
        return [{"id": "fill", "tipo": "preencher", "controle": {"classe": "TEdit"},
                 "valor": "TESTE"},
                {"id": "click", "tipo": "clicar", "controle": {"classe": "TBitBtn"}}]

    def perform(self, action):
        self.events.append(action["id"])
        if action["id"] == self.fail:
            raise RuntimeError("falha de tela")
        return {"janela": "Pessoas"}

    def reset(self):
        self.events.append("reset")

    def capture(self, path):
        path.write_bytes(b"fake")


def test_runner_logs_every_attempt_and_error_then_resets(tmp_path):
    backend = FakeBackend(fail="click")
    state = Explorer(configuration(), backend, tmp_path).run()
    rows = [json.loads(line) for line in (tmp_path / "passos.jsonl").read_text(encoding="utf-8").splitlines()]
    assert state["status"] == "CONCLUIDO_COM_ERROS"
    assert any(r["resultado"] == "ANTES" and r["acao"]["valor"] == "TESTE" for r in rows)
    assert any(r["resultado"] == "ERRO" and "falha de tela" in r["erro"] for r in rows)
    assert "valor=TESTE" in (tmp_path / "passos.log").read_text(encoding="utf-8")
    assert backend.events.count("reset") == len(state["concluidas"]) + 1


def test_sequence_open_failure_skips_route_and_continues(tmp_path):
    class FailingOpen(FakeBackend):
        def open(self, route):
            super().open(route)
            if route["menu"][-1] == "Pessoas..." and self.events.count("open") == 2:
                raise RuntimeError("menu temporariamente indisponivel")

    config = configuration()
    config["rotas"].append({"modulo": "acesso", "menu": ["Cadastros", "Empresas..."]})
    backend = FailingOpen()
    state = Explorer(config, backend, tmp_path).run()
    rows = [json.loads(line) for line in (tmp_path / "passos.jsonl").read_text(encoding="utf-8").splitlines()]
    assert state["status"] == "CONCLUIDO_COM_ERROS"
    assert state["erros"] == 1
    assert any(row["resultado"] == "ERRO_ABERTURA_SEQUENCIA" for row in rows)
    assert all(not key.startswith("0:") for key in state["concluidas"])
    assert any(key.startswith("1:") for key in state["concluidas"])


def test_resume_does_not_repeat_completed_sequences(tmp_path):
    first = FakeBackend()
    state = Explorer(configuration(), first, tmp_path).run()
    second = FakeBackend()
    again = Explorer(configuration(), second, tmp_path).run()
    assert again["concluidas"] == state["concluidas"]
    assert not any(event in {"fill", "click"} for event in second.events)


def test_pending_action_requires_reconciliation(tmp_path):
    config = validate_config(configuration())
    journal = Journal(tmp_path, config)
    journal.state["pendente"] = {"acao": "click"}
    journal.save()
    with pytest.raises(RuntimeError, match="pendente"):
        Explorer(config, FakeBackend(), tmp_path)


def test_mutations_need_explicit_disposable_base():
    config = configuration()
    config["politica"]["permitir_gravacao"] = True
    with pytest.raises(ValueError, match="base_descartavel"):
        validate_config(config)


def test_generator_produces_screen_routes_without_immediate_actions():
    from automatiza.explorador_cli import CATALOG
    config = generate(CATALOG, include_pending=True)
    assert len(config["rotas"]) > 30
    assert all(route["menu"][-1].endswith("...") or route["modulo"] == "administracao"
               for route in config["rotas"])
    assert all("Sair" not in route["menu"] for route in config["rotas"])
    assert {route["modulo"] for route in config["rotas"]} == {
        "acesso", "refeitorio", "portaria", "estacionamento", "escola", "administracao"}


def test_button_policy_does_not_click_save_by_default():
    config = validate_config(configuration())
    backend = WindowsExplorerBackend(config)
    save = {"legenda": "Salvar", "classe": "TBitBtn", "id_controle": 1}
    cancel = {"legenda": "Cancelar", "classe": "TBitBtn", "id_controle": 2}
    assert not backend._button_allowed(save, config)
    assert backend._button_allowed(cancel, config)
    config["politica"].update(permitir_gravacao=True, base_descartavel_confirmada=True,
                              botoes_autorizados=["Salvar"])
    assert backend._button_allowed(save, config)


def test_password_label_never_gets_test_values():
    config = validate_config(configuration())
    backend = WindowsExplorerBackend(config)
    field = {"legenda": "", "rotulo": "Senha", "classe": "TEdit", "id_controle": 4}
    assert backend._values_for(field, config) == []


def test_validation_checks_actual_control_state():
    class Field:
        def __init__(self, value, state=0, name="TEdit"):
            self.value, self.state, self.name = value, state, name

        def window_text(self):
            return self.value

        def get_check_state(self):
            return self.state

        def class_name(self):
            return self.name

    backend = WindowsExplorerBackend(validate_config(configuration()))
    assert backend._validate_control({"tipo": "preencher", "valor": "TESTE"},
                                     Field("TESTE"), None)["status"] == "APROVADO"
    failure = backend._validate_control({"tipo": "preencher", "valor": "TESTE"},
                                        Field("OUTRO"), None)
    assert failure == {"status": "FALHOU", "esperado": "TESTE", "observado": "OUTRO"}
    assert backend._validate_control({"tipo": "alternar"},
                                     Field("", 1, "TCheckBox"), 0)["status"] == "APROVADO"


def test_runner_marks_mismatched_result_as_failure(tmp_path):
    class InvalidResult(FakeBackend):
        def perform(self, action):
            super().perform(action)
            return {"validacao": {"status": "FALHOU", "esperado": "TESTE", "observado": "OUTRO"}}

    state = Explorer(configuration(), InvalidResult(), tmp_path).run()
    rows = [json.loads(line) for line in (tmp_path / "passos.jsonl").read_text(encoding="utf-8").splitlines()]
    assert state["status"] == "CONCLUIDO_COM_ERROS"
    assert any(row["resultado"] == "VALIDACAO_FALHOU" for row in rows)
    assert not any(row["resultado"] == "VALIDACAO_APROVADO" for row in rows)


def test_report_keeps_unopened_routes_visible(tmp_path):
    config = configuration()
    config["rotas"].append({"modulo": "acesso", "menu": ["Cadastros", "Empresas..."]})
    (tmp_path / "passos.jsonl").write_text(
        json.dumps({"rota": "acesso:Cadastros > Pessoas...", "resultado": "INVENTARIO"}) + "\n"
        + json.dumps({"rota": "acesso:Cadastros > Pessoas...", "resultado": "VALIDACAO_APROVADO"}) + "\n",
        encoding="utf-8")
    summary = write_report(config, tmp_path)
    assert summary["rotas_planejadas"] == 2
    assert summary["rotas_abertas"] == 1
    assert summary["validacoes_aprovadas"] == 1
    assert summary["rotas"][1]["abertura"] is False
