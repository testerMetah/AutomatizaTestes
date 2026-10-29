# Acesso: TFrmExportacaoMarcacoes

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Exportação Marcações CSV/TXT.

- DFM: `Acesso/UFrmExportacaoMarcacoes.dfm`
- PAS: `Acesso/UFrmExportacaoMarcacoes.pas`
- Handler de abertura: `acFerExportacaoMarcacoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmExportacaoMarcacoes | TFrmExportacaoMarcacoes | outro | Exportação de Marcações | — | — | — | Visible=True |
| Label1 | TLabel | rótulo | Período | — | — | — | — |
| Label2 | TLabel | rótulo | a | — | — | — | — |
| Label3 | TLabel | rótulo | Layout de exportação | — | — | — | — |
| Label4 | TLabel | rótulo | Diretório de destino | — | — | — | — |
| Label5 | TLabel | rótulo | Nome do Arquivo | — | — | — | — |
| edtPerDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/0000;1;_ | 10 | Text=01/10/2024 |
| edtPerHoraInicio | TMaskEdit | campo de texto/data | — | 1 | !90:00;1;_ | 5 | Text=00:00 |
| edtPerDataFim | TMaskEdit | campo de texto/data | — | 2 | !99/99/0000;1;_ | 10 | Text=29/11/2024 |
| edtPerHoraFim | TMaskEdit | campo de texto/data | — | 3 | !90:00;1;_ | 5 | Text=23:59 |
| edtDirDestino | TEdit | campo de texto/data | — | 5 | — | — | Text=D:\teste |
| edtNomeArquivo | TEdit | campo de texto/data | — | 6 | — | — | Text=MARCACOES.CSV |
| btnDirDestino | TBitBtn | outro | ... | 7 | — | — | — |
| ckbIncluirLinhaCabecalho | TCheckBox | seleção | Incluir linha de cabeçário no arquivo | 8 | — | — | — |
| edtIncluirLinhaCabecario | TEdit | campo de texto/data | — | 9 | — | — | — |
| cbxEntradas | TCheckBox | seleção | Entradas | 10 | — | — | — |
| cbxSaidas | TCheckBox | seleção | Saídas | 11 | — | — | — |
| cbxIncluirMarc | TCheckBox | seleção | Incluir marcs. bloqueadas | 12 | — | — | — |
| GroupBox1 | TGroupBox | contêiner | Seleção de passantes | 13 | — | — | — |
| Label11 | TLabel | rótulo | Crachás | — | — | — | — |
| Label12 | TLabel | rótulo | a | — | — | — | — |
| Label13 | TLabel | rótulo | Nome | — | — | — | — |
| edtCrachasInicio | TEdit | campo de texto/data | — | 0 | — | — | — |
| edtCrachasFim | TEdit | campo de texto/data | — | 1 | — | — | — |
| edtNome | TEdit | campo de texto/data | — | 2 | — | — | — |
| cbxNome1 | TCheckBox | seleção | — | 3 | — | — | — |
| cbxNome2 | TCheckBox | seleção | — | 4 | — | — | — |
| btnExportar | TBitBtn | outro | Exportar | 14 | — | — | — |
| cbxLayoutExportacao | TDBLookupComboBox | seleção | — | 4 | — | — | — |
| cdsLayout | TClientDataSet | outro | — | — | — | — | — |
| cdsLayoutId | TIntegerField | outro | — | — | — | — | — |
| cdsLayoutDescricao | TStringField | outro | — | — | — | — | — |
| dsLayout | TDataSource | outro | — | — | — | — | — |
| OpenDialog | TOpenDialog | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 367 | `TLayoutExpMarcacoesController.Create`, `FLayoutExpMarcacoesController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 322: `Exporta��o Concluida.`
- Linha 456: `Data de in�cio Inv�lida.`
- Linha 465: `Hora de in�cio Inv�lida.`
- Linha 474: `Data de fim inv�lida.`
- Linha 483: `Hora de fim inv�lida.`
- Linha 491: `Informe o layout.`
- Linha 499: `Diret�rio de destino inv�lido.`
- Linha 508: `Informe o nome arquivo.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
