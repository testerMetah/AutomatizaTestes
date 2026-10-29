# Administracao: TFrmAdministracaoViewsParametrosSistema

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Parâmetros > Parâmetros do Sistema.

- DFM: `Administracao/Views/Acessus.Administracao.Views.ParametrosSistema.dfm`
- PAS: `Administracao/Views/Acessus.Administracao.Views.ParametrosSistema.pas`
- Handler de abertura: `actParametrosSistemaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmAdministracaoViewsParametrosSistema | TFrmAdministracaoViewsParametrosSistema | outro | Parâmetros do Sistema | — | — | — | Visible=True |
| pnlFundoCadastro | TPanel | contêiner | — | 0 | — | — | — |
| btnOk | THoverSpeedButton | ação | Salvar (Ctrl+S) | 0 | — | — | — |
| btnCancelar | THoverSpeedButton | ação | Fechar (Ctrl+F4) | 1 | — | — | — |
| pnlParametros | TPanel | contêiner | — | 1 | — | — | — |
| PaginaModulos | TPageControl | contêiner | — | 0 | — | — | — |
| tsGeral | TTabSheet | contêiner | Geral | — | — | — | — |
| prmUtilizarMDITabs | TCheckBox | seleção | Utilizar controle MDI para Tabs. | 0 | — | — | — |
| prmModulosUtilizarMDITabs | TCheckListBox | seleção | — | 1 | — | — | — |
| prmAlterarSenha | TCheckBox | seleção | Alterar senha no primeiro login | 2 | — | — | — |
| tsClassApp | TTabSheet | contêiner | ClassApp API | — | — | — | — |
| prmAtivarClassAppAPI | TCheckBox | seleção | Ativar ClassApp API | 0 | — | — | — |
| gbxClassAppAPI | TGroupBox | contêiner | Parâmetros ClassApp API | 1 | — | — | — |
| lblUrl | TLabel | rótulo | URL:  | — | — | — | — |
| lblToken | TLabel | rótulo | Token:  | — | — | — | — |
| lblTipoVinculoClassApp | TLabel | rótulo | Tipo de Vínculo:  | — | — | — | — |
| prmURLClassAppAPI | TEdit | campo de texto/data | — | 0 | — | — | — |
| prmValorTokenClassApp | TEdit | campo de texto/data | — | 1 | — | — | — |
| prmTipoVinculoClassApp | TComboBox | seleção | — | 2 | — | — | — |
| tsPortaria | TTabSheet | contêiner | Portaria | — | — | — | — |
| prmNovaTelaVisitantesTerceiros | TCheckBox | seleção | Usar nova tela de cadastro de visitantes/terceiros | 0 | — | — | — |
| tsRefeitorio | TTabSheet | contêiner | Refeitório | — | — | — | — |
| gbConfigReservas | TGroupBox | contêiner | Configuração das Reservas de Refeição | 0 | — | — | — |
| prmExcluirAcessosAoReservar | TCheckBox | seleção | Excluir acessos de regras ao reservar | 0 | — | — | — |
| prmAutorizarReservasDurantePeriodoConsumo | TCheckBox | seleção |  | 1 | — | — | — |
| gbConfigRefeitorio | TGroupBox | contêiner | Configuração do Refeitório | 1 | — | — | — |
| prmAgruparColetoresRefeitorio | TCheckBox | seleção | Agrupar coletores por refeitório | 0 | — | — | — |
| tsEmail | TTabSheet | contêiner | E-Mail | — | — | — | — |
| gbxEmailConfig | TGroupBox | contêiner | Configuração do Servidor SMTP | 0 | — | — | — |
| lblSmtpHost | TLabel | rótulo | Servidor SMTP: | — | — | — | — |
| lblSmtpPort | TLabel | rótulo | Porta: | — | — | — | — |
| lblSmtpUsername | TLabel | rótulo | Usuário: | — | — | — | — |
| lblSmtpPassword | TLabel | rótulo | Senha: | — | — | — | — |
| lblSmtpFromName | TLabel | rótulo | Nome do Remetente: | — | — | — | — |
| lblSmtpFromEmail | TLabel | rótulo | E-mail Remetente: | — | — | — | — |
| prmSmtpHost | TEdit | campo de texto/data | — | 0 | — | — | — |
| prmSmtpPort | TSpinEdit | campo de texto/data | — | 1 | — | — | — |
| prmSmtpUsername | TEdit | campo de texto/data | — | 2 | — | — | — |
| prmSmtpPassword | TEdit | campo de texto/data | — | 3 | — | — | — |
| prmSmtpFromName | TEdit | campo de texto/data | — | 4 | — | — | Text=Sistema de Controle de Acesso |
| prmSmtpFromEmail | TEdit | campo de texto/data | — | 5 | — | — | — |
| chkSmtpUseSSL | TCheckBox | seleção | Usar SSL | 6 | — | — | — |
| chkSmtpUseTLS | TCheckBox | seleção | Usar TLS | 7 | — | — | Checked=True |
| gbxEmailDestinatarios | TGroupBox | contêiner | Destinatários (um por linha) | 1 | — | — | — |
| lblDestinatarios | TLabel | rótulo | E-mails para: | — | — | — | — |
| mmDestinatarios | TMemo | outro | — | 0 | — | — | — |
| btnTestarEmail | THoverSpeedButton | ação | Testar Envio | 1 | — | — | — |
| tsGeracaoAcesso | TTabSheet | contêiner | Geração de Acesso | — | — | — | — |
| gbConfigGeracaoAcesso | TGroupBox | contêiner | Configuração da Geração de Acesso | 0 | — | — | — |
| lblNroDiasGeracaoAcesso | TLabel | rótulo | Quantidade padrão de dias a gerar acesso: | — | — | — | — |
| prmNroDiasGeracaoAcesso | TSpinEdit | campo de texto/data | — | 0 | — | 2 | — |
| tsImportacaoApi | TTabSheet | contêiner | Importação API | — | — | — | — |
| GroupBox1 | TGroupBox | contêiner |  Afastamentos  | 0 | — | — | — |
| Label1 | TLabel | rótulo | Quantidade de anos a considerar | — | — | — | — |
| prmQuantidadeAnosConsiderar | TSpinEdit | campo de texto/data | — | 0 | — | 2 | — |
| ActionList1 | TActionList | outro | — | — | — | — | — |
| actSalvar | TAction | ação | Salvar (Ctrl+S) | — | — | — | — |
| actFechar | TAction | ação | Fechar (Ctrl+F4) | — | — | — | — |
| DefaultIcons | TImageList | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `FormCreate` | 280 | — |
| `SalvarTodosParametros` | 478 | — |
| `SalvarParametro` | 527 | `FController.GravarParametro` |
| `actSalvarExecute` | 776 | — |
| `SalvarDestinatarios` | 887 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 780: `Parâmetros do sistema salvos com sucesso! ✅`
- Linha 785: `Erro ao salvar parâmetros: `
- Linha 818: `Configure o e-mail remetente antes de testar.`
- Linha 858: `E-mail de teste enviado com sucesso para: `
- Linha 862: `Falha ao enviar e-mail de teste:`

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
