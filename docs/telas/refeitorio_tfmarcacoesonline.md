# Refeitório > Consultas > Marcações Online...

> Inventário estático de `Acesso/UMarcacoesOnline.dfm` e `Acesso/UMarcacoesOnline.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFMarcacoesOnline`
- Abertura: `acConMarcacoesOnlineExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FMarcacoesOnline` | `TFMarcacoesOnline` | Consulta de Marcações Online | — | `—` | — | Visible=True | — |
| `MetaEquipLocalizar1` | `TMetaEquipLocalizar` | — | — | `—` | — | — | — |
| `GridConsulta` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `PnlFundo` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnContarRegistros` | `THoverSpeedButton` | Contar Registros (F5) | 0 | `—` | — | — | Action=ActContarRegistros, OnClick=ActContarRegistrosExecute |
| `BtnConsultar` | `THoverSpeedButton` | Consultar (F6) | 1 | `—` | — | — | Action=ActConsultar, OnClick=ActConsultarExecute |
| `Panel3` | `TPanel` | — | 2 | `—` | — | — | — |
| `PaginaLoc` | `TPageControl` | — | 0 | `—` | — | — | — |
| `TbsPeriodo` | `TTabSheet` | Período (Ctrl+A) | — | `—` | — | — | — |
| `LblDe` | `TLabel` | De | — | `—` | — | — | — |
| `LblAte` | `TLabel` | Até | — | `—` | — | — | — |
| `dtInicio` | `TMaskEdit` | — | 0 | `!99/99/9999;1; ` | 10 | Text=  /  /     | OnExit=dtInicioExit |
| `DtTermino` | `TMaskEdit` | — | 2 | `!99/99/9999;1; ` | 10 | Text=  /  /     | OnExit=dtInicioExit |
| `tmInicio` | `TMaskEdit` | — | 1 | `!99:99;1; ` | 5 | Text=  :   | OnExit=tmInicioExit |
| `TmTermino` | `TMaskEdit` | — | 3 | `!99:99;1; ` | 5 | Text=  :   | OnExit=tmInicioExit |
| `TbsCracha` | `TTabSheet` | Crachá (Ctrl+B) | — | `—` | — | — | — |
| `LblCracha` | `TLabel` | Número de Crachá | — | `—` | — | — | — |
| `ednrocracha` | `TEdit` | — | 0 | `—` | — | — | — |
| `TbsColetorFuncao` | `TTabSheet` | Coletor/Função (Ctrl+D) | — | `—` | — | — | — |
| `lblCampoColetor` | `TLabel` | Coletor | — | `—` | — | — | — |
| `LblFuncao` | `TLabel` | Função | — | `—` | — | — | — |
| `mlColetor` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | — |
| `lblColetor` | `TLabel` | lblColetor | — | `—` | — | — | — |
| `edColetor` | `TEdit` | — | 0 | `—` | — | — | OnExit=edColetorExit |
| `EdFuncao` | `TEdit` | — | 1 | `—` | — | — | — |
| `TbsSentido` | `TTabSheet` | Sentido (Ctrl+E) | — | `—` | — | — | — |
| `LblSentido` | `TLabel` | Sentido | — | `—` | — | — | — |
| `CmbSentido` | `TComboBox` | — | 0 | `—` | — | Text=Todos, ItemIndex=3 | — |
| `TbsTipoColeta` | `TTabSheet` | Tipo de Coleta (Ctrl+F) | — | `—` | — | — | — |
| `LblTipoColeta` | `TLabel` | Tipo de Coleta | — | `—` | — | — | — |
| `CmbTipoColeta` | `TComboBox` | — | 0 | `—` | — | Text=Todas, ItemIndex=2 | — |
| `TbsSituacao` | `TTabSheet` | Situação (Ctrl+G) | — | `—` | — | — | — |
| `LblSituacao` | `TLabel` | Situação | — | `—` | — | — | — |
| `CmbSituacao` | `TComboBox` | — | 0 | `—` | — | Text=Ambos, ItemIndex=2 | — |
| `TbsPessoa` | `TTabSheet` | Pessoa (Ctrl+H) | — | `—` | — | — | — |
| `mlPessoa` | `TMetaEquipLocalizar` | F4 | — | `—` | — | Visible=False | — |
| `lblPessoa` | `TLabel` | lblPessoa | — | `—` | — | Visible=False | — |
| `EdPessoa` | `TEdit` | — | 0 | `—` | — | Text=EdPessoa, Visible=False | OnExit=EdPessoaExit |
| `cmbTipoPessoa` | `TComboBox` | — | 1 | `—` | — | Text=Todos, ItemIndex=0 | OnChange=cmbTipoPessoaChange |
| `BtnLimparFiltros` | `THoverSpeedButton` | Limpar Filtros (Ctrl+X) | 1 | `—` | — | — | Action=ActLimparFiltros, OnClick=ActLimparFiltrosExecute |
| `ActionList1` | `TActionList` | — | — | `—` | — | — | — |
| `ActFechar` | `TAction` | Fechar (Alt+F4) | — | `—` | — | — | — |
| `ActLimparFiltros` | `TAction` | Limpar Filtros (Ctrl+X) | — | `—` | — | — | — |
| `ActLocalizarPessoa` | `TAction` | ActLocalizarPessoa | — | `—` | — | — | — |
| `ActConsultar` | `TAction` | Consultar (F6) | — | `—` | — | — | — |
| `ActPeriodo` | `TAction` | ActPeriodo | — | `—` | — | — | — |
| `ActCracha` | `TAction` | ActCracha | — | `—` | — | — | — |
| `ActColetorFuncao` | `TAction` | ActColetorFuncao | — | `—` | — | — | — |
| `ActSentido` | `TAction` | ActSentido | — | `—` | — | — | — |
| `ActTipoColeta` | `TAction` | ActTipoColeta | — | `—` | — | — | — |
| `ActSituacao` | `TAction` | ActSituacao | — | `—` | — | — | — |
| `ActPessoa` | `TAction` | ActPessoa | — | `—` | — | — | — |
| `ActContarRegistros` | `TAction` | Contar Registros (F5) | — | `—` | — | — | — |
| `ActBuscarFiltros` | `TAction` | F4 | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 213: `Possui `
- Linha 409: `Data Inválida!`
- Linha 432: `Coletor não cadastrado`
- Linha 700: `Hora Inválida!`
- Linha 709: `Data de Início deve ser informada.`
- Linha 716: `A hora de Início deve ser informada.`
- Linha 723: `Data de Término deve ser informada.`
- Linha 730: `A hora de Término deve ser informada.`

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActBuscarFiltrosExecute`
- `ActColetorFuncaoExecute`
- `ActConsultarExecute`
- `ActContarRegistrosExecute`
- `ActCrachaExecute`
- `ActLimparFiltrosExecute`
- `ActPeriodoExecute`
- `ActPessoaExecute`
- `ActSentidoExecute`
- `ActSituacaoExecute`
- `ActTipoColetaExecute`
- `BtnConsultarClick`
- `ValidarFiltros`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
