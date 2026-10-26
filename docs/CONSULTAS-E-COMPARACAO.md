# Consultas prontas e comparação antes/depois

As ferramentas abaixo não acessam o desktop. Consultas pontuais têm timeout de cinco segundos, espera por bloqueios de um segundo e quantidade máxima de registros. Mesmo somente leitura consome algum recurso do servidor; não é promessa de carga zero. Nenhuma rotina inicia serviços ou modifica cadastros.

## Consultar

Copie `examples/consulta-afastamentos.modelo.json` para outro arquivo e substitua `[0]` pelos IdPessoa internos. Pode usar várias pessoas, até 100. Campos opcionais:

| Campo | Significado |
| --- | --- |
| pessoas | IDs internos de Pessoas; lista vazia desativa esse filtro. |
| contrato | Valor exato de Pessoas.ContratoExportacao; vínculo com o RH ainda precisa ser confirmado. |
| causa | Texto exato da causa segundo as regras de comparação do SQL Server. |
| inicio_de | DataInicio maior ou igual a esta data. |
| inicio_ate | DataInicio menor que esta data, limite exclusivo. |
| limite | 1 a 10000; se excedido, a amostra é recusada, sem salvar resultado truncado. |

Filtros preenchidos se combinam com AND. É obrigatório pelo menos um filtro. O período filtra o **início** do afastamento, não todos os afastamentos que atravessam o período. Use datas ISO locais sem fuso; `null` desativa o filtro. Os parâmetros são enviados separadamente do SQL.

```powershell
.\.venv\Scripts\python.exe .\scripts\conferir.py consultar --filtros .\meus-filtros.json --saida .\reports\conferencia\antes.json
# Depois da ação manual e da espera de importação:
.\.venv\Scripts\python.exe .\scripts\conferir.py consultar --filtros .\meus-filtros.json --saida .\reports\conferencia\depois.json
.\.venv\Scripts\python.exe .\scripts\conferir.py comparar --antes .\reports\conferencia\antes.json --depois .\reports\conferencia\depois.json --saida .\reports\conferencia\comparacao-01
```

A comparação gera HTML e JSON com inclusões, remoções e campos alterados. Recusa origem/filtros diferentes e amostras invertidas. Os arquivos de saída existentes são preservados; escolha outro nome por execução.

É uma diferença entre dois momentos: se algo foi excluído e reinserido entre eles, o resultado líquido pode esconder essas etapas. Use o observador contínuo para preservar as mudanças intermediárias visíveis nas amostras. Uma diferença por si só não aprova nem reprova uma regra de negócio.

## Modelos de cenários

`examples/casos-offline` contém oito modelos individuais: inclusão, exclusão e recadastro de férias e ocorrências, mais duas alternativas para datas antigas. Todos vêm desativados e sem pessoa válida, para não produzir uma conclusão fictícia.

As alternativas de datas antigas representam expectativas distintas: escolha conforme a regra de corte confirmada. O ano ilustrativo não representa uma regra descoberta. Para várias pessoas, crie um caso por pessoa, com ID exclusivo. Confirme causa, período e prazo, depois siga [Análise e casos](ANALISE-E-CASOS.md) para registrar a expectativa antes da ação manual. O cadastro/exclusão no RH continua manual nesta etapa.

## Inspeção pontual da configuração

```powershell
.\.venv\Scripts\python.exe .\scripts\inspecionar_integracao.py
```

Lê até 100 configurações não secretas de DADOS_IMPORTACAO_API, AcessusSyncTarefas e AcessusSyncAgendamento. Exclui credenciais e o conteúdo genérico de opções. Resultados ficam em `reports/integracao-config`.

Em 15/10/2026 às 10h02 de São Paulo, foi observado um registro de importação API com `intervalo_minutos=1`, `contratos_alterados=2000-01-01`, empresa 1 e unidade vazia. Não havia tarefas nem agendamentos AcessusSync nessas tabelas naquele instante. Esses valores não comprovam serviço em execução, regra efetiva de datas antigas ou uso dessa configuração pela integração do RH.

Validação inicial: uma consulta real filtrada retornou 11 registros. A comparação local entre o início e o estado observado da sessão registrou 23 diferenças líquidas. A coleta contínua já havia observado 33 eventos intermediários; são medidas diferentes, não uma divergência entre relatórios.
