# Estacionamento > Cadastros > Veículos

> Fonte estática: `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Veiculos.pas` e `.dfm` no commit `28074dd`. Confirmar contra o build instalado antes de usar como oráculo de teste.

## Form e herança

- Classe: `TFrmEstacionamentoViewsCadastroVeiculos`.
- Herda a tela padrão de cadastro; controles `Pagina`, `GridCadastro`, `btnInserir`, `btnAlterar`, `btnexcluir`, `btnOk` e `btnCancelar` vêm da classe base. A ordem de tabulação deles deve ser conferida no DFM ancestral e na UI.
- Abre pelo handler `TFrmEstacionamentoViewsPrincipal.actCadVeiculosExecute` (ver `mapa_sistema.md`).

## Controles do cadastro

| Nome | Classe | Rótulo/caption | Tipo | TabOrder | Padrão/limite no DFM |
|---|---|---|---|---:|---|
| `EdNomeVeiculo` | `TEdit` | Nome do Veículo | Texto | 5 | Maiúsculas; `MaxLength=200` |
| `EdPlaca` | `TEdit` | Placa | Texto | 10 | Formatação automática `AAA-XXXX` no evento `OnChange` |
| `cmbTipoVeiculo` | `TComboBox` | Tipo de Veículo | Lista | 4 | Automóvel (`ItemIndex=0`) |
| `CmbStatusVeiculos` | `TComboBox` | Situação | Lista | 6 | Ativo (`ItemIndex=0`) |
| `cmbVeiculoUso` | `TComboBox` | Uso do Veículo | Lista | 7 | Próprio (`ItemIndex=0`) |
| `cmbBoxReserva` | `TComboBox` | Tipo de Vaga | Lista | 8 | Não Preferencial (`ItemIndex=0`) |
| `EdEstacionamento` | `TEdit` | Estacionamento | Código | 3 | Sem limite declarado |
| `edTag` | `TEdit` | Tag | Código | 2 | `0` ao limpar |
| `cmbPessoaPreCad` | `TComboBox` | Tipo de Motorista | Lista | 11 | Pré-Cadastro no DFM; `Pessoa` ao limpar |
| `EdPessoa` | `TEdit` | Motorista | Código | 9 | `0` ao limpar |
| `EdObservacao` | `TMemo` | Observações | Texto | 1 | `TabStop=False` |
| `btnCadTags` | `THoverSpeedButton` | Cadastrar Tags (Ctrl+N) | Botão | 12 | Abre cadastro de crachás/TAGs |

Os filtros da aba de grade incluem `ednomeloc` (Motorista, Ctrl+B), `edVeiculo` (Veículo, Ctrl+D), `edtPlaca` (Placa, Ctrl+F), `cmbTipoVei` (Tipo, Ctrl+G), `edtEstacionamento` (Estacionamento, também Ctrl+F no DFM), `cmbStatus` (Ctrl+H) e `edtTag` (Ctrl+W). Os dois filtros com Ctrl+F são uma **dúvida/conflito** do código; conferir qual ação recebe o atalho no build instalado.

## Validações e mensagens exatas

| Condição | Mensagem | Origem |
|---|---|---|
| Nome vazio após `Trim` | `O Nome do veículo deve ser informado.` | `ValidarCampos` |
| Placa vazia após `Trim` | `A placa do veículo deve ser informada.` | `ValidarCampos` |
| Placa inválida | `Placa inválida!` | `ValidarCampos` |
| TAG já vinculada a outro veículo | `Esta Tag já está vinculada ao veículo: "<nome>".` | `ActSalvarExecute` |
| TAG não encontrada ao sair do campo | `Tag não cadastrado` (rótulo, não popup) | `edTagExit` |
| Falha ao verificar/excluir TAG | `Erro ao verificar e excluir Tag vinculada ao Veículo. Entre em contato com o suporte!` | `ActExcluirExecute` |
| Falha ao excluir no banco | `Problemas com a exclusão no Banco de Dados!` + quebra de linha + `Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!` | `ActExcluirExecute` |

`ValidarPlaca` remove hífen, converte para maiúsculas e aceita exatamente sete caracteres: três letras `A-Z` seguidas de quatro letras ou dígitos `A-Z0-9`. `EdPlacaKeyPress` bloqueia caracteres fora de letras, dígitos e Backspace. A regra aceita combinações mais amplas que formatos oficiais específicos; não presumir validação de placa Mercosul completa. Fonte: `ValidarPlaca`, `EdPlacaChange`, `EdPlacaKeyPress`.

## Ações e dependências

- **Incluir:** `ActIncluirExecute` usa o fluxo da classe base e põe foco em `EdNomeVeiculo`.
- **Alterar:** só entra se `CdsVeiculos.RecordCount > 0`; usa a classe base e põe foco em `EdPlaca` (`ActAlterarExecute`).
- **Salvar:** verifica se a TAG já está vinculada, distinguindo inclusão e alteração; depois chama o salvamento herdado e aciona Exibir Tudo (`ActSalvarExecute`). A base chama `ValidarCampos` e `GravaCampos`, mostra erro se a gravação falhar e retorna à grade. Ver [base_cadastro_padrao.md](base_cadastro_padrao.md).
- **Consultar/Exibir Tudo:** `ActExibirTudoExecute` busca `FVeiculosController.GetTodos`, carrega o dataset da grade e ordena por `NOME`. `ActIrExecute` consulta pelo nome quando `ednomeloc` está preenchido. Há **dúvida**: o laço recebe `VeiculosItem`, mas preenche a grade usando `FVeiculosModel`; isso pode produzir dados incorretos.
- **Excluir:** pede `Excluir o registro?`, verifica/exclui a TAG vinculada, chama `FVeiculosController.Excluir` e remove a linha local se a operação retornar verdadeiro (`ActExcluirExecute`). `TVeiculosDAO.Excluir` marca `Veiculos.excluido = 'S'` por ID e registra histórico de operação `D`; é exclusão lógica. `TVeiculosDAO.Inserir` insere nova linha com `excluido = 'N'` e histórico `I`, então recriar após excluir usa outro ID. A confirmação da TAG e os efeitos em outros vínculos exigem leitura de `TCrachaDAO`.
- **Cancelar:** botão herdado; volta à grade (`TFrmPadrao.ActCancelarExecute`).
- **Relatório:** não há ação de relatório nesta tela; relatórios de veículos são itens separados no menu Estacionamento.
- **Cadastrar Tags:** se o veículo está em inclusão, pergunta `Para prosseguir com o cadastro de TAG, é necessário salvar os dados do veículo primeiro.` + quebra de linha + `Deseja salvar agora?`; se confirmado, salva e abre `TFrmRegCrachas` (`ActCadastrarTagsExecute`). O botão fica oculto se a ação de registro de TAGs no form principal está desabilitada (`CadastroShow`).
- **Motorista:** o combo alterna `Pessoa` e `Pré-Cadastro`; `EdPessoaExit` resolve o código e o rótulo. O código de TAG é resolvido via `TCrachaController` em `edTagExit`.

## Dúvidas para validar no build

1. O conflito de Ctrl+F entre Placa e Estacionamento.
2. O possível uso de `FVeiculosModel` em vez de `VeiculosItem` na consulta por nome.
3. Os efeitos da exclusão da TAG e de outros vínculos, além de restrições de unicidade no banco.
4. A ordem de tabulação e a identificação no pywinauto dos controles herdados.
