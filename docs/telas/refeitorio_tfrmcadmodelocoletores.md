# Refeitório > Cadastro > Modelo de Coletores...

> Inventário estático de `Acesso/uFrmCadModeloColetores.dfm` e `Acesso/uFrmCadModeloColetores.pas` no commit `28074dd`. Esta ficha combina inventário estático com notas de leitura manual das procedures; ainda requer conferência de controllers, DAOs e do build instalado.

- Form: `TFrmCadModeloColetores`
- Abertura: `actCadModeloColetoresExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmCadModeloColetores` | `TFrmCadModeloColetores` (herdado) | Cadastro de Modelo de Coletores | — | `—` | — | — | — |
| `Pagina` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Grid` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `GridCadastro` | `TDBGrid` (herdado) | — | — | `—` | — | Visible=True | — |
| `pnlCimaPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `PaginaLoc` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabSheet2` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `ednomeloc` | `TEdit` (herdado) | — | — | `—` | — | — | OnChange=ednomelocChange |
| `btnExibirTudo` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `pnlFundoPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `btnexcluir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | Visible=False, Enabled=False | — |
| `btnInserir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnAlterar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `Cadastro` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Label7` | `TLabel` | Sinal Decimal: | — | `—` | — | Visible=False | — |
| `pnlFundoCadastro` | `TPanel` (herdado) | — | 4 | `—` | — | — | — |
| `btnOk` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnCancelar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `gbxLayoutArquivo` | `TGroupBox` | Layout nos Arquivos  | 3 | `—` | — | Visible=False | — |
| `PnlGridLayout` | `TPanel` | — | 0 | `—` | — | — | — |
| `pcLayoutArquivo` | `TPageControl` | — | 0 | `—` | — | — | OnChange=pcLayoutArquivoChange |
| `tabCabecalho` | `TTabSheet` | Cabeçalho | — | `—` | — | — | — |
| `DbgLayoutCab` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `tabDetalhe` | `TTabSheet` | Detalhes | — | `—` | — | — | — |
| `DbgLayoutDet` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `tabRodape` | `TTabSheet` | Rodapé | — | `—` | — | — | — |
| `DbgLayoutRod` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `PanelGridLayoutBotao` | `TPanel` | — | 1 | `—` | — | — | — |
| `Label3` | `TLabel` | Campo | — | `—` | — | — | — |
| `Label4` | `TLabel` | Tipo | — | `—` | — | — | — |
| `Label5` | `TLabel` | Tamanho | — | `—` | — | — | — |
| `BtnLayoutNovo` | `TSpeedButton` | — | — | `—` | — | — | Action=acLayoutNovo |
| `Label6` | `TLabel` | Formato | — | `—` | — | — | — |
| `BtnLayoutExcluir` | `TSpeedButton` | — | — | `—` | — | — | Action=acLayoutExcluir |
| `EdCampo` | `TEdit` | — | 0 | `—` | — | Text=EDCAMPO | — |
| `CbxTipo` | `TComboBox` | — | 1 | `—` | — | — | — |
| `BtnOkLayout` | `TBitBtn` | OK | 4 | `—` | — | — | Action=acLayoutOK |
| `BtnCancelaLayout` | `TBitBtn` | Cancelar | 5 | `—` | — | — | Action=acLayoutCancelar |
| `EdTamanho` | `TSpinEdit` | — | 2 | `—` | — | — | — |
| `EdFormato` | `TEdit` | — | 3 | `—` | — | Text=EDTIPO | — |
| `PnlGridLayoutLado` | `TPanel` | — | 2 | `—` | — | — | — |
| `pnlSetas` | `TPanel` | — | 0 | `—` | — | — | — |
| `BtnSetaParaCima` | `THoverSpeedButton` | — | 0 | `—` | — | — | Action=acSetaParaCima, OnClick=acSetaParaCimaExecute |
| `BtnSetaParaBaixo` | `THoverSpeedButton` | — | 1 | `—` | — | — | Action=acSetaParaBaixo, OnClick=acSetaParaBaixoExecute |
| `Panel1` | `TPanel` | — | 3 | `—` | — | — | — |
| `cbxSinalDecimal` | `TComboBox` | — | 0 | `—` | — | Visible=False | — |
| `rgFormatoCampos` | `TRadioGroup` | Formato dos Campos | 1 | `—` | — | Visible=False | — |
| `EdCaracterSeparador` | `TEdit` | — | 2 | `—` | — | Text=EdMarca, Visible=False | — |
| `PnlCampos` | `TPanel` | — | 5 | `—` | — | — | — |
| `lblNome` | `TLabel` | Nome: | — | `—` | — | — | — |
| `lblMarca` | `TLabel` | Marca: | — | `—` | — | — | — |
| `mlMarca` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lblNomeMarca` | `TLabel` | lblNomeMarca | — | `—` | — | — | — |
| `EdNome` | `TEdit` | — | 0 | `—` | — | Text=EDNOME | — |
| `EdMarca` | `TEdit` | — | 1 | `—` | — | Text=EdMarca | OnExit=EdMarcaExit |
| `Campos` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel4` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` (herdado) | — | — | `—` | — | — | — |
| `ActExcluir` | `TAction` (herdado) | — | — | `—` | — | Visible=False, Enabled=False | — |
| `ActCancelar` | `TAction` (herdado) | — | — | `—` | — | — | — |
| `acLayoutOK` | `TAction` | OK | — | `—` | — | — | — |
| `acLayoutCancelar` | `TAction` | Cancelar | — | `—` | — | — | — |
| `acLayoutNovo` | `TAction` | — | — | `—` | — | — | — |
| `acLayoutAlterar` | `TAction` | — | — | `—` | — | — | — |
| `acLayoutExcluir` | `TAction` | — | — | `—` | — | — | — |
| `acSetaParaCima` | `TAction` | — | — | `—` | — | — | — |
| `acSetaParaBaixo` | `TAction` | — | — | `—` | — | — | — |
| `ActTSNome` | `TAction` | Nome (Ctrl+B) | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 171: `Tem deseja excluir o item `
- Linha 266: `Excluir o registro?`
- Linha 271: `Problemas com a exclusão no Banco de Dados!`
- Linha 490: `Marca de Coletor inexistente`
- Linha 731: `O Nome do Modelo de coletores é obrigatório.`
- Linha 739: `A Marca do Modelo de coletores é obrigatório.`
- Linha 747: `Para este tipo de Formato de Campo é obrigatório informar o Caracter.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActAlterarExecute`
- `ActCancelarExecute`
- `ActExcluirExecute`
- `ActExibirTudoExecute`
- `ActIncluirExecute`
- `ActIrExecute`
- `ActSalvarExecute`
- `ActTSNomeExecute`
- `ActionList1Update`
- `ValidarCampos`
- `acLayoutCancelarExecute`
- `acLayoutExcluirExecute`

## Fluxo e regras identificados

O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário.

- `ValidarCampos`: Nome vazio mostra `O Nome do Modelo de coletores é obrigatório.`; Marca convertida para inteiro <= 0 mostra `A Marca do Modelo de coletores é obrigatório.`; formato por caractere sem separador mostra `Para este tipo de Formato de Campo é obrigatório informar o Caracter.`. Cada caso aborta o salvamento.
- `GravaCampos`: grava Nome e ID da Marca por `FModeloColetoresController.Inserir/Atualizar`. Após isso chama `GravaCamposLayout`, que insere/atualiza linhas de layout e exclui as marcadas. O retorno de `GravaCamposLayout` não é verificado em `GravaCampos`: dúvida sobre consistência em falha parcial.
- `ActExcluirExecute`: confirma `Excluir o registro?`, chama `FModeloColetoresController.Excluir` e retira a linha do dataset se bem-sucedido. Em falha mostra `Problemas com a exclusão no Banco de Dados!` seguido de CR e `Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`.
- `ActCancelarExecute`: cancela edição do dataset de layout, libera lista de exclusão de layout e chama o Cancelar herdado. Não há relatório nesta unit.
- Fonte: `Acesso/uFrmCadModeloColetores.pas`, procedures `ValidarCampos`, `GravaCampos`, `GravaCamposLayout`, `ActExcluirExecute` e `ActCancelarExecute`. Dúvida: verificar no DAO se exclusão do modelo afeta coletores já associados.

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
