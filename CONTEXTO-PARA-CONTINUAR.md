## Novo executor exploratório de telas — 21/10/2026

Usuário pediu programar teste que, quando executado, abra formulários do Acessus,
preencha campos e clique botões em muitas ordens, com diário detalhado de cada
ação e erro. Implementado em `src/automatiza/explorador.py`,
`explorador_windows.py` e `explorador_cli.py`; exemplo com 72 rotas candidatas
em `examples/explorador-acessus-2111.json`; manual em
`docs/EXPLORADOR-ACESSUS.md`. Gera ações isoladas, pares ordenados e sequências
aleatórias reproduzíveis por semente, com limites configuráveis. Escreve
`passos.log`, `passos.jsonl` e `estado.json`, registrando também navegação,
fechamento e controles ignorados. Botões que podem gravar exigem política
explícita para base descartável. Suíte de código: 224 testes passaram, 2 de
integração/desktop excluídos, 3 subtestes. O explorador NÃO foi executado nos
módulos reais da 2.11.1; os mapas de rotas vêm da 2.11.0. Não afirmar que cobre
todos os controles especiais, equipamentos, grades ou regras de negócio.

## Atualização concluída em 21/10/2026: Acessus 2.11.1

Usuário autorizou copiar a release 2.11.1 de
`\\dexter\Arquivos\Sistemas\Acessus Release\Versões\v2.0\2.11.1` para `C:\acesso`
e executar o Atualizador. Concluído: 653 arquivos iguais por SHA-256, backup SQL
COPY_ONLY/CHECKSUM de desk-tec/novo123 verificado, 652 arquivos locais anteriores
salvos, Atualizador exibiu conclusão, VERSOES no banco novo123 registra 2.11.1.0,
serviço de importação voltou a Running. Evidências em
`reports/atualizacao/20261021-2111/LEIA-ME.md`. A credencial Dexter foi salva no
Gerenciador de Credenciais do Windows; não registrar senha em arquivos ou saídas.
Pilotos CRUD/API abaixo foram executados na 2.11.0 e não revalidados na 2.11.1.

## Tarefa vigente 2026-10-21: projeto automático de ciclos CRUD/API

Atualização 21/10/2026 ~10:49 (America/Sao_Paulo): projeto implementado em
`src/automatiza/ciclos*.py`, exemplo `examples/ciclos-sirh.json`, manual
`docs/CICLOS-AUTOMATICOS-SIRH.md`, resultado
`reports/ciclos-dev/RESULTADO-CONSOLIDADO.md`. Cinco pilotos reais encerrados:
`piloto-real-v5` PASSOU (9 etapas); `piloto-ferias-reserva` COM RESSALVAS
(18 etapas, causa de férias incorreta e reservas sem API); `piloto-ocorrencia-nova`
PASSOU (11); `piloto-ocorrencia-horaria` PASSOU (10, 08:15–12:45);
`piloto-ocorrencia-virada` PASSOU (8, 23:30–01:30 no dia seguinte). Total
56 etapas. O plano de exemplo com três rodadas gerou 158 etapas, mas não foi
executado integralmente. Suíte `pytest -m 'not banco and not desktop'` passou
216 testes e 3 subtestes; 2 testes de integração foram excluídos. Não há
executor de ciclos ativo; antes de qualquer nova execução, conferir processos,
`estado.json`, diário e origem para evitar duplicar gravações. Os registros dos
pilotos terminaram presentes nos períodos-base. RH precisou reiniciar a sessão
do operador durante piloto da virada; as interrupções constam do diário.
Reservas continuam sem endpoint API e a causa `FÃ©rias` continua incorreta no
Acessus 2.11. Modalidades horárias diferentes da ocorrência 013 exigem mapeamento.
Os parágrafos abaixo deste bloco são históricos e incluem estados já superados.

Pedido mais recente do usu?rio SUBSTITUI a antiga restri??o de n?o cadastrar: programar o projeto para sequ?ncias com alguns registros, importar, alterar, importar, excluir, importar, recriar, variar ordem. Trabalhar no projeto, sem depender de um agente executando manualmente os passos. C?digo novo: src/automatiza/ciclos.py, ciclos_sirh.py, ciclos_ui.py, ciclos_cli.py; manifesto examples/ciclos-sirh.json; docs/CICLOS-AUTOMATICOS-SIRH.md; tests/unit/test_ciclos*.py. Gera??o determin?stica por semente, di?rio pr?prio, retomada sem repetir a??o gravada, UI RH + API + destino SQL somente leitura. Credencial API j? autorizada foi salva em Credential Manager do Windows sob AutomatizaTestes/SIRH; n?o exportar senha. Reservas ainda sem endpoint API, devem ser marcadas BLOQUEADO antes de alterar.

Hist?rico substitu?do pelo resultado consolidado acima. O piloto real-v5 e a su?te
unit?ria foram conclu?dos. Consulte os di?rios e o estado atuais, n?o os
checkpoints intermedi?rios de 09:49.

## Latest follow-up completed: 2026-10-20 14:12

User requested continuation of the API tests, with no new registrations. Read reports/integracao-api/20261020/auditoria-103518/COMPLEMENTO.md first. Own test diary appended. Authenticated GET /endpoint returned 458 names, no reservation/meal/consumption route. Installed import executable contains gera-afastamento and current-period SQL filters: all 20 occurrence outcomes match this criterion (static evidence, not proof of API execution path or business requirement). Malformed holiday label is present in executable and SQL rows 2-5; code points 195/169 rather than 233. No source project for the product was found in this automation workspace. No database/business changes. Pending implementation: reservation API route/importer support and corrected executable label. Do not claim these defects fixed. Tests and investigation completed with documented limitations; no further registrations authorized. Supervisor rearmed for this continuation.

## Resultado vigente ? auditoria conclu?da em 20/10/2026

A confer?ncia solicitada dos cadastros existentes terminou; n?o cadastrar mais casos. Entregar reports/integracao-api/20261020/auditoria-103518/RELATORIO.md e diario-testes.txt. S?o 32 casos: API preservou campos de 20 ocorr?ncias e 5 f?rias; destino tem 1 ocorr?ncia e 4 f?rias com per?odos corretos e sem duplica??o em dois ciclos; 19 ocorr?ncias e 1 f?rias passada ausentes; 7 reservas/consumos n?o importados e sem rota publicada no Swagger. Regra de exclus?o por vig?ncia/tipo deve ser confirmada antes de aprovar esses casos. Falha comprovada na causa das 4 f?rias: F??rias, UNICODE SQL 195/169 em vez de 233. N?o corrigir dados/c?digo sem nova tarefa; esta tarefa era testar e relatar.

Retomada autom?tica real confirmada nesta conversa: supervisor aguardou cota e retomou no turno 01a15a18-4f80-7b51-a92d-d62693a1f5d4. Supervisor vinculado ? conversa atual 01a15903-c3d6-71d2-b507-4720613af0df. Ao concluir este trabalho com status concluido, supervisor para novas continua??es desse trabalho, conforme projetado. Uma nova tarefa exige rearmar pelo comando Ativar. Windows precisa estar ligado e sess?o dispon?vel; n?o prometer execu??o desligado.

## Tarefa vigente ? 20/10/2026, confer?ncia API e di?rio de testes

Pedido atual: parar novos cadastros e conferir importa??o API SIRH de ocorr?ncias, f?rias e reservas, com logs pr?prios de teste (hor?rio, a??o, esperado, observado). N?O criar mais casos. Origem RHFagundes, unidade 0004 contrato 4; destino novo123 pessoa 5. Acessus j? atualizado 2.11; Atualizador executado. API configurada e autentica??o confirmada.

Auditoria somente leitura em andamento: scripts/auditar_importacao_api.py; sa?da reports/integracao-api/20261020/auditoria-103518. Processo iniciado ?s 10:35:18, sess?o exec 77782. Conferir se terminou ANTES de repetir. Produz diario-testes.txt/jsonl, origem.json, api.json, destino-antes/depois.json, casos-conferidos.json e RELATORIO.md. Capturou 20 ocorr?ncias, 5 f?rias e 7 reservas/consumos na origem; API HTTP200 retornou 20 ocorr?ncias e 5 f?rias. Destino inicial: 5 afastamentos, zero reservas, zero refeit?rios. Aguarda dois ciclos autom?ticos de f?rias/afastamentos para comparar IDs e duplica??es. N?o exporta log bruto do sistema nem segredos.

Ainda falta revisar resultado final por caso, explicar os n?o importados e entregar di?rio ao usu?rio. Reservas sem rota publicada no Swagger; n?o substituir por importa??o SQL para declarar aprova??o API. Ocorr?ncia 011 vigente importada com t?rmino atualizado para 22/10/2026. Quatro f?rias importadas anteriormente, passada ausente. Casos futuros de ocorr?ncia podem ser filtrados por vig?ncia; n?o declarar que todos passaram. H? casos de horas 08:15?12:45, 23:30?01:30 e 04:30/dia. N?o usar scripts antigos de cadastro com handles obsoletos. Nenhuma nova grava??o autorizada depois do pedido de parar cadastros.

Usu?rio pediu conferir retomada ap?s cota. Supervisor estava conclu?do e ligado ? conversa antiga; configura??o corrigida para CODEX_THREAD_ID atual, 01a15903-c3d6-71d2-b507-4720613af0df. Reativar/verificar via scripts/configurar-retomada-codex.ps1 -Acao Ativar/Status. A retomada ? para continuar esta tarefa, sem reiniciar cadastros. Estado hist?rico abaixo n?o substitui este pedido.

# Contexto para continuar o projeto de automação

## API SIRH configurada e autenticando ? 20/10/2026

Usu?rio forneceu e autorizou configurar e-mail/URL/senha da API. Salvo pela tela Configura??o API; reabertura confirmou os tr?s campos, sem exportar senha. URL https://apimetadados.metahequipamentos.com.br/ e e-mail metahdev02@gmail.com. HTTPS 443 agora acess?vel. Servi?o FrmSyncImpViewsPrincipal Running; log atual de 20/10/2026 09:30:03 registra StatusCode=200 e token obtido com sucesso. Falha de conectividade anterior ? hist?rica. Evid?ncia sanitizada: reports/configuracao-api/20261020/resultado.json. Autentica??o n?o comprova reserva importada nem correspond?ncia da API com RHFagundes. Destino continua desk-tec/novo123 e conex?o SQL RHFagundes preservada.


## Conex?o SIRH criada em 20/10/2026

Usu?rio autorizou criar a conex?o SIRH. Cadastro salvo pela tela do Importador Metadados: ConexaoBD Id 2, TipoBD 0 (SQL Server), desk-tec/RHFagundes. Credenciais existentes foram reutilizadas em mem?ria ap?s consulta de origem bem-sucedida; nenhuma senha registrada no relat?rio. Cadastro API Id 1 preservado. Destino Acessus continua desk-tec/novo123, j? atualizado pelo Atualizador da 2.11. A configura??o de Importar Reservas agora abre, e suas duas abas foram capturadas; fechada sem Confirmar/importar. Zero reservas no destino. Evid?ncia: reports/conexao-sirh/20261020/resultado.json. Bloqueio anterior por aus?ncia de conex?o SIRH resolvido. Falha de conectividade da API permanece separada.


## Confer?ncia posterior ao login ? 20/10/2026

Seis m?dulos abertos na 2.11.0. As 20 rotas antes pendentes/falhas de Acesso foram inspecionadas. Nove inclus?es vazias de coletores/regras/programa??o foram capturadas e canceladas. Administra??o: incluir usu?rio provoca Access violation 015C537D / leitura 000001E4; aviso fechado e inclus?o cancelada. Op??es do Sistema permanece ausente. Refeit?rio: Importar Reservas bloqueado por falta de conex?o SIRH cadastrada; di?logo de configura??o n?o abre. Servi?o Running, mas log atual mostra erro de conex?o 12029 ao obter token. API 192.168.50.105 n?o responde em 443/80; confirma??o de endere?o para RHFagundes solicitada. Baseline destino: zero reservas e zero refeit?rios, 10 pessoas. Nenhuma grava??o de neg?cio pela inspe??o. 176 testes unit?rios passaram ap?s ajustes de captura. Mapas: docs/mapeamentos/vm-211-20261020/LEIA-ME.md. Esta sess?o inspecionou 31 rotas e registrou 3 bloqueios/indisponibilidades; n?o revalidou as 90 rotas restantes j? inspecionadas ou inventariadas na 2.10. Fluxos de neg?cio permanecem pendentes de infraestrutura, dados e expectativas confirmados.


## Atualiza??o de 20/10/2026 ? Acessus 2.11 instalado

Atualiza??o autorizada e conclu?da em C:\acesso; Atualizador conclu?do em desk-tec/novo123. 661 arquivos conferidos, zero diverg?ncias; backup SQL verificado e arquivos afetados preservados. Servi?o de importa??o encontrado Running, parado durante a c?pia e restaurado Running. 176 testes unit?rios passaram. Painel v2.11.0 aberto na tela de login, senha vazia; solicitado login manual. Confer?ncia de todas as pend?ncias continua ap?s login, sem consider?-la conclu?da. Leia reports/atualizacao/20261020-211-preparacao/LEIA-ME.md e pendencias.json. Sempre rodar Atualizador ao trocar banco, mesmo sem mudan?a de vers?o. Estado abaixo ? hist?rico.


## Tarefa vigente — retomada automática do Codex, 20/10/2026

Pedido mais recente substituiu temporariamente a inspeção de telas pela
configuração de retomada após renovação real de cota. Configuração concluída,
com prova real: erro usageLimitExceeded em 19/10 e retomada nesta mesma conversa
em 20/10 às 08:14, após inicialização do Windows às 08:09. Não reativar tarefas
anteriores automaticamente ao concluir esta configuração.

Leia [RETOMADA-AUTOMATICA-CODEX.md](docs/RETOMADA-AUTOMATICA-CODEX.md): código,
tarefa agendada, evidências, limitações e comandos para desativar/reativar.
10 testes locais e três subcasos passaram; não são validação de negócio.
Nenhuma dependência nova, troca de conta/modelo/autenticação/permissões,
atualização Acessus ou gravação/importação de negócio nesta configuração.
Histórico, credenciais, perfis e pendências anteriores preservados.

Correção do checkpoint de telas abaixo: Acesso chegou às rotas 1–21;
última tentativa falhou na rota 22, Comunicação → Comandos com Equipamentos.
Conferir JSONL e processos antes de qualquer retomada dessa tarefa futura.

## Steering mais recente — release 2.11.0 no Dexter e regra do Atualizador

Usuário informou a release em
`\\dexter\Arquivos\Sistemas\Acessus Release\Versões\v2.0\2.11.0`.
Após atualizar Acessus, executar o Atualizador no banco de destino. Ao trocar
esse banco, executar novamente. Não confundir RHFagundes (origem) com novo123
(destino Acessus). Leia `docs/ATUALIZACAO-ACESSUS.md`.

- Release ainda sem acesso: SMB 445 do Dexter acessível, mas listagem retorna
  WinError1326; net view acesso negado. Explorador aberto em \\dexter\Arquivos
  para autenticação de rede do Windows. Não usar senhas do RH/Acessus no servidor.
- Pergunta pendente: atualizar agora/mapear2.11 ou concluir inventário2.10 primeiro.
  Nenhum executável atualizado e nenhum Atualizador de banco executado.
- Inspeção atual2.10 em `reports/inspecao-telas/vm-20261019` com Markdown/JSON por
  tela e `docs/mapeamentos/vm-20261019/LEIA-ME.md` com cobertura real parcial.
  Refeitório20, Portaria12, Estacionamento19, Escola26 e Administração2 rotas
  inspecionadas; Administração/Opções do Sistema ausente no menu e documentada.
  Acesso ainda em andamento: última tentativa da rota20 falhou na navegação,
  após rotas1–19. Consultar os JSONL antes de retomar. Existem tentativas anteriores
  preservadas; o catálogo usa o registro mais recente de cada rota.
- Ainda falta complementar os diálogos de inclusão separados (coletores/regras/
  usuários) e a configuração de importação de reservas no Refeitório. Scripts
  atualizados para capturar esses diálogos e cancelar sem salvar. Não declarar
  inspeção completa enquanto essas pendências não forem tratadas.
- Tarefa de reserva/importação anterior continua pendente; não foi criado dado
  de negócio nem iniciado serviço durante esta inspeção de módulos.

## Última tarefa — reserva via API SIRH, preparação parcial em 19/10

Usuário mudou o foco para criar reserva no Frequência e conferir importação no
Acessus por tela, SQL e log. Autorizou configurar API, instalar e iniciar serviço.
Leia `docs/TESTE-RESERVA-SIRH.md` antes de continuar.

- Reserva/Consumo RH TFrm_RHPA5210 e relatório Acessus TFrmRelResCon abertos.
  Cenário de abertura `05-abrir-reservas.json` PASSOU, execução
  `reports/execucoes/20261019-150455-fbafbbe9`.
- Instalado AcessusSyncImportacao.exe /install /silent com UAC padrão.
  Serviço FrmSyncImpViewsPrincipal, descrição Acessus - Importação API,
  início Auto, permanece PARADO. Não havia serviço instalado nesta VM.
- API já configurada aponta para https://apimetadados.metahequipamentos.com.br/.
  Falta confirmar se atende a RHFagundes; pergunta pendente ao usuário. Não houve
  gravação da configuração nem início de importação nesta tarefa.
- Candidato real consultado sem salvar: Cleonice, contrato129/unidade0001.
  Acessus tem três cadastros candidatos (7/8/9); não escolher arbitrariamente.
  Baseline novo123: zero RefeicoesReservas e zero Refeitorios.
- Criado suporte a sql_reserva_verificar/sql_reserva_aguardar com filtros exatos
  em RefeicoesReservas. Tabela não tem IdPessoa; usa credencial e outros vínculos.
  Planejamento desativado: examples/reservas-sirh/caso-pendente.json.
- 164 testes unitários passaram. Cadastro completo por tela e importação da
  reserva ainda não executados. Não tratar infraestrutura como fluxo pronto.
- Relatório real de preparação PENDENTE_CONFIRMACAO_API:
  reports/reserva-sirh/20261019-150635-2553b9dc/relatorio.html.
- Log correto observado: C:\acesso\Logs\AcessusSyncProcessoService.log.
  Conteúdo de 16/10 é histórico, não evidência de importação atual. Não exportar
  logs brutos nem credenciais. Continuar com dados/expectativas confirmados.

## Último estado — RHFagundes, ocorrências e férias abertas

- Usuário selecionou e autorizou RHFagundes. Alias ativo e perfil
  `RHFagundes_para_novo123.json` conferidos; destino do importador desk-tec/novo123.
  Não houve alteração de origem/serviços pela automação. Não registrar senhas.
- Usuário autorizou confirmar avisos de entrada com OK e continuar. RhApp agora
  faz isso para mensagens Information/Informação com um único botão OK, exigindo
  disponibilidade posterior do módulo. Não confirma Sim ou operações de dados.
- Frequência acessível. Ocorrências e Férias Cedidas passaram em execução real.
  Férias exigiu corrigir fallback WinError 299 para o mnemônico %pf.
- Lote de quatro cenários **PASSOU**: estrutura SQL, janela Acessus, ocorrências,
  férias. Relatório `reports/lotes/20261019-145247-757fa142/indice.html`.
- 155 testes unitários passaram; relatório
  `reports/validacao-rhfagundes-20261019/testes.html`.
- Primeira abertura de ocorrências exibiu EPrinter; posterior conferência achou
  Print to PDF já padrão e Spooler executando, sem reconfigurar. Nova abertura
  de Frequência resolveu a tentativa, mas causa original não foi comprovada.
- Nenhuma gravação de negócio. Ainda faltam dados reais confirmados e fluxos
  completos. Foi oferecido levantar candidatos reais para seleção do usuário.
  IdExportacao repetido e ContratoExportacao zero foram observados em consulta
  limitada; não assumir vínculo RH/Acessus sem conferir pessoa/contrato.
- A origem RHBraslux e seu bloqueio por limite de contratos abaixo são históricos.

## Última atualização — Frequência encerra por limite de contratos

Usuário autorizou dar OK nos avisos de entrada. Foram confirmados o aviso
“O módulo atual está cancelado” e a mensagem seguinte, que explica o motivo:
**506 contratos ativos cadastrados para limite contratado de 100**.
Após o segundo OK, Frequência encerra. Evidência:
`reports/rh-limite-contratos.png`. Abertura reproduzida pelo menu normal do painel.
Identificação atual do painel RH: usuário 2695 e operador MASTER; nenhuma senha
foi digitada nesta etapa porque o painel já estava autenticado corretamente.
Não atribuir o bloqueio a login não preenchido ou falta de OK. Não alterar
licença, contratos ou origem para contorná-lo. Não houve gravação de negócio.
Leia a atualização mais recente em `docs/ESTADO-VM-20261019.md`.

## Atualização de 19/10/2026 às 14h04 — Acessus acessível

- Usuário informou credenciais na conversa; não copiar senhas para arquivos.
  Ambos os painéis já estavam autenticados ao inspecionar; não houve digitação
  de credenciais nesta etapa.
- Acessus aberto pelo painel: cenário de janela PASSOU, execução
  `reports/execucoes/20261019-140234-148436b4`.
- Menus Acessus corrigidos para UIA com itens visíveis únicos. Cadastro de Pessoas
  e Acesso por Pessoa validados sem gravação, relatório:
  `reports/validacao-telas-acessus/20261019-140435-78f66ba6/relatorio.html`.
- DesktopApp.start reconhece Acessus.exe e usa o painel irmão, sem alterar .env;
  reabertura real validada. 152 testes unitários passaram após estas correções:
  `reports/validacao-acessus-20261019/testes.html`.
- RH autenticado permanece bloqueado em Frequência por “O módulo atual está
  cancelado”. Aviso foi confirmado e processo encerrou. Motivo desconhecido.
- Dados reais de pessoa/contrato, causa, datas e expectativas ainda não foram
  confirmados. Não gravar dados nem afirmar cobertura completa dos fluxos.
- Esta atualização substitui a pendência anterior de login no Acessus.

## Continuidade de 19/10/2026 às 14h — bloqueios reais confirmados

Leia primeiro a seção de continuidade em `docs/ESTADO-VM-20261019.md`.
Ela prevalece sobre as pendências históricas abaixo.

- Execução anterior `20261019-133940-58e103ff` terminou FALHOU às 13:39:50.
  Não há execução dessa tentativa ainda pendente. Alias ativo RHBraslux
  confirmado no painel autenticado, sem salvar alteração.
- Frequência bloqueado: abertura nativa mostrou “O módulo atual está cancelado”
  (`reports/rh-informacao-nativa.png`); outras tentativas registraram
  EAccessViolation em RH.bpl no ErroLog.Txt. Causa do cancelamento desconhecida.
- Executor corrigido para rejeitar mensagens bloqueantes e aguardar estabilidade
  da janela. Rodada real `20261019-135910-b0a3f90a` falhou na precondição de
  conexão, com diagnóstico, sem tentar abrir ocorrências.
- Acessus.Modulo.exe aberto na pasta correta; aguarda login manual. A abertura
  direta de Acessus.exe foi recusada pelo aplicativo. .env não foi alterado.
- 152 testes unitários passaram; relatório
  `reports/validacao-continuidade-20261019/testes.html`.
- Nenhum cadastro/exclusão foi feito. Usuário precisa confirmar pessoa/contrato,
  causa, datas e expectativas antes de gravar. Foram solicitados esses dados e
  login manual no Acessus, sem solicitar senha por mensagem.
- Próximo trabalho: resolver o bloqueio do RH sem alterar origem ou serviços
  silenciosamente; validar ocorrências/férias/Acessus e então implementar e
  validar inclusão, exclusão e recadastro com conferência SQL. Não afirmar que
  os fluxos completos passaram ou que estão prontos.

## Atualização de 19/10/2026 — VM ligada, compartilhamentos reparados

Esta atualização prevalece sobre pendências históricas divergentes abaixo.
O usuário autorizou corrigir o necessário para executar testes na VM e atualizar
os arquivos Markdown. Não significa que cenários ainda não implementados passaram.

- VM `AutomatizaTestes`, UUID `cb6316ea-9551-4d91-a0b5-f8c5e67ba51d`, está ligada.
- Restauradas `OrigemAutomatiza` (somente leitura) e `ResultadoVM` (escrita),
  também salvas permanentemente com bloqueio compartilhado da API VirtualBox.
  Não editar o XML da VM ligada. Script idempotente no host:
  `scripts/reparar-compartilhamentos-vm.ps1`.
- Preparação real da VM: `reports/vm/TESTESVM/configuracao-20261019-133434-830962`,
  estado PREPARACAO_TECNICA_CONFERIDA, 149 testes unitários aprovados naquela rodada.
- Cenário SQL real: `reports/vm/TESTESVM/execucoes/20261019-133609-17624270`,
  PASSOU com perfil RHFagundes → desk-tec/novo123. Não valida origem ativa do RH.
- Executor de lotes instalado na Central: `src/automatiza/lotes.py`.
  `examples/lote-preparacao.json` reúne os quatro cenários; `lote-sql.json`
  permite conferir SQL sem autenticação nos sistemas de tela.
- Corrigida publicação de relatórios simulados: cenários com banco/adaptador
  injetado e lotes com executor injetado não publicam em ResultadoVM. Artefatos
  simulados da primeira rodada preservados em
  `reports/vm/TESTESVM/artefatos-unitarios-20261019`, sem valor de teste real.
- A Central exige login manual no RH; não tenta novamente credenciais recusadas.
  O RH foi aberto e deixou visível o diálogo de identificação, sem preenchê-lo.
- Validação host após correções: 150 testes, relatório
  `reports/validacao-reparo-vm-20261019.html`. Conferir o documento de estado
  para a última rodada da VM antes de afirmar a contagem atual.
- Leia `docs/ESTADO-VM-20261019.md` e `docs/PREPARACAO-PARA-TESTAR.md`.

Preparado em 15/10/2026, fuso America/Sao_Paulo. Este arquivo é um resumo de continuidade, não uma transcrição completa nem uma declaração de que processos antigos continuam ativos.

## Atualização mais recente: levantamento ampliado de Acessus, RH e SQL

- Atualização posterior: o usuário pediu executar o cadastro real e depois fazer
  o necessário para liberar esse teste. A tentativa ficou bloqueada antes do
  cadastro; nenhuma ocorrência foi criada. Guia atual:
  docs/DESBLOQUEIO-TESTE-REAL.md. Diagnóstico reutilizável:
  scripts/diagnosticar-acessos.ps1 -Base bras1.
- Schannel falhou localmente, sem rede e sem senha de usuário, com
  SEC_E_NO_CREDENTIALS/0x8009030E. Isso reforça a investigação do contexto de
  execução; não prova defeito no certificado ou senha errada no servidor.
- RhApp e DesktopApp agora verificam o desktop antes de abrir/controlar sistemas.
  O atalho de diagnóstico consegue reutilizar C:\Python314 e os pacotes da .venv
  quando o executável original da .venv está inacessível. Não houve reinstalação.
- A política desta sessão impede solicitar saída do sandbox. O usuário deve
  revisar as opções autorizadas no controle de permissões do aplicativo ou
  /permissions na CLI; restrição gerenciada exige administrador. Não tentar
  contornar isolamento com outro desktop, worker, serviço ou tarefa agendada.
- Validação mais recente: 131 testes unitários aprovados. Relatório:
  reports/diagnostico-acessos/testes.html. O pacote anterior de levantamento é
  um snapshot anterior a essas mudanças e não foi refeito nesta etapa.
- O usuário pediu o máximo de informações dos sistemas e da bras1, avisou que a
  base mudará conforme os testes e liberou o computador durante esta tarefa.
  A liberação não autoriza automaticamente novas inspeções em sessões futuras.
- Relatório central: docs/LEVANTAMENTO-ACESSUS-RH-SQL.md. Leia-o para distinguir
  achados atuais, recursos estáticos e evidências históricas do SQL.
- Acessus: 32 EXE/BPL, 223 estruturas distintas, 16.744 componentes; catálogo
  docs/mapeamentos/acessus-completo/estatico-20261015-ampliado/catalogo.json.
- RH: 1.559 EXE/BPL/DLL, 4.782 estruturas distintas, 156.082 componentes, após
  deduplicar extração inicial e complementar. Índice em
  docs/mapeamentos/rh-completo/INDICE-AMPLIADO.md. Frequência: 175 caminhos
  terminais declarados; não são 175 rotas validadas em execução.
- Foram encontrados textos SQL de férias em RHFERIASCEDIDASPA e ocorrências em
  RHREGOCORRENCIAS/RHOCORRENCIAS, com GERAAFASTAMENTO='S', filtros de situação,
  início e vigência, além de tratamento de DataTermino=0 no destino. Os 101
  trechos sanitizados estão em docs/PISTAS-SQL-INTEGRACAO.md. Não foram executados;
  valores de parâmetros e caminho efetivo do serviço continuam sem confirmação.
- A sessão da ferramenta está em CodexSandboxDesktop, enquanto o desktop de
  entrada é Default. Não tentar contornar esse isolamento. As ferramentas atuais
  não conseguiram navegar normalmente na área de trabalho do usuário.
- Login RH não foi confirmado. A tentativa direta anterior retornou Usuário
  inválido; não houve repetição de login nesta ampliação. Um diálogo de Diretório
  do Sistema indicava C:\META\RHSIS e recebeu Cancelar, sem salvar configuração.
- desk-tec/192.168.50.61:1433 estava acessível por TCP. ODBC 17 e Native Client 11
  falharam na negociação criptográfica (08001), sem mudar configurações de
  segurança. Não houve consulta SQL concluída nesta ampliação nem nova versão
  do motor confirmada. Não confundir instalação local SQLEXPRESS com o servidor.
- O catálogo SQL anterior foi reorganizado em docs/DICIONARIO-BRAS1-HISTORICO.md:
  142 tabelas, 2 views, 1 procedimento, 1 gatilho, 1.373 colunas, 268 índices
  distintos e 176 FKs. As 343 linhas de índices são participações de colunas.
- As ferramentas agora aceitam SQL_DATABASE ou --base; removida a restrição ao
  nome bras1. Conferem DB_NAME() antes das leituras de coleta, preservam origem
  nos relatórios e recusam misturas de bases/servidores. Veja docs/BASES-DE-TESTE.md.
  O esquema esperado das consultas de negócio continua sendo o do Acessus.
- O inventário SQL foi ampliado com consultas de opções, estimativas de catálogo,
  dependências e restrições. Essas consultas novas não foram validadas no servidor.
- Evidências desta etapa: reports/levantamento-20261015. Nenhuma alteração de
  negócio, instalação ou reconfiguração de serviço foi realizada. Não copiar
  credenciais para relatórios ou mensagens. A documentação antiga abaixo é
  histórica quando divergir desta atualização.
- Validação final desta ampliação: 127 testes unitários passaram; relatório
  reports/levantamento-20261015/testes-unitarios.html. Pacote local:
  reports/levantamento-20261015/levantamento-acessus-rh-sql.zip, com manifesto e
  verificação SHA256. O pacote exclui .env e executáveis instalados.

## Instrução inicial ao próximo agente

Leia este arquivo e o README.md antes de agir. Responda em português simples. O usuário está trabalhando manualmente no mesmo computador: não interfira em mouse, teclado, foco, janelas, aplicativos ou serviços. Comece resumindo o estado e aguarde a próxima tarefa; a leitura deste contexto não autoriza novas execuções, instalações ou testes reais.

## Usuário e objetivo

- O usuário é tester de aplicações Delphi e não tem o Delphi nem acesso ao código-fonte.
- Quer automatizar testes com ferramentas gratuitas, principalmente no Módulo de Acesso do Acessus e na integração com o RH Metadados.
- Quer cadastrar ocorrências que geram afastamento e férias para várias pessoas, excluir, recadastrar com novas datas, testar datas antigas, esperar a importação e receber relatório de cada comportamento.
- Consultas SQL podem variar bastante: deve continuar possível escrevê-las manualmente, além das consultas prontas.
- Prefere autonomia para trabalho autorizado que não interfira no uso do computador. Não pedir para ele clicar em cada botão para mapear telas.
- A máquina virtual foi adiada por falta de espaço. Não retomar instalação/configuração de VM sem novo pedido.
- Último pedido: orientar uso do Codex CLI para poupar recursos e criar este arquivo para continuar em outra conversa.

## Regra essencial: não atrapalhar o trabalho

- Enquanto o usuário trabalha, não executar iniciar.ps1, testes desktop/todos, inspeção de janelas, cliques, teclas, capturas de tela ou automação de login.
- Não abrir, minimizar, restaurar ou fechar RH/Acessus; não reiniciar nem reconfigurar serviços.
- Não alterar dados de negócio no SQL nem realizar cadastros/exclusões reais sem uma tarefa apropriada e um momento liberado pelo usuário.
- Trabalho já autorizado em segundo plano incluiu código, documentos, análise local e consultas pontuais/limitadas somente de leitura na bras1. Isso não significa carga zero no servidor nem autorização para consultas pesadas.
- Testes de tela devem aguardar o usuário reservar o computador. O CLI não elimina a disputa de mouse/teclado da automação de tela.
- Não instalar nada, migrar configurações, trocar modelos, criar tarefas agendadas ou atualizar programas apenas por ler este resumo.

## Ambiente e segredos

- Projeto: C:\AutomatizaTestes. Terminal PowerShell, Windows 11 Pro 64 bits.
- Equipamento informado: Ryzen 7 5700G, 8 núcleos/16 processadores lógicos, 31,4 GB RAM, C: 222,5 GB com 70 GB livres na consulta do usuário. Valores podem ter mudado.
- Virtualização de firmware habilitada; hipervisor detectado. Não alterar Hyper-V, BIOS ou recursos do Windows por conta própria.
- Acessus: C:\acesso\Acessus.Modulo.exe; entrar no Módulo de Acesso a partir do painel. Pasta de trabalho correta: C:\acesso.
- RH: C:\meta\rhsis\rh.exe; processos RHID.exe e RHPA.exe. Caminho de telas: Frequência → Programações → Registro de Ocorrências / Férias Cedidas.
- Após login, RH às vezes minimiza. Existe aviso de configurações inválidas conhecido; tratamento previsto no código, ainda sem validação real completa.
- SQL Server informado: desk-tec; banco de testes autorizado: bras1; autenticação SQL. Credenciais/configurações estão no .env local.
- NÃO copiar senhas do .env para este arquivo, README, saídas, argumentos de comandos ou mensagens. Não exibir o conteúdo completo do .env. Há segredos também em tabelas de configurações: evitar SELECT * nessas estruturas.

## Tecnologia e organização

- Python em .venv, pacote editável automatiza-testes, src/automatiza.
- Dependências: pywinauto, pyodbc, python-dotenv, pytest, pytest-html e Pillow. Robot Framework não foi instalado; atualmente usa pytest.
- database.py: consultas parametrizadas, transação desfeita e conexão fechada. Isso não transforma SQL livre em seguro; o comando consulta aceita SQL arbitrário.
- desktop.py / rh.py: código de conexão, abertura e entrada automática preparado; fluxo real completo ainda pendente. Não afirmar que cadastro/exclusão por tela já funciona automaticamente.
- delphi_resources.py: leitura estática de recursos dos executáveis sem executar os sistemas. Nove formulários do RH mapeados, 640 componentes declarados, incluindo componentes não visuais. Mapas estáticos não garantem seletores em execução.
- observador.py: leitura periódica de dbo.Afastamentos, histórico antes/depois, coleta inicial, sinal de parada, bloqueio contra duplicidade e relatórios.
- analise.py: relatório por pessoa, alertas, reaparecimentos de chaves de origem, CSVs e pacote ZIP de evidências com manifesto SHA256.
- casos_offline.py: avalia expectativas a partir das amostras; não executa operações no RH e não comprova causalidade do serviço.
- acompanhante.py: análise contínua dos arquivos locais; consulta somente o estado dos serviços uma vez por minuto. Não faz novas consultas SQL recorrentes.
- referencias.py: consulta pontual de nomes e chaves para até 100 pessoas observadas; exclui CPF, contato e senhas.
- conferencia.py / scripts/conferir.py: consulta filtrada por pessoa, contrato, causa e início; captura amostras e compara dois arquivos da mesma origem/filtros, gerando HTML e JSON. Recusa resultado truncado e preserva saídas existentes.
- scripts/mapear_banco.py: inventário pontual dos metadados da bras1, sem varrer registros.
- scripts/inspecionar_integracao.py: consulta limitada de colunas não secretas de importação, tarefas e agendamentos.

## Comandos existentes — referência, não executar automaticamente

```powershell
cd C:\AutomatizaTestes
.\scripts\testar.ps1 -Grupo base
.\scripts\testar.ps1 -Grupo banco
.\scripts\observar.ps1
.\scripts\observar.ps1 -Acao status
.\scripts\observar.ps1 -Acao parar
.\scripts\analisar.ps1 -Acao status
.\scripts\analisar.ps1 -Acao gerar
.\scripts\analisar.ps1 -Acao exportar
.\scripts\analisar.ps1 -Acao registrar -Arquivo .\meu-caso.json
.\.venv\Scripts\python.exe -m automatiza.cli consulta
```

- Grupo base: testes de código sem banco nem desktop. Banco: consulta real de conexão. Desktop/todos podem controlar janelas.
- observar.ps1 inicia processo oculto, padrão duas horas e 15 segundos entre amostras, iniciando também a análise. Não inicia diariamente nem sobrevive ao desligamento automaticamente.
- Consultar estado antes de iniciar outra coleta. Não interromper uma coleta existente só para atualizar código.
- Arquivo reports/observacao/ativo.json aponta a sessão. Não presumir que a sessão esteja ativa com base na existência desse arquivo; conferir processo/bloqueio e data da última amostra.
- Exemplos preparados: examples/casos-offline (8 casos, todos desativados), examples/consulta-afastamentos.modelo.json e examples/integracao-rh.modelo.json (outro formato, para consultas manuais por cenário).
- Casos esperados devem ser preenchidos e registrados antes da ação manual, com amostra anterior recente, ID interno, causa e datas exatas. Modelos têm datas ilustrativas de 2026/2001; não usar sem ajustar.

## Evidências históricas e limites conhecidos

- Última execução de testes de código registrada nesta conversa: 117 passaram, relatório reports/base-20261015-100442-917.html. Não é validação de 117 regras de negócio.
- Sessão histórica: reports/observacao/20261015-120131-418f3482. Na última conferência havia 16 inclusões, 17 remoções, 0 alterações e 11 registros atuais; coleta e análise sem falhas. NÃO tratar esses números ou processos como atuais sem conferir.
- Pacote exportado e manifesto verificado: reports/evidencias/evidencias-20261015-125910-11464829.zip, 22 arquivos com hashes consistentes e sem .env.
- Inspeção de metadados em reports/banco/20261015-095741: 142 tabelas, 2 views, 1 procedimento, 1 gatilho; 1373 colunas e 176 vínculos de colunas em FKs. As 343 linhas de índices representam participações de colunas, não 343 índices distintos.
- dbo.Afastamentos: Id, DataInicio, DataTermino, IdPessoa, Causa, IdFreq. PK_Ferias em Id; índice único UQ_IdFreqAfastamentos em IdFreq; FK para Pessoas.id.
- Pessoas.IdExportacao e ContratoExportacao são candidatos para vincular RH e Acessus, ainda sem correspondência de negócio confirmada.
- Foram observados términos literais em 1899-12-30: possível data-base Delphi. Não assumir que significa NULL/fim aberto, nem reprovar automaticamente. O relatório destaca a interpretação pendente.
- Configuração pontual em reports/integracao-config/20261015-100206: intervalo_minutos=1, contratos_alterados=2000-01-01, empresa 1 e unidade vazia; nenhuma tarefa/agendamento nas duas tabelas AcessusSync consultadas. Isso não comprova frequência real, regra de corte ou configuração efetivamente usada pelo serviço RH.
- Estado histórico de serviços: Importação API executando; AcessusSync, MetahConnectService e Comunicação parados. Não reconfigurar e não inferir responsável pela integração apenas por isso.
- Comparação local de duas amostras: 23 diferenças líquidas em reports/conferencia/20261015-primeira-validacao/comparacao. Histórico contínuo tinha 33 eventos; medidas diferentes, pois duas amostras escondem mudanças intermediárias.

## Documentação e próximo trabalho

Pedido adicional em 15/10/2026: inspecionar o Painel de Módulos e as telas dentro
de cada módulo, salvando mapas para uso no código. O usuário autorizou controlar
as telas e prosseguir sem sua presença nesta tarefa. A inspeção foi executada;
essa autorização não inicia automaticamente outra inspeção em conversas futuras.

- Resultado: docs/mapeamentos/acessus-completo/LEIA-ME.md; catálogo consolidado
  e rotas-para-codigo.json na mesma pasta. Escopo em docs/PLANO-INSPECAO-TELAS.md.
- Foram inspecionadas 120 rotas nos seis módulos: Acesso (41), Refeitório (20),
  Portaria (12), Estacionamento (19), Escola (26) e Administração (2). Também
  foram mapeados o painel, a abertura dos seis módulos e Ajuda → Novidades.
- Administração → Opções do Sistema está declarado no executável, mas não
  aparece no menu em execução; causa não confirmada. Quatro opções Sair dos
  módulos e LogOff/Sair do painel não foram acionados.
- Capturas estruturadas, abas e formulários vazios cancelados estão em
  reports/inspecao-telas/20261015: 337 arquivos de tela referenciados, 172
  variações de abas e 45 inclusões vazias canceladas. Valores de campos, grades e listas foram
  omitidos. Não foram acionados botões de salvamento, processamento, exclusão
  ou envio a equipamentos. Isso não valida regras de negócio ou integrações.
- Extração estática atual: docs/mapeamentos/acessus-completo/estatico-20261015-v2,
  com 157 estruturas distintas e 11.272 componentes, incluindo não visuais.
  A primeira extração sem v2 é parcial; preferir o catálogo v2 e o consolidado.
- As barras de menu são TActionMainMenuBar e não expuseram HMENU nativo.
  A navegação funcionou por click_input em itens UIA. select/Invoke UIA falhou.
  A árvore de menus UIA pode repetir irmãos como filhos: não usá-la para inferir
  submenus recursivamente. Rotas declaradas vieram de ActionBars nos recursos.
- A tentativa de ler TPageControl usando TabControlWrapper provocou um erro
  COMCTL32 no Acessus. Aviso registrado e fechado; técnica abandonada. Abas
  foram percorridas depois por cliques em TabItem UIA. Nenhuma inclusão foi salva.
- scripts/inspecionar_telas.py captura controles sem valores; navegar_inspecao.py
  e percorrer_telas.py foram usados na sessão autorizada. Não executar estes
  navegadores automaticamente. consolidar_inspecao.py analisa só arquivos locais.
- O extrator passou nos cinco testes unitários existentes de test_delphi_resources.py.
  Não foram executadas suítes de banco/desktop nem cenários reais de negócio.
- A conferência local final não encontrou arquivos referenciados ausentes,
  controles duplicados nos mapas utilizados ou valores nos campos omitidos.
  Manifesto SHA256 em reports/inspecao-telas/20261015/manifesto-sha256.json.
  Os seis módulos ficaram em suas janelas principais, sem formulários abertos,
  e o painel recebeu o foco ao final. Não presumir esse estado em outra sessão.

O README.md foi reescrito em português com sequência prática: acompanhar banco, registrar caso esperado, comparar amostras e exportar evidências. Nomes técnicos permanecem exatos para copiar comandos. Leia também docs/ANALISE-E-CASOS.md, CONSULTAS-E-COMPARACAO.md, ESTRUTURA-BRAS1.md, INTEGRACAO-RH.md e docs/mapeamentos.

Falta confirmar regras da integração (datas antigas, causa, término sem data e serviço), vínculo de pessoas/contratos, validar seletores e login em execução e implementar operações de tela por cenário. Para todo o sistema, ainda será necessário inventariar módulos/regras e definir dados/restauração. Não inventar aprovações sem resultado esperado.

## Passagem para o CLI

- Em 15/10/2026, Get-Command encontrou codex.exe no PATH e codex --version respondeu 0.162.0-alpha.17.2. É uma versão vinculada à instalação local do aplicativo; o caminho completo contém um identificador de versão e pode mudar. Não fixar esse caminho em atalhos.
- node e npm também foram encontrados, mas não foi necessário instalar outra cópia do Codex.
- Iniciar no PowerShell: `cd C:\AutomatizaTestes` e `codex "Leia CONTEXTO-PARA-CONTINUAR.md e README.md. Resuma onde paramos e aguarde minha próxima tarefa. Não controle janelas nem execute testes reais."`.
- Se necessário, autenticar pelo fluxo oficial do CLI, escolhendo entrar com ChatGPT. Não colocar chave/senha na linha de comando. Disponibilidade e limites dependem da conta; projeto de testes gratuito não significa uso ilimitado da IA.
- O arquivo fornece continuidade do projeto, não transfere automaticamente toda a conversa nem garante as mesmas ferramentas/plugins/permissões do aplicativo gráfico. Validar capacidades reais do CLI quando forem necessárias.
- Fechar o aplicativo gráfico pode reduzir uso da interface, mas não prometer números de economia ou que todos os processos auxiliares terminem. Não fechar esta sessão automaticamente.
