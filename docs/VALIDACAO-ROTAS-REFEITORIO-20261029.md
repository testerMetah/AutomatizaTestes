# Validação de rotas do Refeitório — 29/10/2026

Build instalado: 2.11.1. As rotas abaixo foram acionadas pelo menu UIA do painel do Refeitório. `print_control_identifiers` exportou a árvore win32 para `docs/mapas-de-tela/`. Cada formulário foi fechado sem clicar em Salvar, Consultar, Importar ou Relatório.

| Form | Resultado da abertura | Mapa |
|---|---|---|
| `TFrmRefeicoes` | Abriu e fechou | `refeitorio_tfrmrefeicoes.yaml` |
| `TFrmRelCreditos` | Abriu e fechou | `refeitorio_tfrmrelcreditos.yaml` |
| `TFrmRelRefeicoesTotal` | Abriu e fechou | `refeitorio_tfrmrelrefeicoestotal.yaml` |
| `TFrmRelReservasRefeicoes` | Abriu e fechou | `refeitorio_tfrmrelreservasrefeicoes.yaml` |
| `TFrmAuditoriaHistoricoRefeitorio` | Item da rota estática não ficou visível/habilitado para UIA; não abriu | bloqueado |
| `TFrmGerarRefeicao` | Item da rota estática não ficou visível/habilitado para UIA; não abriu | bloqueado |

Os quatro YAMLs abertos têm `validado_na_ui: true` **apenas para a rota** e `controles_validados: []`: nenhuma ação em controle interno é permitida até inspecionar sua hierarquia e seletor. A fumaça de abrir/fechar passou para todos em `resultados/robot-telas/20261029-105843/`. Essa rodada `--tag smoke` teve 91 testes encontrados, 8 PASS, 0 FAIL e 83 SKIP; inclui suítes antigas que se autoignoraram. O `Rodar-Telas.bat` foi corrigido depois da rodada para manter `--exclude bloqueado` também ao filtrar por tag.

O mapa de Reservas de Refeições já tinha Incluir e Cancelar validados. A árvore da aba de inclusão mostrou também `Salvar (Ctrl+S)`, associado a `btn_ok`. O cenário `tests/telas/refeitorio_reservas_validacoes.robot` exerceu `ValidarCampos` da unit `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.pas`: ao salvar sem credencial, o build mostrou exatamente `É necessário selecionar uma pessoa.`. PASS em `resultados/robot-telas/20261029-110120/`; a tela foi cancelada sem gravação.

## Dúvidas

1. Auditorias/Históricos do Refeitório e Importar Refeições constam na fonte, mas a rota do menu não funcionou no build instalado. Conferir se o item mudou de legenda, está oculto por perfil ou foi removido.
2. A abertura dos relatórios não confirma filtros, geração, exportação nem conteúdo. Esses comportamentos continuam pendentes.
