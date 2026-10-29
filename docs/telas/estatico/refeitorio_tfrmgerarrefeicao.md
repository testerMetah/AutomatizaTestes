# Refeitorio: TFrmGerarRefeicao

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Refeitório > Importar Refeições.

- DFM: `Refeitorio/Views/Acessus.Refeitorio.Views.UFrmImportarRefeicao.dfm`
- PAS: `Refeitorio/Views/Acessus.Refeitorio.Views.UFrmImportarRefeicao.pas`
- Handler de abertura: `acRefImportarRefeicoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmGerarRefeicao | TFrmGerarRefeicao | outro | Importar Refeições | — | — | — | — |
| PnlPrincipal | TPanel | contêiner | — | 0 | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | 0 | — | — | — |
| btnImportarRefeicoes | THoverSpeedButton | ação | Importar Refeições (Ctrl+I) | 0 | — | — | — |
| CPImp | TCardPanel | contêiner | Tipo Importação | 1 | — | — | — |
| impAtual | TCard | outro | Importação atual | 0 | — | — | — |
| PnlMain | TPanel | contêiner | — | 0 | — | — | — |
| ImgDesc | TImage | outro | — | — | — | — | — |
| ImgTmp | TImage | outro | — | — | — | — | — |
| LblTmp | TLabel | rótulo | Intervalo Das Marcações: | — | — | — | — |
| ChkDesc | TCheckBox | seleção | Desconsiderar Marcações Duplicadas | 0 | — | — | — |
| MskTmp | TMaskEdit | campo de texto/data | — | 1 | !90:00;1;_ | 5 | Text=00:00, Enabled=False |
| impF | TCard | outro | Implementação futura | 1 | — | — | — |
| CpSelecao | TCardPanel | contêiner | — | 0 | — | — | — |
| CdPessoas | TCard | outro | Pessoas | 0 | — | — | — |
| ImgPessoas | TImage | outro | — | — | — | — | — |
| LblPessoas | TLabel | rótulo | Lista de Pessoas: | — | — | — | — |
| MlPessoas | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstPessoas | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverPessoa | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverPessoa | TShape | outro | — | — | — | — | — |
| BtnRemoverPessoa | TSpeedButton | ação | — | — | — | — | — |
| CdPreCadastros | TCard | outro | Pré-Cadastros | 1 | — | — | — |
| ImgPreCadastros | TImage | outro | — | — | — | — | — |
| LblPreCadastros | TLabel | rótulo | Lista de Pré-Cadastros: | — | — | — | — |
| MlPreCadastros | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstPreCadastros | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverPreCadastro | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverPreCadastro | TShape | outro | — | — | — | — | — |
| BtnRemoverPreCadastro | TSpeedButton | ação | — | — | — | — | — |
| CdSetores | TCard | outro | Setores | 2 | — | — | — |
| ImgSetores | TImage | outro | — | — | — | — | — |
| LblSetores | TLabel | rótulo | Lista de Setores: | — | — | — | — |
| MlSetores | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstSetores | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverSetor | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverSetor | TShape | outro | — | — | — | — | — |
| BtnRemoverSetor | TSpeedButton | ação | — | — | — | — | — |
| CdEmpresaAcesso | TCard | outro | Empresa De Acesso | 3 | — | — | — |
| ImgEmpresaAcesso | TImage | outro | — | — | — | — | — |
| LblEmpresaAcesso | TLabel | rótulo | Lista de Empresas de Acesso: | — | — | — | — |
| MlEmpresaAcesso | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstEmpresaAcesso | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverEmpresaAcesso | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverEmpresaAcesso | TShape | outro | — | — | — | — | — |
| BtnRemoverEmpresaAcesso | TSpeedButton | ação | — | — | — | — | — |
| CdFiltros | TCard | outro | Filtros | 4 | — | — | — |
| ImgFiltros | TImage | outro | — | — | — | — | — |
| LblFiltros | TLabel | rótulo | Lista De Filtros: | — | — | — | — |
| MlFiltros | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstFiltros | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverFiltro | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverFiltro | TShape | outro | — | — | — | — | — |
| BtnRemoverFiltro | TSpeedButton | ação | — | — | — | — | — |
| PnlDesconsiderarDuplicadas | TPanel | contêiner | — | 1 | — | — | — |
| LblDesconsiderarDup | TLabel | rótulo | Desconsiderar Marcações Duplicadas | — | — | — | — |
| ImgDesconsiderarDuplicadas | TImage | outro | — | — | — | — | — |
| ChkDesconsiderarDuplicadas | TCheckBox | seleção | — | 0 | — | — | — |
| pnlIntervaloMarc | TPanel | contêiner | — | 2 | — | — | — |
| ImgIntervalo | TImage | outro | — | — | — | — | — |
| LblIntervaloMarcacoes | TLabel | rótulo | Intervalo Das Marcações: | — | — | — | — |
| MskIntervalo | TMaskEdit | campo de texto/data | — | 0 | !90:00;1;_ | 5 | Text=00:00, Enabled=False |
| PnlPeriodo | TPanel | contêiner | — | 3 | — | — | — |
| LblPeriodo | TLabel | rótulo | Período De Importação: | — | — | — | — |
| ImgPeriodo | TImage | outro | — | — | — | — | — |
| LblAte | TLabel | rótulo | Até | — | — | — | — |
| MskHoraIni | TMaskEdit | campo de texto/data | — | 0 | !90:00;1;_ | 5 | Text=  :   |
| MskHoraFim | TMaskEdit | campo de texto/data | — | 1 | !90:00;1;_ | 5 | Text=  :   |
| MskDiaIni | TMaskEdit | campo de texto/data | — | 2 | !99/99/0000;1;_ | 10 | Text=  /  /     |
| MskDiaFim | TMaskEdit | campo de texto/data | — | 3 | !99/99/0000;1;_ | 10 | Text=  /  /     |
| PnlSelecao | TPanel | contêiner | — | 4 | — | — | — |
| ImgSelecao | TImage | outro | — | — | — | — | — |
| LblSelecao | TLabel | rótulo | Seleção: | — | — | — | — |
| CmbSelecao | TComboBox | seleção | — | 0 | — | — | Text=Geral, ItemIndex=0 |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList | TActionList | outro | — | — | — | — | — |
| ActImportarRefeicao | TAction | ação | Importar Refeições (Ctrl+I) | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 190 | — |
| `ValidarCampos` | 262 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 142: `Importação de Refeições Concluída`
- Linha 279: `"`
- Linha 290: `"`
- Linha 297: `"`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
