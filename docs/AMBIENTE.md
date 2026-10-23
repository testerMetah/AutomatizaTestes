# Ambiente observado em 23/10/2026

| Item | Valor | Situação |
| --- | --- | --- |
| Projeto | `C:\AutomatizaTestes` | confirmado |
| Acessus | `C:\acesso\Acessus.exe` | versão 2.11.1.0 |
| Python 32 bits | `C:\python32b\Python312-32\python.exe` | 3.12.10 |
| Venv 32 bits | `C:\python32b\venv32` | instalada; usar nos testes |
| Python do sistema e `.venv` antiga | 64 bits | não usar para automação do Acessus |
| Banco único de Acessus e serviços | `desk-tec / AcessoFagundes` | confirmado como teste; `DB_NAME()` e `SELECT 1` passaram |
| Banco RH Metadados/Frequência | `desk-tec / RHFagundes` | confirmado como teste; conexão não verificada |
| Oracle RH | `dexter / orcl / rhtimegprevisao` | informado pelo usuário; conexão não verificada |

O perfil SQL usa autenticação SQL e ODBC Driver 17. Credenciais ficam no `.env`, fora desta documentação. Na venv 32 bits: pywinauto 0.6.9, pyodbc 5.3.0, pytest 9.1.1 e Pillow 12.3.0.

| Serviço | Executável | Nome interno | Estado em 23/10/2026 | INI e banco escrito nele |
| --- | --- | --- | --- | --- |
| Importação API | `C:\acesso\AcessusSyncImportacao.exe` | `FrmSyncImpViewsPrincipal` | instalado, em execução, início automático | `ConexaoConfig.ini`: `AcessoFagundes`; conexão em memória não verificada após alteração |
| Sync | `C:\acesso\AcessusSyncService.exe` | `FrmViewsPrincipalService` | instalado, parado, início manual | `ConexaoConfig.ini`: `AcessoFagundes` |
| Comunicação | `C:\acesso\AcessusComService.exe` | `SrvAcessusCom` | instalado, parado, início manual | `AccessusComConfig.ini`: `AcessoFagundes` |

Acessus e os três serviços compartilham o banco `AcessoFagundes`. Somente o RH Metadados/Frequência usa `RHFagundes`. Em 23/10/2026, foi alterada apenas a linha `Database` de `C:\acesso\ConexaoConfig.ini` (`novo123` → `AcessoFagundes`) e `C:\acesso\AccessusComConfig.ini` (`sm` → `AcessoFagundes`). O `.env` do projeto também teve apenas `SQL_DATABASE` alterado de `novo123` para `AcessoFagundes`. Backups: `C:\acesso\ConexaoConfig.ini.bak-20261023`, `C:\acesso\AccessusComConfig.ini.bak-20261023` e `C:\AutomatizaTestes\.env.bak-20261023` (ignorado pelo Git). O serviço de Importação API **não foi reiniciado**; seu destino efetivo nesta execução não foi verificado.

## Instalação e reversão dos dois serviços novos

Comandos executados em terminal elevado, com início manual e sem dar start:

```cmd
sc.exe create FrmViewsPrincipalService binPath= C:\acesso\AcessusSyncService.exe start= demand DisplayName= AcessusSync
sc.exe create SrvAcessusCom binPath= C:\acesso\AcessusComService.exe start= demand
```

Para remover os serviços, após confirmar que estão parados, em terminal elevado:

```cmd
sc.exe delete FrmViewsPrincipalService
sc.exe delete SrvAcessusCom
```

Para reverter os INIs, restaurar cada `.bak-20261023` sobre o arquivo correspondente após decidir como lidar com a Importação API em execução. `C:\acesso\config.ini` usa `licenciamento` para outro componente e não foi alterado.

Execute `powershell -NoProfile -File scripts\verificar_ambiente.ps1` para diagnóstico somente leitura.

## Atualização do diagnóstico em 23/10/2026

`RHFagundes` também passou em `SELECT 1` com `DB_NAME()` conferido. O diagnóstico passou em Python 32 bits, Acessus.exe, ambos bancos, três serviços instalados, Git e espaço em disco. Sync e Comunicação continuam parados. Nenhum INI foi alterado nesta etapa. Comando correto nesta máquina: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verificar_ambiente.ps1`.

## Estado atual apos criacao da base isolada (23/10/2026, 10:16)

O destino historico acima foi substituido por **`desk-tec/Acessus_AUTOTEST_20261023`**, confirmado como teste. RH permanece `desk-tec/RHFagundes`. Os dois INIs em `C:\acesso` e o `.env` do projeto apontam ao novo destino. Backups dos INIs: `C:\acesso\backup-config-AUTOTEST-20261023-095100`; backups adicionais com sufixo `bak-AUTOTEST-20261023-1008`.

A base nova recebeu 147 tabelas sem dados da base antiga. Tem uma empresa e um administrador iniciais, zero pessoas, unidades e coletores. O atualizador tentou 415 scripts e reportou erros de objetos duplicados; auditar antes de aprovar o schema. A conexao SQL de importacao `RHFagundes` foi salva. A configuracao API nao salvou porque exige coletor.

`SrvAcessusCom`, `FrmViewsPrincipalService` e `FrmSyncImpViewsPrincipal` estao Running. O log de importacao registra ausencia de `DADOS_IMPORTACAO_API`; portanto Running nao comprova importacao. `scripts/iniciar_servicos_teste.ps1` valida o destino e inicia os servicos em terminal elevado.
