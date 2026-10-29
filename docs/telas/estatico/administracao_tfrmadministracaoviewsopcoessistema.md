# Administracao: TFrmAdministracaoViewsOpcoesSistema

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Opções do Sistema.

- DFM: `Administracao/Views/Acessus.Administracao.Views.OpcoesSistema.dfm`
- PAS: `Administracao/Views/Acessus.Administracao.Views.OpcoesSistema.pas`
- Handler de abertura: `actOpcoesSistemaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAdministracaoViewsOpcoesSistema | TFrmAdministracaoViewsOpcoesSistema | outro | Opções do Sistema | — | — | — | Visible=True |
| pnlFundoCadastro | TPanel | contêiner | — | 0 | — | — | — |
| btnOk | THoverSpeedButton | ação | Salvar (Ctrl+S) | 0 | — | — | — |
| btnCancelar | THoverSpeedButton | ação | Fechar (Ctrl+F4) | 1 | — | — | — |
| pnlOpcoes | TPanel | contêiner | — | 1 | — | — | — |
| PaginaModulos | TPageControl | contêiner | — | 0 | — | — | — |
| tsAdministracao | TTabSheet | contêiner | Administração | — | — | — | — |
| lbQuantidadeCaracteresSenha | TLabel | rótulo | Quantidade mínima de caracteres para senha usuário: | — | — | — | — |
| lbQuantidadeCaracteresEspeciaisSenha | TLabel | rótulo | Quantidade: | — | — | — | — |
| lbQuantidadeLetraMaiusculaSenha | TLabel | rótulo | Quantidade: | — | — | — | — |
| lbQuantidadeLetraMinusculaSenha | TLabel | rótulo | Quantidade: | — | — | — | — |
| lbQuantidadeNumerosSenha | TLabel | rótulo | Quantidade: | — | — | — | — |
| opcQuantidadeCaracteresSenha | TSpinEdit | campo de texto/data | — | 0 | — | — | — |
| opcQuantidadeCaracteresEspeciaisSenha | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| opcExigirCaracteresEspeciaisSenha | TCheckBox | seleção | Exigir caracteres especiais na senha. | 2 | — | — | — |
| opcExigirLetraMaiusculaSenha | TCheckBox | seleção | Exigir letra maiúscula na senha. | 3 | — | — | — |
| opcQuantidadeLetraMaiusculaSenha | TSpinEdit | campo de texto/data | — | 4 | — | — | — |
| opcQuantidadeLetraMinusculaSenha | TSpinEdit | campo de texto/data | — | 5 | — | — | — |
| opcExigirLetraMinusculaSenha | TCheckBox | seleção | Exigir letra minúscula na senha. | 6 | — | — | — |
| opcExigirNumerosSenha | TCheckBox | seleção | Exigir números na senha. | 7 | — | — | — |
| opcQuantidadeNumerosSenha | TSpinEdit | campo de texto/data | — | 8 | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| actSalvar | TAction | ação | Salvar (Ctrl+S) | — | — | — | — |
| actFechar | TAction | ação | Fechar (Ctrl+F4) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 189 | — |
| `SalvarTodasOpcoes` | 367 | — |
| `SalvarOpcao` | 402 | `FController.GravarOpcao` |
| `actSalvarExecute` | 678 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 685: `Configurações de segurança salvas com sucesso! ✅`
- Linha 690: `Erro ao salvar opções: `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
