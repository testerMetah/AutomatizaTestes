from pathlib import Path

import pytest

from automatiza.ciclos import Blocked
from automatiza.ciclos_sirh import SirhBackend


def test_hourly_occurrence_requires_mapped_code_and_explicit_times():
    backend = SirhBackend.__new__(SirhBackend)
    case = {"tipo": "ocorrencia", "ocorrencia": "013", "gera_afastamento": False,
            "inicio": "2026-11-03T08:15:00", "termino": "2026-11-03T12:45:00",
            "termino_alterado": "2026-11-03T13:15:00"}
    backend.available(case)
    with pytest.raises(Blocked):
        backend.available({**case, "ocorrencia": "011"})
    with pytest.raises(Blocked):
        backend.available({**case, "termino": "2026-11-03T00:00:00"})


@pytest.fixture
def observation(tmp_path, monkeypatch):
    import automatiza.ciclos_sirh as module
    clock = [0]
    monkeypatch.setattr(module.time, "monotonic", lambda: clock[0])
    monkeypatch.setattr(module.time, "sleep", lambda n: clock.__setitem__(0, clock[0] + n))
    log = tmp_path / "service.log"
    log.write_bytes(b"")
    backend = SirhBackend.__new__(SirhBackend)
    backend.config = {"log_servico": str(log), "timeout_segundos": 4,
                      "intervalo_segundos": 1, "pessoa": 5}
    case = {"tipo": "ferias", "inicio": "2090-01-01T00:00:00", "causa_esperada": "Férias"}
    return backend, case, log


def row(case, end, **changes):
    return dict(Id=4, IdPessoa=5, DataInicio=case["inicio"], DataTermino=end,
                Causa=changes.get("Causa", "Férias"))


def test_absence_without_completed_cycle_does_not_pass(observation, tmp_path):
    backend, case, log = observation
    backend.api_state = lambda _: []
    backend.target = lambda _: []
    result = backend.observe(case, None, tmp_path, lambda *args: None)
    assert result["status"] == "FALHOU_TIMEOUT"
    assert result["ciclos_concluidos"] == 0


@pytest.mark.parametrize("defect", ["none", "text", "duplicate", "person", "period"])
def test_business_fields_and_duplicates_checked(observation, tmp_path, defect):
    backend, case, log = observation
    end = "2090-01-10T00:00:00"
    def api(_):
        if not log.read_bytes():
            log.write_bytes(b"Finalizou GetFeriasCedidas com sucesso.")
        return [end]
    backend.api_state = api
    result_row = row(case, end, Causa="FÃ©rias" if defect == "text" else "Férias")
    if defect == "person":
        result_row["IdPessoa"] = 999
    if defect == "period":
        result_row["DataTermino"] = "2090-01-09T00:00:00"
    backend.target = lambda _: [result_row] * (2 if defect == "duplicate" else 1)
    result = backend.observe(case, end, tmp_path, lambda *args: None)
    assert result["status"] == ("PASSOU" if defect == "none" else
                                "FALHOU_TEXTO" if defect == "text" else "FALHOU_TIMEOUT")


def test_delete_waits_for_api_absence_and_destination_removal(observation, tmp_path):
    backend, case, log = observation
    calls = [0]
    def api(_):
        calls[0] += 1
        log.write_bytes(b"Finalizou GetFeriasCedidas com sucesso.")
        return ["2090-01-10T00:00:00"] if calls[0] < 2 else []
    backend.api_state = api
    backend.target = lambda _: [row(case, "2090-01-10T00:00:00")] if calls[0] < 2 else []
    result = backend.observe(case, None, tmp_path, lambda *args: None)
    assert result["status"] == "PASSOU"
    assert calls[0] >= 4
