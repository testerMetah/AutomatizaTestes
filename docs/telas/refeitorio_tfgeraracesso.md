# Refeitório > Acesso > Gerar Acesso...

> Inventário estático de `Acesso/UGerarAcesso.dfm` e `Acesso/UGerarAcesso.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFGerarAcesso`
- Abertura: `acAceGerarAcessoExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FGerarAcesso` | `TFGerarAcesso` | Gerar Acesso | — | `—` | — | Visible=True | — |
| `pnlPrincipal` | `TPanel` | — | 1 | `—` | — | — | — |
| `LblNroDiasGerar` | `TLabel` | Nº de Dias para Gerar: | — | `—` | — | — | — |
| `LblSelecao` | `TLabel` | Seleção: | — | `—` | — | — | — |
| `lblVersao` | `TLabel` | Versão do Gerador de Acesso: | — | `—` | — | — | — |
| `EdNroDiasGerar` | `TSpinEdit` | — | 0 | `—` | 2 | — | OnExit=EdNroDiasGerarExit |
| `CmbTipoSelecao` | `TComboBox` | — | 1 | `—` | — | Text=Geral, ItemIndex=0 | OnChange=CmbTipoSelecaoChange |
| `CmbVersao` | `TComboBox` | — | 2 | `—` | — | Text=2.0, ItemIndex=1 | — |
| `CpTipoSelecoes` | `TCardPanel` | — | 3 | `—` | — | — | — |
| `CdFiltros` | `TCard` | Filtros | 0 | `—` | — | — | — |
| `PnlFiltro` | `TPanel` | — | 0 | `—` | — | — | — |
| `MlFiltro` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `LblFiltro` | `TLabel` | Filtro: | — | `—` | — | — | — |
| `lblNomeFiltro` | `TLabel` | lblNomeFiltro | — | `—` | — | — | — |
| `EdFiltro` | `TEdit` | — | 0 | `—` | — | Text=EdFiltro | OnExit=EdFiltroExit |
| `CdPessoas` | `TCard` | Pessoas | 1 | `—` | — | — | — |
| `LblPessoas` | `TLabel` | Lista de Pessoas: | — | `—` | — | — | — |
| `mlPessoa` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `LstPessoas` | `TListBox` | — | 0 | `—` | — | — | — |
| `BtnRemoverPessoa` | `THoverSpeedButton` | Ctrl+Del | 1 | `—` | — | — | Action=ActApagar, OnClick=ActApagarExecute |
| `CdSetores` | `TCard` | Setores | 2 | `—` | — | — | — |
| `mlSetor` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `LblSetores` | `TLabel` | Lista de Setores: | — | `—` | — | — | — |
| `LstSetores` | `TListBox` | — | 0 | `—` | — | — | — |
| `BtnExcluirSetor` | `THoverSpeedButton` | Ctrl+Del | 1 | `—` | — | — | Action=ActApagar, OnClick=ActApagarExecute |
| `CdVeiculos` | `TCard` | Veiculos | 3 | `—` | — | — | — |
| `Label3` | `TLabel` | Lista de Veículos: | — | `—` | — | — | — |
| `mlVeiculo` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `LstVeiculos` | `TListBox` | — | 0 | `—` | — | — | — |
| `BtnRemoverVeiculo` | `THoverSpeedButton` | Ctrl+Del | 1 | `—` | — | — | Action=ActApagar, OnClick=ActApagarExecute |
| `CdEscola` | `TCard` | Escola | 4 | `—` | — | — | — |
| `lblEscola` | `TLabel` | Lista de Alunos: | — | `—` | — | — | — |
| `mlEscola` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `LstEscola` | `TListBox` | — | 0 | `—` | — | — | — |
| `btnRemoverEscola` | `THoverSpeedButton` | Ctrl+Del | 1 | `—` | — | — | Action=ActApagar, OnClick=ActApagarExecute |
| `pnlFundoPadrao` | `TPanel` | — | 0 | `—` | — | — | — |
| `btngeraracesso` | `THoverSpeedButton` | Gerar Acesso (Ctrl+G) | 0 | `—` | — | — | Action=ActGerar, OnClick=ActGerarExecute |
| `ActionList1` | `TActionList` | — | — | `—` | — | — | — |
| `ActGerar` | `TAction` | Gerar Acesso (Ctrl+G) | — | `—` | — | — | — |
| `ActFechar` | `TAction` | ActFechar | — | `—` | — | — | — |
| `ActBuscar` | `TAction` | F4 | — | `—` | — | — | — |
| `ActApagar` | `TAction` | Ctrl+Del | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 171: `Geração de Acesso Concluída`
- Linha 306: `Filtro não cadastrado`
- Linha 665: `Atenção: Erro ao reaplicar cortes de reservas ativas.`
- Linha 669: `Erro ao processar cortes de reservas: `
- Linha 677: `Erro ao Gerar Acesso: `
- Linha 771: `Inclua pelo menos um aluno na lista.`
- Linha 779: `Inclua pelo menos uma turma na lista.`
- Linha 787: `Inclua pelo menos um turno na lista.`
- Linha 797: `Selecione algum veículo na lista.`
- Linha 806: `O Filtro deve ser informado.`
- Linha 814: `Selecione alguma pessoa na lista.`
- Linha 822: `Selecione algum setor na lista.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActApagarExecute`
- `ActBuscarExecute`
- `ActFecharExecute`
- `ActGerarExecute`
- `ValidarCampos`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
