# Fase 1 — infraestrutura de teste

O banco único do Acessus e de todos os serviços Acessus é `desk-tec / AcessoFagundes`; o RH Metadados/Frequência usa `desk-tec / RHFagundes`. Os dois foram confirmados como bancos de teste. O perfil `profiles/RHFagundes_para_AcessoFagundes.json` e `config/ambiente-teste.json` declaram esses destinos sem credenciais.

`TestTarget.from_config()` lê o destino; `assert_matches()` confere a configuração e, quando recebe `SqlServer`, o `DB_NAME()` real. `wait_until()` espera uma condição com prazo e erro descritivo. `TestServiceController` permite consultar os três nomes internos configurados, mas start/stop exige `TEST_SERVICE_CONTROL_APPROVED` igual ao nome do serviço e conexão com o banco de teste. Essa variável não deve ser definida sem autorização explícita.

Em 23/10/2026, foram feitas cópias `.bak-20261023` e alteradas apenas as linhas `Database` de `C:\acesso\ConexaoConfig.ini` (`novo123` → `AcessoFagundes`) e `C:\acesso\AccessusComConfig.ini` (`sm` → `AcessoFagundes`), além de `SQL_DATABASE` no `.env` do projeto (`novo123` → `AcessoFagundes`). Os serviços Sync e Comunicação foram instalados com início manual e estão parados. A Importação API já estava em execução e não foi reiniciada. Comandos exatos de instalação e remoção, estados e caminhos estão em `docs/AMBIENTE.md`.

O diagnóstico de leitura `DB_NAME()` e `SELECT 1` passou em `AcessoFagundes`. Nenhum teste escreveu no banco. A venv Python 32 bits está em `C:\python32b\venv32`; os testes unitários passaram (231 testes e 3 subtests) com o diretório temporário ajustado. `AuditRun` em `auditoria.py` fornece JSONL, resumo, HTML e capturas por etapa.

Pendente: confirmar por leitura o banco efetivo do processo atual da Importação API; a alteração do INI pode não afetar a conexão já aberta. A origem `RHFagundes` ainda não teve `SELECT 1` verificado. Fase 2 não iniciada.
