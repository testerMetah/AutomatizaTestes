\# AGENTS.md: Projeto de testes automatizados do Acessus



> Leia este arquivo inteiro antes de qualquer ação. Ele é a sua instrução permanente neste projeto.

> Os campos entre `\[colchetes]` são lacunas que o Gabriel preenche ou que você DEVE perguntar a ele.



\---



\## 0. Quem sou eu e o que quero de você



Sou o Gabriel, trabalho com automação e teste de software. Estou \*\*aprendendo automação de testes\*\* e

construindo este projeto aos poucos. Então:



\- Explique o que você decidiu e \*\*por quê\*\*, em linguagem direta. Eu quero entender o código, não só receber ele.

\- Prefiro aprender por tópicos: quando introduzir um conceito novo (ex.: page object, polling, fixture),

&#x20; explique em poucas linhas e aplique \*\*no meu projeto real\*\*, não num exemplo genérico.

\- Trabalhe em \*\*fases curtas\*\* e pare no fim de cada uma para eu validar.

\- Se faltar informação, \*\*pergunte\*\*. Nunca invente regra de negócio.

\- Responda sempre em português do Brasil.



\---



\## 1. O que é o sistema sob teste



\*\*Acessus\*\*: aplicação desktop \*\*Delphi/VCL, 32 bits, MDI\*\* (`C:\\acesso\\Acessus.exe`).

Possui muitos módulos e cadastros (ex.: Refeitório > Escola, pessoas, crachás, ocorrências, férias etc.).

Lista completa dos módulos: `\[preencher ou descobrir explorando, veja a seção 5]`.



O Acessus \*\*não é um fluxo único\*\*. Existem vários tipos de cenário:



| Tipo | Descrição |

|---|---|

| \*\*A. Cadastro isolado\*\* | Cadastro feito e verificado só dentro do Acessus (e/ou banco). Não envolve outro software. |

| \*\*B. Fluxo com importação\*\* | Existe um \*\*Software de cadastro\*\* (`\[nome]`) onde se cadastram ocorrências, crachás, pessoas, férias etc.; um \*\*Serviço Windows\*\* (`\[nome do serviço]`) importa esses dados e grava no \*\*SQL Server\*\*; o Acessus então exibe/usa esses dados. |

| \*\*C. Outros\*\* | `\[descrever conforme surgirem]` |



O fluxo B é \*\*apenas um dos cenários\*\*. Não construa o projeto inteiro em volta dele.

O framework deve ser \*\*genérico\*\*; cada cenário é uma camada em cima.



\### Componentes do fluxo B (quando aplicável)

\- \*\*Software de cadastro\*\*: `\[web/desktop, caminho, como abre]`

\- \*\*Serviço\*\*: `\[nome no services.msc]`, controlado por `sc`/psutil/pywin32. Pode ser parado, iniciado e \*\*reiniciado no meio de uma importação\*\*.

\- \*\*SQL Server\*\*: instância `\[host\\instância]`, banco `\[nome]`, autenticação `\[Windows/SQL]`. Tabelas principais: `\[listar]`.



\---



\## 2. Regra de ouro sobre a fonte da verdade



\*\*O repositório do GitHub está desatualizado.\*\* Os desenvolvedores fazem alterações que \*\*não são enviadas ao GitHub\*\*

e que eu preciso testar a cada build novo.



Portanto:



1\. Use o repositório \*\*somente\*\* para entender a estrutura geral e o histórico do projeto de testes.

2\. Nunca conclua que "o sistema funciona assim" só porque o código/teste antigo diz isso.

3\. O comportamento \*\*atual\*\* do Acessus vem de, nesta ordem:

&#x20;  1. O que eu escrevi no briefing da mudança (`docs/mudancas/`)

&#x20;  2. O sistema \*\*rodando\*\* (explorar a interface e observar)

&#x20;  3. O \*\*schema real do banco\*\* (consultar, não presumir)

&#x20;  4. Perguntas diretas a mim

4\. Se um teste antigo falhar num build novo, \*\*não "conserte o teste" automaticamente\*\*. Pode ser um bug real do sistema ou

&#x20;  uma mudança intencional. Me mostre a divergência (esperado vs. obtido) e pergunte qual dos dois é.



\---



\## 3. Stack e ambiente (obrigatório)



\- Windows. Python \*\*32 bits\*\* em venv dedicada: `C:\\python32b\\venv32`. \*\*Ative sempre antes de rodar\*\*.

&#x20; Misturar com Python 64 bits causa erro de arquitetura com o Acessus.

\- \*\*pywinauto\*\* (backend `win32` por padrão; testar `backend="uia"` quando um controle/menu não aparecer no `win32`).

\- \*\*Robot Framework\*\* para os casos de teste; Python para as keywords/bibliotecas.

\- \*\*pyodbc\*\* (ou equivalente 32 bits compatível) para SQL Server.

\- Controle de serviço: `sc`, `psutil` ou `pywin32`.

\- Pasta do projeto de testes: `C:\\AutomatizaTestes\\` (código em `src/automatiza/`, docs em `docs/`). É o projeto REAL; trabalhe sempre nele. O script `teste\_regras\_conflitos\_escola.py` pode estar nesta pasta ou em outro lugar: procure antes de dizer que não existe.

&#x20; \*\*Aproveite o que já existe\*\*. Não reescreva do zero sem me pedir.



\### Particularidades do Delphi/VCL que já descobri

\- A janela principal é `TFrmPrincipal`, com `TActionMainMenuBar`, `TStatusBar` e `MDIClient`.

\- Menus são \*\*renderizados de forma customizada\*\*: o backend `win32` nem sempre enxerga os itens. Investigar `uia`

&#x20; ou navegar por atalhos de teclado/`TActionMainMenuBar`.

\- Existem botões só de ícone (`THoverButton`) sem texto: localizar por `found\_index`, posição ou relação com o container.

\- Há \*\*splash screens\*\* e janelas MDI filhas: sempre esperar a janela correta existir antes de agir.

\- Antes de automatizar uma tela nova, \*\*mapeie a árvore de controles\*\* (`print\_control\_identifiers`) e salve num arquivo em

&#x20; `docs/mapas-de-tela/` para consulta futura.



\---



\## 4. Objetivo: simular o usuário real, com profundidade



Não quero só o "caminho feliz". Quero testar \*\*como um usuário de verdade usaria e abusaria do sistema\*\*:



\- Criar, editar, \*\*deletar e recriar a mesma coisa igual\*\* (mesmo código, mesmo nome, mesmo crachá)

\- Criar \*\*muitos registros\*\* de uma vez (volume)

\- Criar na ordem "errada" (dependente antes do principal), duplicados, campos vazios, limites, caracteres especiais, acentos

\- Repetir a mesma operação várias vezes seguidas

\- No fluxo B: \*\*parar/iniciar/reiniciar o serviço\*\* antes, durante e depois da importação

\- Fechar e reabrir o Acessus no meio de operações

\- Conferir sempre as \*\*consequências\*\*: o que ficou no banco, como aparece na tela, o que aconteceu nos registros relacionados



Existem possivelmente \*\*mais de 1000 combinações\*\*. Você \*\*não vai escrever 1000 testes\*\*. Veja a seção 6.



\---



\## 5. Antes de escrever qualquer código: diagnóstico (Fase 0)



Faça \*\*sem alterar nenhum arquivo\*\* e me entregue um relatório com:



1\. Estrutura atual de `C:\\AutomatizaTestes\\` e o que cada arquivo faz

2\. O que está frágil (esperas fixas, caminhos hardcoded, seletores instáveis, código duplicado)

3\. Que bibliotecas/keywords já existem e podem ser reaproveitadas

4\. Lista de módulos/cadastros do Acessus que você consegue identificar (pelo projeto atual e, se eu autorizar, explorando a UI)

5\. Perguntas que você precisa que eu responda

6\. Proposta de estrutura (seção 7), \*\*sem executar\*\*



Espere minha aprovação antes de seguir.



\---



\## 6. Como lidar com as combinações: dados, não código



Modele cada cenário em \*\*dimensões\*\* e gere os casos por combinação:



| Dimensão | Exemplos de valores |

|---|---|

| Entidade | pessoa, crachá, ocorrência, férias, `\[...]` |

| Operação | criar, editar, deletar, recriar, criar em massa |

| Estado do serviço (fluxo B) | rodando, parado, reiniciado no meio da importação |

| Qualidade do dado | válido, no limite, vazio, duplicado, caracteres especiais |

| Ordem/sequência | A→B, B→A, apagar e recriar igual |



Técnicas a usar:

\- \*\*Testes orientados a dados\*\* com `\[Template]` do Robot Framework: uma linha da tabela = um cenário.

\- \*\*Sequências aleatórias de operações com seed fixa\*\*: se uma falhar, dá para reproduzir exatamente.

\- \*\*Priorização por risco\*\*: me proponha primeiro os cenários de maior risco (borda, deleção/recriação, reinício do serviço, volume).

&#x20; Não gere tudo cegamente.



\---



\## 7. Arquitetura desejada (camadas)



```

AutomatizaTestes/

├─ AGENTS.md

├─ docs/

│   ├─ cenarios/            # regras de negócio por cadastro/fluxo (um .md por cenário)

│   ├─ mudancas/            # briefings de mudança por build (seção 8)

│   └─ mapas-de-tela/       # árvores de controle exportadas do Acessus

├─ libs/

│   ├─ db/                  # consultas, inserts de preparação e limpeza (nenhum SQL solto nos testes)

│   ├─ service/             # start/stop/restart + esperar importação terminar

│   ├─ ui\_acessus/          # page objects do Acessus (pywinauto)

│   ├─ ui\_cadastro/         # page objects do software de cadastro (se houver)

│   └─ data/                # geradores de dados com seed fixa

├─ tests/

│   ├─ smoke/

│   ├─ cadastros/           # cenários tipo A

│   ├─ importacao/          # cenários tipo B

│   └─ regressao/

├─ resultados/              # logs, screenshots, relatórios por execução

└─ config/                  # ambiente (hosts, banco de TESTE, caminhos); nada de senha no código

```



Adapte à estrutura que já existe. Mude o mínimo necessário e me explique cada mudança.



\---



\## 8. Fluxo de trabalho por mudança dos devs (o processo central)



A cada build novo eu vou criar um arquivo `docs/mudancas/AAAA-MM-DD-\[titulo].md` neste modelo:



```markdown

\# Mudança: \[título]

\- Build/versão testada:

\- O que o dev disse que mudou:

\- Telas/cadastros afetados:

\- Regra nova ou alterada (comportamento esperado):

\- O que pode quebrar por tabela (regressão):

\- Tabelas do banco envolvidas:

\- O que eu já vi/testei manualmente:

```



Quando eu pedir para testar uma mudança, você deve:

1\. Ler o briefing \*\*e\*\* `docs/cenarios/` relacionados.

2\. \*\*Antes de codar\*\*, me listar: (a) cenários que testam a mudança diretamente, (b) cenários de regressão relacionados,

&#x20;  (c) perguntas sobre regra de negócio que ficaram abertas.

3\. Esperar minha aprovação.

4\. Implementar/ajustar, rodar, e me entregar o resultado com evidências.



\---



\## 9. Regras de qualidade para todo teste



\*\*Isolamento e limpeza\*\*

\- Cada teste cria \*\*seus próprios dados\*\* com um prefixo único (ex.: `AUTOTEST\_<timestamp>\_`) e \*\*limpa no final\*\*, mesmo se falhar (teardown).

\- Nunca depender de dados que outro teste criou.

\- \*\*Nunca rodar contra banco de produção.\*\* Use somente o banco de teste definido em `config/`. Se não tiver certeza de qual banco está

&#x20; conectado, \*\*pare e pergunte\*\*. Antes de qualquer `DELETE`/`UPDATE` em massa, valide o banco e use o prefixo de teste na cláusula.



\*\*Verificação (duas camadas)\*\*

\- Prefira verificar no \*\*banco\*\* (rápido e exato). Use a \*\*tela\*\* quando a exibição for justamente o que está sendo testado.

\- Todo teste tem um \*\*resultado esperado explícito\*\*, vindo de regra de negócio que eu confirmei. Teste que só "confere o que o sistema já faz" não vale.



\*\*Estabilidade\*\*

\- \*\*Proibido `sleep` fixo.\*\* Use espera por condição (polling com timeout e mensagem de erro clara).

\- Seletores resilientes: prefira nome de classe + auto\_id + hierarquia; use posição/`found\_index` só quando não houver alternativa, comentando o motivo.

\- Trate splash screens, janelas de confirmação e erros inesperados do Delphi (diálogos de exceção) de forma explícita.



\*\*Evidência em toda falha\*\*

Salvar em `resultados/<data-hora>/<teste>/`:

\- SQL executado + resultado esperado vs. obtido

\- Screenshot do Acessus (e do software de cadastro, se aplicável)

\- Log/estado do serviço

\- Versão do build (arquivo/versão do `Acessus.exe`), data/hora e banco usado



\*\*Tags do Robot (para eu escolher o que rodar a cada build)\*\*

`smoke` · `mudanca-atual` · `regressao` · `cadastro-<nome>` · `importacao` · `servico` · `banco` · `lento`



\*\*Reprodutibilidade\*\*

\- Dados aleatórios sempre com \*\*seed registrada\*\* no log.

\- Mensagens de falha devem dizer \*o que\* se esperava, \*o que\* aconteceu e \*onde\* olhar.



\---



\## 10. O que NÃO fazer



\- Não reescrever o projeto inteiro sem aprovação.

\- Não assumir regra de negócio nem "corrigir" teste que falhou sem me consultar.

\- Não confiar no GitHub como retrato do sistema atual.

\- Não rodar nada destrutivo fora do banco/ambiente de teste.

\- Não colocar senhas, strings de conexão ou caminhos pessoais fixos no código.

\- Não criar um teste por combinação; use dados e geração.

\- Não instalar bibliotecas pesadas ou mudar a versão do Python sem avisar (o 32 bits é obrigatório).

\- Não entregar uma montanha de código de uma vez: entregue por fases pequenas.



\---



\## 11. Fases de entrega



| Fase | Entrega | Pare para validar |

|---|---|---|

| 0 | Diagnóstico + proposta de estrutura (seção 5) | Sim |

| 1 | Infra: config de ambiente, conexão com banco de teste, controle do serviço, utilitários de espera/evidência | Sim |

| 2 | Base de UI do Acessus: abrir/fechar/ativar, navegar menus, mapas de tela dos módulos principais | Sim |

| 3 | \*\*Um\*\* cenário completo de ponta a ponta (cadastro isolado simples), com dados, verificação no banco e na tela, limpeza | Sim |

| 4 | Fluxo B: cadastro → importação pelo serviço → banco → Acessus | Sim |

| 5 | Cenários agressivos: deletar/recriar, volume, reinício do serviço, sequências aleatórias com seed | Sim |

| 6 | Tags, smoke/regressão, relatório por execução, briefing de mudança integrado | Sim |



\---



\## 12. Informações que ainda preciso fornecer (pergunte se eu esquecer)



\- \[x] Software de cadastro: RH Metadados/Frequência. Forma exata de abertura e uso ainda pendente.

\- \[x] Três componentes distintos identificados: AcessusSyncImportacao.exe (`FrmSyncImpViewsPrincipal`), AcessusSyncService.exe (`FrmViewsPrincipalService`) e AcessusComService.exe (`SrvAcessusCom`). Os três nomes estão confirmados no SCM em 23/10/2026. Os dois últimos foram instalados com início manual e permanecem parados. Todos usam o banco único `AcessoFagundes` nos INIs; a Importação API já rodava e seu banco efetivo em memória ainda precisa ser validado. Forma de receber dados ainda pendente.

\- \[x] Servidor `desk-tec`; `RHFagundes` é usado pelo RH Metadados/Frequência; `AcessoFagundes` é o banco único do Acessus e de todos os serviços Acessus. Perfil SQL indica autenticação SQL. Ambos foram confirmados pelo usuário como bancos de teste em 22/10/2026. A conexão de leitura `SELECT 1` com `AcessoFagundes` passou. Escrita ainda exige autorização específica para o cenário. Configuração em `config/ambiente-teste.json`.

\- \[ ] Tabelas principais por cadastro (ou permissão para você listar o schema)

\- \[ ] Regras de negócio por cadastro (`docs/cenarios/\*.md`)

\- \[ ] Como recebo as informações do que os devs mudaram (mensagem, ticket, conversa)

\- \[ ] Prioridade: quais cadastros testar primeiro



\---



\## 13. Instrução inicial para qualquer IA assumir o projeto



> Leia o AGENTS.md inteiro. Execute \*\*somente a Fase 0\*\* (seção 5): analise `C:\\AutomatizaTestes\\` e me entregue o relatório.

> \*\*Não altere nenhum arquivo e não rode nada que escreva no banco.\*\* Termine com a lista de perguntas da seção 12 que ainda estão sem resposta

> e espere minha aprovação para a Fase 1.

## Estado operacional mais recente (23/10/2026)

As fases iniciais ja foram autorizadas pelo Gabriel; a secao 13 e historica. Destino atual: `desk-tec/Acessus_AUTOTEST_20261023`, confirmado como teste; Acessus e tres servicos usam esse unico banco. Origem RH: `desk-tec/RHFagundes`. Tres servicos Running. API bloqueada porque `TFConfigAPI` exige coletor. Consulte `docs/HANDOFF.md`, `docs/AMBIENTE.md` e `docs/PERGUNTAS-ABERTAS.md`. Gabriel confirmou exclusao logica no Acessus e nova linha ao recriar igual; detalhes por entidade pendentes.
