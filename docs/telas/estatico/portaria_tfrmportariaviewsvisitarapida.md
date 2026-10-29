# Portaria: TFrmPortariaViewsVisitaRapida

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Visita Rápida.

- DFM: `Portaria/Views/Acessus.Portaria.Views.VisitaRapida.dfm`
- PAS: `Portaria/Views/Acessus.Portaria.Views.VisitaRapida.pas`
- Handler de abertura: `actVisitaRapidaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmPortariaViewsVisitaRapida | TFrmPortariaViewsVisitaRapida | outro | Visita Rápida | — | — | — | Visible=True |
| CardPanel1 | TCardPanel | contêiner | CardPanel1 | 0 | — | — | — |
| cdEntrada | TCard | outro | Entrada | 0 | — | — | — |
| lblEntrada | TLabel | rótulo | Entrada de Visitante | — | — | — | — |
| Panel1 | TPanel | contêiner | — | 0 | — | — | — |
| Image6 | TImage | outro | — | — | — | — | — |
| Label5 | TLabel | rótulo | CPF: | — | — | — | — |
| lblErroCPF | TLabel | rótulo | lblErroCPF | — | — | — | — |
| mlEstrangeiro | TMetaEquipLocalizar | outro | Buscar Estrangeiro | — | — | — | Visible=False |
| lblNomeEstrangeiro | TLabel | rótulo | lblNomeEstrangeiro | — | — | — | Visible=False |
| edtCpf | TEdit | campo de texto/data | — | 0 | — | 11 | — |
| btnLocalizar | THoverSpeedButton | ação | Novo cadastro | 1 | — | — | — |
| chkEstrangeiro | TCheckBox | seleção | Estrangeiro | 2 | — | — | — |
| btnLimparEstrangeiro | THoverSpeedButton | ação |  | 3 | — | — | Visible=False |
| EdtIdEstrangeiro | TEdit | campo de texto/data | — | 4 | — | — | Text=EdtIdEstrangeiro, Visible=False |
| cdpEntrada | TCardPanel | contêiner | — | 1 | — | — | Visible=False |
| cdNovaVisita | TCard | outro | Nova Visita | 0 | — | — | — |
| Image7 | TImage | outro | — | — | — | — | — |
| Label3 | TLabel | rótulo | Data/Hora de Início: | — | — | — | — |
| Label4 | TLabel | rótulo | Dados da visita | — | — | — | — |
| Label6 | TLabel | rótulo | Crachá: | — | — | — | — |
| Image3 | TImage | outro | — | — | — | — | — |
| Image9 | TImage | outro | — | — | — | — | — |
| Label7 | TLabel | rótulo | Observação: | — | — | — | — |
| Image4 | TImage | outro | — | — | — | — | — |
| lblColetores | TLabel | rótulo | Coletores: | — | — | — | — |
| Label13 | TLabel | rótulo | Nome: | — | — | — | — |
| Image10 | TImage | outro | — | — | — | — | — |
| lblNomeVisita | TLabel | rótulo | lblNomeVisita | — | — | — | — |
| imgVisitaFace | TImage | outro | — | — | — | — | — |
| Image11 | TImage | outro | — | — | — | — | — |
| Label1 | TLabel | rótulo | Responsável: | — | — | — | — |
| MetaResponsavel | TMetaEquipLocalizar | outro | — | — | — | — | — |
| lblResponsavel | TLabel | rótulo | lblResponsavel | — | — | — | — |
| ImgSemFace | TImage | outro | — | — | — | — | Visible=False |
| edtVisitaDataInicio | TMaskEdit | campo de texto/data | — | 0 | !99/99/9999;1;_ | 10 | Text=  /  /     |
| edtVisitaHoraInicio | TMaskEdit | campo de texto/data | — | 1 | !99:99;1;_ | 5 | Text=  :   |
| edtVisitaCracha | TEdit | campo de texto/data | — | 2 | — | 15 | — |
| edtVisitaObservacao | TMemo | outro | — | 3 | — | 512 | — |
| btnCriarVisita | THoverSpeedButton | ação | Criar Visita | 4 | — | — | — |
| btnCancelar | THoverSpeedButton | ação | Cancelar | 5 | — | — | — |
| ChkColetores | TCheckListBox | seleção | — | 6 | — | — | Enabled=False |
| cmbTodosColetores | TCheckBox | seleção | Marcar todos Coletores | 8 | — | — | Enabled=False |
| btnConfigColetores | THoverSpeedButton | ação | Coletores (Ctrl+G) | 7 | — | — | Visible=False |
| EdResponsavel | TEdit | campo de texto/data | — | 9 | — | 5 | Visible=False, Enabled=False |
| cdNovoCadastro | TCard | outro | Novo Cadastro | 1 | — | — | — |
| Label10 | TLabel | rótulo | Nome: | — | — | — | — |
| Image5 | TImage | outro | — | — | — | — | — |
| Label11 | TLabel | rótulo | Telefone (Opcional): | — | — | — | — |
| Image8 | TImage | outro | — | — | — | — | — |
| Label12 | TLabel | rótulo | Cadastro de visitante | — | — | — | — |
| EdNome | TEdit | campo de texto/data | — | 0 | — | 255 | — |
| EdTelefone | TEdit | campo de texto/data | — | 1 | — | 11 | — |
| btnCancelarCadastro | THoverSpeedButton | ação | Cancelar | 2 | — | — | — |
| btnSalvarCadastro | THoverSpeedButton | ação | Salvar | 3 | — | — | — |
| GroupBox1 | TGroupBox | contêiner | Fotografia | 4 | — | — | — |
| imgFoto | TImage | outro | — | — | — | — | — |
| BtnLimpar | THoverSpeedButton | ação | Limpar | 0 | — | — | — |
| btnSelectImage | THoverSpeedButton | ação | Procurar | 1 | — | — | — |
| btnCamera | THoverSpeedButton | ação | Câmera | 2 | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| actLocalizarVisitanteTerceiro | TAction | ação | Novo cadastro | — | — | — | — |
| actEntrada | TAction | ação | Entrada | — | — | — | — |
| actSaida | TAction | ação | Saída | — | — | — | — |
| actConsulta | TAction | ação | Consulta | — | — | — | — |
| actLocalizarCrachas | TAction | ação | — | — | — | — | — |
| actCancelar | TAction | ação | Cancelar | — | — | — | — |
| actCriarVisita | TAction | ação | Criar Visita | — | — | — | — |
| actCancelarCadastro | TAction | ação | Cancelar | — | — | — | — |
| actSalvarCadastro | TAction | ação | Salvar | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 193 | `TPreCadastroController.Create`, `VisitantesTerceirosController.SetConexao`, `TCrachaController.Create`, `FCrachasController.SetConexao`, `TVisitantesTerceirosHistoricosController.Create`, `FHistoricosController.SetConexao`, `TEstadoVisitaController.Create`, `FEstadoVisitaController.SetConexao` |
| `actCancelarCadastroExecute` | 313 | — |
| `actCancelarExecute` | 319 | — |
| `actSalvarCadastroExecute` | 456 | `VisitantesTerceirosController.Inserir` |
| `ValidarCamposVisita` | 739 | `FCrachasController.VerificaCrachaVinculado`, `FHistoricosController.GetVisitaAtiva`, `FHistoricosController.GetVisitaAtivaPorCracha` |
| `GravaFoto` | 926 | `FFaceControlIdController.GetFacePorPessoa`, `FFaceControlIdController.Excluir`, `FFaceControlIdController.Inserir` |
| `GravarVisita` | 1121 | `FPessoasController.GetPessoa`, `FHistoricosController.Inserir`, `FEstadoVisitaController.Inserir` |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 361: `Visita criada!`
- Linha 378: `Deseja encerrar a visita em andamento de `
- Linha 407: `Erro ao encerrar a visita:`
- Linha 417: `Visita encerrada com sucesso.`
- Linha 463: `Informe o nome do visitante.`
- Linha 483: `Erro ao salvar o cadastro. Tente novamente.`
- Linha 491: `Erro ao salvar o cadastro:`
- Linha 754: `Informe a data de início da visita.`
- Linha 761: `Data Inválida!`
- Linha 769: `A data não pode ser inferior ao dia atual!`
- Linha 778: `Informe a hora de início da visita.`
- Linha 786: `Informe o número do crachá.`
- Linha 822: `Este visitante já possui uma visita em andamento.`
- Linha 836: `Este crachá já está em uso em uma visita ativa.`
- Linha 861: `Selecione ao menos um coletor para criar a visita.`
- Linha 1024: `Não foi possível comunicar o encerramento ao equipamento.`
- Linha 1164: `Erro ao gravar a visita. Tente novamente.`
- Linha 1347: `Responsável não cadastrado.`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
