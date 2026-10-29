# Acesso: TFrmProgramacaoRegrasAcesso

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Acesso > Programação de Regras de Acesso....

- DFM: `Acesso/UFrmProgramacaoRegrasAcesso.dfm`
- PAS: `Acesso/UFrmProgramacaoRegrasAcesso.pas`
- Handler de abertura: `acAceProgramacaoRegrasAcessoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmProgramacaoRegrasAcesso | TFrmProgramacaoRegrasAcesso | outro | Programação de Regras de Acesso | — | — | — | — |
| Pagina | TPageControl | contêiner | — | — | — | — | — |
| Grid | TTabSheet | contêiner | — | — | — | — | — |
| GridCadastro | TDBGrid | grade | — | — | — | — | Visible=True |
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
| Panel3 | TPanel | contêiner | — | 0 | — | — | — |
| Label1 | TLabel | rótulo | Nome: | — | — | — | — |
| Label2 | TLabel | rótulo | Descrição: | — | — | — | — |
| Label3 | TLabel | rótulo | Início: | — | — | — | — |
| Label4 | TLabel | rótulo | Fim: | — | — | — | — |
| Label5 | TLabel | rótulo | Situação: | — | — | — | — |
| edNomeProgramacao | TEdit | campo de texto/data | — | 0 | — | — | — |
| edDescricao | TEdit | campo de texto/data | — | 1 | — | — | — |
| dtInicio | TMaskEdit | campo de texto/data | — | 2 | !99/99/0000;1;_ | 10 | Text=  /  /     |
| dtTermino | TMaskEdit | campo de texto/data | — | 3 | !99/99/0000;1;_ | 10 | Text=  /  /     |
| tmInicio | TMaskEdit | campo de texto/data | — | 4 | !90:00;1;_ | 5 | Text=  :  , Enabled=False |
| tmTermino | TMaskEdit | campo de texto/data | — | 5 | !90:00;1;_ | 5 | Text=  :  , Enabled=False |
| cmbStatus | TComboBox | seleção | — | 6 | — | — | Text=Ativo, ItemIndex=0 |
| Panel1 | TPanel | contêiner | — | 1 | — | — | — |
| Panel8 | TPanel | contêiner | — | 0 | — | — | — |
| DGridProgramacoes | TDrawGrid | grade | — | 0 | — | — | — |
| Panel9 | TPanel | contêiner | — | 1 | — | — | — |
| cbExcluirFaixaAcesso | TCheckBox | seleção | Excluir acessos antigos | 0 | — | — | — |
| Panel5 | TPanel | contêiner | — | 2 | — | — | — |
| Label6 | TLabel | rótulo | Pessoa: | — | — | — | — |
| Label12 | TLabel | rótulo | Pré-Cadastro: | — | — | — | — |
| lbPessoas | TListBox | seleção | — | 0 | — | — | — |
| lbPreCadastros | TListBox | seleção | — | 1 | — | — | — |
| btnRemoverPessoa | THoverSpeedButton | ação | Remover Pessoa | 2 | — | — | — |
| Panel6 | TPanel | contêiner | Acesso | 3 | — | — | — |
| Shape2 | TShape | outro | — | — | — | — | — |
| MetaEquipLocalizar1 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| Panel7 | TPanel | contêiner | Acesso | 4 | — | — | — |
| Shape7 | TShape | outro | — | — | — | — | — |
| MetaEquipLocalizar2 | TMetaEquipLocalizar | outro | — | — | — | — | — |
| btnRemoverPreCadastro | THoverSpeedButton | ação | Remover Pré-Cad. | 5 | — | — | — |
| pnlFundoCadastro | TPanel | contêiner | — | 3 | — | — | — |
| btnOk | THoverSpeedButton | ação | — | — | — | — | — |
| btnCancelar | THoverSpeedButton | ação | — | — | — | — | — |
| btnVisualizarProgramacao | THoverSpeedButton | ação | Visualizar Programação | 2 | — | — | — |
| Campos | TTabSheet | contêiner | — | — | — | — | — |
| Panel4 | TPanel | contêiner | — | — | — | — | — |
| CdsProgramacoes | TClientDataSet | outro | — | — | — | — | — |
| CdsProgramacoesId | TIntegerField | outro | — | — | — | — | — |
| CdsProgramacoesNome | TStringField | outro | — | — | — | — | — |
| CdsProgramacoesRegra | TStringField | outro | — | — | — | — | — |
| CdsProgramacoesSituacao | TStringField | outro | — | — | — | — | — |
| CdsProgramacoesDataHoraInicio | TDateTimeField | outro | — | — | — | — | — |
| CdsProgramacoesDataHoraTermino | TDateTimeField | outro | — | — | — | — | — |
| DsProgramacoes | TDataSource | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 164 | `TProgramacoesRegrasAcessoController.Create`, `TRegrasAcessoController.Create`, `FProgramacaoController.SetConexao`, `FRegrasAcessoController.SetConexao` |
| `cbExcluirFaixaAcessoClick` | 313 | — |
| `ActExcluirExecute` | 938 | `FProgramacaoController.Excluir` |
| `ActExibirTudoExecute` | 954 | — |
| `ValidarCampos` | 1236 | `FProgramacaoController.RegraEstaEmUso`, `FProgramacaoController.ObterNomeProgramacaoConflito` |
| `GravaCampos` | 1469 | `FProgramacaoController.ValidarProgramacao`, `FProgramacaoController.VerificarConflitosItens`, `FProgramacaoController.Inserir`, `FProgramacaoController.Atualizar` |
| `ActIncluirExecute` | 1641 | — |
| `ActSalvarExecute` | 1676 | — |
| `ActCancelarExecute` | 1708 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 942: `Excluir o registro?`
- Linha 947: `Problemas com a exclusão no Banco de Dados!`
- Linha 1136: `Programação não encontrada.`
- Linha 1250: `Informe o nome da programação`
- Linha 1258: `Data de início inválida`
- Linha 1265: `Data de término inválida`
- Linha 1276: `Data inválida`
- Linha 1284: `A data inicial não pode ser anterior ao dia atual!`
- Linha 1292: `A data inicial não pode ser maior que a data de término!`
- Linha 1317: `Selecione uma regra de acesso`
- Linha 1367: `A data inicial não pode ser anterior à data inicial da regra selecionada (%s)!`
- Linha 1376: `A data de término não pode ser superior à data final da regra selecionada (%s)!`
- Linha 1387: `Hora de início inválida`
- Linha 1394: `Hora de término inválida`
- Linha 1410: `Erro ao validar horários: `
- Linha 1421: `Para horário normal, a data/hora de término deve ser maior que a data/hora de início!`
- Linha 1431: `Para horário noturno em um mesmo dia, o horário de término deve ser maior que o horário de início!`
- Linha 1440: `📋 **HORÁRIO NOTURNO DETECTADO**`
- Linha 1489: `Erros de validação:`
- Linha 1566: `Programação salva como Inativa. Para aplicar, altere o status para Ativo.`
- Linha 1576: `Erro ao salvar programação.`
- Linha 1671: `Nenhuma programação selecionada para edição.`
- Linha 1681: `Usuário MASTER não pode salvar registros.`
- Linha 1695: `Deseja gerar acesso?`
- Linha 1741: `Habilite a edição para visualizar os dados da programação.`
- Linha 1748: `Preencha o nome da programação para visualizar os dados.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
