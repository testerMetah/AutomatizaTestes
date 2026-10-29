# Refeitório > Acesso > Regras de Acesso...

> Inventário estático de `Acesso/UFrmRegrasAcesso.dfm` e `Acesso/UFrmRegrasAcesso.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFRegrasAcesso`
- Abertura: `ActRegrasAcessoExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FRegrasAcesso` | `TFRegrasAcesso` (herdado) | Regras de Acesso | — | `—` | — | — | — |
| `Pagina` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `Grid` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `GridCadastro` | `TDBGrid` (herdado) | — | — | `—` | — | Visible=False | — |
| `pnlCimaPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `PaginaLoc` | `TPageControl` (herdado) | — | — | `—` | — | — | — |
| `TabSheet2` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `ednomeloc` | `TEdit` (herdado) | — | — | `—` | — | — | OnChange=ednomelocChange |
| `btnExibirTudo` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `pnlFundoPadrao` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `btnexcluir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnInserir` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnAlterar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `Cadastro` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `pnlFundoCadastro` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `btnOk` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `btnCancelar` | `THoverSpeedButton` (herdado) | — | — | `—` | — | — | — |
| `PgCadastro2` | `TPageControl` | — | 1 | `—` | — | — | — |
| `TabHorario` | `TTabSheet` | Horário | — | `—` | — | — | — |
| `bgkDays` | `TPanel` | — | 1 | `—` | — | — | — |
| `lblDataHoraFim` | `TLabel` | até | — | `—` | — | — | — |
| `lblDataHoraIni` | `TLabel` | Período: | — | `—` | — | — | — |
| `lblNome` | `TLabel` | Nome: | — | `—` | — | — | — |
| `DtEncerramento` | `TMaskEdit` | — | 3 | `!99/99/9999;1;_` | 10 | Text=  /  /     | — |
| `dtInicio` | `TMaskEdit` | — | 1 | `!99/99/9999;1;_` | 10 | Text=  /  /     | — |
| `EdNome` | `TEdit` | — | 0 | `—` | — | Text=EdNome | — |
| `gbxDiasSemana` | `TPanel` | — | 5 | `—` | — | — | — |
| `pnlDom` | `TPanel` | Acesso | 0 | `—` | — | — | — |
| `btnDom` | `TSpeedButton` | — | — | `—` | — | — | Action=ActDom |
| `pnlQua` | `TPanel` | Acesso | 3 | `—` | — | — | — |
| `btnQua` | `TSpeedButton` | — | — | `—` | — | — | Action=ActQua |
| `pnlQui` | `TPanel` | Acesso | 4 | `—` | — | — | — |
| `btnQui` | `TSpeedButton` | — | — | `—` | — | — | Action=ActQui |
| `pnlSab` | `TPanel` | — | 5 | `—` | — | — | — |
| `btnSab` | `TSpeedButton` | — | — | `—` | — | — | Action=ActSab |
| `pnlSeg` | `TPanel` | — | 1 | `—` | — | — | — |
| `btnSeg` | `TSpeedButton` | — | — | `—` | — | — | Action=ActSeg |
| `pnlSex` | `TPanel` | — | 6 | `—` | — | — | — |
| `btnSex` | `TSpeedButton` | — | — | `—` | — | — | Action=ActSex |
| `pnlTer` | `TPanel` | Acesso | 2 | `—` | — | — | — |
| `btnTer` | `TSpeedButton` | — | — | `—` | — | — | Action=ActTer |
| `tmInicio` | `TMaskEdit` | — | 2 | `!99:99;1;_` | 5 | Text=  :   | OnExit=tmInicioExit |
| `tmTermino` | `TMaskEdit` | — | 4 | `!99:99;1;_` | 5 | Text=  :   | OnExit=tmTerminoExit |
| `ChkSepararRegraDIa` | `TCheckBox` | Repetir diariamente | 6 | `—` | — | — | OnClick=ChkSepararRegraDIaClick |
| `ChkHoraInicioMaiorTermino` | `TCheckBox` | Horário Noturno | 7 | `—` | — | — | — |
| `ChkPersonalizar` | `TCheckBox` | Personalizar | 8 | `—` | — | Enabled=False | OnClick=ChkPersonalizarClick |
| `DayView1` | `TPanel` | — | 0 | `—` | — | Visible=False | — |
| `pnlPeriodo` | `TPanel` | — | 0 | `—` | — | — | — |
| `pnlUnderTime` | `TPanel` | — | 1 | `—` | — | — | — |
| `Label2` | `TLabel` | 0h | — | `—` | — | — | — |
| `Label3` | `TLabel` | 12h | — | `—` | — | — | — |
| `Label4` | `TLabel` | 23h | — | `—` | — | — | — |
| `Label5` | `TLabel` | 6h | — | `—` | — | — | — |
| `Label8` | `TLabel` | 18h | — | `—` | — | — | — |
| `TabAcesso` | `TTabSheet` | Acesso | — | `—` | — | — | — |
| `PgcTipoSelecoes` | `TPageControl` | — | 6 | `—` | — | — | — |
| `TabFiltros` | `TTabSheet` | TabFiltros | — | `—` | — | — | — |
| `pnlFiltrosPrincipal` | `TPanel` | — | 0 | `—` | — | — | — |
| `Label9` | `TLabel` | Filtro: | — | `—` | — | — | — |
| `mlFiltro` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lblNomeFiltro` | `TLabel` | lblNomeFiltro | — | `—` | — | — | — |
| `EdFiltro` | `TEdit` | — | 0 | `—` | — | Text=EdFiltro | OnExit=EdFiltroExit |
| `TabPessoas` | `TTabSheet` | TabPessoas | — | `—` | — | — | — |
| `lblPessoas` | `TLabel` | Lista de pessoas: | — | `—` | — | — | — |
| `mlPessoas` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `LstPessoas` | `TListBox` | — | 0 | `—` | — | — | — |
| `PnlRemoverPessoa` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnRemoverPessoa` | `TSpeedButton` | — | — | `—` | — | — | OnClick=BtnRemoverPessoaClick |
| `TabSetores` | `TTabSheet` | TabSetores | — | `—` | — | — | — |
| `Label7` | `TLabel` | Lista de setores: | — | `—` | — | — | — |
| `mlSetor` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `LstSetores` | `TListBox` | — | 0 | `—` | — | — | — |
| `PnlExcluirSetor` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnExcuirSetor` | `TSpeedButton` | — | — | `—` | — | — | OnClick=BtnExcluirSetorClick |
| `TabVeiculos` | `TTabSheet` | TabVeiculos | — | `—` | — | — | — |
| `Label11` | `TLabel` | Lista de Veiculos: | — | `—` | — | — | — |
| `mlVeiculo` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `LstVeiculos` | `TListBox` | — | 0 | `—` | — | — | — |
| `PnlRemoverVeiculo` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnRemoverVeiculo` | `TSpeedButton` | — | — | `—` | — | — | OnClick=BtnRemoverVeiculoClick |
| `TabPreCadastros` | `TTabSheet` | TabPreCadastros | — | `—` | — | — | — |
| `lblPreCadastros` | `TLabel` | Lista de pré-cadastros: | — | `—` | — | — | — |
| `mlPreCadastros` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `LstPreCadastros` | `TListBox` | — | 0 | `—` | — | — | — |
| `PnlRemoverPreCadastro` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnRemoverPreCadastro` | `TSpeedButton` | — | — | `—` | — | — | OnClick=BtnRemoverPessoaClick |
| `TabEscola` | `TTabSheet` | TabEscola | — | `—` | — | — | — |
| `lblEscola` | `TLabel` | Lista de alunos: | — | `—` | — | — | — |
| `mlEscola` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `LstEscola` | `TListBox` | — | 0 | `—` | — | — | — |
| `Panel1` | `TPanel` | — | 1 | `—` | — | — | — |
| `btnRemoverEscola` | `TSpeedButton` | — | — | `—` | — | — | OnClick=BtnRemoverPessoaClick |
| `pnlSituacao` | `TPanel` | — | 0 | `—` | — | — | — |
| `Label10` | `TLabel` | Situação: | — | `—` | — | — | — |
| `cmbStatus` | `TComboBox` | — | 0 | `—` | — | Text=Ativo, ItemIndex=0 | — |
| `pnlTipoRegra` | `TPanel` | — | 1 | `—` | — | Visible=False, Enabled=False | — |
| `lblTipoRegra` | `TLabel` | Tipo da regra: | — | `—` | — | — | — |
| `CbxLiberaBloqueia` | `TComboBox` | — | 0 | `—` | — | Text=LIBERAR, ItemIndex=1 | — |
| `pnlSentidoAcesso` | `TPanel` | — | 2 | `—` | — | — | — |
| `lblSentido` | `TLabel` | Sentido do Acesso: | — | `—` | — | — | — |
| `CmbTipoAcesso` | `TComboBox` | — | 0 | `—` | — | Text=ENTRADA, ItemIndex=0 | — |
| `pnlQuantidadeAcesso` | `TPanel` | — | 3 | `—` | — | — | — |
| `lblQtdAcesso` | `TLabel` | Quantidade de Acesso: | — | `—` | — | — | — |
| `EdQtdeAcesso` | `TSpinEdit` | — | 0 | `—` | — | — | OnChange=EdQtdeAcessoChange |
| `pnlIncluirPreCadastros` | `TPanel` | — | 4 | `—` | — | — | — |
| `ChkPreCadastro` | `TCheckBox` | Incluir pré-cadastros | 0 | `—` | — | Checked=True | — |
| `pnlFiltrarPor` | `TPanel` | — | 5 | `—` | — | — | — |
| `Label1` | `TLabel` | Filtrar por: | — | `—` | — | — | — |
| `CmbTipoSelecao` | `TComboBox` | — | 0 | `—` | — | — | OnChange=CmbTipoSelecaoChange |
| `TabColetores` | `TTabSheet` | Coletores | — | `—` | — | — | — |
| `ChkColetores` | `TCheckListBox` | — | 0 | `—` | — | — | — |
| `pnlColetores` | `TPanel` | — | 1 | `—` | — | — | — |
| `lblColetores` | `TLabel` | Selecionar coletores: | — | `—` | — | — | — |
| `Campos` | `TTabSheet` (herdado) | — | — | `—` | — | — | — |
| `Panel4` | `TPanel` (herdado) | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` (herdado) | — | — | `—` | — | — | — |
| `ActExcluir` | `TAction` (herdado) | — | — | `—` | — | Visible=False, Enabled=False | — |
| `ActCancelar` | `TAction` (herdado) | — | — | `—` | — | — | — |
| `ActDom` | `TAction` | Dom | — | `—` | — | — | — |
| `ActSeg` | `TAction` | Seg | — | `—` | — | — | — |
| `ActTer` | `TAction` | Ter | — | `—` | — | — | — |
| `ActQua` | `TAction` | Qua | — | `—` | — | — | — |
| `ActQui` | `TAction` | Qui | — | `—` | — | — | — |
| `ActSex` | `TAction` | Sex | — | `—` | — | — | — |
| `ActSab` | `TAction` | Sáb | — | `—` | — | — | — |
| `ActTSNome` | `TAction` | Nome (Ctrl+B) | — | `—` | — | — | — |
| `ActGerarAcesso` | `TAction` | Gerar Acesso (Repetir Diariamente) | — | `—` | — | — | — |
| `PopupMenu1` | `TPopupMenu` | — | — | `—` | — | — | — |
| `GerarAcessoRepetirDiariamente1` | `TMenuItem` | — | — | `—` | — | — | Action=ActGerarAcesso |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

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

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActAlterarExecute`
- `ActDomExecute`
- `ActExcluirExecute`
- `ActExibirTudoExecute`
- `ActGerarAcessoExecute`
- `ActIncluirExecute`
- `ActIrExecute`
- `ActQuaExecute`
- `ActQuiExecute`
- `ActSabExecute`
- `ActSalvarExecute`
- `ActSegExecute`
- `ActSexExecute`
- `ActTSNomeExecute`
- `ActTerExecute`
- `BtnExcluirSetorClick`
- `BtnExcluirVeiculoClick`
- `BtnRemoverPessoaClick`
- `BtnRemoverVeiculoClick`
- `ValidarCampos`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
