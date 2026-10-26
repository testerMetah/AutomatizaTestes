Current evidence (2026-10-20): reports/integracao-api/20261020/auditoria-103518/COMPLEMENTO.md and diario-testes.txt. Historical preparation below is superseded by this audit.

# Teste de reserva: Frequência → API SIRH → Acessus

## API SIRH configurada e autenticando ? 20/10/2026

Usu?rio forneceu e autorizou configurar e-mail/URL/senha da API. Salvo pela tela Configura??o API; reabertura confirmou os tr?s campos, sem exportar senha. URL https://apimetadados.metahequipamentos.com.br/ e e-mail metahdev02@gmail.com. HTTPS 443 agora acess?vel. Servi?o FrmSyncImpViewsPrincipal Running; log atual de 20/10/2026 09:30:03 registra StatusCode=200 e token obtido com sucesso. Falha de conectividade anterior ? hist?rica. Evid?ncia sanitizada: reports/configuracao-api/20261020/resultado.json. Autentica??o n?o comprova reserva importada nem correspond?ncia da API com RHFagundes. Destino continua desk-tec/novo123 e conex?o SQL RHFagundes preservada.


## Conex?o SIRH criada em 20/10/2026

Usu?rio autorizou criar a conex?o SIRH. Cadastro salvo pela tela do Importador Metadados: ConexaoBD Id 2, TipoBD 0 (SQL Server), desk-tec/RHFagundes. Credenciais existentes foram reutilizadas em mem?ria ap?s consulta de origem bem-sucedida; nenhuma senha registrada no relat?rio. Cadastro API Id 1 preservado. Destino Acessus continua desk-tec/novo123, j? atualizado pelo Atualizador da 2.11. A configura??o de Importar Reservas agora abre, e suas duas abas foram capturadas; fechada sem Confirmar/importar. Zero reservas no destino. Evid?ncia: reports/conexao-sirh/20261020/resultado.json. Bloqueio anterior por aus?ncia de conex?o SIRH resolvido. Falha de conectividade da API permanece separada.


## Escopo e estado em 19/10/2026

O usuário pediu criar uma reserva no Frequência e comprovar sua importação
no Acessus pela tela, pelo banco do Acessus e pelo log do importador. Autorizou
configurar a API no módulo Acesso, instalar AcessusSyncImportacao e iniciar o
serviço. O teste completo **ainda não foi executado**.

Relatório real de preparação e estado anterior:
`reports/reserva-sirh/20261019-150635-2553b9dc/relatorio.html`.
Estado **PENDENTE_CONFIRMACAO_API**, sem reserva criada e sem ciclo de importação
iniciado. Não confundir com aprovação de negócio.

## Descoberto nas telas e no SQL

- RH autenticado, alias RHFagundes. Programações → Reserva ou Consumo abre
  `TFrm_RHPA5210`, título Reserva/Consumo. Menu extraído: Reserva ou Cons&umo;
  fallback de navegação `%pu`. Cenário real de abertura PASSOU:
  `reports/execucoes/20261019-150455-fbafbbe9`.
- Individual: contrato, início, término, tipo de refeição, refeitório, refeição,
  cardápio, quantidade e autorização. Campos de código têm pesquisa; existem
  programação coletiva e Tipos de Dia. A gravação ainda não foi acionada.
- Contrato 129 consultado na unidade 0001: Cleonice Licheski, situação Ativo,
  admissão 30/06/2026. SQL da origem confirma empresa 1090 e pessoa 10900129.
  Nenhuma programação encontrada para unidade 0001/contrato 129 no estado anterior.
  Esse é um candidato, não uma seleção de dados confirmada para gravação.
- Acessus novo123 contém três pessoas com esse nome e IdExportacao 129:
  IDs 7, 8 e 9; ContratoExportacao zero. Não escolher uma delas arbitrariamente.
  É necessário descobrir a regra efetiva de correspondência, inclusive credencial.
- Reservas no Acessus: `dbo.RefeicoesReservas`. Campos reais: id, credencial,
  refeicoes, id_refeitorio, IdExportacao, datahoraini, datahorafim, situacao,
  status, id_empresa e campos de autorização. A tabela **não tem IdPessoa**.
  Baseline: zero reservas e zero refeitórios em novo123.
- RH: `RHPROGRESERVACONSUMO`, chave unidade/contrato/nroordem, com início,
  término, refeitório, refeição, tipo, cardápio e quantidade. Cadastros reais em
  RHREFEITORIOS e RHREFEICOES foram consultados sem alterações.
- Acessus: Relatórios → Reservas e Consumos abre `TFrmRelResCon`. Relatório
  aberto e capturado; nenhuma consulta com período inventado foi executada.

## API e serviço

- Acesso → Ferramentas → Importador Metadados → tipo API do SIRH → Configurar
  abre `TFConfigAPI`. URL, usuário e senha já estavam preenchidos; a configuração
  foi apenas inspecionada e cancelada, sem salvar alterações.
- Endpoint sem parâmetros/credenciais:
  `https://apimetadados.metahequipamentos.com.br/`, resolvido nesta VM como
  192.168.50.105. Intervalo existente de um minuto, contratos desde 01/01/2000,
  empresa Acessus 1, sem filtro de unidade. Não há prova atual de que essa API
  atende a RHFagundes. Essa confirmação foi solicitada ao usuário.
- GET de metadados Swagger via Python falhou por certificado autoassinado
  não confiável. Isso não demonstra que o serviço falhará: ele ainda não foi
  iniciado. Não houve envio de credenciais nesse GET nem mudança de confiança TLS.
- Serviço instalado com elevação padrão do Windows usando o executável existente:
  `C:\acesso\AcessusSyncImportacao.exe /install /silent`.
  Nome interno `FrmSyncImpViewsPrincipal`, descrição **Acessus - Importação API**,
  início Auto, estado **Stopped/PARADO**. Não estava instalado antes desta etapa.
  Origem/destino do executável em ConexaoConfig.ini: desk-tec/novo123.
- Não foi iniciado enquanto a origem da API está sem confirmação. Iniciar o
  importador pode importar vários cadastros, não só a reserva escolhida.
- Logs encontrados em C:\acesso\Logs: AcessusSyncImportacao.log e
  **AcessusSyncProcessoService.log** (esse é o nome observado). Últimas linhas
  datadas de 16/10/2026, portanto históricas. Não usar essas linhas para aprovar
  um teste de hoje. O log histórico contém falha sobre horas extras; não é
  resultado da reserva nova. Não publicar logs brutos, tokens ou senhas.

## Código entregue

- `examples/cenarios/05-abrir-reservas.json`: cenário de abertura sem gravação,
  executável pela Central com RHFagundes_para_novo123.
- `RhApp.open_screen('reservas')` e `Acesso.open_screen('reservas_consumos')`:
  rotas confirmadas nas telas.
- Ações `sql_reserva_verificar` e `sql_reserva_aguardar`: consultam a tabela
  correta do Acessus, com parâmetros, empresa, credencial, refeitório e período
  exatos; admitem também IdExportacao, refeicoes, situacao e status. Espera exige
  contagem e estabilidade e registra as linhas filtradas na auditoria.
  Isso é infraestrutura de conferência, não fluxo completo de cadastro validado.
- `examples/reservas-sirh/caso-pendente.json`: planejamento desativado, com
  candidatos reais e dados ainda nulos. Não é um cenário executável de cadastro.
- 164 testes unitários passaram, relatório
  `reports/validacao-reservas-sirh-20261019/testes.html`. Sem valor de aprovação
  de importação real. Datas sintéticas dos testes unitários não são dados do caso.

## Sequência para concluir

1. Confirmar API correspondente à origem RHFagundes e sua configuração válida.
2. Definir uma pessoa/contrato sem ambiguidade e os códigos reais de refeitório,
   refeição, cardápio e tipo; confirmar período e resultado esperado antes de salvar.
3. Completar o cenário, tirar baseline recente da origem e do destino e registrar
   posição/tamanho atual dos logs para separar o ciclo novo dos históricos.
4. Iniciar o serviço instalado, usando elevação administrativa padrão, e conferir
   estado e novos logs. Se for necessária importação inicial de cadastros, separar
   essa preparação da reserva que será testada.
5. Criar a reserva pela tela, salvar, reconsultar no RH e comprovar o registro na
   origem. Não inserir a reserva diretamente por SQL.
6. Aguardar o ciclo e comparar pessoa/credencial, empresa, refeitório, refeição,
   período, situação e quantidade/duplicidade na tela e em RefeicoesReservas.
7. Anexar evidências do ciclo atual e concluir PASSOU/FALHOU/INCONCLUSIVO conforme
   os dados observados. Não aprovar somente porque o serviço está Running.
