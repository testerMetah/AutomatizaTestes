# Refeitório > Comunicação > Comandos Por Equipamentos...

> Inventário estático de `Acesso/uFrmComunicacaoEquipamentos.dfm` e `Acesso/uFrmComunicacaoEquipamentos.pas` no commit `28074dd`. Esta ficha ainda precisa de análise manual das regras de Salvar, Consultar, Excluir, Cancelar e Relatório. Não usar como resultado esperado de teste sem conferir o build instalado.

- Form: `TFrmComunicacaoEquipamentos`
- Abertura: `acComComandosEquipamentosExecute` em `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas`

## Controles declarados no DFM

`TabOrder` é local ao contêiner; `—` significa propriedade herdada ou não declarada aqui.

| Nome | Classe | Caption | TabOrder | Máscara | MaxLength | Padrão | Eventos/ação |
|---|---|---|---:|---|---:|---|---|
| `FrmComunicacaoEquipamentos` | `TFrmComunicacaoEquipamentos` | Comunicação com Equipamentos | — | `—` | — | Visible=True | — |
| `PgComandos` | `TPageControl` | — | 0 | `—` | — | — | — |
| `TabFilaComandos` | `TTabSheet` | Fila de Comandos | — | `—` | — | — | — |
| `dbgFilaComandos` | `TDBGrid` | — | 0 | `—` | — | Visible=False | — |
| `Panel11` | `TPanel` | — | 1 | `—` | — | — | — |
| `BtnNovoComando` | `THoverSpeedButton` | Novo Comando (Ctrl+N) | 0 | `—` | — | — | Action=ActNovoComando, OnClick=ActNovoComandoExecute |
| `BtnAtualizarFilaComandos` | `THoverSpeedButton` | Atualizar (F5) | 1 | `—` | — | — | Action=AtcAtualizarFilaComandos, OnClick=AtcAtualizarFilaComandosExecute |
| `BtnExcluirListaComandos` | `THoverSpeedButton` | Excluir Item (Ctrl+Del) | 2 | `—` | — | — | Action=AtcExcluirListaComandos, OnClick=AtcExcluirListaComandosExecute |
| `TabEnviarInfo` | `TTabSheet` | Enviar Informações | — | `—` | — | — | — |
| `Panel12` | `TPanel` | — | 0 | `—` | — | — | — |
| `BtnEnviarSelecionado` | `THoverSpeedButton` | Enviar (Ctrl+S) | 0 | `—` | — | — | Action=ActEnviarSelecionado, OnClick=ActEnviarSelecionadoExecute |
| `BtnVoltar` | `THoverSpeedButton` | Voltar (Ctrl+D) | 1 | `—` | — | — | Action=ActCancelar, OnClick=ActCancelarExecute |
| `rdgEnviar` | `TRadioGroup` | Adicionar à fila: | 1 | `—` | — | — | OnClick=rdgEnviarClick |
| `pnlSelecaoColetor` | `TPanel` | Selecione um coletor... | 2 | `—` | — | — | — |
| `GroupBox1` | `TGroupBox` | Filtrar | 3 | `—` | — | — | — |
| `PgFiltrar` | `TPageControl` | — | 0 | `—` | — | — | — |
| `TabFiltro` | `TTabSheet` | TabFiltro | — | `—` | — | — | — |
| `dbgPessoasFiltro` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `pnFiltro` | `TPanel` | — | 1 | `—` | — | — | — |
| `TabPessoa` | `TTabSheet` | TabPessoa | — | `—` | — | — | — |
| `Label1` | `TLabel` | Pessoa: | — | `—` | — | — | — |
| `Panel1` | `TPanel` | Acesso | 0 | `—` | — | — | — |
| `MlPessoas` | `TMetaEquipLocalizar` | F4 | — | `—` | — | — | OnClick=MlPessoasClick |
| `lbPessoas` | `TListBox` | — | 1 | `—` | — | — | — |
| `btnExcluiFiltro` | `THoverSpeedButton` | Shift+Del | 2 | `—` | — | — | Action=ActRemoverPessoas, OnClick=ActRemoverPessoasExecute |
| `cbTipoFiltro` | `TComboBox` | — | 1 | `—` | — | — | OnClick=cbTipoFiltroClick, OnChange=cbTipoFiltroChange |
| `pnlLeft` | `TPanel` | — | 1 | `—` | — | — | — |
| `dbgColetores` | `TDBGrid` | — | 0 | `—` | — | Visible=True | — |
| `ActionList1` | `TActionList` | — | — | `—` | — | — | — |
| `ActEnviarDataHora` | `TAction` | Enviar | — | `—` | — | — | — |
| `AtcAtualizarFilaComandos` | `TAction` | Atualizar (F5) | — | `—` | — | — | — |
| `ActFechar` | `TAction` | Fechar (Alt+F4) | — | `—` | — | — | — |
| `ActEnviarConfig` | `TAction` | Enviar | — | `—` | — | — | — |
| `ActEnviarDigitais` | `TAction` | Enviar | — | `—` | — | — | — |
| `ActExcluirDigitais` | `TAction` | Excluir | — | `—` | — | — | — |
| `ActStatusColetor` | `TAction` | Solicitar Status | — | `—` | — | — | — |
| `ActStatusComunicacao` | `TAction` | Solicitar | — | `—` | — | — | — |
| `ActColetarDigitais` | `TAction` | Coletar | — | `—` | — | — | — |
| `AtcExcluirListaComandos` | `TAction` | Excluir Item (Ctrl+Del) | — | `—` | — | — | — |
| `ActEnviarFaces` | `TAction` | Enviar | — | `—` | — | — | — |
| `ActExcluirFaces` | `TAction` | Excluir | — | `—` | — | — | — |
| `ActColetarFaces` | `TAction` | Coletar | — | `—` | — | — | — |
| `ActEnviarSelecionado` | `TAction` | Enviar (Ctrl+S) | — | `—` | — | — | — |
| `ActNovoComando` | `TAction` | Novo Comando (Ctrl+N) | — | `—` | — | — | — |
| `ActCancelar` | `TAction` | Voltar (Ctrl+D) | — | `—` | — | — | — |
| `ActEnviarUsuarios` | `TAction` | ActEnviarUsuarios | — | `—` | — | — | — |
| `ActExcluirUsuarios` | `TAction` | ActExcluirUsuarios | — | `—` | — | — | — |
| `ActBuscarPessoas` | `TAction` | F4 | — | `—` | — | — | — |
| `ActRemoverPessoas` | `TAction` | Shift+Del | — | `—` | — | — | — |
| `ActLimpezaTotal` | `TAction` | ActLimpezaTotal | — | `—` | — | — | — |
| `CdsFilaComandosPessoas` | `TWideStringField` | — | — | `—` | — | — | — |
| `Timer1` | `TTimer` | — | — | `—` | — | — | — |

## Mensagens literais detectadas

Esta lista contém o primeiro literal de cada chamada encontrada na unit. Mensagens concatenadas têm partes dinâmicas; a mensagem completa exige leitura da procedure. Mensagens em controllers ou na classe base ficam fora desta lista.

- Linha 450: `Selecione uma opção de envio antes de selecionar os coletores.`
- Linha 460: `Erro: Comando não encontrado`
- Linha 503: `Erro ao interagir com o coletor: `
- Linha 1344: `Selecione uma opção para enviar!`
- Linha 1351: `Comando selecionado não é Limpeza Total!`
- Linha 1387: `Selecione um item para excluí-lo.`
- Linha 1564: `Erro ao gravar fila para o coletor: `
- Linha 1576: `Comandos processados e enviados à fila.`
- Linha 1840: `TopData Fit não suporta comando de Faces! Selecione apenas coletores compatíveis.`
- Linha 1930: `Os coletores selecionados não suportam Biometria! Selecione apenas coletores com biometria habilitada.`
- Linha 1932: `Nenhum coletor selecionado! Selecione pelo menos um coletor com biometria habilitada.`
- Linha 1987: `Selecione uma opção válida para enviar!`
- Linha 1996: `Selecione uma opção para enviar!`
- Linha 2004: `Selecione pelo menos um coletor na lista!`
- Linha 2015: `É necessário selecionar o tipo de filtragem`
- Linha 2035: `Comando não reconhecido: `

## Ações encontradas na unit

A presença da procedure indica código a analisar; não implica que a ação esteja visível no build.

- `ActBuscarPessoasExecute`
- `ActCancelarExecute`
- `ActColetarDigitaisExecute`
- `ActColetarFacesExecute`
- `ActEnviarConfigExecute`
- `ActEnviarDataHoraExecute`
- `ActEnviarDigitaisExecute`
- `ActEnviarFacesExecute`
- `ActEnviarSelecionadoExecute`
- `ActEnviarUsuariosExecute`
- `ActExcluirDigitaisExecute`
- `ActExcluirFacesExecute`
- `ActExcluirUsuariosExecute`
- `ActFecharExecute`
- `ActLimpezaTotalExecute`
- `ActNovoComandoExecute`
- `ActRemoverPessoasExecute`
- `ActStatusComunicacaoExecute`
- `AtcExcluirListaComandosExecute`

## Pendências de análise

- Identificar dependências adicionais nas procedures herdadas, controllers e DAOs.
- Confirmar mensagens completas e controles na UI do build testado.
