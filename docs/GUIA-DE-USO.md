# Guia de uso: escolha o que quer fazer

## Ajuda dentro do painel

O painel tem um ícone **ⓘ** ao lado dos campos, botões, cartões e estados. Passe o mouse para ler uma explicação rápida. Clique no ícone para manter o balão aberto. Use **Tab** para chegar ao ícone e **Enter** para abri-lo pelo teclado. Clique fora ou aperte **Esc** para fechar. O link **Ver no glossário** explica palavras técnicas.

O botão fixo **Explicar esta tela** abre instruções curtas para a página atual. **Modo ajuda** mostra uma frase curta sob os campos e vem ligado na primeira visita. Sua escolha fica guardada no navegador. A página **Catálogo de Testes**, destacada no menu, mostra o alcance, o risco, o banco e os requisitos de cada teste. Comece pelo roteiro de cinco passos no topo.

Para adicionar ajuda a um controle novo, acrescente uma chave em `src/automatiza/painel_ajuda.json`, dentro de `ajudas`, com título, o que é, o que acontece, quando usar, exemplo, risco e como saber se deu certo. Coloque `data-ajuda="sua.chave"` no rótulo, botão ou título em `src/automatiza/painel.html`. O teste `tests/unit/test_painel_ajuda.py` detecta chaves faltantes e textos sem uso. Cartões do Catálogo ficam no mesmo JSON, em `catalogo`; termos ficam em `glossario`.

## Quero abrir o painel

Dê duplo clique em `Abrir-Painel.bat` na raiz do projeto. Ele usa o Python 32 bits de `C:\python32b\venv32`, escolhe `127.0.0.1:8765` ou a próxima porta livre e abre o navegador. O console mostra a URL; **fechar o console encerra o painel**. A automação desktop deve rodar na sua sessão Windows interativa, com a tela desbloqueada.

## Quero conferir se estou no banco certo

Na página **Início**, clique **Rodar checagem do ambiente**. Cada item aparece como `OK`, `ALERTA` ou `ERRO`. São verificados: Python 32 bits, versão/caminho dos executáveis, Server/Database nos dois INIs de cada instalação, driver ODBC, `SELECT 1`/`DB_NAME()` dos bancos configurados e estado dos três serviços. Um `ERRO` faz `automatiza ambiente` retornar código diferente de zero. A página mostra o banco efetivo no topo quando a conexão de auditorias passa.

Na CLI: `automatiza ambiente`. A instalação principal usa o perfil `sequencias` e a cópia do PC físico usa `auditorias`. Perfis ficam em `profiles/`; não coloque senhas neles.

## Quero testar Auditorias/Históricos

Na página **Auditorias/Históricos**, escolha módulo ou **todos**, perfil, variações extremas e filtro opcional. O comando CLI equivalente aparece antes do botão Executar. A execução:

1. Descobre o PID pelo caminho do executável. `--pid` é opcional para desambiguar uma instância.
2. Se necessário, abre `Acessus.Modulo.exe` da pasta do perfil, autentica com `TESTE_USUARIO`/`TESTE_SENHA` do `.env`, abre o módulo e entra em **Consultas → Auditorias/Históricos**.
3. Exporta o mapa da tela e percorre históricos, filtros, campos e cinco variações. `--extremo` executa cinco entradas extremas separadamente.
4. Registra cada passo nos dois logs permanentes; salva tentativas e capturas na pasta da rodada.
5. Se detectar processo morto, janela sem resposta, período sem novos passos ou `Access violation`, captura a janela, reinicia o módulo e retoma tentativas não concluídas. Após três reinícios, marca o restante como erro de automação e segue ao próximo módulo.
6. Gera `RELATORIO.html` autocontido, contagens por módulo, achados agrupados e links para screenshots.

Exemplos: `automatiza auditorias --modulo refeitorio`; `automatiza auditorias --modulo todos --extremo`; `automatiza auditorias --modulo escola --filtro Pessoa --pular 1,3`.

O perfil `auditorias` aponta a `C:\AcessusHostFisico` e `desk-tec/AcessoFagundes`. Confirme que os INIs da cópia apontam ao mesmo destino. Não use mouse/teclado enquanto a automação opera. Uma mudança de layout pode exigir remapear os seletores em `src/automatiza/seletores_auditorias.py`.

## Quero acompanhar ou parar a execução

Abra **Execução ao vivo**. A saída chega por consulta periódica, o estado mostra rodando/concluído/falhou, e **PARAR** encerra o processo e os filhos. O painel aceita somente uma execução iniciada por ele por vez. A observação SQL começa em segundo plano para não segurar o painel.

## Quero investigar um erro

Em **Resultados**, abra a rodada e `RELATORIO.html`. A tabela traz estados por módulo; **Achados agrupados** reúne mensagens semelhantes, com quantidade e ocorrências. Abra `resultados/passo-a-passo.log` para o passo a passo cronológico, ou o JSONL para campos estruturados. Filtre pelo estado (por exemplo `ERRO_APLICACAO`). O screenshot do diálogo é feito antes de clicar em OK. `ERRO_AUTOMACAO` pode indicar seletor, janela ou travamento, então compare o mapa da build.

Use **Comparar rodadas** para listar erros novos, corrigidos, regredidos e persistentes; a chave é módulo + histórico + filtro + estado. Na CLI: `automatiza comparar-rodadas resultados/rodada-antiga resultados/rodada-nova`.

## Quero testar uma build nova

Use **Preparar nova build**. A página mostra versão de origem `\\VBOXSVR\OrigemAcessus`, versão local, `product.key` e INIs. Feche todos os módulos da cópia. O botão exige digitar `COPIAR BUILD`, faz backup de `C:\AcessusHostFisico`, copia os arquivos e valida os principais. Confira novamente os INIs e, se a build exigir migração de schema, siga [ATUALIZACAO-ACESSUS.md](ATUALIZACAO-ACESSUS.md) no banco de teste. Depois rode **Início → Checagem** e a auditoria.

## Quero rodar outros fluxos

- **Sequências e Robot:** escolha YAML ou seed fixa; `automatiza sequencias --arquivo tests/sequencias/checagem_leitura.yaml` e `automatiza robot --tag smoke`. Ações sem adaptador/regra retornam `BLOQUEADO`, não aprovado.
- **Observação SQL:** iniciar, anotar ação manual, consultar status e parar. CLI: `automatiza observar iniciar --duracao 1800 --intervalo 15`; `automatiza observar anotar --nota "cadastrei teste"`; `automatiza observar status`; `automatiza observar parar`.
- **Comparar consultas:** salve retratos antes/depois com arquivo de filtros JSON e compare localmente. A seção mostra o comando equivalente. Formato do arquivo: [CONSULTAS-E-COMPARACAO.md](CONSULTAS-E-COMPARACAO.md).
- **Ciclos RH/SIRH:** planejar não escreve; executar/suite exigem `--confirmo-escrita` e que destino do plano, perfil e `DB_NAME()` coincidam com banco permitido. No painel, confirme o nome do banco efetivo e a frase de ciência. Um manifesto antigo apontando a `novo123` é recusado pelo perfil atual até ser adaptado a uma base de teste confirmada.
- **Testes unitários:** `automatiza testes-unitarios`.
- **Comandos:** a página didática lê `src/automatiza/catalogo_comandos.py`, a mesma fonte de `automatiza comandos`; inclui exemplos de PowerShell para PID, versão e serviços.

## Configuração e segurança

A página **Configuração** edita somente campos não secretos dos perfis. Se o nome do banco for alterado, o perfil perde a marca de teste confirmado e a escrita fica bloqueada. Edite credenciais apenas no `.env` local; valores secretos são mascarados. `profiles/auditorias.json` e `profiles/sequencias.json` guardam caminhos/bancos, não senhas. A escrita é proibida fora dos bancos confirmados em `profiles/` e `config/ambiente-teste.json`.

Arquivos em `resultados/` e `reports/` podem conter dados de teste e são ignorados pelo Git. Faça backup se precisar levá-los a outra máquina.
