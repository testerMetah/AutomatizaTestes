from pathlib import Path

from automatiza.sequencias.engine import generate, load_yaml, run_case
from automatiza.sequencias.relatorio import Report


class SequenceLibrary:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def executar_sequencia(self, arquivo):
        return self._run(load_yaml(Path(arquivo)))

    def executar_sequencia_com_seed(self, seed, passos=8):
        return self._run(generate(int(seed), count=int(passos)))

    def _run(self, case):
        report = Report()
        result = run_case(case, report)
        path = report.finish()
        print(f"Relatório: {path.resolve()}")
        if result["estado"] == "FALHOU": raise AssertionError(result["erro"])
        if result["estado"] == "BLOQUEADO":
            from robot.api import SkipExecution
            raise SkipExecution(f"BLOQUEADO; veja {path.resolve()}")
        return str(path)
