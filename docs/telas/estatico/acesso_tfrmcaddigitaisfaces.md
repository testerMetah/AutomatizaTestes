# Acesso: TFrmCadDigitaisFaces

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Cadastros > Digitais e Faces....

- DFM: `Acesso/uFrmCadDigitaisFaces.dfm`
- PAS: `Acesso/uFrmCadDigitaisFaces.pas`
- Handler de abertura: `acCadDigitaisExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmCadDigitaisFaces | TFrmCadDigitaisFaces | outro | Cadastro de Faces e Digitais | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| BtnAlterarTipoPessoa | THoverSpeedButton | ação | Alterar Tipo de Pessoa (Ctrl+Q) | 3 | — | — | Visible=False |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pg_TipoCadastro | TPageControl | contêiner | — | 1 | — | — | — |
| Digitais | TTabSheet | contêiner | Digitais | — | — | — | — |
| pg_Digitais | TPageControl | contêiner | — | 0 | — | — | — |
| TabDimep | TTabSheet | contêiner | Dimep | — | — | — | — |
| ImgMaoDimepDigital | TImage | outro | — | — | — | — | — |
| imgAnelarDirDimep | TImage | outro | — | — | — | — | — |
| imgAnelarEsqDimep | TImage | outro | — | — | — | — | — |
| imgIndicadorDirDimep | TImage | outro | — | — | — | — | — |
| imgIndicadorEsqDimep | TImage | outro | — | — | — | — | — |
| imgMedioDirDimep | TImage | outro | — | — | — | — | — |
| imgMedioEsqDimep | TImage | outro | — | — | — | — | — |
| imgMinimoDirDimep | TImage | outro | — | — | — | — | — |
| imgMinimoEsqDimep | TImage | outro | — | — | — | — | — |
| imgPolegarDirDimep | TImage | outro | — | — | — | — | — |
| imgPolegarEsqDimep | TImage | outro | — | — | — | — | — |
| TabTopData | TTabSheet | contêiner | TopData | — | — | — | — |
| ImgMaoTopDataDigital | TImage | outro | — | — | — | — | — |
| imgMinimoEsqTopData | TImage | outro | — | — | — | — | — |
| imgAnelarEsqTopData | TImage | outro | — | — | — | — | — |
| imgMedioEsqTopData | TImage | outro | — | — | — | — | — |
| imgIndicadorEsqTopData | TImage | outro | — | — | — | — | — |
| imgPolegarEsqTopData | TImage | outro | — | — | — | — | — |
| imgPolegarDirTopData | TImage | outro | — | — | — | — | — |
| imgIndicadorDirTopData | TImage | outro | — | — | — | — | — |
| imgMedioDirTopData | TImage | outro | — | — | — | — | — |
| imgAnelarDirTopData | TImage | outro | — | — | — | — | — |
| imgMinimoDirTopData | TImage | outro | — | — | — | — | — |
| TabControlId | TTabSheet | contêiner | Control ID | — | — | — | — |
| ImgMaoControlIdDigital | TImage | outro | — | — | — | — | — |
| imgMinimoEsqControlID | TImage | outro | — | — | — | — | — |
| imgAnelarEsqControlId | TImage | outro | — | — | — | — | — |
| imgMedioEsqControlId | TImage | outro | — | — | — | — | — |
| imgIndicadorEsqControlId | TImage | outro | — | — | — | — | — |
| imgPolegarEsqControlId | TImage | outro | — | — | — | — | — |
| imgPolegarDirControlId | TImage | outro | — | — | — | — | — |
| imgIndicadorDirControlId | TImage | outro | — | — | — | — | — |
| imgMedioDirControlId | TImage | outro | — | — | — | — | — |
| imgAnelarDirControlId | TImage | outro | — | — | — | — | — |
| imgMinimoDirControlId | TImage | outro | — | — | — | — | — |
| lblDig | TLabel | rótulo | lblDig | — | — | — | — |
| Faces | TTabSheet | contêiner | Faces | — | — | — | — |
| pg_Faces | TPageControl | contêiner | — | 0 | — | — | — |
| FaceDimep | TTabSheet | contêiner | Dimep | — | — | — | — |
| FaceControlId | TTabSheet | contêiner | Control ID | — | — | — | — |
| GBFotoControlId | TGroupBox | contêiner | Fotografia | 0 | — | — | — |
| imgFotoControlId | TImage | outro | — | — | — | — | — |
| pnlBarraBotoes | TPanel | contêiner | — | 0 | — | — | — |
| btnSelectImage | THoverSpeedButton | ação | Selecionar Imagem (Ctrl+F) | 0 | — | — | — |
| btnCamera | THoverSpeedButton | ação | Câmera (Ctrl+C) | 1 | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | Visible=False, Enabled=False |
| btnVerificarDigitaisRepeditasTodos | TButton | ação | TODOS | 2 | — | — | Visible=False, Enabled=False |
| btnVerificarDigitaisRepeditasPorPessoa | TButton | ação | POR PESSOA | 3 | — | — | Visible=False, Enabled=False |
| btnExcluirDig | THoverSpeedButton | ação | Excluir Digitais (Ctrl+Del) | 4 | — | — | — |
| btnCadastrar | THoverSpeedButton | ação | Salvar Face (Ctrl+S) | 5 | — | — | — |
| btnVoltar | THoverSpeedButton | ação | Voltar (Ctrl+D) | 6 | — | — | — |
| Panel5 | TPanel | contêiner | — | 2 | — | — | — |
| Label1 | TLabel | rótulo | Pessoa: | — | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| EdPessoa | TEdit | campo de texto/data | — | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| Panel2 | TPanel | contêiner | Panel2 | 1 | — | — | — |
| Label2 | TLabel | rótulo | Tipo de Pessoa: | — | — | — | — |
| imgDigitalChecked1 | TImage | outro | — | — | — | — | Visible=False |
| imgDigital | TImage | outro | — | — | — | — | Visible=False |
| imgDigitalExcluir | TImage | outro | — | — | — | — | Visible=False |
| imgDigitalChecked | TImage | outro | — | — | — | — | Visible=False |
| cmbTipoPessoa | TComboBox | seleção | — | 0 | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActAlterar | TAction | ação | Detalhes | — | — | — | — |
| ActExcluir | TAction | ação | Excluir Digitais (Ctrl+Del) | — | — | — | — |
| ActSalvar | TAction | ação | — | — | — | — | — |
| ActCancelar | TAction | ação | — | — | — | — | — |
| ActAddDigital | TAction | ação | Salvar Face (Ctrl+S) | — | — | — | — |
| ActAddFace | TAction | ação | Cadastrar Face | — | — | — | — |
| ActSelectImagem | TAction | ação | Selecionar Imagem (Ctrl+F) | — | — | — | — |
| ActFoto | TAction | ação | Câmera (Ctrl+C) | — | — | — | — |
| ActDelImage | TAction | ação | Limpar | — | — | — | — |
| ActVoltar | TAction | ação | Voltar (Ctrl+D) | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActAlterarTipoPessoa | TAction | ação | Alterar Tipo de Pessoa (Ctrl+Q) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| DsDigitaisPessoa | TDataSource | outro | — | — | — | — | — |
| CdsDigitaisPessoa | TClientDataSet | outro | — | — | — | — | — |
| CdsDigitaisPessoaId | TIntegerField | outro | — | — | — | — | — |
| CdsDigitaisPessoaTipoPessoa | TStringField | outro | — | — | — | — | — |
| CdsDigitaisPessoaIdPessoa | TIntegerField | outro | — | — | — | — | — |
| CdsDigitaisPessoaNomePessoa | TStringField | outro | — | — | — | — | — |
| CdsDigitaisPessoaDigDimep | TIntegerField | outro | — | — | — | — | — |
| CdsDigitaisPessoaDigCid | TIntegerField | outro | — | — | — | — | — |
| CdsDigitaisPessoaDigTop | TIntegerField | outro | — | — | — | — | — |
| CdsDigitaisPessoaFaceDimep | TBooleanField | outro | — | — | — | — | — |
| CdsDigitaisPessoaFaceCid | TBooleanField | outro | — | — | — | — | — |
| OpenDialog1 | TOpenDialog | outro | — | — | — | — | — |
| cdsDigitaisControlID | TClientDataSet | outro | — | — | — | — | — |
| cdsDigitaisControlIDid | TIntegerField | outro | — | — | — | — | — |
| cdsDigitaisControlIDdedo | TIntegerField | outro | — | — | — | — | — |
| cdsDigitaisControlIDmao | TStringField | outro | — | — | — | — | — |
| cdsDigitaisControlIDdigital | TWideStringField | outro | — | — | — | — | — |
| cdsDigitaisControlIDidpessoa | TIntegerField | outro | — | — | — | — | — |
| cdsDigitaisControlIDtipopessoa | TIntegerField | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 363 | `FDigitalTopDataController.Excluir`, `FDigitalControlIDController.GetDigitalTodos`, `FFaceControlIdController.GetFacePorPessoa`, `FFaceControlIdController.Excluir` |
| `ActExibirTudoExecute` | 532 | `TDigital_ControlidController.Create`, `DigitaisControlidController.SetConexao`, `TDigitalController.Create`, `DigitaisDimepController.SetConexao`, `TFaceControlIdController.Create`, `FacesController.SetConexao`, `TPessoasController.Create`, `PessoasController.SetConexao` |
| `ActIrExecute` | 681 | `FPessoasController.GetPessoasDigitais`, `FPessoasController.GetPessoasPorNome` |
| `FormCreate` | 2032 | `TDigitaisPessoaController.Create`, `FDigitaisPessoaController.SetConexao`, `TDigitalController.Create`, `FDigitalDimepController.SetConexao`, `TDigital_ControlidController.Create`, `FDigitalControlIDController.SetConexao`, `TDigital_TopDataController.Create`, `FDigitalTopDataController.SetConexao` |
| `GravaCampos` | 2156 | `FFaceControlIdController.GetFacePorPessoa`, `FFaceControlIdController.Excluir`, `FFaceControlIdController.Inserir` |
| `ValidarCampos` | 2727 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 378: `Deseja excluir TODAS as digitais TopData deste usuário?`
- Linha 389: `Não há digitais TopData cadastradas para este usuário.`
- Linha 491: `Deseja excluir a face CONTROL ID?`
- Linha 1579: `Verificação concluída! Relatório salvo em: `
- Linha 1584: `Gostaria de excluir as digitais corrompidas identificadas?`
- Linha 1589: `Digitais corrompidas excluídas com sucesso.`
- Linha 1591: `Erro ao excluir digitais corrompidas.`
- Linha 1603: `Digitais duplicadas excluídas com sucesso.`
- Linha 1605: `Erro ao excluir digitais duplicadas.`
- Linha 1844: `Verificação concluída! Relatório salvo em: `
- Linha 1847: `Gostaria de excluir as digitais corrompidas?`
- Linha 1851: `Digitas corrompidas excluidas.`
- Linha 1853: `Erro ao excluir Digitas corrompidas.`
- Linha 1862: `Digitas duplicadas excluidas.`
- Linha 1864: `Erro ao excluir Digitas duplicadas.`
- Linha 2176: `É necessário inserir uma imagem para salvar uma face`
- Linha 2287: `Foto atualizada com sucesso`
- Linha 2289: `Erro ao atualizar foto[0]`
- Linha 2292: `Erro ao atualizar foto[1]`
- Linha 2330: `Foto cadastrada com sucesso`
- Linha 2332: `Erro ao cadastrar foto`
- Linha 2523: `Deseja excluir esta digital?`
- Linha 2805: `Erro ao capturar digital: `
- Linha 2812: `A digital capturada está corrompida. Tente novamente.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
