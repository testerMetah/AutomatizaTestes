# Escola: TfrmMigracaoDados

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Migração....

- DFM: `Escola/Views/Migracao/MigracaoDados.dfm`
- PAS: `Escola/Views/Migracao/MigracaoDados.pas`
- Handler de abertura: `actMigracaoExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| frmMigracaoDados | TfrmMigracaoDados | outro | Sistema de Migração de Dados | — | — | — | Visible=True |
| Panel1 | TPanel | contêiner | — | 0 | — | — | — |
| btnConectarOrigem | TButton | ação | Conectar Origem | 0 | — | — | Visible=False, Enabled=False |
| btnMigrarDados | TButton | ação | Migrar Tudo | 1 | — | — | Visible=False, Enabled=False |
| btnMigrarTurnosTurmas | TButton | ação | Turnos e Turmas | 2 | — | — | Visible=False, Enabled=False |
| btnMigrarFuncionarios | TButton | ação | Funcionários | 3 | — | — | Visible=False, Enabled=False |
| btnMigrarAlunos | TButton | ação | Alunos | 4 | — | — | Visible=False, Enabled=False |
| btnMigrarResponsaveis | TButton | ação | Responsáveis | 5 | — | — | Visible=False, Enabled=False |
| btnMigrarCrachas | TButton | ação | Crachás | 6 | — | — | Visible=False, Enabled=False |
| btnVincularResponsaveis | TButton | ação | Vincular Responsáveis | 7 | — | — | Visible=False, Enabled=False |
| btnImportarCSV | TButton | ação | Importar CSV | 8 | — | — | — |
| btnImportarCrachasCSV | TButton | ação | Importar crachas CSV | 9 | — | — | Visible=False, Enabled=False |
| btnGerarCrachasAuto | TButton | ação | Gerar crachas CSV | 10 | — | — | — |
| PageControl1 | TPageControl | contêiner | — | 1 | — | — | — |
| tsLog | TTabSheet | contêiner | Log de Migração | — | — | — | — |
| mmLog | TMemo | outro | — | 0 | — | — | — |
| Panel2 | TPanel | contêiner | — | 1 | — | — | — |
| Label1 | TLabel | rótulo | Progresso: | — | — | — | — |
| ProgressBar1 | TProgressBar | outro | — | 0 | — | — | — |
| tsConfig | TTabSheet | contêiner | Configuração | — | — | — | Enabled=False |
| edtServidorOrigem | TLabeledEdit | campo de texto/data | — | 0 | — | — | Text=DEV-MANAGER |
| edtDatabaseOrigem | TLabeledEdit | campo de texto/data | — | 1 | — | — | Text=carmo |
| edtUsuarioOrigem | TLabeledEdit | campo de texto/data | — | 2 | — | — | Text=sa |
| edtSenhaOrigem | TLabeledEdit | campo de texto/data | — | 3 | — | — | Text=Metadados01 |
| FDConnectionOrigem | TFDConnection | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `ValidarCPF` | 1345 | — |
| `ValidarEmail` | 1353 | — |
| `FormCreate` | 2089 | `TPessoasController.Create`, `TResponsaveisController.Create`, `TAlunosController.Create`, `TCrachaController.Create`, `TTurmasController.Create`, `TTurnosController.Create`, `FPessoasController.SetConexao`, `FResponsaveisController.SetConexao` |
| `ValidarSexo` | 2202 | — |
| `ExcluirVinculoCrachaPessoa` | 2375 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 338: `Erro na importação: `
- Linha 736: `Atribuição de crachás concluída com sucesso!`
- Linha 747: `Erro ao atribuir crachás: `
- Linha 1187: `Importação de Alunos e Responsáveis concluída!`
- Linha 1198: `Importação de Pessoas concluída!`
- Linha 1224: `Importação de Alunos e Responsáveis concluída com sucesso!`
- Linha 1229: `Erro na importação: `
- Linha 1256: `Importação de Pessoas concluída com sucesso!`
- Linha 1261: `Erro na importação: `
- Linha 1390: `Arquivo não encontrado!`
- Linha 1718: `Arquivo não encontrado!`
- Linha 1932: `Conecte primeiro ao banco origem!`
- Linha 1943: `Conecte primeiro ao banco origem!`
- Linha 1959: `Conecte primeiro ao banco origem!`
- Linha 1987: `Migração concluída com sucesso!`
- Linha 1993: `Erro durante migração: `
- Linha 2006: `Conecte primeiro ao banco origem!`
- Linha 2017: `Conecte primeiro ao banco origem!`
- Linha 2028: `Conecte primeiro ao banco origem!`
- Linha 2040: `Conecte primeiro ao banco origem!`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
