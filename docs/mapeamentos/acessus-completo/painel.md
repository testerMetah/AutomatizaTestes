# Painel de Módulos

Classe observada: `TFrmModuloViewsPrincipal`.
Título observado: Sistema Acessus | Painel de Módulos - v2.10.0.

Os seis módulos foram abertos pelo menu `Modulos`. Os botões gráficos são `THoverButton` sem título acessível;
seus IDs numéricos mudam entre sessões. Preferir as rotas de menu observadas.

| Módulo | Rota confirmada |
|---|---|
| [Acesso](acesso.md) | Modulos → Acesso |
| [Refeitório](refeitorio.md) | Modulos → Refeitório |
| [Portaria](portaria.md) | Modulos → Portaria |
| [Estacionamento](estacionamento.md) | Modulos → Estacionamento |
| [Escola](escola.md) | Modulos → Escola |
| [Administração](administracao.md) | Modulos → Administração |

Ajuda → Novidades foi aberta, mapeada e fechada. LogOff e Sair não foram acionados.

Os mapas estão em `reports/inspecao-telas/20261015/painel-corrigido.json` e `painel-novidades-1.json`.
A imagem do painel está em `reports/inspecao-telas/20261015/painel.png`.

A barra é `TActionMainMenuBar`, sem HMENU nativo observado. A sessão usou `click_input` em itens UIA;
`select`/Invoke UIA falhou. A árvore UIA repete irmãos como filhos em alguns itens: não inferir submenus recursivamente.
