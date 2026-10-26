import copy
import json
import sys
from contextlib import nullcontext

import pytest

from automatiza.ciclos import Blocked, Runner, plan


@pytest.fixture
def config():
    return {"versao": 1, "casos": [
        {"id": "a", "tipo": "ferias", "presente": True,
         "inicio": "2026-12-31T00:00:00", "termino": "2027-01-14T00:00:00",
         "termino_alterado": "2027-01-15T00:00:00"},
        {"id": "b", "tipo": "ocorrencia", "presente": False,
         "inicio": "2026-10-20T00:00:00", "termino": "2026-10-22T00:00:00",
         "termino_alterado": "2026-10-23T00:00:00"}]}


class Backend:
    def __init__(self, config):
        self.rows = {c["id"]: c["termino"] if c["presente"] else None for c in config["casos"]}
        self.mutations = []
        self.observations = []
        self.crash = False
        self.fail_import = False
        self.block = False

    def preflight(self):
        pass

    def available(self, case):
        if self.block:
            raise Blocked("Endpoint indisponível")

    def source(self, case):
        return self.rows[case["id"]]

    def mutate(self, case, action, end, directory, step):
        self.mutations.append((case["id"], action, end))
        self.rows[case["id"]] = end
        if self.crash:
            self.crash = False
            raise RuntimeError("Processo interrompido depois da gravação")

    def observe(self, case, end, directory, emit):
        self.observations.append((case["id"], end))
        emit(end, self.source(case))
        return {"status": "FALHOU_TEXTO" if self.fail_import else "PASSOU"}


def test_seed_replay_and_different_orders(config):
    assert plan(config, 11, 3) == plan(config, 11, 3)
    assert plan(config, 11, 3)["etapas"] != plan(config, 12, 3)["etapas"]


@pytest.mark.parametrize("seed", range(20))
def test_all_sequences_obey_state_and_restore(config, seed):
    p = plan(config, seed, 3)
    state = {c["id"]: c["termino"] if c["presente"] else None for c in config["casos"]}
    for s in p["etapas"]:
        assert state[s["caso"]] == s["antes"]
        if s["acao"] == "criar":
            assert s["antes"] is None
        if s["acao"] in {"excluir", "alterar", "restaurar"}:
            assert s["antes"] is not None
        state[s["caso"]] = s["depois"]
    assert state == {c["id"]: c["termino"] for c in config["casos"]}
    for c in config["casos"]:
        actions = [s["acao"] for s in p["etapas"] if s["caso"] == c["id"]]
        assert {"criar", "alterar", "excluir", "importar"} <= set(actions)


def test_complete_run_has_imports_between_changes(config, tmp_path):
    backend = Backend(config)
    result = Runner(plan(config, 5), backend, tmp_path).run()
    assert result["status"] == "PASSOU"
    assert backend.mutations and backend.observations
    assert (tmp_path / "diario.txt").exists()
    assert "AMOSTRA" in (tmp_path / "diario.jsonl").read_text(encoding="utf-8")
    assert (tmp_path / "relatorio.html").exists()


def test_resume_does_not_repeat_committed_mutation(config, tmp_path):
    backend = Backend(config)
    backend.crash = True
    p = plan(config, 3)
    with pytest.raises(RuntimeError):
        Runner(p, backend, tmp_path).run()
    first = backend.mutations[0]
    total_expected = sum(s["acao"] != "importar" for s in p["etapas"])
    result = Runner(p, backend, tmp_path).run()
    assert result["status"] == "PASSOU"
    assert len(backend.mutations) == total_expected
    assert "RECUPERADO" in (tmp_path / "diario.txt").read_text(encoding="utf-8")


def test_foreign_state_is_not_overwritten(config, tmp_path):
    backend = Backend(config)
    backend.rows = {k: "2030-01-01T00:00:00" for k in backend.rows}
    result = Runner(plan(config, 4), backend, tmp_path).run()
    assert len(result["bloqueados"]) == 2
    assert backend.mutations == []


def test_unavailable_flow_does_not_mutate(config, tmp_path):
    backend = Backend(config)
    backend.block = True
    result = Runner(plan(config, 1), backend, tmp_path).run()
    assert result["status"] == "CONCLUIDO_COM_RESSALVAS"
    assert not backend.mutations and not backend.observations


def test_business_failure_is_recorded_and_sequence_continues(config, tmp_path):
    backend = Backend(config)
    backend.fail_import = True
    result = Runner(plan(config, 1), backend, tmp_path).run()
    assert result["falhas"] == len(backend.observations) > 1
    assert not result["bloqueados"]
    assert backend.rows == {c["id"]: c["termino"] for c in config["casos"]}


def test_changed_plan_cannot_resume(config, tmp_path):
    Runner(plan(config, 1), Backend(config), tmp_path)
    with pytest.raises(ValueError):
        Runner(plan(config, 2), Backend(config), tmp_path)


def test_validation_rejects_ineffective_change(config):
    config["casos"][0]["termino_alterado"] = config["casos"][0]["termino"]
    with pytest.raises(ValueError):
        plan(config, 1)


def test_secret_not_written_into_plan(config):
    config["senha_api"] = "never-save-this"
    with pytest.raises(ValueError):
        plan(config, 1)


def test_preflight_failure_has_test_diary(config, tmp_path):
    backend = Backend(config)
    def fail():
        raise RuntimeError("private error details")
    backend.preflight = fail
    with pytest.raises(RuntimeError):
        Runner(plan(config, 1), backend, tmp_path).run()
    diary = (tmp_path / "diario.txt").read_text(encoding="utf-8")
    assert "precondicoes" in diary and "INTERROMPIDO" in diary
    assert "private error details" not in diary


def test_rejects_unplanned_action_or_broken_history(config, tmp_path):
    p = plan(config, 1)
    p["etapas"][0]["acao"] = "sql_update"
    with pytest.raises(ValueError):
        Runner(p, Backend(config), tmp_path)
    p = plan(config, 1)
    p["etapas"][-1]["antes"] = "2030-01-01T00:00:00"
    with pytest.raises(ValueError):
        Runner(p, Backend(config), tmp_path)


def test_suite_reuses_new_case_after_first_seed(config, tmp_path, monkeypatch):
    from automatiza import ciclos_cli, ciclos_sirh, observador
    source = {c["id"]: c["termino"] if c["presente"] else None for c in config["casos"]}

    class SharedBackend(Backend):
        def __init__(self, incoming):
            super().__init__(incoming)
            self.rows = source

    monkeypatch.setattr(ciclos_sirh, "SirhBackend", SharedBackend)
    monkeypatch.setattr(observador, "observer_lock", lambda *args, **kwargs: nullcontext())
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(config), encoding="utf-8")
    out = tmp_path / "suite"
    monkeypatch.setattr(sys, "argv", ["ciclos", "suite", "--arquivo", str(manifest),
                                    "--saida", str(out), "--semente", "10", "--sementes", "2"])
    ciclos_cli.main()
    summary = json.loads((out / "resultado.json").read_text(encoding="utf-8"))
    assert [s["status"] for s in summary] == ["PASSOU", "PASSOU"]
    assert source == {c["id"]: c["termino"] for c in config["casos"]}
    second = json.loads((out / "semente-11" / "plano.json").read_text(encoding="utf-8"))
    assert all(s["acao"] != "criar" for s in second["etapas"][:2])
