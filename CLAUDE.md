# Instruções permanentes para Claude Code

Leia [AGENTS.md](AGENTS.md) **inteiro** antes de agir; ele é a fonte de verdade das regras permanentes. Este arquivo é apenas a porta de entrada para Claude Code. Se houver divergência, siga AGENTS.md e a instrução mais recente do usuário.

Projeto: `C:\AutomatizaTestes`. Entrada diária: `Abrir-Painel.bat`; CLI: `automatiza` via `C:\python32b\venv32\Scripts\automatiza.exe`. Leia [README.md](README.md), [docs/GUIA-DE-USO.md](docs/GUIA-DE-USO.md), [docs/ARQUITETURA.md](docs/ARQUITETURA.md) e [docs/HANDOFF.md](docs/HANDOFF.md).

Regras centrais: Python **sempre 32 bits** para Acessus; testes desktop na sessão Windows interativa; nunca escrever em produção; confirmar `DB_NAME()` e lista de bancos de teste antes de escrita; não registrar senhas/strings de conexão; não alterar testes para esconder falhas; preservar logs permanentes e scripts antigos; usar regra de negócio confirmada para oráculos. Novas builds exigem mapa da tela e conferência dos INIs.

Comandos: `automatiza ambiente`, `automatiza comandos`, `automatiza auditorias --modulo todos`, `automatiza robot --tag smoke`, `automatiza testes-unitarios`. Ações de escrita em ciclos exigem `--confirmo-escrita`; o painel pede confirmação do banco efetivo. Para executar testes diretamente: `C:\python32b\venv32\Scripts\python.exe -m pytest tests/unit -q --basetemp=C:\AutomatizaTestes\resultados\pytest-manual -p no:cacheprovider`.
