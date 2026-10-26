# Arquitetura e manutenção

## Camadas

`Abrir-Painel.bat` chama `automatiza.nova_cli painel` na venv Python 32 bits. `nova_cli.py` também é o entry point do pacote `automatiza`; comandos históricos são delegados a `automatiza.cli`, preservando scripts antigos. O painel (`painel.py` + `painel.html`) usa apenas a biblioteca HTTP padrão, escuta em `127.0.0.1`, recebe um token local de sessão e lança a CLI em subprocesso. O console da página consulta linhas novas e permite encerrar a árvore de processos.

`catalogo_comandos.py` fornece a lista didática tanto para `automatiza comandos` quanto para o painel. `perfis_teste.py` carrega perfis declarativos, monta `Settings` e valida `DB_NAME()` contra a lista de teste antes de escrita. `diagnostico_unificado.py` faz as checagens de leitura. `database.py` executa SQL via pyodbc e confirma o banco efetivo; rollback não torna SQL arbitrário seguro.

### Sentinela e pausa

`nova_cli.py` inicia `sentinela/runtime.py` em um processo Python 32 bits separado para os comandos de teste. O processo registra `RegisterHotKey` e mostra avisos Win32/Tk sem ativação; o diálogo de pausa pode receber foco. Arquivos JSON em `%TEMP%` usam substituição atômica para estado, pedido, confirmação, heartbeat e resultado. Se o registro global falhar, a sentinela tenta as outras teclas; um hook de teclado de baixo nível é a última alternativa que ainda consome a tecla. `pausa.py` concentra o ponto seguro, o relógio ativo e a recusa dos atalhos reservados no gateway. O supervisor de Auditorias e o script legado usam os mesmos pontos antes de gestos de interface. Após 1,35 s sem confirmação, a sentinela tenta suspender os filhos da CLI e os retoma antes de continuar ou cancelar. O painel nunca é suspenso.

### Auditorias/Históricos

`supervisor_auditorias.py` descobre o processo por caminho, abre/login/navega, executa levantamento e teste, monitora progresso e retoma após travamento. `processos_auditorias.py` usa pywin32 porque `psutil` não instala nesta venv 32 bits sem compilação C++. `seletores_auditorias.py` reúne classes, nomes e menus das telas observadas; remapeie por build. A suíte existente `scripts/testar_auditorias_cronologico.py` continua responsável pelas interações e usa `AUTOMATIZA_PERFIL` para selecionar o banco, preservando variáveis legadas de filtro/extremo. `diario_auditorias.py` escreve os dois logs permanentes em acréscimo e sincroniza a cada ação. `relatorio_auditorias.py` lê os JSONLs, agrupa mensagens normalizadas, compara rodadas e gera HTML sem internet.

Um checkpoint é a tupla índice do histórico + filtro + subcampo + número da tentativa. Na retomada, checkpoints já gravados são pulados. Se o limite de reinícios for atingido, o supervisor escreve `ERRO_AUTOMACAO` para filtros ainda não executados, com o motivo. Um diálogo de erro é capturado antes de ser fechado.

`oraculos_auditorias.py` só aplica contagem quando um documento de `docs/cenarios/` tiver front matter `status: CONFIRMADA` e entrada `auditorias_contagens` com módulo, histórico, filtro e SQL `SELECT COUNT(*)` simples. O valor do filtro é passado por parâmetro `?`. Hoje não existe regra de contagem confirmada; portanto a suíte é exploratória. Não extrapole a regra geral de exclusão lógica para contagens específicas.

`fixtures_sinteticas.py` fornece prefixo `AUTOTEST_<timestamp>_` e `finally` que chama limpeza específica da entidade mesmo após falha parcial em criação. Quem criar a fixture real fornece callbacks de criação/limpeza e deve verificar os identificadores/prefixo.

### Demais fluxos

`sequencias/` lê cenários YAML, gera ordens com seed, usa somente regras confirmadas como oráculo, expõe keywords ao Robot e produz `reports/<execucao>/RELATORIO.html`. `acoes/` e `ui/` são o backend genérico novo; ações de escrita ainda sem adaptador retornam `BLOQUEADO`. `observador.py` coleta retratos SQL de `dbo.Afastamentos`; `analise.py` avalia casos esperados e `conferencia.py` compara estados. `ciclos_cli.py` e `ciclos_sirh.py` são adaptadores especializados que podem escrever via RH/API e exigem manifesto, banco e autorização do usuário final na nova CLI.

## Desenvolvimento de uma tela nova

1. Leia `docs/mudancas/` e `docs/cenarios/`; não use código antigo como fonte da regra de negócio.
2. Exporte a árvore de controles para `docs/mapas-de-tela/` e registre build/caminho.
3. Mapeie seletores por classe/hierarquia; posição somente se necessária e explicada.
4. Separe ação, dados de entrada, resultado esperado e evidências. Use polling com timeout, sem `sleep` fixo.
5. Para escrita, confirme banco de teste via `DB_NAME()`, prefixe dados sintéticos e garanta limpeza em `finally`.
6. Rode `automatiza testes-unitarios`; depois valide na sessão Windows real e guarde logs/screenshots.

## Pastas de saída

`resultados/passo-a-passo.log` e `resultados/passo-a-passo-detalhado.jsonl` nunca são reescritos. Cada rodada de auditoria tem `tentativas.jsonl`, `resumo.json`, `RELATORIO.html` e PNGs. Os demais fluxos usam `reports/`. Ambas as pastas são ignoradas pelo Git. `docs/LOGS-AUDITORIAS.md` explica os campos de cada linha.
