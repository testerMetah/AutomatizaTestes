# Inspeção do painel e dos seis módulos

Ampliação posterior nesta data: os utilitários de sincronização, importação e
outros EXE/BPL da instalação também foram lidos. O
[catálogo estático ampliado](estatico-20261015-ampliado/catalogo.json) contém
32 arquivos, 223 estruturas distintas e 16.744 componentes. Ele complementa a
inspeção em execução descrita abaixo, sem adicionar novas rotas validadas.
Veja o [levantamento integrado](../../LEVANTAMENTO-ACESSUS-RH-SQL.md).

Inspeção autorizada em 15/10/2026.

Mapas de navegação e controles para preparar a automação. A abertura de uma tela não valida suas regras de negócio.

| Módulo | Rotas declaradas | Inspecionadas | Diálogos/avisos | Outras situações |
|---|---:|---:|---:|---:|
| [Acesso](acesso.md) | 42 | 41 | 0 | 1 |
| [Refeitório](refeitorio.md) | 21 | 20 | 0 | 1 |
| [Portaria](portaria.md) | 13 | 12 | 0 | 1 |
| [Estacionamento](estacionamento.md) | 20 | 19 | 0 | 1 |
| [Escola](escola.md) | 26 | 26 | 0 | 0 |
| [Administração](administracao.md) | 3 | 2 | 0 | 1 |

Foram inspecionadas 120 rotas, 172 variações de abas e 45 formulários vazios de inclusão, cancelados sem salvar.

## Material salvo

- [Painel de Módulos](painel.md): módulos, abertura e ajuda.
- [Catálogo consolidado](catalogo-telas.json): cobertura, rotas, abas, avisos e pendências.
- [Rotas para o código](rotas-para-codigo.json): classes, títulos e botões únicos nas capturas.
- [Catálogo estático](estatico-20261015-v2/catalogo.json): fontes, hashes e mapas de formulários.
- 157 estruturas distintas e 11272 componentes declarados, incluindo não visuais.
- Árvores de execução e histórico em `reports/inspecao-telas/20261015`.

## Limites e ocorrências

- Inspeção de navegação e controles, sem validar regras de negócio.
- Formulários vazios de inclusão foram cancelados; sem preenchimento ou salvamento.
- Não foram acionados botões de processamento, exclusão, impressão ou envio a equipamentos.
- Menus UIA têm filhos espúrios; hierarquia declarada vem de ActionBars e rotas observadas.
- Leitura de abas por TabControlWrapper causou erro COMCTL32; técnica abandonada.
- Formulários embutidos nos executáveis podem não estar disponíveis no módulo.
- Valores de campos, grades e listas foram omitidos dos mapas em execução.

A opção Administração → Opções do Sistema existe no recurso, mas não aparece no menu em execução. A causa não foi confirmada.
As quatro opções Sair dos módulos e LogOff/Sair do painel foram inventariadas sem acionamento.

As barras TActionMainMenuBar não expuseram HMENU nativo. A navegação desta sessão usou cliques em itens UIA.
Os métodos atuais do projeto que dependem de menu_select precisam considerar essa diferença antes da automação dos cenários.

Arquivos iniciais sem o sufixo `validado` para as janelas principais e o mapa `acesso-pessoas-inicial.json`
foram substituídos por capturas com a hierarquia corrigida. O mapa inicial `painel.json` também foi substituído
por `painel-corrigido.json`; não inferir submenus pela árvore UIA inicial.
