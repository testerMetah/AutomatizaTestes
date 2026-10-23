@AGENTS.md

No PowerShell em C:\AutomatizaTestes: `& C:\python32b\venv32\Scripts\Activate.ps1`; `$env:PYTHONPATH='C:\AutomatizaTestes\src'`. Diagnóstico: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verificar_ambiente.ps1`.

Smoke: `python -m robot --include smoke tests\sequencias\suites.robot`. Regressão: `python -m robot --include regressao tests\sequencias\suites.robot`. Teste isolado: `python -m robot --test "Checagem leitura" tests\sequencias\suites.robot`. Seed: `python -m automatiza.sequencias.cli --seed 42 --passos 8`. Suíte Python: `python -m pytest tests\unit -ra --basetemp=reports\pytest-temp -p no:cacheprovider`.

Só usar bancos confirmados em config/ambiente-teste.json. Não iniciar/instalar Sync (novo123) ou Comunicação (sm) sem autorização; não escrever em banco não confirmado, alterar INIs ou C:\Referencia; DELETE/UPDATE sempre com prefixo AUTOTEST_<timestamp>_ na cláusula. Cenário sem seletor/regra validado fica BLOQUEADO ou AVISO. Leia docs/HANDOFF.md.
