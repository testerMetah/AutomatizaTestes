# Portaria: TFrmPortariaViewsImportacao

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Importação.

- DFM: `Portaria/Views/Acessus.Portaria.Views.Importacao.dfm`
- PAS: `Portaria/Views/Acessus.Portaria.Views.Importacao.pas`
- Handler de abertura: `acConfImportacaoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmPortariaViewsImportacao | TFrmPortariaViewsImportacao | outro | Importação de Terceiros | — | — | — | Visible=True |
| Label1 | TLabel | rótulo | Usuario | — | — | — | — |
| Label2 | TLabel | rótulo | Senha | — | — | — | — |
| Label4 | TLabel | rótulo | Servidor | — | — | — | — |
| Label5 | TLabel | rótulo | Porta | — | — | — | — |
| Label6 | TLabel | rótulo | DataBase | — | — | — | — |
| Label3 | TLabel | rótulo | Seleciona Conexão | — | — | — | — |
| edtUsuario | TEdit | campo de texto/data | — | 4 | — | — | Text=root |
| edtServidor | TEdit | campo de texto/data | — | 1 | — | — | Text=localhost |
| btnImportar | TButton | ação | Importar | 8 | — | — | — |
| edtPorta | TEdit | campo de texto/data | — | 2 | — | — | Text=3306 |
| edtDataBase | TEdit | campo de texto/data | — | 3 | — | — | Text=terceiros |
| cbxConexao | TComboBox | seleção | — | 0 | — | — | Enabled=False |
| edtSenha | TMaskEdit | campo de texto/data | — | 5 | — | — | Text=1234 |
| cbxSincronizar | TCheckBox | seleção | Sincronizar | 7 | — | — | — |
| cbxVisivel | TCheckBox | seleção | — | 6 | — | — | — |
| FDConnection | TFDConnection | outro | — | — | — | — | — |
| FDPhysMySQLDriverLink | TFDPhysMySQLDriverLink | outro | — | — | — | — | — |
| QryEmpresas | TFDQuery | outro | — | — | — | — | — |
| QryFuncionarios | TFDQuery | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 179 | `TEmpresaAcessoController.Create`, `FEmpresaAcessoController.SetConexao`, `TPreCadastroController.Create`, `FPreCadastroController.SetConexao`, `TConexaoController.Create` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 104: ` n�o localizado para realizar conex�o`
- Linha 124: `Importa��o Concluida...`
- Linha 129: `Erro ao conectar com Mysql: `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
