## Navegação customizada de Trabalho

`TFrmTrabalhoViewsPrincipal` não usa a árvore `TActionManager` dos demais módulos; oito `TSpeedButton` na lateral chamam procedures diretamente em `Trabalho/Views/Acessus.Trabalho.Views.Principal.pas`:

| Botão/ação | Destino | Unit `.pas/.dfm` |
|---|---|---|
| Painel de Controle / `actPainelDeControleExecute` | Aba `TabPainel` no próprio form | `Trabalho/Views/Acessus.Trabalho.Views.Principal` |
| Cadastro / `actCadastroExecute` | Aba `TabCadastro`; seleciona `TabGridTiposDeEPIs` | mesma unit |
| Controle de EPIs / `actControleDeEPIsExecute` | Aba `TabControleDeEPIs` | mesma unit |
| Acesso / `actAcessoExecute` | Form `TFGerarAcesso`, esconde `PgRight` | `Acesso/UGerarAcesso.pas/.dfm` |
| Segurança e Saúde / `actSegurancaESaudeExecute` | Aba `TabSegurancaESaude` | mesma unit |
| Documentos Fiscais / `actDocumentosFiscaisExecute` | Aba `TabDocumentosFiscais` | mesma unit |
| Contratos Sociais / `actContratosSociaisExecute` | Aba `TabContratosSociais` | mesma unit |
| Sobre / `actSobreExecute` | Aba `TabSobre` | mesma unit |

O DFM declara grades e botões de cadastro de EPIs dentro do próprio form. Nesta cópia, os botões internos não têm `OnClick` ou `Action` no DFM; a implementação funcional deve ser conferida no build instalado. `FormCreate` esconde as abas para navegação pela lateral.
