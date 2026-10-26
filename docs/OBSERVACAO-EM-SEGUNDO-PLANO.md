# Conferência SQL enquanto você testa manualmente

O acompanhamento agora inclui análise por pessoa, alertas, casos esperados e exportação de evidências. Consulte [Análise e casos](ANALISE-E-CASOS.md). O acompanhante inicia junto com as novas coletas; `-SemAnalise` permite iniciar apenas o observador SQL.

O observador consulta `dbo.Afastamentos` na base selecionada para o teste, inicialmente `bras1`. Veja [seleção da base](BASES-DE-TESTE.md).
Ele não abre aplicativos, não acessa mouse/teclado, não tira capturas de tela,
não grava no SQL Server e não inicia/reinicia serviços.

## Iniciar, consultar e parar

Dentro de `C:\AutomatizaTestes`:

```powershell
# Executa por duas horas, em processo oculto, com consulta a cada 15 segundos.
.\scripts\observar.ps1

# Exibe apenas o estado atual e o caminho do relatório.
.\scripts\observar.ps1 -Acao status

# Encerra por um sinal em arquivo, após a consulta atual, preservando os dados.
.\scripts\observar.ps1 -Acao parar
```

Para mudar a duração ou filtrar os IDs internos do Acessus:

```powershell
.\scripts\observar.ps1 -DuracaoMinutos 60 -IntervaloSegundos 15 -Pessoas 101,102,103
```

Os IDs acima são ilustrativos. Sem `-Pessoas`, todos os afastamentos da base selecionada
são observados. A trava de processo impede duas observações simultâneas.
O estado também verifica a trava: um processo morto não continua sendo
apresentado como ativo somente porque deixou um resumo antigo.

## Registrar o que você fez no RH

Essa etapa é opcional, mas ajuda a correlacionar o resultado:

```powershell
.\scripts\observar.ps1 -Acao anotar -Nota "Incluí férias no contrato X, de DD/MM a DD/MM; IdPessoa no Acessus Y."
```

As anotações são declarações de ação manual, não prova de que o RH gravou.
Elas aparecem no relatório na próxima coleta (ou são atualizadas imediatamente
quando a sessão já terminou).

## Arquivos e interpretação

Cada sessão fica em `reports/observacao/<sessao>`:

- `relatorio.html`: resumo e últimas 200 mudanças, com antes/depois.
- `eventos.jsonl`: histórico completo de inclusões, remoções e alterações.
- `inicial.json`: primeira amostra válida; registros iniciais não contam como inclusões.
- `atual.json`: última amostra válida.
- `amostras.jsonl`: horário, quantidade de linhas e tempo de cada consulta válida.
- `erros.jsonl`: falhas de coleta sem mensagem SQL ou senha.
- `resumo.json`: estado do processo, contagens e eventos recentes.
- `anotacoes.jsonl`: ações informadas manualmente.

Os horários são salvos em UTC. Para São Paulo, em 15/10/2026, subtraia três horas.
O comando de status mostra o caminho exato do relatório; nenhum navegador é aberto automaticamente.

A comparação usa a chave `Id` do Acessus. Alterações de pessoa, datas, causa ou
`IdFreq` preservam antes/depois. Exclusão seguida de inclusão com outro `Id`
produz eventos separados; a ferramenta não presume que sejam o mesmo cadastro.

Uma falha de consulta não é tratada como tabela vazia. A amostra anterior é
preservada e a comparação é retomada quando há nova leitura válida. Cinco
falhas consecutivas encerram a sessão com estado de erro.

As consultas têm tempo limite curto, prioridade baixa em caso de deadlock e
até um segundo de espera por bloqueios. Não se usa `NOLOCK`, para evitar
registrar dados ainda não confirmados. O intervalo mínimo é cinco segundos;
o padrão é 15. Há limite de 10 mil linhas por amostra; excedê-lo gera erro em
vez de apresentar desaparecimentos falsos por truncamento.

O relatório observa **o destino**, não o serviço nem a origem. Ele não dá
PASSOU/FALHOU automaticamente. Para afirmar que uma exclusão propagou, é
necessário correlacionar a existência anterior, a exclusão no RH e a remoção
do registro esperado no Acessus. Mudanças entre duas amostras podem passar
despercebidas. Eventos anteriores ao início da sessão não são recuperados.
