# Acesso: TFrmLayoutExportacao

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Layout Exportação Marcações.

- DFM: `Acesso/UFrmLayoutExportacao.dfm`
- PAS: `Acesso/UFrmLayoutExportacao.pas`
- Handler de abertura: `acFerLayoutExportacaoMarcacoesExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmLayoutExportacao | TFrmLayoutExportacao | outro | Layout para exportação de marcações | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | Descrição (Ctrl+B) | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| Label3 | TLabel | rótulo | Empresa | — | — | — | — |
| Label1 | TLabel | rótulo | Descrição | — | — | — | — |
| Label2 | TLabel | rótulo | Separador por campos | — | — | — | — |
| Label4 | TLabel | rótulo | Início do contador | — | — | — | — |
| Label5 | TLabel | rótulo | Nome | — | — | — | — |
| Label6 | TLabel | rótulo | Crachá | — | — | — | — |
| Label7 | TLabel | rótulo | Código da empresa | — | — | — | — |
| Label11 | TLabel | rótulo | Dia | — | — | — | — |
| Label12 | TLabel | rótulo | Mês | — | — | — | — |
| Label13 | TLabel | rótulo | Ano | — | — | — | — |
| Label14 | TLabel | rótulo | Hora | — | — | — | — |
| Label15 | TLabel | rótulo | Minuto | — | — | — | — |
| Label16 | TLabel | rótulo | Código do relógio | — | — | — | — |
| Label17 | TLabel | rótulo | Status | — | — | — | — |
| Label19 | TLabel | rótulo | Função | — | — | — | — |
| Label20 | TLabel | rótulo | Contador | — | — | — | — |
| Label21 | TLabel | rótulo | Campo adicional 1 | — | — | — | — |
| Label22 | TLabel | rótulo | Campo adicional 2 | — | — | — | — |
| Label23 | TLabel | rótulo | Campo adicional 3 | — | — | — | — |
| Label24 | TLabel | rótulo | Campo adicional 4 | — | — | — | — |
| Label25 | TLabel | rótulo | Campo adicional 5 | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 67 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| ckbTodas | TCheckBox | seleção | Todas | 1 | — | — | — |
| edtDescricao | TEdit | campo de texto/data | — | 2 | — | 150 | — |
| rbMovimentoComum | TRadioButton | seleção | Movimento comum | 3 | — | — | — |
| rbMovimentoAFD | TRadioButton | seleção | Movimento de AFD | 4 | — | — | — |
| edtSeparadorCampos | TEdit | campo de texto/data | — | 5 | — | — | Text=; |
| edtInicioContador | TEdit | campo de texto/data | — | 6 | — | — | — |
| ckbLetrasMaiusculo | TCheckBox | seleção | Letras em maiúsculo | 7 | — | — | — |
| Panel2 | TPanel | contêiner | Campo | 8 | — | — | — |
| Panel3 | TPanel | contêiner | Ordem | 9 | — | — | — |
| Panel1 | TPanel | contêiner | Tam | 10 | — | — | — |
| Panel5 | TPanel | contêiner | Zeros | 11 | — | — | — |
| Panel6 | TPanel | contêiner | Campo | 12 | — | — | — |
| Panel7 | TPanel | contêiner | Ordem | 13 | — | — | — |
| Panel8 | TPanel | contêiner | Tam | 14 | — | — | — |
| Panel9 | TPanel | contêiner | Zeros | 15 | — | — | — |
| edtNomeOrdem | TEdit | campo de texto/data | — | 16 | — | — | — |
| edtNomeTam | TEdit | campo de texto/data | — | 17 | — | — | — |
| ckbNomeZeros | TCheckBox | seleção | — | 18 | — | — | — |
| edtCrachaOrdem | TEdit | campo de texto/data | — | 19 | — | — | — |
| edtCrachaTam | TEdit | campo de texto/data | — | 20 | — | — | — |
| ckbCrachaZeros | TCheckBox | seleção | — | 21 | — | — | — |
| edtCodigoEmpresaOrdem | TEdit | campo de texto/data | — | 22 | — | — | — |
| edtCodigoEmpresaTam | TEdit | campo de texto/data | — | 23 | — | — | — |
| ckbCodigoEmpresaZeros | TCheckBox | seleção | — | 24 | — | — | — |
| edtDiaOrdem | TEdit | campo de texto/data | — | 25 | — | — | — |
| edtDiaTam | TEdit | campo de texto/data | — | 26 | — | — | — |
| edtMesOrdem | TEdit | campo de texto/data | — | 27 | — | — | — |
| edtMesTam | TEdit | campo de texto/data | — | 28 | — | — | — |
| edtAnoOrdem | TEdit | campo de texto/data | — | 29 | — | — | — |
| edtAnoTam | TEdit | campo de texto/data | — | 30 | — | — | — |
| edtHoraOrdem | TEdit | campo de texto/data | — | 31 | — | — | — |
| edtHoraTam | TEdit | campo de texto/data | — | 32 | — | — | — |
| edtMinutoOrdem | TEdit | campo de texto/data | — | 33 | — | — | — |
| edtMinutoTam | TEdit | campo de texto/data | — | 34 | — | — | — |
| edtCodigoRelogioOrdem | TEdit | campo de texto/data | — | 35 | — | — | — |
| edtCodigoRelogioTam | TEdit | campo de texto/data | — | 36 | — | — | — |
| ckbCodigoRelogioZeros | TCheckBox | seleção | — | 37 | — | — | — |
| edtStatusOrdem | TEdit | campo de texto/data | — | 38 | — | — | — |
| edtStatusTam | TEdit | campo de texto/data | — | 39 | — | — | — |
| ckbStatusZeros | TCheckBox | seleção | — | 40 | — | — | — |
| edtFuncaoOrdem | TEdit | campo de texto/data | — | 41 | — | — | — |
| edtFuncaoTam | TEdit | campo de texto/data | — | 42 | — | — | — |
| ckbFuncaoZeros | TCheckBox | seleção | — | 43 | — | — | — |
| edtContadorOrdem | TEdit | campo de texto/data | — | 44 | — | — | — |
| edtContadorTam | TEdit | campo de texto/data | — | 45 | — | — | — |
| ckbContadorZeros | TCheckBox | seleção | — | 46 | — | — | — |
| edtCampoAdicional1Ordem | TEdit | campo de texto/data | — | 47 | — | — | — |
| edtCampoAdicional1Tam | TEdit | campo de texto/data | — | 48 | — | — | — |
| ckbCampoAdicional1Zeros | TCheckBox | seleção | — | 49 | — | — | — |
| edtNomeCampoAdicional1 | TEdit | campo de texto/data | — | 50 | — | — | — |
| edtCampoAdicional2Ordem | TEdit | campo de texto/data | — | 51 | — | — | — |
| edtCampoAdicional2Tam | TEdit | campo de texto/data | — | 52 | — | — | — |
| ckbCampoAdicional2Zeros | TCheckBox | seleção | — | 53 | — | — | — |
| edtNomeCampoAdicional2 | TEdit | campo de texto/data | — | 54 | — | — | — |
| edtCampoAdicional3Ordem | TEdit | campo de texto/data | — | 55 | — | — | — |
| edtCampoAdicional3Tam | TEdit | campo de texto/data | — | 56 | — | — | — |
| ckbCampoAdicional3Zeros | TCheckBox | seleção | — | 57 | — | — | — |
| edtNomeCampoAdicional3 | TEdit | campo de texto/data | — | 58 | — | — | — |
| edtCampoAdicional4Ordem | TEdit | campo de texto/data | — | 59 | — | — | — |
| edtCampoAdicional4Tam | TEdit | campo de texto/data | — | 60 | — | — | — |
| ckbCampoAdicional4Zeros | TCheckBox | seleção | — | 61 | — | — | — |
| edtNomeCampoAdicional4 | TEdit | campo de texto/data | — | 62 | — | — | — |
| edtCampoAdicional5Ordem | TEdit | campo de texto/data | — | 63 | — | — | — |
| edtCampoAdicional5Tam | TEdit | campo de texto/data | — | 64 | — | — | — |
| ckbCampoAdicional5Zeros | TCheckBox | seleção | — | 65 | — | — | — |
| edtNomeCampoAdicional5 | TEdit | campo de texto/data | — | 66 | — | — | — |
| DBLCBXEmpresa | TDBLookupComboBox | seleção | — | 0 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActTSDescricao | TAction | ação | Descrição (Ctrl+B) | — | — | — | — |
| DsLayout | TDataSource | outro | — | — | — | — | — |
| CdsLayout | TClientDataSet | outro | — | — | — | — | — |
| CdsLayoutId | TIntegerField | outro | — | — | — | — | — |
| CdsLayoutDescricao | TStringField | outro | — | — | — | — | — |
| CdsEmpresas | TClientDataSet | outro | — | — | — | — | — |
| CdsEmpresasId | TIntegerField | outro | — | — | — | — | — |
| CdsEmpresasNome | TStringField | outro | — | — | — | — | — |
| DSEmpresas | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ActExcluirExecute` | 168 | `FLayoutExpMarcacoesController.Excluir` |
| `ActExibirTudoExecute` | 184 | `FLayoutExpMarcacoesController.GetTodos` |
| `ActIrExecute` | 202 | `FLayoutExpMarcacoesController.GetPorDescricao` |
| `FormCreate` | 359 | `TLayoutExpMarcacoesController.Create`, `FLayoutExpMarcacoesController.SetConexao`, `TEmpresasController.Create`, `FEmpresasController.SetConexao` |
| `GravaCampos` | 380 | `FLayoutExpMarcacoesController.Inserir`, `FLayoutExpMarcacoesController.Atualizar` |
| `ValidarCampos` | 585 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 172: `Excluir o registro?`
- Linha 177: `Problemas com a exclus�o no Banco de Dados!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
