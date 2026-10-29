# Acesso: TFrmImportadorCSV

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Importardor CSV.

- DFM: `Acesso/uFrmImportadorCSV.dfm`
- PAS: `Acesso/uFrmImportadorCSV.pas`
- Handler de abertura: `acFerImportadorCSVExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmImportadorCSV | TFrmImportadorCSV | outro | Importador de Arquivos CSV | — | — | — | Visible=True |
| lblImportar | TLabel | rótulo | Importando 1 de 100 | — | — | — | Visible=False |
| Image1 | TImage | outro | — | — | — | — | Visible=False |
| ProgressBar | TProgressBar | outro | — | 0 | — | — | Visible=False |
| PageControl1 | TPageControl | contêiner | — | 1 | — | — | — |
| TabPessoas | TTabSheet | contêiner | Pessoas | — | — | — | — |
| Label1 | TLabel | rótulo | Informe o arquivo CSV de pessoas | — | — | — | — |
| edtPasta | TEdit | campo de texto/data | — | 0 | — | — | — |
| btnPasta | TButton | ação | ... | 1 | — | — | — |
| btnImportarPessoas | TButton | ação | Importar Pessoas | 2 | — | — | — |
| TabFotos | TTabSheet | contêiner | Fotos | — | — | — | — |
| Label2 | TLabel | rótulo | Informe a pasta das fotos | — | — | — | — |
| edtPastaFotos | TEdit | campo de texto/data | — | 0 | — | — | — |
| btnPastaFotos | TButton | ação | ... | 1 | — | — | — |
| rgCriterioFoto | TRadioGroup | seleção | Nomear imagem por | 2 | — | — | ItemIndex=0 |
| btnImportarFotos | TButton | ação | Importar Fotos | 3 | — | — | — |
| OpenDialog | TOpenDialog | outro | — | — | — | — | — |
| OpenDialogPasta | TFileOpenDialog | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 89 | `TConexaoController.Create`, `FConexaoClienteController.SetConexao` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 149: `Arquivo não encontrado!`
- Linha 163: `Pasta não encontrada!`
- Linha 174: `Selecione o arquivo/pasta primeiro!`
- Linha 197: `Importação concluída com sucesso! %d registro(s) importado(s).`
- Linha 199: `Importação concluída com %d registro(s) importado(s) e %d falha(s). `
- Linha 206: `Erro durante a importação: `
- Linha 224: `Selecione a pasta com as imagens primeiro!`
- Linha 242: `Importação de fotos concluída! %d foto(s) importada(s).`
- Linha 244: `Importação de fotos concluída com %d foto(s) importada(s) e %d falha(s). `
- Linha 251: `Erro durante a importação de fotos: `
- Linha 522: `Arquivo não encontrado: `
- Linha 679: `Pasta não encontrada: `
- Linha 692: `Nenhum arquivo ".jpg", ".jpeg", ".png" ou ".bmp" encontrado na pasta.`
- Linha 841: `Arquivo não localizado: `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
