# Estrutura bras1 — inspeção em 15/10/2026

Inventário realizado somente por metadados: 142 tabelas, 2 views, 1 procedimento e 1 gatilho. Foram registradas 1.373 colunas de tabelas/views, 176 vínculos de colunas de chaves estrangeiras e 343 participações de colunas em índices (não são 343 índices distintos).

Arquivos completos da inspeção: `reports/banco/20261015-095741`. O inventário representa a estrutura visível ao login naquele instante; não determina sozinho as regras de negócio.

## Caminho confirmado para validação

- `dbo.Afastamentos`: Id, DataInicio, DataTermino, IdPessoa, Causa e IdFreq.
- Chave primária `PK_Ferias` em Id; índice único `UQ_IdFreqAfastamentos` em IdFreq.
- FK `FK_Ferias_Pessoas`: Afastamentos.IdPessoa → Pessoas.id.
- `dbo.Pessoas`: IdExportacao e ContratoExportacao são candidatos a ajudar no vínculo com o RH. A correspondência exata não está confirmada. Nome e essas chaves foram consultados pontualmente para as 12 pessoas já observadas, sem CPF, contato ou senha.

Não há um gatilho declarado diretamente em Afastamentos no inventário. Isso não identifica qual aplicação ou serviço escreve nessa tabela, nem prova a origem de cada registro.

## Estruturas candidatas para aprofundamento

| Estrutura | Evidência e limite |
| --- | --- |
| DADOS_IMPORTACAO_API | Colunas de intervalo, contratos_alterados, empresa e unidade. Valores não consultados; inclui campos de credenciais que não devem ser exportados. |
| AcessusSyncTarefas | Tipo, opções, status e vínculo à empresa. Não foi lido o conteúdo de opções. |
| AcessusSyncAgendamento | Horários, dias, periodicidade e FK para tarefas. Configuração não comprova execução. |
| HISTORICO_ACESSUSSYNC_TAREFAS / AGENDAMENTOS | Estrutura de histórico de configurações; não assumir que seja log de importação. |
| parametros / PARAMETROS_SISTEMA | Estrutura genérica de configuração; valores não consultados indiscriminadamente. |
| Ocorrencias | Apenas id/Nome na estrutura; sua aplicação a ocorrências do RH não está demonstrada. Existe também VeiculosOcorrencias. |

O único gatilho encontrado é `TRG_METAH_FILTROS_UPDATE`, em METAH_FILTROS, habilitado. Seu código não foi consultado. Não foram executadas contagens completas, leitura de dados biométricos, credenciais, alterações de configuração ou comandos de serviço.

Próximas confirmações de negócio: vínculo pessoa/contrato RH, causa que gera afastamento, regra de corte por data e significado de término 30/12/1899. Até isso estar demonstrado, o relatório distingue observações de conclusões de caso.
