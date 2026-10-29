# Acesso: TFRegrasAcesso

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Regras de Acesso....

- DFM: `Acesso/UFrmRegrasAcesso.dfm`
- PAS: `Acesso/UFrmRegrasAcesso.pas`
- Handler de abertura: `acAceRegrasAcessoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FRegrasAcesso | TFRegrasAcesso | outro | Regras de Acesso | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=False |
| pnlCimaPadrao | TPanel | contêiner | — | — | — | — | — |
| PaginaLoc | TPageControl | contêiner | — | — | — | — | — |
| TabSheet2 | TTabSheet | contêiner | — | — | — | — | — |
| ednomeloc | TEdit | campo de texto/data | — | — | — | — | — |
| btnExibirTudo | THoverSpeedButton | ação | — | — | — | — | — |
| pnlFundoPadrao | TPanel | contêiner | — | — | — | — | — |
| btnexcluir | THoverSpeedButton | ação | — | — | — | — | — |
| btnInserir | THoverSpeedButton | ação | — | — | — | — | — |
| btnAlterar | THoverSpeedButton | ação | — | — | — | — | — |
| Cadastro | TTabSheet | contêiner | — | — | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | — | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| PgCadastro2 | TPageControl | contêiner | — | 1 | — | — | — |
| TabHorario | TTabSheet | contêiner | Horário | — | — | — | — |
| bgkDays | TPanel | contêiner | — | 1 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| lblDataHoraFim | TLabel | rótulo | até | — | — | — | — |
| lblDataHoraIni | TLabel | rótulo | Período: | — | — | — | — |
| lblNome | TLabel | rótulo | Nome: | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Image18 | TImage | outro | — | — | — | — | — |
| DtEncerramento | TMaskEdit | campo de texto/data | — | 3 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| dtInicio | TMaskEdit | campo de texto/data | — | 1 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| EdNome | TEdit | campo de texto/data | — | 0 | — | — | Text=EdNome |
| gbxDiasSemana | TPanel | contêiner | — | 5 | — | — | — |
| pnlDom | TPanel | contêiner | Acesso | 0 | — | — | — |
| shpDom | TShape | outro | — | — | — | — | — |
| btnDom | TSpeedButton | ação | — | — | — | — | — |
| pnlQua | TPanel | contêiner | Acesso | 3 | — | — | — |
| shpQua | TShape | outro | — | — | — | — | — |
| btnQua | TSpeedButton | ação | — | — | — | — | — |
| pnlQui | TPanel | contêiner | Acesso | 4 | — | — | — |
| shpQui | TShape | outro | — | — | — | — | — |
| btnQui | TSpeedButton | ação | — | — | — | — | — |
| pnlSab | TPanel | contêiner | — | 5 | — | — | — |
| shpSab | TShape | outro | — | — | — | — | — |
| btnSab | TSpeedButton | ação | — | — | — | — | — |
| pnlSeg | TPanel | contêiner | — | 1 | — | — | — |
| shpSeg | TShape | outro | — | — | — | — | — |
| btnSeg | TSpeedButton | ação | — | — | — | — | — |
| pnlSex | TPanel | contêiner | — | 6 | — | — | — |
| shpSex | TShape | outro | — | — | — | — | — |
| btnSex | TSpeedButton | ação | — | — | — | — | — |
| pnlTer | TPanel | contêiner | Acesso | 2 | — | — | — |
| shpTer | TShape | outro | — | — | — | — | — |
| btnTer | TSpeedButton | ação | — | — | — | — | — |
| tmInicio | TMaskEdit | campo de texto/data | — | 2 | !99:99;1;_ | 5 | Text=  :   |
| tmTermino | TMaskEdit | campo de texto/data | — | 4 | !99:99;1;_ | 5 | Text=  :   |
| ChkSepararRegraDIa | TCheckBox | seleção | Repetir diariamente | 6 | — | — | — |
| ChkHoraInicioMaiorTermino | TCheckBox | seleção | Horário Noturno | 7 | — | — | — |
| ChkPersonalizar | TCheckBox | seleção | Personalizar | 8 | — | — | Enabled=False |
| DayView1 | TPanel | contêiner | — | 0 | — | — | Visible=False |
| Image8 | TImage | outro | — | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| pnlPeriodo | TPanel | contêiner | — | 0 | — | — | — |
| shpBackground | TShape | outro | — | — | — | — | — |
| shpPeriodo | TShape | outro | — | — | — | — | — |
| pnlUnderTime | TPanel | contêiner | — | 1 | — | — | — |
| Shape3 | TShape | outro | — | — | — | — | — |
| Label2 | TLabel | rótulo | 0h | — | — | — | — |
| Label3 | TLabel | rótulo | 12h | — | — | — | — |
| Label4 | TLabel | rótulo | 23h | — | — | — | — |
| Label5 | TLabel | rótulo | 6h | — | — | — | — |
| Label8 | TLabel | rótulo | 18h | — | — | — | — |
| Shape4 | TShape | outro | — | — | — | — | — |
| Shape5 | TShape | outro | — | — | — | — | — |
| Shape6 | TShape | outro | — | — | — | — | — |
| TabAcesso | TTabSheet | contêiner | Acesso | — | — | — | — |
| PgcTipoSelecoes | TPageControl | contêiner | — | 6 | — | — | — |
| TabFiltros | TTabSheet | contêiner | TabFiltros | — | — | — | — |
| pnlFiltrosPrincipal | TPanel | contêiner | — | 0 | — | — | — |
| Label9 | TLabel | rótulo | Filtro: | — | — | — | — |
| mlFiltro | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblNomeFiltro | TLabel | rótulo | lblNomeFiltro | — | — | — | — |
| Image13 | TImage | outro | — | — | — | — | — |
| EdFiltro | TEdit | campo de texto/data | — | 0 | — | — | Text=EdFiltro |
| TabPessoas | TTabSheet | contêiner | TabPessoas | — | — | — | — |
| Image14 | TImage | outro | — | — | — | — | — |
| lblPessoas | TLabel | rótulo | Lista de pessoas: | — | — | — | — |
| mlPessoas | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstPessoas | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverPessoa | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverPessoa | TShape | outro | — | — | — | — | — |
| BtnRemoverPessoa | TSpeedButton | ação | — | — | — | — | — |
| TabSetores | TTabSheet | contêiner | TabSetores | — | — | — | — |
| Image15 | TImage | outro | — | — | — | — | — |
| Label7 | TLabel | rótulo | Lista de setores: | — | — | — | — |
| mlSetor | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstSetores | TListBox | seleção | — | 0 | — | — | — |
| PnlExcluirSetor | TPanel | contêiner | — | 1 | — | — | — |
| ShpExcluirSetor | TShape | outro | — | — | — | — | — |
| BtnExcuirSetor | TSpeedButton | ação | — | — | — | — | — |
| TabVeiculos | TTabSheet | contêiner | TabVeiculos | — | — | — | — |
| Image17 | TImage | outro | — | — | — | — | — |
| Label11 | TLabel | rótulo | Lista de Veiculos: | — | — | — | — |
| mlVeiculo | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstVeiculos | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverVeiculo | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverVeiculo | TShape | outro | — | — | — | — | — |
| BtnRemoverVeiculo | TSpeedButton | ação | — | — | — | — | — |
| TabPreCadastros | TTabSheet | contêiner | TabPreCadastros | — | — | — | — |
| Image19 | TImage | outro | — | — | — | — | — |
| lblPreCadastros | TLabel | rótulo | Lista de pré-cadastros: | — | — | — | — |
| mlPreCadastros | TMetaEquipLocalizar | outro | — | — | — | — | — |
| LstPreCadastros | TListBox | seleção | — | 0 | — | — | — |
| PnlRemoverPreCadastro | TPanel | contêiner | — | 1 | — | — | — |
| ShpRemoverPreCadastro | TShape | outro | — | — | — | — | — |
| BtnRemoverPreCadastro | TSpeedButton | ação | — | — | — | — | — |
| TabEscola | TTabSheet | contêiner | TabEscola | — | — | — | — |
| imgEscola | TImage | outro | — | — | — | — | — |
| lblEscola | TLabel | rótulo | Lista de alunos: | — | — | — | — |
| mlEscola | TMetaEquipLocalizar | outro | — | — | — | — | — |
| imgAlunos | TImage | outro | — | — | — | — | Visible=False |
| imgTurmas | TImage | outro | — | — | — | — | Visible=False |
| imgTurnos | TImage | outro | — | — | — | — | Visible=False |
| LstEscola | TListBox | seleção | — | 0 | — | — | — |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| Shape1 | TShape | outro | — | — | — | — | — |
| btnRemoverEscola | TSpeedButton | ação | — | — | — | — | — |
| pnlSituacao | TPanel | contêiner | — | 0 | — | — | — |
| Image16 | TImage | outro | — | — | — | — | — |
| Label10 | TLabel | rótulo | Situação: | — | — | — | — |
| cmbStatus | TComboBox | seleção | — | 0 | — | — | Text=Ativo, ItemIndex=0 |
| pnlTipoRegra | TPanel | contêiner | — | 1 | — | — | Visible=False, Enabled=False |
| Image12 | TImage | outro | — | — | — | — | — |
| lblTipoRegra | TLabel | rótulo | Tipo da regra: | — | — | — | — |
| CbxLiberaBloqueia | TComboBox | seleção | — | 0 | — | — | Text=LIBERAR, ItemIndex=1 |
| pnlSentidoAcesso | TPanel | contêiner | — | 2 | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| lblSentido | TLabel | rótulo | Sentido do Acesso: | — | — | — | — |
| CmbTipoAcesso | TComboBox | seleção | — | 0 | — | — | Text=ENTRADA, ItemIndex=0 |
| pnlQuantidadeAcesso | TPanel | contêiner | — | 3 | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| lblQtdAcesso | TLabel | rótulo | Quantidade de Acesso: | — | — | — | — |
| EdQtdeAcesso | TSpinEdit | campo de texto/data | — | 0 | — | — | — |
| pnlIncluirPreCadastros | TPanel | contêiner | — | 4 | — | — | — |
| Image2 | TImage | outro | — | — | — | — | — |
| ChkPreCadastro | TCheckBox | seleção | Incluir pré-cadastros | 0 | — | — | Checked=True |
| pnlFiltrarPor | TPanel | contêiner | — | 5 | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Filtrar por: | — | — | — | — |
| CmbTipoSelecao | TComboBox | seleção | — | 0 | — | — | — |
| TabColetores | TTabSheet | contêiner | Coletores | — | — | — | — |
| ChkColetores | TCheckListBox | seleção | — | 0 | — | — | — |
| pnlColetores | TPanel | contêiner | — | 1 | — | — | — |
| lblColetores | TLabel | rótulo | Selecionar coletores: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| ActExcluir | TAction | ação | — | — | — | — | Visible=False, Enabled=False |
| ActCancelar | TAction | ação | — | — | — | — | — |
| ActDom | TAction | ação | Dom | — | — | — | — |
| ActSeg | TAction | ação | Seg | — | — | — | — |
| ActTer | TAction | ação | Ter | — | — | — | — |
| ActQua | TAction | ação | Qua | — | — | — | — |
| ActQui | TAction | ação | Qui | — | — | — | — |
| ActSex | TAction | ação | Sex | — | — | — | — |
| ActSab | TAction | ação | Sáb | — | — | — | — |
| ActTSNome | TAction | ação | Nome (Ctrl+B) | — | — | — | — |
| ActGerarAcesso | TAction | ação | Gerar Acesso (Repetir Diariamente) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| CdsRegrasAcesso | TClientDataSet | outro | — | — | — | — | — |
| CdsRegrasAcessoId | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessoNome | TStringField | outro | — | — | — | — | — |
| CdsRegrasAcessodatahorainicio | TDateTimeField | outro | — | — | — | — | — |
| CdsRegrasAcessodatahoratermino | TDateTimeField | outro | — | — | — | — | — |
| CdsRegrasAcessotiporegra | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessotiposelecao | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessoSepararPorDia | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessobloquearsabados | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessobloqueardomingos | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessoqtdeacesso | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessotipoacesso | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessoDiasSemana | TStringField | outro | — | — | — | — | — |
| CdsRegrasAcessosituacao | TIntegerField | outro | — | — | — | — | — |
| CdsRegrasAcessosituacaoNome | TStringField | outro | — | — | — | — | — |
| CdsRegrasAcessopersonalizar | TStringField | outro | — | — | — | — | — |
| DsRegrasAcesso | TDataSource | outro | — | — | — | — | — |
| PopupMenu1 | TPopupMenu | outro | — | — | — | — | — |
| GerarAcessoRepetirDiariamente1 | TMenuItem | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 271 | `TRegrasAcessoController.Create`, `FRegrasAcessoController.SetConexao` |
| `ActSalvarExecute` | 508 | — |
| `ActExcluirExecute` | 676 | `FRegrasAcessoController.Excluir` |
| `ActExibirTudoExecute` | 705 | `FRegrasAcessoController.GetRegraAcessoEscola`, `FRegrasAcessoController.GetRegraAcessoTodas` |
| `ActIncluirExecute` | 739 | — |
| `ActIrExecute` | 791 | — |
| `BtnExcluirSetorClick` | 811 | — |
| `GravaCampos` | 1616 | `FRegrasAcessoController.Inserir`, `FRegrasAcessoController.GetRegraAcessoPorId`, `FRegrasAcessoController.Atualizar` |
| `ValidarCampos` | 1876 | — |
| `BtnExcluirVeiculoClick` | 2296 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 549: `Preencha uma data inicial!`
- Linha 556: `Data inicial Inválida!`
- Linha 565: `Preencha uma data final!`
- Linha 572: `Data final Inválida!`
- Linha 582: `Preencha uma hora inicial!`
- Linha 589: `Hora inicial Inválida!`
- Linha 597: `Preencha uma hora final!`
- Linha 604: `Hora final Inválida!`
- Linha 617: `O horário final deve ser maior que o horário inicial!`
- Linha 632: `A data final não pode ser menor que a data inicial!`
- Linha 642: `A data final não pode ser maior que `
- Linha 662: `Deseja gerar acesso?`
- Linha 680: `Excluir o registro?`
- Linha 685: `Problemas com a exclusão no Banco de Dados!`
- Linha 688: `Deseja gerar acesso?`
- Linha 1543: `Filtro não cadastrado`
- Linha 1557: `Filtro não cadastrado`
- Linha 1853: `Hora Inválida!`
- Linha 1868: `Hora Inválida!`
- Linha 1884: `O nome da regra deve ser informado.`
- Linha 1895: `Data de Início deve ser informada.`
- Linha 1902: `Data inicial Inválida!`
- Linha 1910: `Data de Término deve ser informada.`
- Linha 1917: `Data final Inválida!`
- Linha 1929: `Data de Início deve ser informada quando "Personalizar" está marcado.`
- Linha 1936: `Data inicial Inválida!`
- Linha 1944: `Data de Término deve ser informada quando "Personalizar" está marcado.`
- Linha 1951: `Data final Inválida!`
- Linha 1961: `A hora de Início deve ser informada.`
- Linha 1968: `Hora inicial Inválida!`
- Linha 1976: `A hora de Término deve ser informada.`
- Linha 1983: `Hora final Inválida!`
- Linha 2002: `Ao menos 1 coletor deve ser selecionado.`
- Linha 2014: `Selecione algum aluno na lista.`
- Linha 2015: `Selecione alguma turma na lista.`
- Linha 2016: `Selecione algum turno na lista.`
- Linha 2027: `O Filtro deve ser informado.`
- Linha 2035: `Selecione alguma pessoa na lista.`
- Linha 2043: `Selecione algum setor na lista.`
- Linha 2051: `Selecione algum veículo na lista.`
- Linha 2068: `A data/hora de término não pode ser menor que a data/hora de início.`
- Linha 2076: `Erro ao processar datas: `
- Linha 2093: `A data/hora de término não pode ser menor que a data/hora de início.`
- Linha 2101: `Erro ao processar datas personalizadas: `
- Linha 2114: `Na modalidade de regra de acesso particionada por dia, a hora de início não pode ser igual a hora de término.`
- Linha 2122: `Para horários que atravessam a meia noite, marque a opção "Horário Noturno".`
- Linha 2137: `A data de término não pode ser menor que a data de início.`
- Linha 2146: `O período não pode ser superior a 1 ano.`
- Linha 2154: `Erro ao processar datas padrão: `
- Linha 2167: `A data de término não pode ser menor que a data de início.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
