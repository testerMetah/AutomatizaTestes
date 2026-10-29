# Refeitório > Consultas > Acesso Por Pessoa...

> Inventário estático de `Acesso/UAcessoPorPessoa.dfm` e `Acesso/UAcessoPorPessoa.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFAcessoPorPessoa`
- Abertura: `acConAcessoPessoaExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FAcessoPorPessoa` | `TFAcessoPorPessoa` | Acesso por Pessoa | — | `—` | — | Visible=True | — |
| `pnlTopo` | `TPanel` | — | 0 | `—` | — | — | — |
| `mlPessoa` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `lblPessoa` | `TLabel` | lblPessoa | — | `—` | — | — | — |
| `Label3` | `TLabel` | Crachá: | — | `—` | — | — | — |
| `Label4` | `TLabel` | Coletor: | — | `—` | — | — | — |
| `lblPeriodoCalculado` | `TLabel` | lblPeriodoCalculado | — | `—` | — | — | — |
| `Label5` | `TLabel` | Período Calculado: | — | `—` | — | — | — |
| `EdPessoa` | `TEdit` | — | 1 | `—` | — | Text=EdPessoa | OnExit=EdPessoaExit, OnChange=EdPessoaChange |
| `CmbCracha` | `TComboBox` | — | 3 | `—` | — | — | OnChange=CmbCrachaChange |
| `CmbTipoPessoa` | `TComboBox` | — | 0 | `—` | — | Text=Pessoas, ItemIndex=0 | OnChange=CmbTipoPessoaChange |
| `gbPeriodo` | `TGroupBox` |       Período | 4 | `—` | — | — | — |
| `PnlPeriodo` | `TPanel` | — | 0 | `—` | — | — | — |
| `Label2` | `TLabel` | Até | — | `—` | — | — | — |
| `dtInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1;_` | 10 | Text=  /  /     | — |
| `tmInicio` | `TMaskEdit` | — | 1 | `!99:99;1;_` | 5 | Text=  :   | — |
| `DtEncerramento` | `TMaskEdit` | — | 2 | `!99/99/9999;1;_` | 10 | Text=  /  /     | — |
| `tmTermino` | `TMaskEdit` | — | 3 | `!99:99;1;_` | 5 | Text=  :   | — |
| `CmbColetorFuncao` | `TComboBox` | — | 2 | `—` | — | — | — |
| `BtnBuscarNomePadrao` | `THoverSpeedButton` | Consultar (F5) | 5 | `—` | — | — | Action=ActConsultar, OnClick=ActConsultarExecute |
| `PnlDados` | `TPanel` | — | 1 | `—` | — | — | — |
| `ScbAcessos` | `TScrollBox` | — | 2 | `—` | — | — | — |
| `StbDetalhes` | `TStatusBar` | — | — | `—` | — | — | — |
| `ActionList1` | `TActionList` | — | — | `—` | — | — | — |
| `ActConsultar` | `TAction` | Consultar (F5) | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 163: `Selecione um crachá.`
- Linha 173: `Crachá inválido.`
- Linha 292: `Não existem dados calculados para esse crachá e coletor.`
- Linha 899: `Pessoa deve ser informada.`
- Linha 907: `Coletor/Função deve ser informado.`
- Linha 914: `A data de início deve ser informada.`
- Linha 921: `A hora de início deve ser informada.`
- Linha 928: `A data de encerramento deve ser informada.`
- Linha 935: `A hora de término deve ser informada.`
- Linha 942: `O crachá deve ser informado.`
- Linha 997: `Aluno não cadastrado`
- Linha 1022: `Pessoa não cadastrada`
- Linha 1047: `Pessoa não cadastrada`
- Linha 1075: `Pessoa não cadastrada`
- Linha 1101: `Pessoa não cadastrada`
- Linha 1240: `Aluno não possui crachá.`
- Linha 1259: `Responsavel não possui crachá.`
- Linha 1276: `Pessoa não possui crachá.`
- Linha 1294: `Pessoa não possui crachá.`
- Linha 1310: `Pré-Cadastro não possui crachá.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActConsultarExecute`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
