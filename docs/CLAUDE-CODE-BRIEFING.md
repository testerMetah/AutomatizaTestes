# Briefing para assumir o projeto

## a) Em 10 minutos

O projeto real é `C:\AutomatizaTestes`; o sistema é Acessus desktop Delphi/VCL 32 bits. Ative `C:\python32b\venv32`, leia `AGENTS.md`, rode `scripts/verificar_ambiente.ps1` com ExecutionPolicy Bypass e abra o último `reports/*/RELATORIO.html`. O smoke de leitura funciona. CRUD, importação acionada e reinício de Sync/Comunicação estão BLOQUEADOS por mapa/regra/segurança. Primeiro passo útil: mapear uma tela atual sem gravar dados, fixar seus seletores em `docs/mapas-de-tela/`, obter regra e limpeza, então liberar uma entidade.

## b) Mapa do banco (estrutura, sem dados reais)

Ambos SQL Server em `desk-tec` e confirmados como teste em `config/ambiente-teste.json`. Destino `AcessoFagundes`: Acessus e serviços. Origem `RHFagundes`: RH Metadados/Frequência. Metadados consultados em 2026-10-23; confirmar no início de cada cenário. Nenhuma amostra de pessoa/documento foi coletada.

| Banco.tabela | Chave observada | Colunas principais observadas | Entidade/tela provável |
|---|---|---|---|
| AcessoFagundes.dbo.Pessoas | id | nome, status, cpf, idempresa, idUnidade, excluido | Pessoas |
| AcessoFagundes.dbo.RegCrachas | id | Codigo, IdPessoa, TipoCracha, DataHoraRegistro, excluido | Crachás |
| AcessoFagundes.dbo.Unidades | id | idEmpresa, nome, codigo, status | Unidade |
| AcessoFagundes.dbo.Ocorrencias | id | Nome | Ocorrência |
| AcessoFagundes.dbo.Afastamentos | Id | IdPessoa, IdFreq, DataInicio, DataTermino, Causa | Férias/afastamento, vínculo ainda incerto |
| RHFagundes.dbo.RHPESSOAS | EMPRESA, PESSOA | NOME | Pessoa RH |
| RHFagundes.dbo.RHCONTRATOS | UNIDADE, CONTRATO | CRACHA, SITUACAO | Contrato/pessoa RH |
| RHFagundes.dbo.RHCRACHASATIVOS | NROCRACHA, DATAHORAINICIO, DATAHORATERMINO | UNIDADE, CONTRATO, TIPOCRACHAATIVO, PESSOAACESSO | Crachá RH |
| RHFagundes.dbo.RHREGOCORRENCIAS | UNIDADE, CONTRATO, DATAINICIOOCORRENCIA, OCORRENCIA | DATATERMINOOCORRENCIA | Ocorrência RH |
| RHFagundes.dbo.RHFERIASCEDIDASPA | UNIDADE, CONTRATO, INICIOGOZOFERIAS | TERMINOGOZOFERIAS | Férias RH |
| RHFagundes.dbo.RHUNIDADES | UNIDADE | EMPRESA, DESCRICAO40 | Unidade RH |

Relações candidatas por nome: `RegCrachas.IdPessoa→Pessoas.id`, `Unidades.idEmpresa→empresa`, `RHCONTRATOS.UNIDADE→RHUNIDADES.UNIDADE`. **Ainda não confirmadas como FK física ou regra de importação**; conferir `sys.foreign_keys` e código atual antes de testar.

## c) Mapa de telas do Acessus

Mapas históricos em `docs/mapeamentos/`, sobretudo `acesso-pessoas*.txt` e `vm-211-20261020/`. A janela principal atual vista no 2.11.1 é `Módulo de Acesso - v2.11.1`, classe `TFrmPrincipal`. MDIClient, TActionMainMenuBar e TStatusBar fazem parte da janela principal.

| Menu/tela | Janela/controles | Automatizável? | Motivo |
|---|---|---|---|
| Módulo de Acesso, janela principal | TFrmPrincipal; TActionMainMenuBar, MDIClient | funciona no win32 para observação | Janela encontrada e capturada no smoke |
| Cadastros → Pessoas | Cadastro de Pessoas; ver mapas `acesso-pessoas*.txt` | precisa validação no 2.11.1 | Menu customizado; botões THoverButton sem texto |
| Consultas → Acesso por Pessoa | Acesso por Pessoa | não validado no 2.11.1 | Mapa antigo |
| Refeitório / Escola / Estacionamento / Portaria / Administração | consultar `docs/mapeamentos/vm-211-20261020/` | não validado no 2.11.1 | Controle MDI e menus customizados |
| RH → Frequência → Cadastramento → Pessoas → Dados pessoais → Fixo | formulário RH ainda sem mapa atual | não funcionou como automação nova | RH separado do Acessus; seletor atual pendente |

## d) Fluxo de importação

Cadastro acontece no RH/Frequência (`RHFagundes`). O serviço de importação API `FrmSyncImpViewsPrincipal` está instalado e estava rodando no diagnóstico; Sync `FrmViewsPrincipalService` e Comunicação `SrvAcessusCom` estão instalados/parados/manuais. O destino do Acessus é `AcessoFagundes`. O gatilho exato por entidade, o tempo até terminar, os checkpoints e a forma de exibição ainda não foram confirmados; portanto nenhuma sequência afirma importação concluída. Consulte `docs/AMBIENTE.md` e nunca inicie Sync/Comunicação sem autorização.

## e) Matriz de regras de negócio

| Regra | Fonte | Status | Testes |
|---|---|---|---|
| Acessus e serviços usam o mesmo banco de destino, RH usa outro | Gabriel / config | CONFIRMADA para ambiente | checagem-leitura |
| `SELECT 1` em cada banco retorna 1 | SQL observado | CONFIRMADA como infraestrutura | checagem-leitura |
| Pessoa/crachá/unidade pode ser deletada e recriada igual | requisito de cobertura, sem resultado esperado | NÃO CONFIRMADA | ciclo-pessoa |
| Importação cria/atualiza registros e vínculos específicos | nomes/schema histórico | NÃO CONFIRMADA | fluxo-importacao |
| Férias/ocorrências RH geram registros específicos no Acessus | schema histórico | NÃO CONFIRMADA | fluxo-importacao/volume-baixo |

## f) Inventário de testes

| Suíte/sequência | Tags | Estado em 2026-10-23 | Tempo típico | Dependências |
|---|---|---|---|---|
| checagem_leitura.yaml | smoke, regressao, sequencia-fixa | PASSOU em execução individual (~2 s) | ~2 s | 2 SQL SELECT, UI aberta; inventário de controles |
| ciclo_pessoa.yaml | smoke, regressao, bloqueado | BLOQUEADO | <1 s | mapa atual, regra e limpeza |
| fluxo_importacao.yaml | mudanca-atual, regressao, bloqueado | BLOQUEADO | <1 s | gatilho, mapa, autorização de serviço |
| volume_baixo.yaml | lento, regressao, bloqueado | BLOQUEADO | <1 s | mapa, regra, limpeza |
| aleatória com seed | sequencia-aleatoria (CLI/Robot) | BLOQUEADO no seed 4242 | <1 s | mesmos requisitos |
| pytest tests/unit | unitária existente | executar antes de alterar legado | variável | Python 32 bits |

## g) Falhas e armadilhas

PowerShell bloqueia scripts sem `-ExecutionPolicy Bypass` nesta máquina. `pytest` pode negar `.pytest_cache` e temporário padrão: use `--basetemp=reports\pytest-temp -p no:cacheprovider`. Menus Delphi são customizados e THoverButton pode não ter texto. Splash e janela MDI pedem espera por condição. Código do repositório de referência pode estar desatualizado; `C:\Referencia\Acessus` não existia no diagnóstico desta sessão. `reports/` contém evidências e é ignorado pelo Git.

## h) Convenções e evidências

Dados de teste usam `AUTOTEST_<timestamp>_`; cada sequência tem seed. Log por execução: `reports/<data-hora>/eventos.jsonl`, uma linha JSON por evento com número, horário, sequência, passo, ação, banco/UI e resultado. `RELATORIO.html` é a leitura para pessoas; `resumo.json` serve para automação. Campos sensíveis são mascarados. Nenhum relatório vai para Git. A camada nova de UI está em `src/automatiza/ui/`; módulos legados ainda chamam pywinauto diretamente e precisam migrar antes de alegar cobertura completa.

## i) Glossário

**Pessoa:** cadastro individual. **Crachá:** identificador ligado à pessoa/contrato. **Unidade:** subdivisão de empresa no RH ou Acessus. **Ocorrência:** evento lançado para pessoa/contrato. **Férias/afastamento:** período de ausência. **Origem:** RHFagundes. **Destino:** AcessoFagundes. **Importação:** transferência processada por serviço entre origem e destino, regras ainda pendentes.

## j) Testar mudança dos devs

Copie `docs/mudancas/MODELO.md` para `docs/mudancas/AAAA-MM-DD-titulo.md`; preencha build, regra esperada, telas, regressão, tabelas e observação. Leia cenário e briefing, liste casos diretos/regressão/dúvidas. Depois rode `scripts/verificar_ambiente.ps1`; `python -m robot --include smoke tests/sequencias/suites.robot`; `python -m robot --include regressao tests/sequencias/suites.robot`; e a sequência YAML específica via `python -m automatiza.sequencias.cli --arquivo tests/sequencias/arquivo.yaml`. Compare o esperado com o obtido, preserve divergências e evidências.
