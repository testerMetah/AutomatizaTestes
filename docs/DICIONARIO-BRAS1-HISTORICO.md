# Dicionário da bras1 — evidência histórica

Fonte: `reports/banco/20261015-095741/inventario.json`; observado em 2026-10-15T12:57:41.055194+00:00.
Documento gerado agora a partir dessa coleta anterior. Não foi revalidado no servidor nesta sessão.
Sem registros de negócio ou definições SQL. Permissões do login podem limitar a cobertura.

146 objetos; 1373 colunas; 268 índices distintos; 176 restrições FK, com 176 vínculos de colunas.

## dbo.AcessosAutorizados

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| DataHoraInicio | datetime | 8 | 23/3 | True | False | False |
| DataHoraFim | datetime | 8 | 23/3 | True | False | False |
| Autorizado | tinyint | 1 | 3/0 | True | False | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| IdFreq | nvarchar | 100 | 0/0 | True | False | False |
| importado | char | 1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdExtrasAutorizadas | CLUSTERED | True | True | id | 1 | False |
| UQ_IdFreqAcessosAutorizados | NONCLUSTERED | True | False | IdFreq | 1 | False |

- IdPessoa → dbo.Pessoas.id (FK_ExtrasAutorizadas_Pessoas); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.AcessusSyncAgendamento

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| descricao | nvarchar | 500 | 0/0 | False | False | False |
| horarios | nvarchar | -1 | 0/0 | False | False | False |
| diassemanas | nvarchar | 500 | 0/0 | True | False | False |
| periodicamente | int | 4 | 10/0 | True | False | False |
| id_tarefa | int | 4 | 10/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| status | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_AcessusSyncAgendamento | CLUSTERED | True | True | id | 1 | False |

- id_tarefa → dbo.AcessusSyncTarefas.id (FK_ACESSUSSYNC_AGENDAMENTOS_ACESSUSSYNCTAREFAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_ACESSUSSYNC_AGENDAMENTOS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_ACESSUSSYNC_AGENDAMENTOS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.AcessusSyncTarefas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| descricao | nvarchar | 400 | 0/0 | False | False | False |
| tipo | int | 4 | 10/0 | False | False | False |
| opcoes | nvarchar | -1 | 0/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| status | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_AcessusSyncTarefas | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_ACESSUSSYNC_TAREFAS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_ACESSUSSYNC_TAREFAS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Afastamentos

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| DataInicio | datetime | 8 | 23/3 | False | False | False |
| DataTermino | datetime | 8 | 23/3 | True | False | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| Causa | nvarchar | 100 | 0/0 | True | False | False |
| IdFreq | nvarchar | 100 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Ferias | CLUSTERED | True | True | Id | 1 | False |
| UQ_IdFreqAfastamentos | NONCLUSTERED | True | False | IdFreq | 1 | False |

- IdPessoa → dbo.Pessoas.id (FK_Ferias_Pessoas); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.ALUNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| email | varchar | 150 | 0/0 | True | False | False |
| nascimento | datetime | 8 | 23/3 | False | False | False |
| sexo | char | 1 | 0/0 | False | False | False |
| cpf | char | 11 | 0/0 | True | False | False |
| matricula | bigint | 8 | 19/0 | False | False | False |
| data_matricula | datetime | 8 | 23/3 | True | False | False |
| nivel_ensino | int | 4 | 10/0 | True | False | False |
| serie_ano | char | 10 | 0/0 | True | False | False |
| observacoes | text | 16 | 0/0 | True | False | False |
| id_turma | int | 4 | 10/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ALUNOS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_ALUNOS_EMPRESA); exclusão: SET_NULL; desabilitada: False; não validada: False.
- id_turma → dbo.TURMAS.id (FK_ALUNOS_TURMA); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ALUNOS_RESPONSAVEIS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_aluno | int | 4 | 10/0 | False | False | False |
| id_responsavel | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ALUNOS_RESPONSAVEIS | CLUSTERED | True | True | id_aluno | 1 | False |
| PK_ALUNOS_RESPONSAVEIS | CLUSTERED | True | True | id_responsavel | 2 | False |

- id_aluno → dbo.ALUNOS.id (FK_AR_ALUNO); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_responsavel → dbo.RESPONSAVEIS.id (FK_AR_RESPONSAVEL); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.atualizacao

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| datahora | datetime | 8 | 23/3 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_atualizacao | CLUSTERED | True | True | id | 1 | False |

## dbo.atualizacaoscripts

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | False | False |
| datahoraatuscript | datetime2 | 8 | 27/7 | True | False | False |
| script | ntext | 16 | 0/0 | False | False | False |
| versao | nvarchar | 20 | 0/0 | True | False | False |
| status | nvarchar | 2000 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_atualizacaoscripts | CLUSTERED | True | True | id | 1 | False |

## dbo.AvaliacoesRefeicoes

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| Nota | int | 4 | 10/0 | False | False | False |
| Feedback | varchar | 384 | 0/0 | True | False | False |

## dbo.cardapios

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 100 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| ValorReservaComConsumo | decimal | 9 | 18/2 | True | False | False |
| ValorReservaSemConsumo | decimal | 9 | 18/2 | True | False | False |
| ValorConsumoComReserva | decimal | 9 | 18/2 | True | False | False |
| ValorConsumoSemReserva | decimal | 9 | 18/2 | True | False | False |
| IdRefeitorio | int | 4 | 10/0 | True | False | False |
| IdExportacao | nvarchar | 100 | 0/0 | True | False | False |
| horafim | time | 5 | 16/7 | True | False | False |
| horaini | time | 5 | 16/7 | True | False | False |
| horaIniReserva | time | 5 | 16/7 | True | False | False |
| horaFimReserva | time | 5 | 16/7 | True | False | False |
| TempoDesconsiderar | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Cardapios | CLUSTERED | True | True | id | 1 | False |
| UQ_IdExportacaoCardapios | NONCLUSTERED | True | False | IdExportacao | 1 | False |

- id_empresa → dbo.Empresas.id (FK_CARDAPIOS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.cardapios_refeitorios

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| CardapiosId | int | 4 | 10/0 | False | False | False |
| RefeitoriosId | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__cardapio__5D0990AD29C3C660 | CLUSTERED | True | True | CardapiosId | 1 | False |
| PK__cardapio__5D0990AD29C3C660 | CLUSTERED | True | True | RefeitoriosId | 2 | False |

- CardapiosId → dbo.cardapios.id (FK__cardapios__Carda__269AB60B); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- RefeitoriosId → dbo.Refeitorios.id (FK__cardapios__Refei__278EDA44); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetaStatus

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| DataHora | datetime | 8 | 23/3 | True | False | False |
| Coletor | int | 4 | 10/0 | False | False | False |
| ColetorNome | nvarchar | 40 | 0/0 | True | False | False |
| TipoColetor | nvarchar | 20 | 0/0 | True | False | False |
| NrTerminal | int | 4 | 10/0 | False | False | False |
| IP | nvarchar | 30 | 0/0 | True | False | False |
| Quantidade_Registros | int | 4 | 10/0 | True | False | False |
| Tamanho_Buffer_Registros | int | 4 | 10/0 | True | False | False |
| Quantidade_Cartoes_Lista | int | 4 | 10/0 | True | False | False |
| Tamanho_Lista_Cartoes | int | 4 | 10/0 | True | False | False |
| Quantidade_Digitos | int | 4 | 10/0 | True | False | False |
| DataHoraColetor | datetime | 8 | 23/3 | True | False | False |
| Numero_Tipo_Acionamento | int | 4 | 10/0 | True | False | False |
| Tipo_Acionamento | nvarchar | 160 | 0/0 | True | False | False |
| Numero_Checagem | int | 4 | 10/0 | True | False | False |
| Checagem | nvarchar | 100 | 0/0 | True | False | False |
| Numero_Sentido_Giro | int | 4 | 10/0 | True | False | False |
| Sentido_Giro | nvarchar | 30 | 0/0 | True | False | False |
| Numero_Ativacao | int | 4 | 10/0 | True | False | False |
| Ativacao | nvarchar | 40 | 0/0 | True | False | False |
| Numero_Acesso_Controlado | int | 4 | 10/0 | True | False | False |
| Acesso_Controlado | nvarchar | 60 | 0/0 | True | False | False |
| Versao_Firmware | nvarchar | 20 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ColetaStatus | CLUSTERED | True | True | id | 1 | False |

## dbo.ColetorControlID

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| porta | int | 4 | 10/0 | True | False | False |
| ipservidor | nvarchar | 30 | 0/0 | True | False | False |
| ipautomatico | int | 4 | 10/0 | True | False | False |
| portaescuta | int | 4 | 10/0 | True | False | False |
| usuario | nvarchar | 60 | 0/0 | True | False | False |
| senha | nvarchar | 60 | 0/0 | True | False | False |
| exibirsenha | int | 4 | 10/0 | True | False | False |
| timeout | int | 4 | 10/0 | True | False | False |
| sentidofluxo | int | 4 | 10/0 | True | False | False |
| catracainvertida | int | 4 | 10/0 | True | False | False |
| wiegand_rfid | int | 4 | 10/0 | True | False | False |
| biometria | int | 4 | 10/0 | True | False | False |
| face | int | 4 | 10/0 | True | False | False |
| leitoruhf | text | 16 | 0/0 | True | False | False |
| syncbio | int | 4 | 10/0 | False | False | False |
| Antena | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ColControlID | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_ColControlID); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetorControlID_Block

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| porta | int | 4 | 10/0 | True | False | False |
| ipservidor | nvarchar | 30 | 0/0 | True | False | False |
| ipautomatico | int | 4 | 10/0 | True | False | False |
| portaescuta | int | 4 | 10/0 | True | False | False |
| usuario | nvarchar | 60 | 0/0 | True | False | False |
| senha | nvarchar | 60 | 0/0 | True | False | False |
| exibirsenha | int | 4 | 10/0 | True | False | False |
| timeout | int | 4 | 10/0 | True | False | False |
| modofluxo | int | 4 | 10/0 | True | False | False |
| sentidogiro | int | 4 | 10/0 | True | False | False |
| wiegand_rfid | int | 4 | 10/0 | True | False | False |
| biometria | int | 4 | 10/0 | True | False | False |
| face | int | 4 | 10/0 | True | False | False |
| urna | int | 4 | 10/0 | True | False | False |
| syncbio | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IDBlock | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_IDBlock_Coletor); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetorControlID_Block_Next

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| porta | int | 4 | 10/0 | True | False | False |
| ipservidor | nvarchar | 30 | 0/0 | True | False | False |
| ipautomatico | int | 4 | 10/0 | True | False | False |
| portaescuta | int | 4 | 10/0 | True | False | False |
| usuario | nvarchar | 60 | 0/0 | True | False | False |
| senha | nvarchar | 60 | 0/0 | True | False | False |
| exibirsenha | int | 4 | 10/0 | True | False | False |
| timeout | int | 4 | 10/0 | True | False | False |
| modofluxo | int | 4 | 10/0 | True | False | False |
| sentidogiro | int | 4 | 10/0 | True | False | False |
| wiegand_rfid | int | 4 | 10/0 | True | False | False |
| biometria | int | 4 | 10/0 | True | False | False |
| face | int | 4 | 10/0 | True | False | False |
| urna | int | 4 | 10/0 | True | False | False |
| syncbio | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IDBlock_Next | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_IDBlock_Next_Coletor); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetorDimepBiopoint

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| terminal | int | 4 | 10/0 | True | False | False |
| timeout | int | 4 | 10/0 | True | False | False |
| acionamento | int | 4 | 10/0 | True | False | False |
| tempoacionamento | int | 4 | 10/0 | True | False | False |
| sentidogiro | int | 4 | 10/0 | True | False | False |
| liberarentrada | int | 4 | 10/0 | True | False | False |
| liberarsaida | int | 4 | 10/0 | True | False | False |
| validadigital | int | 4 | 10/0 | True | False | False |
| urna | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ColBiopoint | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_ColBiopoint); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetorDimepMicropoint

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| terminal | int | 4 | 10/0 | True | False | False |
| timeout | int | 4 | 10/0 | True | False | False |
| sentidoentrada | int | 4 | 10/0 | True | False | False |
| acionamento | int | 4 | 10/0 | True | False | False |
| nrfunis | int | 4 | 10/0 | True | False | False |
| urna | int | 4 | 10/0 | True | False | False |
| modotrabalho | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ColMicropoint | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_ColMicropoint); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Coletores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 100 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| idmodelo | int | 4 | 10/0 | False | False | False |
| ip | nvarchar | 30 | 0/0 | True | False | False |
| comunicacao | tinyint | 1 | 3/0 | True | False | False |
| fusosinal | nchar | 2 | 0/0 | True | False | False |
| fusomin | int | 4 | 10/0 | True | False | False |
| funcacesso | int | 4 | 10/0 | True | False | False |
| funcreserva | int | 4 | 10/0 | True | False | False |
| funcconsumo | int | 4 | 10/0 | True | False | False |
| funcentrada | int | 4 | 10/0 | True | False | False |
| funcsaida | int | 4 | 10/0 | True | False | False |
| IdRefeitorio | int | 4 | 10/0 | True | False | False |
| IdCardapio | int | 4 | 10/0 | True | False | False |
| msgliberado | int | 4 | 10/0 | True | False | False |
| msgbloqueado | int | 4 | 10/0 | True | False | False |
| filtro | int | 4 | 10/0 | True | False | False |
| proximidade | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | status | 1 | False |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | comunicacao | 2 | False |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | idmodelo | 3 | False |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | nome | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | ip | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | funcacesso | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | funcreserva | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | funcconsumo | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | fusosinal | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | fusomin | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | funcentrada | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | funcsaida | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | filtro | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | proximidade | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | msgliberado | 0 | True |
| IX_Coletores_Status_Comunicacao | NONCLUSTERED | False | False | msgbloqueado | 0 | True |
| PK_Coletores | CLUSTERED | True | True | id | 1 | False |

- idmodelo → dbo.ModeloColetores.id (FK_Coletores); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ColetoresStatusConexao

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| idcoletor | int | 4 | 10/0 | False | False | False |
| status | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_ColetoresStatusConexao_IdColetor | NONCLUSTERED | False | False | idcoletor | 1 | False |
| IX_ColetoresStatusConexao_IdColetor | NONCLUSTERED | False | False | status | 0 | True |
| PK_ColetoresStatusConexao | CLUSTERED | True | True | idcoletor | 1 | False |

- idcoletor → dbo.Coletores.id (FK_ColetoresStatusConexao_Coletores); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.ConexaoBD

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| TipoBD | tinyint | 1 | 3/0 | False | False | False |
| NomeServidor | varchar | 100 | 0/0 | False | False | False |
| NomeBD | varchar | 50 | 0/0 | False | False | False |
| Usuario | varchar | 50 | 0/0 | True | False | False |
| Senha | varchar | 255 | 0/0 | False | False | False |
| porta | int | 4 | 10/0 | True | False | False |

## dbo.Creditos

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdColetor | int | 4 | 10/0 | False | False | False |
| IdCardapio | int | 4 | 10/0 | False | False | False |
| IdRefeitorio | int | 4 | 10/0 | False | False | False |
| Funcao | int | 4 | 10/0 | True | False | False |
| IdPessoa | int | 4 | 10/0 | True | False | False |
| Qtde | int | 4 | 10/0 | True | False | False |

- IdCardapio → dbo.cardapios.id (FK_Creditos_cardapios); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdColetor → dbo.Coletores.id (FK_Creditos_Coletores); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdPessoa → dbo.Pessoas.id (FK_Creditos_Pessoas); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdRefeitorio → dbo.Refeitorios.id (FK_Creditos_Refeitorios); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.CreditosPessoa

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdColetor | int | 4 | 10/0 | False | False | False |
| IdCardapio | int | 4 | 10/0 | False | False | False |
| IdRefeitorio | int | 4 | 10/0 | False | False | False |
| Funcao | int | 4 | 10/0 | True | False | False |
| IdPessoa | int | 4 | 10/0 | True | False | False |
| saldo | int | 4 | 10/0 | True | False | False |
| mesUltUtilizacao | int | 4 | 10/0 | True | False | False |

- IdCardapio → dbo.cardapios.id (FK_CreditosPessoa_cardapios); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdColetor → dbo.Coletores.id (FK_CreditosPessoa_Coletores); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdPessoa → dbo.Pessoas.id (FK_CreditosPessoa_Pessoas); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdRefeitorio → dbo.Refeitorios.id (FK_CreditosPessoa_Refeitorios); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.DADOS_IMPORTACAO_API

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_coletores | varchar | 50 | 0/0 | False | False | False |
| quantidade_acesso | int | 4 | 10/0 | False | False | False |
| sentido_acesso | int | 4 | 10/0 | False | False | False |
| atualizar_crachas | char | 1 | 0/0 | False | False | False |
| csv_cracha_provisorio | varchar | -1 | 0/0 | True | False | False |
| imp_digitais | char | 1 | 0/0 | True | False | False |
| imp_fotos | char | 1 | 0/0 | True | False | False |
| url_api | nvarchar | 510 | 0/0 | True | False | False |
| email_api | nvarchar | 510 | 0/0 | True | False | False |
| senha_api | nvarchar | -1 | 0/0 | True | False | False |
| intervalo_minutos | int | 4 | 10/0 | True | False | False |
| contratos_alterados | date | 3 | 10/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | True | False | False |
| unidade | varchar | 50 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__DADOS_IM__3213E83F3E640F0E | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_DADOS_IMPORTACAO_API_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_DADOS_IMPORTACAO_API_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.DigitaisPessoa

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_DigitaisPessoa_IdPessoa | NONCLUSTERED | False | False | IdPessoa | 1 | False |
| PK_DigitaisPessoa | CLUSTERED | True | True | id | 1 | False |

## dbo.Digital

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| Dedo | int | 4 | 10/0 | False | False | False |
| Digital | varbinary | -1 | 0/0 | True | False | False |
| Mao | nchar | 2 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_Digital_IdPessoa | NONCLUSTERED | False | False | IdPessoa | 1 | False |
| PK_Digital | CLUSTERED | True | True | id | 1 | False |

## dbo.Digital_Controlid

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| Tipo | tinyint | 1 | 3/0 | True | False | False |
| Mao | nchar | 2 | 0/0 | True | False | False |
| Dedo | int | 4 | 10/0 | True | False | False |
| Digital | text | 16 | 0/0 | True | False | False |
| TipoPessoa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_Digital_CID_IdPessoa | NONCLUSTERED | False | False | IdPessoa | 1 | False |
| PK_Digital_Controlid | CLUSTERED | True | True | id | 1 | False |

## dbo.DIGITAL_TOPDATA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_pessoa | int | 4 | 10/0 | False | False | False |
| tipo_pessoa | int | 4 | 10/0 | False | False | False |
| dedo | int | 4 | 10/0 | True | False | False |
| digital | varchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_DIGITAL_TOPDATA_Pessoa | NONCLUSTERED | False | False | id_pessoa | 1 | False |
| IX_DIGITAL_TOPDATA_Pessoa | NONCLUSTERED | False | False | tipo_pessoa | 2 | False |
| PK__DIGITAL___3213E83FF82A9D10 | CLUSTERED | True | True | id | 1 | False |

## dbo.EmpresaAcesso

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Nome | nvarchar | 100 | 0/0 | False | False | False |
| Cnpj_Cpf | nvarchar | 40 | 0/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_EmpresaAcesso | CLUSTERED | True | True | id | 1 | False |

## dbo.Empresas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 100 | 0/0 | False | False | False |
| cpf_cnpj | nvarchar | 40 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Empresas | CLUSTERED | True | True | id | 1 | False |

## dbo.EPIs

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| equipamento | int | 4 | 10/0 | False | False | False |
| aquisicao | datetime | 8 | 23/3 | False | False | False |
| validade | datetime | 8 | 23/3 | False | False | False |
| estado | int | 4 | 10/0 | False | False | False |
| posse | int | 4 | 10/0 | False | False | False |
| descricao | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_EPIs | CLUSTERED | True | True | id | 1 | False |

## dbo.EQUIPAMENTOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| NOME | varchar | 100 | 0/0 | False | False | False |
| STATUS | int | 4 | 10/0 | False | False | False |
| IDMODELO | int | 4 | 10/0 | False | False | False |
| MARCA | int | 4 | 10/0 | False | False | False |
| COMUNICACAO | int | 4 | 10/0 | False | False | False |
| IP | varchar | 15 | 0/0 | False | False | False |
| PORTA | int | 4 | 10/0 | True | False | False |
| TIMEOUT | int | 4 | 10/0 | True | False | False |
| USUARIO_DIMEP | varchar | 50 | 0/0 | True | False | False |
| SENHA_DIMEP | varchar | 50 | 0/0 | True | False | False |
| ACCESS_KEY | varchar | 100 | 0/0 | True | False | False |
| CODIGORELEASE | varchar | 500 | 0/0 | True | False | False |
| EXPOENTE | varchar | 50 | 0/0 | True | False | False |
| USUARIO_RSA | varchar | 50 | 0/0 | True | False | False |
| SENHA_RSA | varchar | 50 | 0/0 | True | False | False |
| TIPO_MODELO_DIMEP | int | 4 | 10/0 | False | False | False |
| VERSAO_FIRMWARE | varchar | 50 | 0/0 | True | False | False |
| NUMFABRICACAO | varchar | 50 | 0/0 | True | False | False |
| NUMERO_SERIE | varchar | 50 | 0/0 | True | False | False |
| FUNCENTRADA | int | 4 | 10/0 | True | False | False |
| FUNCSaida | int | 4 | 10/0 | True | False | False |
| FUNCACESSO | int | 4 | 10/0 | True | False | False |
| FUNCRESERVA | int | 4 | 10/0 | True | False | False |
| FUNCCONSUMO | int | 4 | 10/0 | True | False | False |
| IDREFEITORIO | int | 4 | 10/0 | True | False | False |
| IDCARDAPIO | int | 4 | 10/0 | True | False | False |
| IDEMPRESA | int | 4 | 10/0 | True | False | False |
| UltimoPonteiro | bigint | 8 | 19/0 | True | False | False |
| DataUltimaColeta | datetime | 8 | 23/3 | True | False | False |
| DataUltimoEnvio | datetime | 8 | 23/3 | True | False | False |
| DATACADASTRO | datetime | 8 | 23/3 | False | False | False |
| DATAALTERACAO | datetime | 8 | 23/3 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IDX_EQUIPAMENTOS_IDEMPRESA | NONCLUSTERED | False | False | IDEMPRESA | 1 | False |
| IDX_EQUIPAMENTOS_IDMODELO | NONCLUSTERED | False | False | IDMODELO | 1 | False |
| IDX_EQUIPAMENTOS_IP | NONCLUSTERED | False | False | IP | 1 | False |
| IDX_EQUIPAMENTOS_MARCA | NONCLUSTERED | False | False | MARCA | 1 | False |
| IDX_EQUIPAMENTOS_NOME | NONCLUSTERED | False | False | NOME | 1 | False |
| IDX_EQUIPAMENTOS_STATUS | NONCLUSTERED | False | False | STATUS | 1 | False |
| IDX_EQUIPAMENTOS_TIPO_MODELO | NONCLUSTERED | False | False | TIPO_MODELO_DIMEP | 1 | False |
| PK_EQUIPAMENTOS | CLUSTERED | True | True | ID | 1 | False |
| UK_EQUIPAMENTOS_IP | NONCLUSTERED | True | False | IP | 1 | False |

- IDMODELO → dbo.MODELO_EQUIPAMENTOS.ID (FK_EQUIPAMENTOS_MODELO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.EQUIPAMENTOS_CONFIG_CONTROLID

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| IDEQUIPAMENTO | int | 4 | 10/0 | False | False | False |
| USUARIO | varchar | 50 | 0/0 | True | False | False |
| SENHA | varchar | 50 | 0/0 | True | False | False |
| PORTA | int | 4 | 10/0 | True | False | False |
| SSL | int | 4 | 10/0 | False | False | False |
| TIMEOUT | int | 4 | 10/0 | False | False | False |
| INTERVALOCOLETA | int | 4 | 10/0 | False | False | False |
| AUTOCOLETA | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_EQUIPAMENTOS_CONFIG_CONTROLID | CLUSTERED | True | True | IDEQUIPAMENTO | 1 | False |

## dbo.EQUIPAMENTOS_CONFIG_DIMEP

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| IDEQUIPAMENTO | int | 4 | 10/0 | False | False | False |
| TERMINAL | int | 4 | 10/0 | False | False | False |
| TIMEOUT | int | 4 | 10/0 | False | False | False |
| INTERVALOCOLETA | int | 4 | 10/0 | False | False | False |
| AUTOCOLETA | int | 4 | 10/0 | False | False | False |
| LEITORA2DE5 | int | 4 | 10/0 | False | False | False |
| LEITORA2DE5DIMEP | int | 4 | 10/0 | False | False | False |
| LEITORA3DE9 | int | 4 | 10/0 | False | False | False |
| LEITORAMAGNETICA | int | 4 | 10/0 | False | False | False |
| LEITORAWIEGAND | int | 4 | 10/0 | False | False | False |
| LEITORASMARTCARD | int | 4 | 10/0 | False | False | False |
| USOSMARTCARD | int | 4 | 10/0 | False | False | False |
| FORMATO2DE5 | varchar | 50 | 0/0 | True | False | False |
| FORMATO2DE5DIMEP | varchar | 50 | 0/0 | True | False | False |
| FORMATO3DE9 | varchar | 50 | 0/0 | True | False | False |
| FORMATOMAGNETICO | varchar | 50 | 0/0 | True | False | False |
| FORMATOABA | varchar | 50 | 0/0 | True | False | False |
| FORMATOWIEGAND | varchar | 50 | 0/0 | True | False | False |
| FORMATOSMARTCARD | varchar | 50 | 0/0 | True | False | False |
| AUTENTICACAOCARTAO | int | 4 | 10/0 | False | False | False |
| AUTENTICACAOTECLADO | int | 4 | 10/0 | False | False | False |
| HABILITARTECLADO | int | 4 | 10/0 | False | False | False |
| HABILITARBIOMETRIA1N | int | 4 | 10/0 | False | False | False |
| INICIOHORARIOVERAO | datetime | 8 | 23/3 | True | False | False |
| FIMHORARIOVERAO | datetime | 8 | 23/3 | True | False | False |
| MSGPISNAOCADASTRADO | varchar | 100 | 0/0 | True | False | False |
| MSGPODEPASSAR | varchar | 100 | 0/0 | True | False | False |
| MSGHORARIOINVALIDO | varchar | 100 | 0/0 | True | False | False |
| TIPOCRIPTOGRAFIA | int | 4 | 10/0 | False | False | False |
| VETOR1 | bigint | 8 | 19/0 | True | False | False |
| VETOR2 | bigint | 8 | 19/0 | True | False | False |
| VERIFICADOR1 | int | 4 | 10/0 | True | False | False |
| VERIFICADOR2 | int | 4 | 10/0 | True | False | False |
| AVANCOPAPEL | int | 4 | 10/0 | False | False | False |
| TIPOCORTE | int | 4 | 10/0 | False | False | False |
| FACE_ENABLED | int | 4 | 10/0 | False | False | False |
| FACE_LIVENESS | int | 4 | 10/0 | False | False | False |
| FACE_ANTISPOOFING | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_EQUIPAMENTOS_CONFIG_DIMEP | CLUSTERED | True | True | IDEQUIPAMENTO | 1 | False |

## dbo.Estacionamento

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Nome | nvarchar | 200 | 0/0 | True | False | False |
| quantidade | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdEstacionamento | CLUSTERED | True | True | id | 1 | False |

## dbo.EstadoVisita

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| estado | int | 4 | 10/0 | False | False | False |
| datahora | datetime | 8 | 23/3 | False | False | False |
| idvisita | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_EstadoVisita | CLUSTERED | True | True | id | 1 | False |

- idvisita → dbo.VisitantesTerceirosHistoricos.id (FK_EstadoVisita_HistoricoVisita); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.EXPORTACAO_AFD

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_EQUIPAMENTO | int | 4 | 10/0 | False | False | False |
| ID_EMPRESA | int | 4 | 10/0 | False | False | False |
| ID_USUARIO | int | 4 | 10/0 | False | False | False |
| DATA_INICIO | datetime | 8 | 23/3 | False | False | False |
| DATA_FIM | datetime | 8 | 23/3 | False | False | False |
| DATA_EXPORTACAO | datetime | 8 | 23/3 | False | False | False |
| TOTAL_REGISTROS | int | 4 | 10/0 | False | False | False |
| REGISTROS_NOVOS | int | 4 | 10/0 | False | False | False |
| REGISTROS_DUPLICADOS | int | 4 | 10/0 | False | False | False |
| STATUS | tinyint | 1 | 3/0 | False | False | False |
| MENSAGEM_ERRO | text | 16 | 0/0 | True | False | False |
| PROTOCOLO_USADO | varchar | 50 | 0/0 | True | False | False |
| TEMPO_EXECUCAO_MS | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IDX_EXP_AFD_DATA | NONCLUSTERED | False | False | DATA_EXPORTACAO | 1 | False |
| IDX_EXP_AFD_EMPRESA | NONCLUSTERED | False | False | ID_EMPRESA | 1 | False |
| IDX_EXP_AFD_EQUIPAMENTO | NONCLUSTERED | False | False | ID_EQUIPAMENTO | 1 | False |
| IDX_EXP_AFD_PERIODO | NONCLUSTERED | False | False | DATA_INICIO | 1 | False |
| IDX_EXP_AFD_PERIODO | NONCLUSTERED | False | False | DATA_FIM | 2 | False |
| PK__EXPORTAC__3214EC27083AFBA5 | CLUSTERED | True | True | ID | 1 | False |

## dbo.EXPORTACAO_AFD_REGISTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_EXPORTACAO | int | 4 | 10/0 | False | False | False |
| NSR | varchar | 20 | 0/0 | False | False | False |
| DATA_MARCACAO | datetime | 8 | 23/3 | False | False | False |
| PIS | varchar | 20 | 0/0 | False | False | False |
| TIPO_MOVIMENTO | varchar | 2 | 0/0 | False | False | False |
| DESCRICAO_MOVIMENTO | varchar | 50 | 0/0 | True | False | False |
| STATUS_REGISTRO | tinyint | 1 | 3/0 | False | False | False |
| DATA_PROCESSAMENTO | datetime | 8 | 23/3 | False | False | False |
| HASH_UNICO | varchar | 64 | 0/0 | True | False | False |
| OBSERVACAO | varchar | 500 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IDX_EXP_REG_DATA | NONCLUSTERED | False | False | DATA_MARCACAO | 1 | False |
| IDX_EXP_REG_EXPORTACAO | NONCLUSTERED | False | False | ID_EXPORTACAO | 1 | False |
| IDX_EXP_REG_NSR | NONCLUSTERED | False | False | NSR | 1 | False |
| IDX_EXP_REG_PIS | NONCLUSTERED | False | False | PIS | 1 | False |
| IDX_EXP_REG_UNICO | NONCLUSTERED | True | False | NSR | 1 | False |
| IDX_EXP_REG_UNICO | NONCLUSTERED | True | False | PIS | 2 | False |
| IDX_EXP_REG_UNICO | NONCLUSTERED | True | False | DATA_MARCACAO | 3 | False |
| IDX_EXP_REG_UNICO | NONCLUSTERED | True | False | TIPO_MOVIMENTO | 4 | False |
| PK__EXPORTAC__3214EC27A8A74853 | CLUSTERED | True | True | ID | 1 | False |

- ID_EXPORTACAO → dbo.EXPORTACAO_AFD.ID (FK_EXP_REG_EXPORTACAO); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.Face_Controlid

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| face | varbinary | -1 | 0/0 | True | False | False |
| timestamp | int | 4 | 10/0 | True | False | False |
| TipoPessoa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Face_Controlid | CLUSTERED | True | True | id | 1 | False |

## dbo.FacePessoa

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FacePessoa_IdPessoa | NONCLUSTERED | False | False | IdPessoa | 1 | False |
| PK_FacePessoa | CLUSTERED | True | True | id | 1 | False |

## dbo.FaixaAcessoColetores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idcoletor | int | 4 | 10/0 | False | False | False |
| funcaocoletor | int | 4 | 10/0 | False | False | False |
| nrocracha | nvarchar | 30 | 0/0 | False | False | False |
| status | int | 4 | 10/0 | True | False | False |
| mensagem | nvarchar | 1000 | 0/0 | True | False | False |
| qtdeacesso | int | 4 | 10/0 | True | False | False |
| excluir | nchar | 2 | 0/0 | True | False | False |
| DiasSemana | nvarchar | 100 | 0/0 | True | False | False |
| tipoacesso | int | 4 | 10/0 | True | False | False |
| datahorainicio | datetime | 8 | 23/3 | True | False | False |
| datahoratermino | datetime | 8 | 23/3 | True | False | False |
| Veiculo | int | 4 | 10/0 | True | False | False |
| origem | nvarchar | 4 | 0/0 | False | False | False |
| IdAcessoAutorizado | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | nrocracha | 1 | False |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | idcoletor | 2 | False |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | funcaocoletor | 3 | False |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | datahorainicio | 4 | False |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | datahoratermino | 5 | False |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | status | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | mensagem | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | qtdeacesso | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | excluir | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | DiasSemana | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | tipoacesso | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | Veiculo | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | origem | 0 | True |
| IX_FaixaAcesso_Decisao | NONCLUSTERED | False | False | IdAcessoAutorizado | 0 | True |
| PK_FaixaAcessoColetores | CLUSTERED | True | True | id | 1 | False |

## dbo.faixadecrachas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| faixa_inicio | varchar | 255 | 0/0 | False | False | False |
| faixa_fim | varchar | 255 | 0/0 | False | False | False |
| registro | datetime | 8 | 23/3 | False | False | False |
| encerramento | datetime | 8 | 23/3 | True | False | False |
| tipo | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__faixadec__3213E83FBD1D3948 | CLUSTERED | True | True | id | 1 | False |

## dbo.FilaComandos

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| DataHora | datetime | 8 | 23/3 | False | False | False |
| IdColetor | int | 4 | 10/0 | False | False | False |
| Comando | int | 4 | 10/0 | False | False | False |
| Ordem | int | 4 | 10/0 | False | False | False |
| Prioridade | int | 4 | 10/0 | False | False | False |
| Tipo | int | 4 | 10/0 | True | False | False |
| IdFiltro | int | 4 | 10/0 | True | False | False |
| Pessoas | nvarchar | -1 | 0/0 | True | False | False |
| PreCadastros | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | IdColetor | 1 | False |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | Prioridade | 2 | False |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | Ordem | 3 | False |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | id | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | Comando | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | Tipo | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | IdFiltro | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | Pessoas | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | DataHora | 0 | True |
| IX_FilaComandos_IdColetor_Prioridade_Ordem | NONCLUSTERED | False | False | PreCadastros | 0 | True |
| PK_FilaComandos | CLUSTERED | True | True | id | 1 | False |

- IdColetor → dbo.Coletores.id (FK_FilaComandos); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.FilaComandosCrachas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| IdFilaComando | int | 4 | 10/0 | False | False | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| IdCracha | nvarchar | 30 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_FilaComandosCrachas | CLUSTERED | True | True | id | 1 | False |

- IdFilaComando → dbo.FilaComandos.id (FK_FilaComandosCrachas); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Filtros

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 200 | 0/0 | False | False | False |
| SQLFiltro | nvarchar | -1 | 0/0 | True | False | False |
| setores | nvarchar | -1 | 0/0 | True | False | False |
| pessoas | nvarchar | -1 | 0/0 | True | False | False |
| precadastros | nvarchar | -1 | 0/0 | True | False | False |
| idsPrecadastro | nvarchar | 510 | 0/0 | True | False | False |
| unidades | nvarchar | -1 | 0/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Filtros | CLUSTERED | True | True | id | 1 | False |

## dbo.FILTROS_PESSOAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_filtro | int | 4 | 10/0 | False | False | False |
| id_pessoa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_FILTROS_PESSOAS | CLUSTERED | True | True | id_filtro | 1 | False |
| PK_FILTROS_PESSOAS | CLUSTERED | True | True | id_pessoa | 2 | False |

- id_filtro → dbo.Filtros.id (FK_FILTROS_PESSOAS_Filtros); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_pessoa → dbo.Pessoas.id (FK_FILTROS_PESSOAS_Pessoas); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.FORMATOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| NOME | nvarchar | 100 | 0/0 | False | False | False |
| DESCRICAO | nvarchar | 400 | 0/0 | False | False | False |
| STATUS | int | 4 | 10/0 | False | False | False |
| IDEMPRESA | int | 4 | 10/0 | False | False | False |
| CONFIGURACAO | nvarchar | -1 | 0/0 | True | False | False |
| SEPARADOR | nvarchar | 20 | 0/0 | True | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |
| DATAALTERACAO | datetime | 8 | 23/3 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FORMATOS_IDEMPRESA | NONCLUSTERED | False | False | IDEMPRESA | 1 | False |
| IX_FORMATOS_NOME | NONCLUSTERED | False | False | NOME | 1 | False |
| IX_FORMATOS_STATUS | NONCLUSTERED | False | False | STATUS | 1 | False |
| PK_FORMATOS | CLUSTERED | True | True | ID | 1 | False |

## dbo.HISTORICO_ACESSO_RAPIDO_REG

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_acesso_rapido | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_selecao | varchar | -1 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| data_hora_inicial | datetime | 8 | 23/3 | False | False | False |
| data_hora_final | datetime | 8 | 23/3 | False | False | False |
| tipo_selecao | int | 4 | 10/0 | False | False | False |
| tipo_sentido | int | 4 | 10/0 | False | False | False |
| coletores | varchar | -1 | 0/0 | True | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_ACESSO_RAPIDO_REG_DATA_HORA_OPERACAO | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_HIST_ACESSO_RAPIDO_REG_ID_ACESSO_RAPIDO | NONCLUSTERED | False | False | id_acesso_rapido | 1 | False |
| IX_HIST_ACESSO_RAPIDO_REG_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_ACESSO_RAPIDO_REG_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| IX_HistoricoAcessoRapidoReg_IdEmpresa | NONCLUSTERED | False | False | id_empresa | 1 | False |
| PK__HISTORIC__3213E83F781FC13A | CLUSTERED | True | True | id | 1 | False |

- id_acesso_rapido → dbo.HistoricoAcessoRapido.Id (FK_HIST_ACESSO_RAPIDO_REG_ACESSO_RAPIDO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_ACESSO_RAPIDO_REG_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HistoricoAcessoRapidoReg_Empresas); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_ACESSUSSYNC_AGENDAMENTOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_acessussync_agendamentos | int | 4 | 10/0 | False | False | False |
| id_tarefa | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | nvarchar | 500 | 0/0 | False | False | False |
| horarios | nvarchar | -1 | 0/0 | False | False | False |
| diassemanas | nvarchar | 500 | 0/0 | False | False | False |
| periodicamente | int | 4 | 10/0 | True | False | False |
| status | bit | 1 | 1/0 | False | False | False |
| tipo_operacao | nchar | 2 | 0/0 | False | False | False |
| observacao | nvarchar | 1000 | 0/0 | True | False | False |
| ip_maquina | nvarchar | 90 | 0/0 | True | False | False |
| nome_maquina | nvarchar | 200 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_ACESSUSSYNC_AGENDAMENTOS | CLUSTERED | True | True | id | 1 | False |

- id_acessussync_agendamentos → dbo.AcessusSyncAgendamento.id (FK_HIST_ACESSUSSYNC_AGENDAMENTOS_ACESSUSSYNCAGENDAMENTO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_tarefa → dbo.AcessusSyncTarefas.id (FK_HIST_ACESSUSSYNC_AGENDAMENTOS_ACESSUSSYNCTAREFAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_ACESSUSSYNC_AGENDAMENTOS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_ACESSUSSYNC_AGENDAMENTOS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_ACESSUSSYNC_TAREFAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_acessussync_tarefas | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | nvarchar | 400 | 0/0 | False | False | False |
| tipo | int | 4 | 10/0 | False | False | False |
| opcoes | nvarchar | -1 | 0/0 | True | False | False |
| status | bit | 1 | 1/0 | False | False | False |
| tipo_operacao | nchar | 2 | 0/0 | False | False | False |
| observacao | nvarchar | 1000 | 0/0 | True | False | False |
| ip_maquina | nvarchar | 90 | 0/0 | True | False | False |
| nome_maquina | nvarchar | 200 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_ACESSUSSYNC_TAREFAS | CLUSTERED | True | True | id | 1 | False |

- id_acessussync_tarefas → dbo.AcessusSyncTarefas.id (FK_HIST_ACESSUSSYNC_TAREFAS_ACESSUSSYNCTAREFAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_ACESSUSSYNC_TAREFAS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_ACESSUSSYNC_TAREFAS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_ALUNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_aluno | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| email | varchar | 150 | 0/0 | True | False | False |
| nascimento | datetime | 8 | 23/3 | False | False | False |
| sexo | char | 1 | 0/0 | False | False | False |
| cpf | char | 11 | 0/0 | True | False | False |
| matricula | bigint | 8 | 19/0 | False | False | False |
| data_matricula | datetime | 8 | 23/3 | False | False | False |
| nivel_ensino | int | 4 | 10/0 | False | False | False |
| serie_ano | char | 10 | 0/0 | False | False | False |
| observacao_aluno | text | 16 | 0/0 | True | False | False |
| id_turma | int | 4 | 10/0 | True | False | False |
| ids_responsaveis | varchar | -1 | 0/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_ALUNOS_CPF | NONCLUSTERED | False | False | cpf | 1 | False |
| IX_HIST_ALUNOS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_ALUNOS_ID_ALUNO | NONCLUSTERED | False | False | id_aluno | 1 | False |
| IX_HIST_ALUNOS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_ALUNOS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK_HIST_ALUNOS | CLUSTERED | True | True | id | 1 | False |

- id_aluno → dbo.ALUNOS.id (FK_HIST_ALUNOS_ALUNO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_ALUNOS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_CARDAPIOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_cardapio | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_refeitorio | int | 4 | 10/0 | True | False | False |
| nome | varchar | 255 | 0/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |
| valor_reserva_com_consumo | decimal | 9 | 10/2 | False | False | False |
| valor_reserva_sem_consumo | decimal | 9 | 10/2 | False | False | False |
| valor_consumo_sem_reserva | decimal | 9 | 10/2 | False | False | False |
| tempo_desconsiderar | int | 4 | 10/0 | False | False | False |
| hora_ini | time | 5 | 16/7 | False | False | False |
| hora_fim | time | 5 | 16/7 | False | False | False |
| hora_ini_reserva | time | 5 | 16/7 | False | False | False |
| hora_fim_reserva | time | 5 | 16/7 | False | False | False |
| id_exportacao | varchar | 50 | 0/0 | True | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_CARDAPIOS_DATA_HORA_OPERACAO | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_HIST_CARDAPIOS_ID_CARDAPIO | NONCLUSTERED | False | False | id_cardapio | 1 | False |
| IX_HIST_CARDAPIOS_ID_EMPRESA | NONCLUSTERED | False | False | id_empresa | 1 | False |
| IX_HIST_CARDAPIOS_ID_REF | NONCLUSTERED | False | False | id_refeitorio | 1 | False |
| IX_HIST_CARDAPIOS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_CARDAPIOS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83F335A1083 | CLUSTERED | True | True | id | 1 | False |

- id_cardapio → dbo.cardapios.id (FK_HIST_CARDAPIOS_CARDAPIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_CARDAPIOS_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_refeitorio → dbo.Refeitorios.id (FK_HIST_CARDAPIOS_REF); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_CARDAPIOS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_CREDENCIAIS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_credencial | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| codigo | varchar | 50 | 0/0 | False | False | False |
| tipo_cracha | int | 4 | 10/0 | False | False | False |
| tipo_uso | int | 4 | 10/0 | False | False | False |
| id_pessoa | int | 4 | 10/0 | True | False | False |
| id_precadastro | int | 4 | 10/0 | True | False | False |
| id_veiculo | int | 4 | 10/0 | True | False | False |
| data_hora_registro | datetime | 8 | 23/3 | False | False | False |
| data_hora_encerramento | datetime | 8 | 23/3 | True | False | False |
| nome_pessoa | varchar | 255 | 0/0 | True | False | False |
| nome_veiculo | varchar | 255 | 0/0 | True | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_CREDENCIAIS_CODIGO | NONCLUSTERED | False | False | codigo | 1 | False |
| IX_HIST_CREDENCIAIS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_CREDENCIAIS_ID_CREDENCIAL | NONCLUSTERED | False | False | id_credencial | 1 | False |
| IX_HIST_CREDENCIAIS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_CREDENCIAIS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83F7D468660 | CLUSTERED | True | True | id | 1 | False |

- id_credencial → dbo.RegCrachas.id (FK_HIST_CREDENCIAIS_CREDENCIAL); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_CREDENCIAIS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_FILA_COMANDOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_fila_comando | int | 4 | 10/0 | False | False | False |
| data_hora_criacao | datetime | 8 | 23/3 | False | False | False |
| data_hora_execucao | datetime | 8 | 23/3 | True | False | False |
| id_coletor | int | 4 | 10/0 | False | False | False |
| nome_coletor | varchar | 100 | 0/0 | False | False | False |
| comando | int | 4 | 10/0 | False | False | False |
| nome_comando | varchar | 50 | 0/0 | False | False | False |
| ordem | int | 4 | 10/0 | False | False | False |
| prioridade | int | 4 | 10/0 | False | False | False |
| nome_prioridade | varchar | 30 | 0/0 | False | False | False |
| tipo | int | 4 | 10/0 | False | False | False |
| nome_tipo | varchar | 30 | 0/0 | False | False | False |
| id_filtro | int | 4 | 10/0 | True | False | False |
| nome_filtro | varchar | 100 | 0/0 | True | False | False |
| pessoas | text | 16 | 0/0 | True | False | False |
| precadastros | text | 16 | 0/0 | True | False | False |
| status | int | 4 | 10/0 | False | False | False |
| nome_status | varchar | 30 | 0/0 | False | False | False |
| mensagem_erro | text | 16 | 0/0 | True | False | False |
| tempo_execucao | int | 4 | 10/0 | False | False | False |
| id_usuario_execucao | int | 4 | 10/0 | False | False | False |
| nome_usuario | varchar | 100 | 0/0 | False | False | False |
| ip_maquina | varchar | 50 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_registro | datetime | 8 | 23/3 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | text | 16 | 0/0 | True | False | False |
| id_responsavel | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__HISTORIC__3213E83F6D9D6540 | CLUSTERED | True | True | id | 1 | False |

## dbo.HISTORICO_FILTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_filtro | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| nome | nvarchar | 200 | 0/0 | False | False | False |
| SQLFiltro | nvarchar | -1 | 0/0 | True | False | False |
| setores | nvarchar | -1 | 0/0 | True | False | False |
| pessoas | nvarchar | -1 | 0/0 | True | False | False |
| precadastros | nvarchar | -1 | 0/0 | True | False | False |
| unidades | nvarchar | -1 | 0/0 | True | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_FILTROS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_FILTROS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_filtro → dbo.Filtros.id (FK_HIST_FILTROS_FILTROS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_FILTROS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_METAH_FILTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 200 | 0/0 | False | False | False |
| setores | varchar | -1 | 0/0 | True | False | False |
| pessoas | varchar | -1 | 0/0 | True | False | False |
| precadastros | varchar | -1 | 0/0 | True | False | False |
| unidades | varchar | -1 | 0/0 | True | False | False |
| id_tarefa | int | 4 | 10/0 | True | False | False |
| id_tipo_filtro | int | 4 | 10/0 | False | False | False |
| descricao | nvarchar | 200 | 0/0 | True | False | False |
| status | int | 4 | 10/0 | False | False | False |
| data_criacao | datetime | 8 | 23/3 | True | False | False |
| data_alteracao | datetime | 8 | 23/3 | True | False | False |
| excluido | varchar | 1 | 0/0 | True | False | False |
| id_filtro | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 100 | 0/0 | True | False | False |
| ip_maquina | varchar | 100 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_FILTRO_FILTRO_DATA | NONCLUSTERED | False | False | id_filtro | 1 | False |
| IX_HIST_FILTRO_FILTRO_DATA | NONCLUSTERED | False | False | data_hora | 2 | False |
| PK_HISTORICO_METAH_FILTROS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_FILTRO_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_filtro → dbo.METAH_FILTROS.ID (FK_HIST_FILTRO_FILTRO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_FILTRO_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_tipo_filtro → dbo.METAH_TIPO_FILTRO.ID (FK_HIST_FILTROS_TIPO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_OPCOES_SINCRONIZACAO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_opcoes_sincronizacao | int | 4 | 10/0 | False | False | False |
| sincronizacao_automatica | bit | 1 | 1/0 | False | False | False |
| tolerancia | int | 4 | 10/0 | False | False | False |
| autorizar_autorizacao_acessos | bit | 1 | 1/0 | False | False | False |
| autorizar_reserva_refeicoes | bit | 1 | 1/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| tipo_operacao | nchar | 2 | 0/0 | False | False | False |
| observacao | nvarchar | 1000 | 0/0 | True | False | False |
| ip_maquina | nvarchar | 90 | 0/0 | True | False | False |
| nome_maquina | nvarchar | 200 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_OPCOES_SINCRONIZACAO | CLUSTERED | True | True | id | 1 | False |

- id_opcoes_sincronizacao → dbo.OPCOES_SINCRONIZACAO.id (FK_HIST_OPCOES_SINCRONIZACAO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_OPCOES_SINCRONIZACAO_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_OPCOES_SINCRONIZACAO_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_OPCOES_SINCRONIZACAO_COLETORES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_opcoes_sincronizacao_coletores | int | 4 | 10/0 | False | False | False |
| id_opcoes_sincronizacao | int | 4 | 10/0 | False | False | False |
| id_coletor | int | 4 | 10/0 | False | False | False |
| tipo_autorizacao | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| status | bit | 1 | 1/0 | False | False | False |
| tipo_operacao | nchar | 2 | 0/0 | False | False | False |
| observacao | nvarchar | 1000 | 0/0 | True | False | False |
| ip_maquina | nvarchar | 90 | 0/0 | True | False | False |
| nome_maquina | nvarchar | 200 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_OPCOES_SINCRONIZACAO_COLETORES | CLUSTERED | True | True | id | 1 | False |

- id_coletor → dbo.Coletores.id (FK_HIST_OPCOES_SINCRONIZACAO_COLETORES_COLETORES); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_OPCOES_SINCRONIZACAO_COLETORES_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_opcoes_sincronizacao → dbo.OPCOES_SINCRONIZACAO.id (FK_HIST_OPCOES_SINCRONIZACAO_COLETORES_OPCOES_SINCRONIZACAO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_OPCOES_SINCRONIZACAO_COLETORES_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_OPCOES_SISTEMA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | varchar | 255 | 0/0 | False | False | False |
| tipo_valor | char | 1 | 0/0 | False | False | False |
| valor_anterior | varchar | 255 | 0/0 | True | False | False |
| valor_novo | varchar | 255 | 0/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__HISTORIC__3213E83FFA6CE5AF | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_OPCOES_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_OPCOES_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_PARAMETROS_SISTEMA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | varchar | 255 | 0/0 | False | False | False |
| tipo_valor | char | 1 | 0/0 | False | False | False |
| valor_anterior | varchar | 255 | 0/0 | True | False | False |
| valor_novo | varchar | 255 | 0/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__HISTORIC__3213E83F6A36A82A | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_PARAM_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_PARAM_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_PESSOAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_pessoa | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| nome | varchar | 255 | 0/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |
| cpf | varchar | 14 | 0/0 | True | False | False |
| data_nascimento | datetime | 8 | 23/3 | True | False | False |
| sexo | varchar | 1 | 0/0 | True | False | False |
| fone | varchar | 20 | 0/0 | True | False | False |
| email | varchar | 255 | 0/0 | True | False | False |
| id_setor | int | 4 | 10/0 | True | False | False |
| id_unidade | int | 4 | 10/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| endereco | varchar | 255 | 0/0 | True | False | False |
| complemento | varchar | 100 | 0/0 | True | False | False |
| cep | varchar | 10 | 0/0 | True | False | False |
| cidade | varchar | 100 | 0/0 | True | False | False |
| uf | varchar | 2 | 0/0 | True | False | False |
| bairro | varchar | 100 | 0/0 | True | False | False |
| numero | varchar | 10 | 0/0 | True | False | False |
| id_exportacao | int | 4 | 10/0 | True | False | False |
| gestor | bit | 1 | 1/0 | True | False | False |
| usuario_login | varchar | 50 | 0/0 | True | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| id_responsavel | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_PESSOAS_CPF | NONCLUSTERED | False | False | cpf | 1 | False |
| IX_HIST_PESSOAS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_PESSOAS_ID_PESSOA | NONCLUSTERED | False | False | id_pessoa | 1 | False |
| IX_HIST_PESSOAS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_PESSOAS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83FD9E1F7BD | CLUSTERED | True | True | id | 1 | False |

- id_pessoa → dbo.Pessoas.id (FK_HIST_PESSOAS_PESSOA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_PESSOAS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_responsavel → dbo.RESPONSAVEIS.id (FK_HISTORICO_PESSOA_RESPONSAVEL); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_PRE_CADASTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_pre_cadastro | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| nome | varchar | 255 | 0/0 | False | False | False |
| telefone | varchar | 20 | 0/0 | True | False | False |
| status | int | 4 | 10/0 | False | False | False |
| cpf | varchar | 14 | 0/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | True | False | False |
| id_exportacao | int | 4 | 10/0 | True | False | False |
| tipo_pessoa | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| empresa_acesso | int | 4 | 10/0 | True | False | False |
| estrangeiro | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_PRE_CADASTROS_CPF | NONCLUSTERED | False | False | cpf | 1 | False |
| IX_HIST_PRE_CADASTROS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_PRE_CADASTROS_ID_PRE_CADASTRO | NONCLUSTERED | False | False | id_pre_cadastro | 1 | False |
| IX_HIST_PRE_CADASTROS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_PRE_CADASTROS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83F3693262F | CLUSTERED | True | True | id | 1 | False |

- empresa_acesso → dbo.EmpresaAcesso.id (FK_HIST_PRE_CADASTROS_EMPRESA_ACESSO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HIST_PRE_CADASTROS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_pre_cadastro → dbo.PreCadastros.Id (FK_HIST_PRE_CADASTROS_PRE_CADASTRO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_PRE_CADASTROS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_REFEICOES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_refeicao | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_coletor | int | 4 | 10/0 | False | False | False |
| id_cardapio | int | 4 | 10/0 | False | False | False |
| funcao | int | 4 | 10/0 | False | False | False |
| tipo_refeicao | int | 4 | 10/0 | False | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| id_pessoa | int | 4 | 10/0 | True | False | False |
| id_pre_cadastro | int | 4 | 10/0 | True | False | False |
| origem | varchar | 10 | 0/0 | False | False | False |
| refeitorio | int | 4 | 10/0 | False | False | False |
| valor_refeicao | decimal | 9 | 10/2 | False | False | False |
| tipo_valor_refeicao | int | 4 | 10/0 | False | False | False |
| utiliza_controle_creditos | bit | 1 | 1/0 | False | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_REFEICOES_DATA_HORA_OPERACAO | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_HIST_REFEICOES_ID_EMPRESA | NONCLUSTERED | False | False | id_empresa | 1 | False |
| IX_HIST_REFEICOES_ID_REF | NONCLUSTERED | False | False | id_refeicao | 1 | False |
| IX_HIST_REFEICOES_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_REFEICOES_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83FCF05BDF8 | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_REFEICOES_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_refeicao → dbo.Refeicoes.Id (FK_HIST_REFEICOES_REF); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_REFEICOES_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_REFEICOES_RESERVAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_reserva | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_gestor | int | 4 | 10/0 | True | False | False |
| id_usuarioliberou | int | 4 | 10/0 | True | False | False |
| id_pessoa | int | 4 | 10/0 | True | False | False |
| id_pre_cadastro | int | 4 | 10/0 | True | False | False |
| id_refeitorio | int | 4 | 10/0 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| datahoraliberacao | datetime | 8 | 23/3 | True | False | False |
| datahora | datetime | 8 | 23/3 | False | False | False |
| credencial | varchar | 50 | 0/0 | False | False | False |
| refeicoes | varchar | 50 | 0/0 | False | False | False |
| idexportacao | int | 4 | 10/0 | True | False | False |
| idfreq | varchar | 100 | 0/0 | True | False | False |
| datahoraini | datetime | 8 | 23/3 | False | False | False |
| datahorafim | datetime | 8 | 23/3 | False | False | False |
| tipopessoa | int | 4 | 10/0 | False | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_RESERVAS_CREDENCIAL | NONCLUSTERED | False | False | credencial | 1 | False |
| IX_HIST_RESERVAS_DATA_HORA_OPERACAO | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_HIST_RESERVAS_ID_EMPRESA | NONCLUSTERED | False | False | id_empresa | 1 | False |
| IX_HIST_RESERVAS_ID_PESSOA | NONCLUSTERED | False | False | id_pessoa | 1 | False |
| IX_HIST_RESERVAS_ID_PRECADASTRO | NONCLUSTERED | False | False | id_pre_cadastro | 1 | False |
| IX_HIST_RESERVAS_ID_RESERVA | NONCLUSTERED | False | False | id_reserva | 1 | False |
| IX_HIST_RESERVAS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_RESERVAS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| IX_Historico_RefeicoesReservas_status | NONCLUSTERED | False | False | status | 1 | False |
| PK__HISTORIC__3213E83FC024C075 | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_RESERVAS_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_gestor → dbo.Pessoas.id (FK_HIST_RESERVAS_GESTOR); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_pessoa → dbo.Pessoas.id (FK_HIST_RESERVAS_PESSOA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_pre_cadastro → dbo.PreCadastros.Id (FK_HIST_RESERVAS_PRECADASTRO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_refeitorio → dbo.Refeitorios.id (FK_HIST_RESERVAS_REF); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_reserva → dbo.RefeicoesReservas.id (FK_HIST_RESERVAS_RESERVA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_RESERVAS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_REFEITORIOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_refeitorio | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| nome | varchar | 255 | 0/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |
| utiliza_controle_creditos | int | 4 | 10/0 | False | False | False |
| id_exportacao | varchar | 50 | 0/0 | True | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |
| sentido_acesso | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_REFEITORIOS_DATA_HORA_OPERACAO | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_HIST_REFEITORIOS_ID_EMPRESA | NONCLUSTERED | False | False | id_empresa | 1 | False |
| IX_HIST_REFEITORIOS_ID_REF | NONCLUSTERED | False | False | id_refeitorio | 1 | False |
| IX_HIST_REFEITORIOS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_REFEITORIOS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK__HISTORIC__3213E83F30AFC20E | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_REFEITORIOS_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_refeitorio → dbo.Refeitorios.id (FK_HIST_REFEITORIOS_REF); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_REFEITORIOS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_REGRAS_ACESSO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_regra_acesso | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| nome | varchar | 255 | 0/0 | False | False | False |
| tipo_regra | int | 4 | 10/0 | False | False | False |
| coletores | varchar | -1 | 0/0 | True | False | False |
| tipo_selecao | int | 4 | 10/0 | False | False | False |
| id_filtro | int | 4 | 10/0 | True | False | False |
| setores | varchar | -1 | 0/0 | True | False | False |
| pessoas | varchar | -1 | 0/0 | True | False | False |
| separar_regra_dia | int | 4 | 10/0 | False | False | False |
| bloquear_sabados | int | 4 | 10/0 | False | False | False |
| bloquear_domingos | int | 4 | 10/0 | False | False | False |
| qtde_acesso | int | 4 | 10/0 | False | False | False |
| considera_pre_cadastro | int | 4 | 10/0 | False | False | False |
| dias_semana | varchar | 50 | 0/0 | True | False | False |
| tipo_acesso | int | 4 | 10/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| data_hora_inicio | datetime | 8 | 23/3 | False | False | False |
| data_hora_termino | datetime | 8 | 23/3 | False | False | False |
| hora_inicio_maior_termino | int | 4 | 10/0 | False | False | False |
| veiculos | varchar | -1 | 0/0 | True | False | False |
| pre_cadastros | varchar | -1 | 0/0 | True | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| personalizar | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_REGRAS_ACESSO_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_REGRAS_ACESSO_ID_REGRA | NONCLUSTERED | False | False | id_regra_acesso | 1 | False |
| IX_HIST_REGRAS_ACESSO_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_REGRAS_ACESSO_NOME | NONCLUSTERED | False | False | nome | 1 | False |
| IX_HIST_REGRAS_ACESSO_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| IX_HistoricoRegrasAcesso_IdEmpresa | NONCLUSTERED | False | False | id_empresa | 1 | False |
| PK__HISTORIC__3213E83FB0082236 | CLUSTERED | True | True | id | 1 | False |

- id_regra_acesso → dbo.RegrasAcesso.id (FK_HIST_REGRAS_ACESSO_REGRA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_REGRAS_ACESSO_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_HistoricoRegrasAcesso_Empresas); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_RESPONSAVEIS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_responsavel | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| email | varchar | 150 | 0/0 | True | False | False |
| nascimento | datetime | 8 | 23/3 | False | False | False |
| sexo | char | 1 | 0/0 | False | False | False |
| cpf | char | 11 | 0/0 | False | False | False |
| ids_alunos | varchar | -1 | 0/0 | True | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_RESPONSAVEIS_CPF | NONCLUSTERED | False | False | cpf | 1 | False |
| IX_HIST_RESPONSAVEIS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_RESPONSAVEIS_ID_RESPONSAVEL | NONCLUSTERED | False | False | id_responsavel | 1 | False |
| IX_HIST_RESPONSAVEIS_ID_USUARIO | NONCLUSTERED | False | False | id_responsavel | 1 | False |
| IX_HIST_RESPONSAVEIS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK_HIST_RESPONSAVEIS | CLUSTERED | True | True | id | 1 | False |

- id_responsavel → dbo.RESPONSAVEIS.id (FK_HIST_RESPONSAVEIS_RESPONSAVEL); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_RESPONSAVEIS_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_TURMAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_turma | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| id_turno | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_TURMAS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_TURMAS_ID_TURMA | NONCLUSTERED | False | False | id_turma | 1 | False |
| IX_HIST_TURMAS_ID_TURNO | NONCLUSTERED | False | False | id_turno | 1 | False |
| IX_HIST_TURMAS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_TURMAS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK_HIST_TURMAS | CLUSTERED | True | True | id | 1 | False |

- id_turma → dbo.TURMAS.id (FK_HIST_TURMAS_ID_TURMA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_TURMAS_ID_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_TURNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_turno | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| situAcao | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_TURNOS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_TURNOS_ID_TURNO | NONCLUSTERED | False | False | id_turno | 1 | False |
| IX_HIST_TURNOS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_TURNOS_TIPO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| PK_HIST_TURNO | CLUSTERED | True | True | id | 1 | False |

- id_turno → dbo.TURNOS.id (FK_HIST_TURNO_ID_TURNO); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_TURNO_ID_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_USUARIOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_usuario_alterou | int | 4 | 10/0 | True | False | False |
| id_empresa_alterou | int | 4 | 10/0 | True | False | False |
| nome | nvarchar | 40 | 0/0 | False | False | False |
| senha | nvarchar | 256 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| permissoes | varchar | 25 | 0/0 | True | False | False |
| administrador | char | 1 | 0/0 | False | False | False |
| permissoes_adicionadas | nvarchar | -1 | 0/0 | True | False | False |
| permissoes_removidas | nvarchar | -1 | 0/0 | True | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora_operacao | datetime | 8 | 23/3 | False | False | False |
| id_coletores | varchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_HIST_USUARIOS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HIST_USUARIOS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa_alterou → dbo.Empresas.id (FK_HIST_USUARIOS_EMPRESAS_id_empresa_alterou); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_HIST_USUARIOS_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario_alterou → dbo.Usuarios.id (FK_HIST_USUARIOS_USUARIOS_id_usuario_alterou); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.HISTORICO_VEICULOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_veiculo | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| placa | varchar | 20 | 0/0 | False | False | False |
| id_pessoa | int | 4 | 10/0 | True | False | False |
| id_precadastro | int | 4 | 10/0 | True | False | False |
| id_tipo_veiculo | int | 4 | 10/0 | True | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |
| id_estacionamento | int | 4 | 10/0 | True | False | False |
| tipo_box_reserva | int | 4 | 10/0 | False | False | False |
| nome | varchar | 255 | 0/0 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |
| veiculo_uso | int | 4 | 10/0 | False | False | False |
| tipo_veiculo_nome | varchar | 50 | 0/0 | False | False | False |
| nome_pessoa | varchar | 255 | 0/0 | True | False | False |
| nome_precadastro | varchar | 255 | 0/0 | True | False | False |
| nome_estacionamento | varchar | 255 | 0/0 | True | False | False |
| tag | varchar | 50 | 0/0 | True | False | False |
| tipo_operacao | char | 1 | 0/0 | False | False | False |
| ip_maquina | varchar | 45 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| data_hora | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HIST_VEICULOS_DATA_HORA | NONCLUSTERED | False | False | data_hora | 1 | False |
| IX_HIST_VEICULOS_ID_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| IX_HIST_VEICULOS_ID_VEICULO | NONCLUSTERED | False | False | id_veiculo | 1 | False |
| IX_HIST_VEICULOS_PLACA | NONCLUSTERED | False | False | placa | 1 | False |
| PK__HISTORIC__3213E83F915CEC74 | CLUSTERED | True | True | id | 1 | False |

## dbo.HistoricoAcessoRapido

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| IdUsuario | int | 4 | 10/0 | False | False | False |
| IdSelecao | nvarchar | 30 | 0/0 | True | False | False |
| DataHora | datetime | 8 | 23/3 | True | False | False |
| DataHoraInicial | datetime | 8 | 23/3 | True | False | False |
| DataHoraFinal | datetime | 8 | 23/3 | True | False | False |
| TipoSelecao | int | 4 | 10/0 | True | False | False |
| TipoSentido | int | 4 | 10/0 | True | False | False |
| Coletores | nvarchar | 500 | 0/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_HistoricoAcessoRapido_IdEmpresa | NONCLUSTERED | False | False | id_empresa | 1 | False |
| PK__Historic__3214EC0751E29A1B | CLUSTERED | True | True | Id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_HistoricoAcessoRapido_Empresas); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Layout

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| Nome | varchar | 100 | 0/0 | False | False | False |
| Campos | varchar | 255 | 0/0 | False | False | False |
| Tamanho | varchar | 255 | 0/0 | False | False | False |
| Formato | varchar | 255 | 0/0 | False | False | False |
| diretorio | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Layout | CLUSTERED | True | True | Id | 1 | False |

## dbo.LayoutExpMarcacoes

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| IdEmpresa | int | 4 | 10/0 | False | False | False |
| Descricao | nvarchar | 300 | 0/0 | False | False | False |
| Campos | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__LayoutEx__3214EC07EDE6062A | CLUSTERED | True | True | Id | 1 | False |

## dbo.Licenca

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| chave | nvarchar | 500 | 0/0 | True | False | False |
| sem_internet | tinyint | 1 | 3/0 | True | False | False |
| sem_servidor | tinyint | 1 | 3/0 | True | False | False |

## dbo.LicencaAtivacoes

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | uniqueidentifier | 16 | 0/0 | False | False | False |
| ChaveLicenca | varchar | 500 | 0/0 | False | False | False |
| ServerName | nvarchar | 200 | 0/0 | False | False | False |
| ActivationDate | datetime | 8 | 23/3 | False | False | False |
| ComputerFingerprint | varchar | 100 | 0/0 | False | False | False |
| TerminalName | nvarchar | 200 | 0/0 | True | False | False |
| IsServerActivation | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_LicencaAtivacoes_ChaveLicenca | NONCLUSTERED | False | False | ChaveLicenca | 1 | False |
| IX_LicencaAtivacoes_ServerName | NONCLUSTERED | False | False | ServerName | 1 | False |
| PK__LicencaA__3214EC27866AB928 | CLUSTERED | True | True | ID | 1 | False |

## dbo.MarcacoesOnline

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| datahora | datetime | 8 | 23/3 | False | False | False |
| idCracha | nvarchar | 30 | 0/0 | False | False | False |
| funcao | int | 4 | 10/0 | False | False | False |
| idcoletor | int | 4 | 10/0 | False | False | False |
| sentido | tinyint | 1 | 3/0 | False | False | False |
| tipocoleta | int | 4 | 10/0 | False | False | False |
| situacao | tinyint | 1 | 3/0 | False | False | False |
| msg | nvarchar | 60 | 0/0 | True | False | False |
| IMPORTADA | nvarchar | 2 | 0/0 | True | False | False |
| idpessoa | bigint | 8 | 19/0 | True | False | False |
| idVisitantesTerceirosHistoricos | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_MarcacoesOnline_Duplicatas | NONCLUSTERED | False | False | datahora | 1 | False |
| IX_MarcacoesOnline_Duplicatas | NONCLUSTERED | False | False | idCracha | 2 | False |
| IX_MarcacoesOnline_Duplicatas | NONCLUSTERED | False | False | idcoletor | 3 | False |
| IX_MarcacoesOnline_Duplicatas | NONCLUSTERED | False | False | sentido | 4 | False |
| IX_MarcacoesOnline_Duplicatas | NONCLUSTERED | False | False | situacao | 5 | False |
| IX_MarcacoesOnline_QtdeAcesso | NONCLUSTERED | False | False | idcoletor | 1 | False |
| IX_MarcacoesOnline_QtdeAcesso | NONCLUSTERED | False | False | sentido | 2 | False |
| IX_MarcacoesOnline_QtdeAcesso | NONCLUSTERED | False | False | situacao | 3 | False |
| IX_MarcacoesOnline_QtdeAcesso | NONCLUSTERED | False | False | datahora | 4 | False |
| IX_MarcacoesOnline_QtdeAcesso | NONCLUSTERED | False | False | idCracha | 0 | True |
| PK_MarcacoesOnline | CLUSTERED | True | True | id | 1 | False |

- idcoletor → dbo.Coletores.id (FK_ColMarcacoesOnline); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.MarcaColetores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | nvarchar | 10 | 0/0 | False | False | False |
| nome | varchar | 50 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_MarcaColetores | CLUSTERED | True | True | id | 1 | False |

## dbo.MensagemColetores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | varchar | 255 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_MensagemId | CLUSTERED | True | True | id | 1 | False |

## dbo.METAH_FILTRO_PESSOAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_FILTRO | int | 4 | 10/0 | False | False | False |
| ID_PESSOA | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FILTRO_PESSOAS_ID_FILTRO | NONCLUSTERED | False | False | ID_FILTRO | 1 | False |
| IX_FILTRO_PESSOAS_ID_PESSOA | NONCLUSTERED | False | False | ID_PESSOA | 1 | False |
| PK__METAH_FI__3214EC27E37134B2 | CLUSTERED | True | True | ID | 1 | False |

- ID_FILTRO → dbo.METAH_FILTROS.ID (FK_FILTRO_PESSOAS_FILTRO); exclusão: CASCADE; desabilitada: False; não validada: False.
- ID_PESSOA → dbo.Pessoas.id (FK_FILTRO_PESSOAS_PESSOA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_FILTRO_PRECADASTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_FILTRO | int | 4 | 10/0 | False | False | False |
| ID_PRECADASTRO | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FILTRO_PRECADASTROS_ID_FILTRO | NONCLUSTERED | False | False | ID_FILTRO | 1 | False |
| PK__METAH_FI__3214EC27D5D1DA2E | CLUSTERED | True | True | ID | 1 | False |

- ID_FILTRO → dbo.METAH_FILTROS.ID (FK_FILTRO_PRECADASTROS_FILTRO); exclusão: CASCADE; desabilitada: False; não validada: False.
- ID_PRECADASTRO → dbo.PreCadastros.Id (FK_FILTRO_PRECADASTROS_PRECADASTROS); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_FILTRO_SETORES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_FILTRO | int | 4 | 10/0 | False | False | False |
| ID_SETOR | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FILTRO_SETORES_ID_FILTRO | NONCLUSTERED | False | False | ID_FILTRO | 1 | False |
| PK__METAH_FI__3214EC275265C6B8 | CLUSTERED | True | True | ID | 1 | False |

- ID_FILTRO → dbo.METAH_FILTROS.ID (FK_FILTRO_SETORES_FILTRO); exclusão: CASCADE; desabilitada: False; não validada: False.
- ID_SETOR → dbo.Setores.id (FK_FILTRO_SETORES_SETOR); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_FILTRO_UNIDADES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_FILTRO | int | 4 | 10/0 | False | False | False |
| ID_UNIDADE | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FILTRO_UNIDADES_ID_FILTRO | NONCLUSTERED | False | False | ID_FILTRO | 1 | False |
| PK__METAH_FI__3214EC27467A9048 | CLUSTERED | True | True | ID | 1 | False |

- ID_FILTRO → dbo.METAH_FILTROS.ID (FK_FILTRO_UNIDADES_FILTRO); exclusão: CASCADE; desabilitada: False; não validada: False.
- ID_UNIDADE → dbo.Unidades.id (FK_FILTRO_UNIDADES_UNIDADE); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_FILTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_TAREFA | int | 4 | 10/0 | True | False | False |
| ID_TIPO_FILTRO | int | 4 | 10/0 | False | False | False |
| NOME | nvarchar | 200 | 0/0 | False | False | False |
| DESCRICAO | nvarchar | 1000 | 0/0 | True | False | False |
| STATUS | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |
| DATAALTERACAO | datetime | 8 | 23/3 | True | False | False |
| EXCLUIDO | varchar | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_FILTROS_ID_TAREFA | NONCLUSTERED | False | False | ID_TAREFA | 1 | False |
| IX_FILTROS_ID_TIPO_FILTRO | NONCLUSTERED | False | False | ID_TIPO_FILTRO | 1 | False |
| PK__METAH_FI__3214EC27402E516B | CLUSTERED | True | True | ID | 1 | False |

- ID_TIPO_FILTRO → dbo.METAH_TIPO_FILTRO.ID (FK_FILTROS_TIPO_FILTRO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.METAH_TAREFA_DIAS_MES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_TAREFA | int | 4 | 10/0 | False | False | False |
| DIA_MES | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TA__3214EC27CB88E247 | CLUSTERED | True | True | ID | 1 | False |

- ID_TAREFA → dbo.METAH_TAREFAS.ID (FK__METAH_TAR__ID_TA__2062B9C8); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_TAREFA_DIAS_SEMANA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_TAREFA | int | 4 | 10/0 | False | False | False |
| DIA_SEMANA | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TA__3214EC27767A7620 | CLUSTERED | True | True | ID | 1 | False |

- ID_TAREFA → dbo.METAH_TAREFAS.ID (FK__METAH_TAR__ID_TA__1D864D1D); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_TAREFA_EQUIPAMENTOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_TAREFA | int | 4 | 10/0 | False | False | False |
| ID_EQUIPAMENTO | int | 4 | 10/0 | False | False | False |
| CAMINHO_AFD | nvarchar | 1000 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TA__3214EC277252D18D | CLUSTERED | True | True | ID | 1 | False |

- ID_TAREFA → dbo.METAH_TAREFAS.ID (FK__METAH_TAR__ID_TA__17CD73C7); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_TAREFA_FILTROS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID_TAREFA | int | 4 | 10/0 | False | False | False |
| ID_FILTRO | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_METAH_TAREFA_FILTROS | CLUSTERED | True | True | ID_TAREFA | 1 | False |
| PK_METAH_TAREFA_FILTROS | CLUSTERED | True | True | ID_FILTRO | 2 | False |

- ID_FILTRO → dbo.METAH_FILTROS.ID (FK_TAREFA_FILTROS_FILTRO); exclusão: CASCADE; desabilitada: False; não validada: False.
- ID_TAREFA → dbo.METAH_TAREFAS.ID (FK_TAREFA_FILTROS_TAREFA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_TAREFA_HORARIOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| ID_TAREFA | int | 4 | 10/0 | False | False | False |
| HORARIO | char | 5 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TA__3214EC278751C2D6 | CLUSTERED | True | True | ID | 1 | False |

- ID_TAREFA → dbo.METAH_TAREFAS.ID (FK__METAH_TAR__ID_TA__1AA9E072); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.METAH_TAREFAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| DESCRICAO | nvarchar | 200 | 0/0 | False | False | False |
| TIPO_ACAO | int | 4 | 10/0 | False | False | False |
| ID_USUARIO | int | 4 | 10/0 | False | False | False |
| ID_EMPRESA | int | 4 | 10/0 | False | False | False |
| STATUS | int | 4 | 10/0 | False | False | False |
| FREQUENCIA | int | 4 | 10/0 | False | False | False |
| MESMO_CAMINHO_AFD | bit | 1 | 1/0 | False | False | False |
| TIPO_AFD | int | 4 | 10/0 | False | False | False |
| FORMATO_CUSTOMIZADO | nvarchar | -1 | 0/0 | True | False | False |
| CAMINHO_UNICO_AFD | nvarchar | 1000 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TA__3214EC278D989964 | CLUSTERED | True | True | ID | 1 | False |

## dbo.METAH_TIPO_FILTRO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| NOME | nvarchar | 100 | 0/0 | False | False | False |
| STATUS | int | 4 | 10/0 | False | False | False |
| DATACRIACAO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__METAH_TI__3214EC27E291FA5B | CLUSTERED | True | True | ID | 1 | False |

## dbo.MODELO_EQUIPAMENTOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | True | False |
| NOME | varchar | 100 | 0/0 | False | False | False |
| TIPO | int | 4 | 10/0 | False | False | False |
| DESCRICAO | varchar | 255 | 0/0 | True | False | False |
| ATIVO | int | 4 | 10/0 | False | False | False |
| DATACADASTRO | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IDX_MODELO_EQUIPAMENTOS_TIPO | NONCLUSTERED | False | False | TIPO | 1 | False |
| PK_MODELO_EQUIPAMENTOS | CLUSTERED | True | True | ID | 1 | False |
| UK_MODELO_EQUIPAMENTOS_NOME | NONCLUSTERED | True | False | NOME | 1 | False |

## dbo.ModeloColetores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idmarca | nvarchar | 10 | 0/0 | False | False | False |
| nome | nvarchar | 40 | 0/0 | False | False | False |
| sinaldecimal | int | 4 | 10/0 | True | False | False |
| formatocampos | int | 4 | 10/0 | True | False | False |
| caracsepara | nchar | 2 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ModeloColetores | CLUSTERED | True | True | id | 1 | False |

- idmarca → dbo.MarcaColetores.id (FK_ModeloCol_Marca); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ModeloColLayout

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idmodelo | int | 4 | 10/0 | False | False | False |
| layout | int | 4 | 10/0 | False | False | False |
| ordem | int | 4 | 10/0 | False | False | False |
| campo | nvarchar | 30 | 0/0 | False | False | False |
| tipo | int | 4 | 10/0 | False | False | False |
| tamanho | int | 4 | 10/0 | True | False | False |
| formato | nvarchar | 30 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_ModeloColLayout | CLUSTERED | True | True | id | 1 | False |

- idmodelo → dbo.ModeloColetores.id (FK_ModeloColLayout); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.ModulosPermissoes

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| Modulo | nvarchar | 100 | 0/0 | False | False | False |
| ID_Usuario | int | 4 | 10/0 | False | False | False |
| Menu | nvarchar | 200 | 0/0 | False | False | False |
| Permissao | tinyint | 1 | 3/0 | False | False | False |
| DataHora | datetime | 8 | 23/3 | False | False | False |
| Id_Usuario_Liberou | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__ModulosP__3214EC077771648D | CLUSTERED | True | True | Id | 1 | False |

- ID_Usuario → dbo.Usuarios.id (FK_ModulosPermissoes_Usuarios); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.Ocorrencias

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Nome | nvarchar | 200 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdOcorrencias | CLUSTERED | True | True | id | 1 | False |

## dbo.OPCOES_SINCRONIZACAO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| sincronizacao_automatica | bit | 1 | 1/0 | False | False | False |
| tolerancia | int | 4 | 10/0 | False | False | False |
| autorizar_autorizacao_acessos | bit | 1 | 1/0 | False | False | False |
| autorizar_reserva_refeicoes | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_OPCOES_SINCRONIZACAO | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_OPCOES_SINCRONIZACAO_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_OPCOES_SINCRONIZACAO_USUARIOS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.OPCOES_SINCRONIZACAO_COLETORES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_opcoes_sincronizacao | int | 4 | 10/0 | False | False | False |
| id_coletor | int | 4 | 10/0 | False | False | False |
| tipo_autorizacao | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| status | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_OPCOES_SINCRONIZACAO_COLETORES | CLUSTERED | True | True | id | 1 | False |

- id_coletor → dbo.Coletores.id (FK_OPCOES_SINCRONIZACAO_COLETORES_COLETORES); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_OPCOES_SINCRONIZACAO_COLETORES_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_opcoes_sincronizacao → dbo.OPCOES_SINCRONIZACAO.id (FK_OPCOES_SINCRONIZACAO_COLETORES_OPCOES_SINCRONIZACAO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.OPCOES_SISTEMA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | varchar | 255 | 0/0 | False | False | False |
| tipo_valor | char | 1 | 0/0 | False | False | False |
| valor | varchar | 255 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__OPCOES_S__3213E83F561E8762 | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_OPCOES_SISTEMA_EMPRESA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.parametros

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | nvarchar | 100 | 0/0 | False | False | False |
| valor | nvarchar | 200 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_parametros | CLUSTERED | True | True | id | 1 | False |

## dbo.PARAMETROS_SISTEMA

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| descricao | varchar | 255 | 0/0 | False | False | False |
| tipo_valor | char | 1 | 0/0 | False | False | False |
| valor | varchar | 255 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__PARAMETR__3213E83F808DBF44 | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_PARAMETROS_SISTEMA_EMPRESA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesAcesso

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| RegistroCrachas | tinyint | 1 | 3/0 | False | False | False |
| FaixaCrachas | tinyint | 1 | 3/0 | False | False | False |
| RegrasAcesso | tinyint | 1 | 3/0 | False | False | False |
| AfastamentosCedidos | tinyint | 1 | 3/0 | False | False | False |
| GerarAcesso | tinyint | 1 | 3/0 | False | False | False |
| AcessoRapido | tinyint | 1 | 3/0 | False | False | False |
| AutorizacaoAcessos | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesAcesso_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesAcesso_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesCadastro

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| Empresas | tinyint | 1 | 3/0 | False | False | False |
| Usuarios | tinyint | 1 | 3/0 | False | False | False |
| Unidades | tinyint | 1 | 3/0 | False | False | False |
| Setores | tinyint | 1 | 3/0 | False | False | False |
| Pessoas | tinyint | 1 | 3/0 | False | False | False |
| VisTerPrecad | tinyint | 1 | 3/0 | False | False | False |
| Filtros | tinyint | 1 | 3/0 | False | False | False |
| DigitaisFaces | tinyint | 1 | 3/0 | False | False | False |
| ModeloColetores | tinyint | 1 | 3/0 | False | False | False |
| CadastroColetores | tinyint | 1 | 3/0 | False | False | False |
| MensagemColetores | tinyint | 1 | 3/0 | False | False | False |
| EmpresaAcesso | tinyint | 1 | 3/0 | False | False | False |
| VisitantesTerceiros | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesCadastro_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesCadastro_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesComunicacao

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| ComandosComEquipamentos | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesComunicacao_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesComunicacao_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesConsulta

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| MarcacoesOnline | tinyint | 1 | 3/0 | False | False | False |
| AcessoPorPessoa | tinyint | 1 | 3/0 | False | False | False |
| StatusConexao | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesConsulta_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesConsulta_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesFerramentas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| ImportadorExportador | tinyint | 1 | 3/0 | False | False | False |
| LayoutExportacao | tinyint | 1 | 3/0 | False | False | False |
| ExportacaoCSV | tinyint | 1 | 3/0 | False | False | False |
| Etiqueta | tinyint | 1 | 3/0 | False | False | False |
| Importacao | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesFerramentas_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesFerramentas_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesRefeitorio

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| Refeitorios | tinyint | 1 | 3/0 | False | False | False |
| Cardapios | tinyint | 1 | 3/0 | False | False | False |
| Refeicoes | tinyint | 1 | 3/0 | False | False | False |
| Creditos | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesRefeitorio_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesRefeitorio_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesRelatorio

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| Crachas | tinyint | 1 | 3/0 | False | False | False |
| Inconsistencias | tinyint | 1 | 3/0 | False | False | False |
| Pessoas | tinyint | 1 | 3/0 | False | False | False |
| Setores | tinyint | 1 | 3/0 | False | False | False |
| Unidades | tinyint | 1 | 3/0 | False | False | False |
| Empresas | tinyint | 1 | 3/0 | False | False | False |
| PreCadastros | tinyint | 1 | 3/0 | False | False | False |
| ReservasConsumos | tinyint | 1 | 3/0 | False | False | False |
| MarcacoesOnline | tinyint | 1 | 3/0 | False | False | False |
| AcessosVisitantesTerceiros | tinyint | 1 | 3/0 | False | False | False |
| AvaliacaoRefeicao | tinyint | 1 | 3/0 | False | False | False |
| Creditos | tinyint | 1 | 3/0 | False | False | False |
| ReservasRefeicoes | tinyint | 1 | 3/0 | False | False | False |
| RefeicoesTotal | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesRelatorio_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesRelatorio_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PermissoesReserva

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | False | False |
| ReservasRefeicoes | tinyint | 1 | 3/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PermissoesReserva_Id | CLUSTERED | True | True | Id | 1 | False |

- Id → dbo.Usuarios.id (FK_PermissoesReserva_Usuarios_Id); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.Pessoas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 200 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | False | False | False |
| cpf | nvarchar | 30 | 0/0 | True | False | False |
| sexo | nchar | 2 | 0/0 | True | False | False |
| fone | nvarchar | 40 | 0/0 | True | False | False |
| email | nvarchar | 100 | 0/0 | True | False | False |
| idsetor | int | 4 | 10/0 | True | False | False |
| idempresa | int | 4 | 10/0 | False | False | False |
| endereco | nvarchar | 120 | 0/0 | True | False | False |
| complemento | nvarchar | 120 | 0/0 | True | False | False |
| cep | nvarchar | 20 | 0/0 | True | False | False |
| cidade | nvarchar | 80 | 0/0 | True | False | False |
| uf | nvarchar | 4 | 0/0 | True | False | False |
| bairro | nvarchar | 120 | 0/0 | True | False | False |
| numero | nvarchar | 20 | 0/0 | True | False | False |
| IdExportacao | int | 4 | 10/0 | True | False | False |
| idUnidade | varchar | 10 | 0/0 | True | False | False |
| gestor | int | 4 | 10/0 | True | False | False |
| login | nvarchar | 100 | 0/0 | True | False | False |
| senha | nvarchar | 30 | 0/0 | True | False | False |
| datacadastro | datetime | 8 | 23/3 | True | False | False |
| datanascimento | datetime | 8 | 23/3 | True | False | False |
| DataUltimaAlteracao | datetime | 8 | 23/3 | True | False | False |
| ContratoExportacao | int | 4 | 10/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |
| id_responsavel | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_Pessoas_IdResponsavel | NONCLUSTERED | False | False | id_responsavel | 1 | False |
| IX_Pessoas_IdResponsavel | NONCLUSTERED | False | False | status | 2 | False |
| IX_Pessoas_IdResponsavel | NONCLUSTERED | False | False | excluido | 3 | False |
| IX_Pessoas_IdResponsavel | NONCLUSTERED | False | False | id | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | status | 1 | False |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | excluido | 2 | False |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | id | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | nome | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | cpf | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | datanascimento | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | sexo | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | idsetor | 0 | True |
| IX_Pessoas_Status_Excluido | NONCLUSTERED | False | False | idempresa | 0 | True |
| PK_Pessoas | CLUSTERED | True | True | id | 1 | False |

- id_responsavel → dbo.RESPONSAVEIS.id (FK_PESSOA_RESPONSAVEL); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- idsetor → dbo.Setores.id (FK_Pessoas_Setores); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.PreCadastros

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| Nome | varchar | 100 | 0/0 | False | False | False |
| Pis | varchar | 12 | 0/0 | True | False | False |
| Cpf | varchar | 15 | 0/0 | True | False | False |
| Status | tinyint | 1 | 3/0 | False | False | False |
| idempresa | int | 4 | 10/0 | True | False | False |
| IdExportacao | int | 4 | 10/0 | True | False | False |
| TipoPessoa | int | 4 | 10/0 | False | False | False |
| telefone | varchar | 20 | 0/0 | True | False | False |
| id_empresa_sistema | int | 4 | 10/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |
| estrangeiro | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_PreCadastros | CLUSTERED | True | True | Id | 1 | False |

- idempresa → dbo.EmpresaAcesso.id (FK_PreCadastros_EmpresaAcesso); exclusão: SET_NULL; desabilitada: False; não validada: False.
- id_empresa_sistema → dbo.Empresas.id (FK_PRECADASTROS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.PROGRAMACOES_HISTORICO_APLICACAO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_programacao | int | 4 | 10/0 | False | False | False |
| id_usuario_aplicacao | int | 4 | 10/0 | True | False | False |
| data_hora_aplicacao | datetime2 | 8 | 27/7 | True | False | False |
| situacao_anterior | int | 4 | 10/0 | True | False | False |
| situacao_posterior | int | 4 | 10/0 | True | False | False |
| observacoes | varchar | 500 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__PROGRAMA__3213E83FFCB635CD | CLUSTERED | True | True | id | 1 | False |

- id_programacao → dbo.PROGRAMACOES_REGRAS_ACESSO.id (FK_PROGRAMACOES_HISTORICO_PROGRAMACAO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.PROGRAMACOES_HISTORICO_DETALHADO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_programacao | int | 4 | 10/0 | False | False | False |
| id_usuario | int | 4 | 10/0 | False | False | False |
| tipo_operacao | varchar | 1 | 0/0 | False | False | False |
| data_hora_operacao | datetime2 | 8 | 27/7 | False | False | False |
| ids_pessoas | varchar | -1 | 0/0 | True | False | False |
| ids_pre_cadastros | varchar | -1 | 0/0 | True | False | False |
| ids_veiculos | varchar | -1 | 0/0 | True | False | False |
| ids_alunos | varchar | -1 | 0/0 | True | False | False |
| ids_responsaveis | varchar | -1 | 0/0 | True | False | False |
| ip_computador | varchar | 50 | 0/0 | True | False | False |
| nome_maquina | varchar | 100 | 0/0 | True | False | False |
| descricao_detalhada | varchar | -1 | 0/0 | True | False | False |
| observacao | varchar | 500 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_PROGRAMACOES_HISTORICO_DETALHADO_DATA | NONCLUSTERED | False | False | data_hora_operacao | 1 | False |
| IX_PROGRAMACOES_HISTORICO_DETALHADO_OPERACAO | NONCLUSTERED | False | False | tipo_operacao | 1 | False |
| IX_PROGRAMACOES_HISTORICO_DETALHADO_PROGRAMACAO | NONCLUSTERED | False | False | id_programacao | 1 | False |
| IX_PROGRAMACOES_HISTORICO_DETALHADO_USUARIO | NONCLUSTERED | False | False | id_usuario | 1 | False |
| PK__PROGRAMA__3213E83FBCF7C9F9 | CLUSTERED | True | True | id | 1 | False |

- id_programacao → dbo.PROGRAMACOES_REGRAS_ACESSO.id (FK_PROGRAMACOES_HISTORICO_DETALHADO_PROGRAMACAO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.PROGRAMACOES_ITENS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_programacao | int | 4 | 10/0 | False | False | False |
| tipo_item | int | 4 | 10/0 | False | False | False |
| id_item | int | 4 | 10/0 | False | False | False |
| acao | int | 4 | 10/0 | False | False | False |
| nome_item | varchar | 200 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_PROGRAMACOES_ITENS_PROGRAMACAO | NONCLUSTERED | False | False | id_programacao | 1 | False |
| PK__PROGRAMA__3213E83F99C06C4E | CLUSTERED | True | True | id | 1 | False |

- id_programacao → dbo.PROGRAMACOES_REGRAS_ACESSO.id (FK_PROGRAMACOES_ITENS_PROGRAMACAO); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.PROGRAMACOES_REGRAS_ACESSO

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| descricao | varchar | 500 | 0/0 | True | False | False |
| data_hora_inicio | datetime2 | 8 | 27/7 | False | False | False |
| data_hora_termino | datetime2 | 8 | 27/7 | False | False | False |
| situacao | int | 4 | 10/0 | True | False | False |
| tipo_acao | int | 4 | 10/0 | True | False | False |
| id_usuario_criacao | int | 4 | 10/0 | True | False | False |
| data_hora_criacao | datetime2 | 8 | 27/7 | True | False | False |
| id_usuario_alteracao | int | 4 | 10/0 | True | False | False |
| data_hora_alteracao | datetime2 | 8 | 27/7 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_PROGRAMACOES_REGRAS_ACESSO_PERIODO | NONCLUSTERED | False | False | data_hora_inicio | 1 | False |
| IX_PROGRAMACOES_REGRAS_ACESSO_PERIODO | NONCLUSTERED | False | False | data_hora_termino | 2 | False |
| IX_PROGRAMACOES_REGRAS_ACESSO_SITUACAO | NONCLUSTERED | False | False | situacao | 1 | False |
| PK__PROGRAMA__3213E83F10951596 | CLUSTERED | True | True | id | 1 | False |

## dbo.PROGRAMACOES_REGRAS_AFETADAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_programacao | int | 4 | 10/0 | False | False | False |
| id_regra_acesso | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_PROGRAMACOES_REGRAS_AFETADAS_PROGRAMACAO | NONCLUSTERED | False | False | id_programacao | 1 | False |
| PK__PROGRAMA__3213E83F17DDC2ED | CLUSTERED | True | True | id | 1 | False |

- id_programacao → dbo.PROGRAMACOES_REGRAS_ACESSO.id (FK_PROGRAMACOES_REGRAS_AFETADAS_PROGRAMACAO); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_regra_acesso → dbo.RegrasAcesso.id (FK_PROGRAMACOES_REGRAS_AFETADAS_REGRA); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Refeicoes

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| Id | int | 4 | 10/0 | False | True | False |
| IdColetor | int | 4 | 10/0 | False | False | False |
| IdCardapio | int | 4 | 10/0 | True | False | False |
| Funcao | int | 4 | 10/0 | False | False | False |
| tipoRefeicao | int | 4 | 10/0 | False | False | False |
| DataHora | datetime | 8 | 23/3 | False | False | False |
| IdPessoa | int | 4 | 10/0 | False | False | False |
| origem | nvarchar | 2 | 0/0 | True | False | False |
| refeitorio | int | 4 | 10/0 | True | False | False |
| ValorRefeicao | decimal | 9 | 18/2 | True | False | False |
| TipoValorRefeicao | int | 4 | 10/0 | True | False | False |
| idprecadastro | int | 4 | 10/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Refeicoes | CLUSTERED | True | True | Id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_REFEICOES_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.RefeicoesReservas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idgestor | int | 4 | 10/0 | True | False | False |
| idusuarioliberou | int | 4 | 10/0 | True | False | False |
| datahoraliberacao | datetime | 8 | 23/3 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| datahora | datetime | 8 | 23/3 | False | False | False |
| credencial | nvarchar | 30 | 0/0 | False | False | False |
| refeicoes | nvarchar | 1024 | 0/0 | False | False | False |
| id_refeitorio | int | 4 | 10/0 | True | False | False |
| IdExportacao | nvarchar | 100 | 0/0 | True | False | False |
| datahoraini | datetime | 8 | 23/3 | True | False | False |
| datahorafim | datetime | 8 | 23/3 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_RefeicoesReservas_status | NONCLUSTERED | False | False | status | 1 | False |
| PK_RefeicoesReservas | CLUSTERED | True | True | id | 1 | False |
| UQ_IdExportacaoRefeicoesReservas | NONCLUSTERED | True | False | IdExportacao | 1 | False |

- id_refeitorio → dbo.Refeitorios.id (FK_IdRefeitorio); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_empresa → dbo.Empresas.id (FK_REFEICOESRESERVAS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Refeitorios

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 100 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| UtilizaControleCreditos | tinyint | 1 | 3/0 | True | False | False |
| IdExportacao | nvarchar | 100 | 0/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |
| sentido_acesso | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Refeitorios | CLUSTERED | True | True | id | 1 | False |
| UQ_IdExportacaoRefeitorios | NONCLUSTERED | True | False | IdExportacao | 1 | False |

- id_empresa → dbo.Empresas.id (FK_REFEITORIOS_EMPRESAS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.RegCrachas

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Codigo | nvarchar | 30 | 0/0 | False | False | False |
| TipoCracha | int | 4 | 10/0 | True | False | False |
| IdPessoa | int | 4 | 10/0 | True | False | False |
| IdPreCadastro | int | 4 | 10/0 | True | False | False |
| TipoUso | tinyint | 1 | 3/0 | False | False | False |
| DataHoraRegistro | datetime | 8 | 23/3 | True | False | False |
| DataHoraEncerramento | datetime | 8 | 23/3 | True | False | False |
| idVeiculo | int | 4 | 10/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | Codigo | 1 | False |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | TipoCracha | 0 | True |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | idVeiculo | 0 | True |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | IdPessoa | 0 | True |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | IdPreCadastro | 0 | True |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | TipoUso | 0 | True |
| IX_RegCrachas_Codigo | NONCLUSTERED | False | False | excluido | 0 | True |
| PK_re | CLUSTERED | True | True | id | 1 | False |

## dbo.registroTransportadora

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| transportadora | nvarchar | 200 | 0/0 | False | False | False |
| placa_veiculo | nvarchar | 14 | 0/0 | True | False | False |
| peso | float | 8 | 53/0 | True | False | False |
| NF | nvarchar | -1 | 0/0 | True | False | False |
| volumes | int | 4 | 10/0 | True | False | False |
| nome_motorista | nvarchar | 200 | 0/0 | False | False | False |
| data_entrada | datetime | 8 | 23/3 | True | False | False |
| data_saida | datetime | 8 | 23/3 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__registro__3213E83F902A35F4 | CLUSTERED | True | True | id | 1 | False |

## dbo.REGRAS_ACESSO_ALUNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_regra | int | 4 | 10/0 | False | False | False |
| id_aluno | int | 4 | 10/0 | False | False | False |

- id_aluno → dbo.ALUNOS.id (FK_RAA_ALUNO); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_regra → dbo.RegrasAcesso.id (FK_RAA_REGRA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.REGRAS_ACESSO_TURMAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_regra | int | 4 | 10/0 | False | False | False |
| id_turma | int | 4 | 10/0 | False | False | False |

- id_regra → dbo.RegrasAcesso.id (FK_RAT_REGRA); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_turma → dbo.TURMAS.id (FK_RAT_TURMA); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.REGRAS_ACESSO_TURNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_regra | int | 4 | 10/0 | False | False | False |
| id_turno | int | 4 | 10/0 | False | False | False |

- id_regra → dbo.RegrasAcesso.id (FK_RATn_REGRA); exclusão: CASCADE; desabilitada: False; não validada: False.
- id_turno → dbo.TURNOS.id (FK_RATn_TURNO); exclusão: CASCADE; desabilitada: False; não validada: False.

## dbo.RegrasAcesso

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Nome | nvarchar | 100 | 0/0 | False | False | False |
| TipoRegra | int | 4 | 10/0 | False | False | False |
| coletores | nvarchar | 400 | 0/0 | False | False | False |
| TipoSelecao | int | 4 | 10/0 | False | False | False |
| IdFiltro | int | 4 | 10/0 | True | False | False |
| Setores | varchar | -1 | 0/0 | True | False | False |
| Pessoas | nvarchar | -1 | 0/0 | True | False | False |
| SepararRegraDia | tinyint | 1 | 3/0 | True | False | False |
| BloquearSabados | tinyint | 1 | 3/0 | True | False | False |
| BloquearDomingos | tinyint | 1 | 3/0 | True | False | False |
| QtdeAcesso | int | 4 | 10/0 | True | False | False |
| ConsideraPreCadastro | int | 4 | 10/0 | False | False | False |
| DiasSemana | nvarchar | 100 | 0/0 | True | False | False |
| tipoacesso | int | 4 | 10/0 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| DataHoraInicio | datetime | 8 | 23/3 | True | False | False |
| DataHoraTermino | datetime | 8 | 23/3 | True | False | False |
| HoraInicioMaiorTermino | tinyint | 1 | 3/0 | True | False | False |
| Veiculos | varchar | -1 | 0/0 | True | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| personalizar | char | 1 | 0/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| IX_RegrasAcesso_IdEmpresa | NONCLUSTERED | False | False | id_empresa | 1 | False |
| PK_RegrasAcesso | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_RegrasAcesso_Empresas); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- IdFiltro → dbo.METAH_FILTROS.ID (FK_RegrasAcesso_METAH_FILTROS); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.RESPONSAVEIS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_empresa | int | 4 | 10/0 | True | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| email | varchar | 150 | 0/0 | True | False | False |
| nascimento | datetime | 8 | 23/3 | True | False | False |
| sexo | char | 1 | 0/0 | False | False | False |
| cpf | varchar | 11 | 0/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_RESPONSAVEIS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_RESPONSAVEIS_EMPRESA); exclusão: SET_NULL; desabilitada: False; não validada: False.

## dbo.Setores

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 100 | 0/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Setores | CLUSTERED | True | True | id | 1 | False |

## dbo.SISTEMA_VERSAO_LOG

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_versao | int | 4 | 10/0 | False | False | False |
| data_ultima_inicializacao | datetime | 8 | 23/3 | False | False | False |
| quantidade_inicializacoes | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__SISTEMA___3213E83FAD7D5DC2 | CLUSTERED | True | True | id | 1 | False |

- id_versao → dbo.VERSOES.id (fk_sistema_versao); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.SP_VERIFICAR_REGISTRO_EXISTENTE

SQL_STORED_PROCEDURE

## dbo.TiposDeEPIs

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| equipamento | nvarchar | -1 | 0/0 | False | False | False |
| descricao | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_TiposDeEPIs | CLUSTERED | True | True | id | 1 | False |

## dbo.TipoVeiculo

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Nome | nvarchar | 200 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdTipoVeiculo | CLUSTERED | True | True | id | 1 | False |

## dbo.TRG_METAH_FILTROS_UPDATE

SQL_TRIGGER

## dbo.TURMAS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| id_turno | int | 4 | 10/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_TURMA | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_TURMAS_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_turno → dbo.TURNOS.id (FK_TURMAS_TURNO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.TURNOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | varchar | 100 | 0/0 | False | False | False |
| situacao | int | 4 | 10/0 | False | False | False |
| id_empresa | int | 4 | 10/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_TURNOS | CLUSTERED | True | True | id | 1 | False |

- id_empresa → dbo.Empresas.id (FK_TURNOS_EMPRESA); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Unidades

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idEmpresa | int | 4 | 10/0 | False | False | False |
| nome | varchar | 50 | 0/0 | False | False | False |
| status | int | 4 | 10/0 | False | False | False |
| codigo | varchar | 10 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__Unidades__3213E83FDC40210C | CLUSTERED | True | True | id | 1 | False |

- idEmpresa → dbo.Empresas.id (FK_Unidade_Empresa); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Usuarios

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| nome | nvarchar | 40 | 0/0 | False | False | False |
| senha | nvarchar | 256 | 0/0 | False | False | False |
| idempresa | int | 4 | 10/0 | False | False | False |
| status | tinyint | 1 | 3/0 | True | False | False |
| permissoes | varchar | 25 | 0/0 | True | False | False |
| administrador | char | 1 | 0/0 | False | False | False |
| primeirologin | bit | 1 | 1/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Usuarios | CLUSTERED | True | True | id | 1 | False |

- idempresa → dbo.Empresas.id (FK_usuario_empresa); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.USUARIOS_COLETORES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id_usuario | int | 4 | 10/0 | False | False | False |
| id_coletor | int | 4 | 10/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_USUARIOS_COLETORES | CLUSTERED | True | True | id_usuario | 1 | False |
| PK_USUARIOS_COLETORES | CLUSTERED | True | True | id_coletor | 2 | False |

- id_coletor → dbo.Coletores.id (FK_USUARIOS_COLETORES_COLETOR); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_usuario → dbo.Usuarios.id (FK_USUARIOS_COLETORES_USUARIO); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.Veiculos

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| placa | nvarchar | 14 | 0/0 | True | False | False |
| idpessoa | int | 4 | 10/0 | True | False | False |
| idtipoveiculo | int | 4 | 10/0 | True | False | False |
| idestacionamento | int | 4 | 10/0 | True | False | False |
| tipoboxreserva | int | 4 | 10/0 | True | False | False |
| observacao | text | 16 | 0/0 | True | False | False |
| nome | nvarchar | 400 | 0/0 | True | False | False |
| situacao | tinyint | 1 | 3/0 | True | False | False |
| Status | int | 4 | 10/0 | True | False | False |
| TipoVeiculoNome | varchar | 255 | 0/0 | True | False | False |
| veiculo_uso | int | 4 | 10/0 | True | False | False |
| id_precadastro | int | 4 | 10/0 | True | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdVeiculos | CLUSTERED | True | True | id | 1 | False |

## dbo.VeiculosOcorrencias

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idveiculo | int | 4 | 10/0 | True | False | False |
| idocorrencia | int | 4 | 10/0 | True | False | False |
| observacao | text | 16 | 0/0 | True | False | False |
| data | date | 3 | 10/0 | True | False | False |
| hora | time | 5 | 16/7 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_IdVeiculosOcorrencias | CLUSTERED | True | True | id | 1 | False |

## dbo.VERSAO_CLIENT

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| versao | varchar | 50 | 0/0 | True | False | False |

## dbo.VERSOES

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| versao | nchar | 20 | 0/0 | True | False | False |
| data_liberacao | date | 3 | 10/0 | True | False | False |
| data_atualizacao | datetime | 8 | 23/3 | True | False | False |
| notas_release | nvarchar | -1 | 0/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_Versoes | CLUSTERED | True | True | id | 1 | False |

## dbo.ViewPessoasDigitais

VIEW

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| ID | int | 4 | 10/0 | False | False | False |
| Nome | nvarchar | 200 | 0/0 | False | False | False |
| TipoPessoa | int | 4 | 10/0 | False | False | False |
| FaceCID | int | 4 | 10/0 | True | False | False |
| DigitaisCID | int | 4 | 10/0 | True | False | False |
| DigitaisDIMEP | int | 4 | 10/0 | True | False | False |

## dbo.VINCULO_FILTROS_NOVOS_ANTIGOS

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| IdMetahFiltros | int | 4 | 10/0 | True | False | False |
| IdFiltro | int | 4 | 10/0 | True | False | False |

## dbo.VisitantesTerceiros

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| Tipo | int | 4 | 10/0 | False | False | False |
| Nome | nvarchar | 200 | 0/0 | False | False | False |
| Cpf | nvarchar | 40 | 0/0 | False | False | False |
| IdEmpresaAcesso | int | 4 | 10/0 | True | False | False |
| Status | tinyint | 1 | 3/0 | True | False | False |
| Foto | varbinary | -1 | 0/0 | True | False | False |
| IdExportacao | int | 4 | 10/0 | True | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_VisitantesTerceiros | CLUSTERED | True | True | id | 1 | False |

## dbo.VisitantesTerceirosHistoricos

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| idVisitantes | int | 4 | 10/0 | False | False | False |
| NrCracha | nvarchar | 30 | 0/0 | False | False | False |
| Observacao | nvarchar | 1024 | 0/0 | False | False | False |
| Cardapios | nvarchar | 400 | 0/0 | False | False | False |
| coletores | nvarchar | 400 | 0/0 | True | False | False |
| DataHoraInicio | datetime | 8 | 23/3 | True | False | False |
| DataHoraTermino | datetime | 8 | 23/3 | True | False | False |
| IdResponsavel | int | 4 | 10/0 | True | False | False |
| Status | int | 4 | 10/0 | True | False | False |
| personalizado | char | 1 | 0/0 | False | False | False |
| excluido | char | 1 | 0/0 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK_VisitantesTerceirosHistoricos | CLUSTERED | True | True | id | 1 | False |

## dbo.VisitantesTerceirosHistoricosReg

USER_TABLE

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| id | int | 4 | 10/0 | False | True | False |
| id_visitantes_terceiros_historicos | int | 4 | 10/0 | False | False | False |
| id_visitantes | int | 4 | 10/0 | False | False | False |
| nr_cracha | varchar | 15 | 0/0 | False | False | False |
| passagens | int | 4 | 10/0 | False | False | False |
| observacao | varchar | 512 | 0/0 | True | False | False |
| cardapio | int | 4 | 10/0 | True | False | False |
| refeitorio | int | 4 | 10/0 | True | False | False |
| coletor | int | 4 | 10/0 | False | False | False |
| usuario | varchar | 100 | 0/0 | True | False | False |
| data_hora_inicio | datetime | 8 | 23/3 | True | False | False |
| data_hora_termino | datetime | 8 | 23/3 | True | False | False |
| id_responsavel | int | 4 | 10/0 | True | False | False |
| data_criacao | datetime | 8 | 23/3 | False | False | False |

| Índice | Tipo | Único | PK | Coluna | Ordem | Incluída |
|---|---|---|---|---|---|---|
| PK__Visitant__3213E83F843ECE82 | CLUSTERED | True | True | id | 1 | False |

- cardapio → dbo.cardapios.id (FK__Visitante__carda__11F49EE0); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- coletor → dbo.Coletores.id (FK__Visitante__colet__13DCE752); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- id_visitantes_terceiros_historicos → dbo.VisitantesTerceirosHistoricos.id (FK__Visitante__id_vi__11007AA7); exclusão: NO_ACTION; desabilitada: False; não validada: False.
- refeitorio → dbo.Refeitorios.id (FK__Visitante__refei__12E8C319); exclusão: NO_ACTION; desabilitada: False; não validada: False.

## dbo.VW_EXPORTACAO_AFD_COMPLETA

VIEW

| Coluna | Tipo | Máximo em bytes | Precisão/escala | Nulo | Identidade | Calculada |
|---|---|---|---|---|---|---|
| EXPORTACAO_ID | int | 4 | 10/0 | False | False | False |
| DATA_EXPORTACAO | datetime | 8 | 23/3 | False | False | False |
| DATA_INICIO | datetime | 8 | 23/3 | False | False | False |
| DATA_FIM | datetime | 8 | 23/3 | False | False | False |
| TOTAL_REGISTROS | int | 4 | 10/0 | False | False | False |
| REGISTROS_NOVOS | int | 4 | 10/0 | False | False | False |
| REGISTROS_DUPLICADOS | int | 4 | 10/0 | False | False | False |
| PROTOCOLO_USADO | varchar | 50 | 0/0 | True | False | False |
| NSR | varchar | 20 | 0/0 | False | False | False |
| DATA_MARCACAO | datetime | 8 | 23/3 | False | False | False |
| PIS | varchar | 20 | 0/0 | False | False | False |
| TIPO_MOVIMENTO | varchar | 2 | 0/0 | False | False | False |
| DESCRICAO_MOVIMENTO | varchar | 50 | 0/0 | True | False | False |
| STATUS_REGISTRO | tinyint | 1 | 3/0 | False | False | False |
| DESCRICAO_COMPLETA | varchar | 16 | 0/0 | False | False | False |
| NOME_EQUIPAMENTO | varchar | 100 | 0/0 | True | False | False |

