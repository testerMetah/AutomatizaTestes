# Mapa do sistema Acessus

> **Ressalva de versão:** o código disponível no GitHub pode estar desatualizado em relação ao Acessus instalado para teste. Alterações recentes dos desenvolvedores nem sempre são enviadas ao repositório. As telas, regras e mensagens extraídas desta cópia do código precisam ser confrontadas com o briefing da mudança e com a aplicação em execução antes de servirem como resultado esperado de um teste.

## Fonte consultada

- Repositório: `https://github.com/Metah-Equipamentos/Acessus.git`
- Cópia local, somente leitura: `C:\Acessus-Fonte`
- Branch principal: `main`
- Último commit: `28074ddf2c3ecae913fd082d453027f148dc50c6`
- Data do commit: 28/10/2026, 16:29:02 (UTC−03:00)
- Autor: MetahDev02 <dev02@metahequipamentos.com.br>
- Arquivos versionados: 704 `.pas` e 312 `.dfm`

## Menus e telas

Extração estática das `TActionManager` dos formulários principais. A presença real de cada item depende das permissões do usuário e do build instalado. `?` indica vínculo não resolvido automaticamente. O caminho da unit é relativo a `C:\Acessus-Fonte`.

| Módulo | Menu > submenu > item | Form aberto | Unit `.pas` / `.dfm` |
|---|---|---|---|
| Acesso | Cadastros > Empresa... | `TFrmCadEmpresas` | `Acesso/uFrmCadEmpresas.pas` / `Acesso/uFrmCadEmpresas.dfm` |
| Acesso | Cadastros > Unidades... | `TFrmCadUnidades` | `Acesso/UFrmCadUnidades.pas` / `Acesso/UFrmCadUnidades.dfm` |
| Acesso | Cadastros > Setores... | `TFrmCadSetores` | `Acesso/UFrmCadSetores.pas` / `Acesso/UFrmCadSetores.dfm` |
| Acesso | Cadastros > Pessoas... | `TFrmCadPessoas` | `Acesso/UFrmCadPessoas.pas` / `Acesso/UFrmCadPessoas.dfm` |
| Acesso | Cadastros > Pré-Cadastros > Pré-Cadastros | `TFrmCadPreCadastro` | `Acesso/UFrmCadPreCadastro.pas` / `Acesso/UFrmCadPreCadastro.dfm` |
| Acesso | Cadastros > Pré-Cadastros > Empresas Acesso | `TFrmCadEmpresaAcesso` | `Acesso/UFrmCadEmpresaAcesso.pas` / `Acesso/UFrmCadEmpresaAcesso.dfm` |
| Acesso | Cadastros > Filtros... | `TFrmCadFiltros` | `Acesso/UFrmCadFiltros.pas` / `Acesso/UFrmCadFiltros.dfm` |
| Acesso | Cadastros > Digitais e Faces... | `TFrmCadDigitaisFaces` | `Acesso/uFrmCadDigitaisFaces.pas` / `Acesso/uFrmCadDigitaisFaces.dfm` |
| Acesso | Cadastros > Coletores > Modelos de Coletores... | `TFrmCadModeloColetores` | `Acesso/uFrmCadModeloColetores.pas` / `Acesso/uFrmCadModeloColetores.dfm` |
| Acesso | Cadastros > Coletores > Cadastro de Coletores... | `TFrmCadColetores` | `Acesso/uFrmCadColetores.pas` / `Acesso/uFrmCadColetores.dfm` |
| Acesso | Cadastros > Coletores > Mensagens dos Coletores... | `TFrmMensagemColetores` | `Acesso/uFrmCadMensagemColetores.pas` / `Acesso/uFrmCadMensagemColetores.dfm` |
| Acesso | Acesso > Crachás > Registro de Crachás... | `TFrmRegCrachas` | `Acesso/UFrmRegCrachas.pas` / `Acesso/UFrmRegCrachas.dfm` |
| Acesso | Acesso > Regras de Acesso... | `TFRegrasAcesso` | `Acesso/UFrmRegrasAcesso.pas` / `Acesso/UFrmRegrasAcesso.dfm` |
| Acesso | Acesso > Afastamentos Cedidos... | `TFrmAfastamentos` | `Acesso/UFrmAfastamentos.pas` / `Acesso/UFrmAfastamentos.dfm` |
| Acesso | Acesso > Gerar Acesso... | `TFGerarAcesso` | `Acesso/UGerarAcesso.pas` / `Acesso/UGerarAcesso.dfm` |
| Acesso | Acesso > Acesso Rápido... > Gerar Acesso Rápido... | `TFGerAcessoRapido` | `Acesso/UGerAcessoRapido.pas` / `Acesso/UGerAcessoRapido.dfm` |
| Acesso | Acesso > Acesso Rápido... > Excluir Acesso Rápido... | `TFExcluirAcessoRapido` | `Acesso/uFExcluirAcessoRapido.pas` / `Acesso/uFExcluirAcessoRapido.dfm` |
| Acesso | Acesso > Autorização de Acessos... | `TFrmAcessosAutorizados` | `Acesso/UFrmAcessosAutorizados.pas` / `Acesso/UFrmAcessosAutorizados.dfm` |
| Acesso | Acesso > Programação de Regras de Acesso... | `TFrmProgramacaoRegrasAcesso` | `Acesso/UFrmProgramacaoRegrasAcesso.pas` / `Acesso/UFrmProgramacaoRegrasAcesso.dfm` |
| Acesso | Consultas > Marcações Online... | `TFMarcacoesOnline` | `Acesso/UMarcacoesOnline.pas` / `Acesso/UMarcacoesOnline.dfm` |
| Acesso | Consultas > Acesso por Pessoa... | `TFAcessoPorPessoa` | `Acesso/UAcessoPorPessoa.pas` / `Acesso/UAcessoPorPessoa.dfm` |
| Acesso | Consultas > Auditorias/Históricos... | `TFrmAuditoriaHistorico` | `Acesso/UFrmAuditoriaHistorico.pas` / `Acesso/UFrmAuditoriaHistorico.dfm` |
| Acesso | Comunicação > Comandos com Equipamentos... | `TFrmComunicacaoEquipamentos` | `Acesso/uFrmComunicacaoEquipamentos.pas` / `Acesso/uFrmComunicacaoEquipamentos.dfm` |
| Acesso | Ferramentas > Importador Metadados... | `TFImportadorExportadorMetadados` | `Acesso/UImportadorExportadorMetadados.pas` / `Acesso/UImportadorExportadorMetadados.dfm` |
| Acesso | Ferramentas > Exportador Metadados... | `TFExportadorMetadados` | `Acesso/UExportadorMetadados.pas` / `Acesso/UExportadorMetadados.dfm` |
| Acesso | Ferramentas > Layout Exportação Marcações | `TFrmLayoutExportacao` | `Acesso/UFrmLayoutExportacao.pas` / `Acesso/UFrmLayoutExportacao.dfm` |
| Acesso | Ferramentas > Exportação Marcações CSV/TXT | `TFrmExportacaoMarcacoes` | `Acesso/UFrmExportacaoMarcacoes.pas` / `Acesso/UFrmExportacaoMarcacoes.dfm` |
| Acesso | Ferramentas > Importardor CSV | `TFrmImportadorCSV` | `Acesso/uFrmImportadorCSV.pas` / `Acesso/uFrmImportadorCSV.dfm` |
| Acesso | Relatórios > Acesso Outros > Crachás... | `TFrmRelCracha` | `Acesso/UFrmRelCracha.pas` / `Acesso/UFrmRelCracha.dfm` |
| Acesso | Relatórios > Acesso Outros > Presença... | `TFrmRelPresenca` | `Acesso/UFrmRelPresenca.pas` / `Acesso/UFrmRelPresenca.dfm` |
| Acesso | Relatórios > Operacional > Pessoas... | `TFrmRelPessoas` | `Acesso/UFrmRelPessoas.pas` / `Acesso/UFrmRelPessoas.dfm` |
| Acesso | Relatórios > Operacional > Setor... | `TFrmRelSetor` | `Acesso/UFrmRelSetor.pas` / `Acesso/UFrmRelSetor.dfm` |
| Acesso | Relatórios > Operacional > Unidade... | `TFrmRelUnidade` | `Acesso/UFrmRelUnidade.pas` / `Acesso/UFrmRelUnidade.dfm` |
| Acesso | Relatórios > Operacional > Empresa... | `TFrmRelEmpresas` | `Acesso/UFrmRelEmpresas.pas` / `Acesso/UFrmRelEmpresas.dfm` |
| Acesso | Relatórios > Operacional > Pré-cadastro... | `TFrmRelPreCadastro` | `Acesso/UFrmRelPreCadastro.pas` / `Acesso/UFrmRelPreCadastro.dfm` |
| Acesso | Relatórios > Operacional > Digitais e Faces... | `TFrmRelDigitaisFaces` | `Acesso/UFrmRelDigitaisFaces.pas` / `Acesso/UFrmRelDigitaisFaces.dfm` |
| Acesso | Relatórios > Reservas e Consumos... | `TFrmRelResCon` | `Acesso/UFrmRelResCon.pas` / `Acesso/UFrmRelResCon.dfm` |
| Acesso | Relatórios > Marcações Online... | `TFrmRelMarcacoesOnline` | `Acesso/UFrmRelMarcacoesOnline.pas` / `Acesso/UFrmRelMarcacoesOnline.dfm` |
| Acesso | Relatórios > Acesso de Visitantes e Terceiros... | `TFrmRelAcessoVisitantesTerceiros` | `Acesso/UFrmRelAcessoVisitantesTerceiros.pas` / `Acesso/UFrmRelAcessoVisitantesTerceiros.dfm` |
| Acesso | Relatórios > Avaliação de Refeições | `TFrmRelAvaliacaoRefeicao` | `Acesso/UFrmRelAvaliacaoRefeicao.pas` / `Acesso/UFrmRelAvaliacaoRefeicao.dfm` |
| Acesso | Relatórios > Histórico Acesso Rapido... | `TFrmRelHistoricoAcessoRapido` | `Acesso/UFrmRelHistoricoAcessoRapido.pas` / `Acesso/UFrmRelHistoricoAcessoRapido.dfm` |
| Acesso | Ajuda > Sobre... | `TFrmSobre` | ? |
| Acesso | Ajuda > Sair | `—` | `Acesso/uFrmPrincipal.pas` |
| Administracao | Cadastros > Usuários | `TFrmAdministracaoViewsCadUsuarios` | `Administracao/Views/Acessus.Administracao.Views.CadUsuarios.pas` / `Administracao/Views/Acessus.Administracao.Views.CadUsuarios.dfm` |
| Administracao | Opções do Sistema | `TFrmAdministracaoViewsOpcoesSistema` | `Administracao/Views/Acessus.Administracao.Views.OpcoesSistema.pas` / `Administracao/Views/Acessus.Administracao.Views.OpcoesSistema.dfm` |
| Administracao | Parâmetros > Parâmetros do Sistema | `TFrmAdministracaoViewsParametrosSistema` | `Administracao/Views/Acessus.Administracao.Views.ParametrosSistema.pas` / `Administracao/Views/Acessus.Administracao.Views.ParametrosSistema.dfm` |
| Administracao | Consultas >  | `TFrmAuditoriaHistoricoAdministracao` | `Acesso/UFrmAuditoriaHistoricoAdministracao.pas` / `Acesso/UFrmAuditoriaHistoricoAdministracao.dfm` |
| Escola | Cadastros > Alunos... | `TFrmEscolaCadAlunos` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Alunos.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Alunos.dfm` |
| Escola | Cadastros > Responsáveis... | `TFrmEscolaCadResponsaveis` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Responsaveis.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Responsaveis.dfm` |
| Escola | Cadastros > Funcionários... | `TFrmEscolaCadFuncionario` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Funcionarios.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Funcionarios.dfm` |
| Escola | Cadastros > Turmas... | `TFrmEscolaCadTurmas` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turmas.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turmas.dfm` |
| Escola | Cadastros > Turnos... | `TFrmEscolaCadTurnos` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turnos.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Turnos.dfm` |
| Escola | Cadastros > Digitais e Faces... | `TFrmCadDigitaisFaces` | `Acesso/uFrmCadDigitaisFaces.pas` / `Acesso/uFrmCadDigitaisFaces.dfm` |
| Escola | Cadastros > Desativações|Ativações... | `TFrmEscolaCadDesativacoes` | `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Desativacoes.pas` / `Escola/Views/Cadastros/Acessus.Escola.Views.Cadastros.Desativacoes.dfm` |
| Escola | Cadastros > Coletores > Coletores... | `TFrmCadColetores` | `Acesso/uFrmCadColetores.pas` / `Acesso/uFrmCadColetores.dfm` |
| Escola | Cadastros > Coletores > Modelos de Coletores... | `TFrmCadModeloColetores` | `Acesso/uFrmCadModeloColetores.pas` / `Acesso/uFrmCadModeloColetores.dfm` |
| Escola | Cadastros > Coletores > Mensagens dos Coletores... | `TFrmMensagemColetores` | `Acesso/uFrmCadMensagemColetores.pas` / `Acesso/uFrmCadMensagemColetores.dfm` |
| Escola | Acesso > Registros de Crachás... | `TFrmRegCrachas` | `Acesso/UFrmRegCrachas.pas` / `Acesso/UFrmRegCrachas.dfm` |
| Escola | Acesso > Regras de Acesso... | `TFRegrasAcesso` | `Acesso/UFrmRegrasAcesso.pas` / `Acesso/UFrmRegrasAcesso.dfm` |
| Escola | Acesso > Gerar Acesso... | `TFGerarAcesso` | `Acesso/UGerarAcesso.pas` / `Acesso/UGerarAcesso.dfm` |
| Escola | Consultas > Marcações Online... | `TFMarcacoesOnline` | `Acesso/UMarcacoesOnline.pas` / `Acesso/UMarcacoesOnline.dfm` |
| Escola | Consultas > Acesso por Pessoa... | `TFAcessoPorPessoa` | `Acesso/UAcessoPorPessoa.pas` / `Acesso/UAcessoPorPessoa.dfm` |
| Escola | Consultas > Auditorias/Históricos... | `TFrmAuditoriaHistoricoEscola` | `Acesso/UFrmAuditoriaHistoricoEscola.pas` / `Acesso/UFrmAuditoriaHistoricoEscola.dfm` |
| Escola | Comunicação > Comunicação com Equipamentos... | `TFrmComunicacaoEquipamentos` | `Acesso/uFrmComunicacaoEquipamentos.pas` / `Acesso/uFrmComunicacaoEquipamentos.dfm` |
| Escola | Ferramentas > Migração... | `TfrmMigracaoDados` | `Escola/Views/Migracao/MigracaoDados.pas` / `Escola/Views/Migracao/MigracaoDados.dfm` |
| Escola | Relatórios > Operacional > Relatório de Alunos | `TFrmEscolaRelAlunos` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Alunos.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Alunos.dfm` |
| Escola | Relatórios > Operacional > Relatório de Digitais e Faces | `TFrmEscolaRelDigitaisFaces` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.DigitaisFaces.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.DigitaisFaces.dfm` |
| Escola | Relatórios > Operacional > Relatório de Funcionários | `TFrmEscolaRelFuncionarios` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Funcionarios.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Funcionarios.dfm` |
| Escola | Relatórios > Operacional > Relatório de Responsáveis | `TFrmEscolaRelResponsaveis` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Responsaveis.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Responsaveis.dfm` |
| Escola | Relatórios > Relatório de Crachás | `TFrmEscolaRelCrachas` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Crachas.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Crachas.dfm` |
| Escola | Relatórios > Relatório de Inconsistências | `TFrmEscolaRelInconsistencias` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Inconsistencias.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Inconsistencias.dfm` |
| Escola | Relatórios > Relatório de Marcações Online | `TFrmEscolaRelMarcacoesOnline` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.MarcacoesOnline.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.MarcacoesOnline.dfm` |
| Escola | Relatórios > Relatório de Presenças | `TFrmEscolaRelPresencas` | `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Presencas.pas` / `Escola/Views/Relatorios/Acessus.Escola.Views.Relatorios.Presencas.dfm` |
| Escola | Ajuda > Sobre... | `TFrmSobre` | ? |
| Estacionamento | Cadastros > Pessoas > Pessoas | `TFrmCadPessoas` | `Acesso/UFrmCadPessoas.pas` / `Acesso/UFrmCadPessoas.dfm` |
| Estacionamento | Cadastros > Pessoas > Pré-Cadastros | `TFrmCadPreCadastro` | `Acesso/UFrmCadPreCadastro.pas` / `Acesso/UFrmCadPreCadastro.dfm` |
| Estacionamento | Cadastros > Estacionamento | `TFrmEstacionamentoViewsCadastro` | `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.pas` / `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.dfm` |
| Estacionamento | Cadastros > Ocorrências | `TFrmEstacionamentoViewsCadastroOcorrencias` | `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Ocorrencias.pas` / `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Ocorrencias.dfm` |
| Estacionamento | Cadastros > Veículos | `TFrmEstacionamentoViewsCadastroVeiculos` | `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Veiculos.pas` / `Estacionamento/Views/Cadastro/Acessus.Estacionamento.Views.Cadastro.Veiculos.dfm` |
| Estacionamento | Cadastros > Coletores > Modelos | `TFrmCadModeloColetores` | `Acesso/uFrmCadModeloColetores.pas` / `Acesso/uFrmCadModeloColetores.dfm` |
| Estacionamento | Cadastros > Coletores > Cadastro | `TFrmCadColetores` | `Acesso/uFrmCadColetores.pas` / `Acesso/uFrmCadColetores.dfm` |
| Estacionamento | Acesso > Registro de Tags | `TFrmRegCrachas` | `Acesso/UFrmRegCrachas.pas` / `Acesso/UFrmRegCrachas.dfm` |
| Estacionamento | Acesso > Regras de Acesso | `TFRegrasAcesso` | `Acesso/UFrmRegrasAcesso.pas` / `Acesso/UFrmRegrasAcesso.dfm` |
| Estacionamento | Acesso > Gerar Acesso | `TFGerarAcesso` | `Acesso/UGerarAcesso.pas` / `Acesso/UGerarAcesso.dfm` |
| Estacionamento | Comunicação com Equipamentos > Comunicação com Antenas | `TFrmEstacionamentoViewsComunicacaoAntenas` | `Estacionamento/Views/ComunicacaoComEquipamentos/Acessus.Estacionamento.Views.ComunicacaoAntenas.pas` / `Estacionamento/Views/ComunicacaoComEquipamentos/Acessus.Estacionamento.Views.ComunicacaoAntenas.dfm` |
| Estacionamento | Monitoramento > Marcações Online | `TFMarcacoesOnline` | `Acesso/UMarcacoesOnline.pas` / `Acesso/UMarcacoesOnline.dfm` |
| Estacionamento | Monitoramento > Veículos no Estacionamento | `TFrmEstacionamentoViewsMonitoramentoSituacaoVeiculo` | `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.Situacao.pas` / `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.Situacao.dfm` |
| Estacionamento | Monitoramento > Gráfico do Estacionamento | `TFrmEstacionamentoViewsMonitoramentoGraficoOcupacaoVagas` | `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.GraficoOcupacaoVagas.pas` / `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.GraficoOcupacaoVagas.dfm` |
| Estacionamento | Monitoramento > Ocorrências do Veículos | `TFrmEstacionamentoViewsMonitoramentoVeiculosOcorrencias` | `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.VeiculosOcorrencias.pas` / `Estacionamento/Views/Monitoramento/Acessus.Estacionamento.Views.Monitoramento.VeiculosOcorrencias.dfm` |
| Estacionamento | Relatórios > Ocorrências do Veículos | `TFrmEstacionamentoViewsRelatorioOcorrencia` | `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.Ocorrencias.pas` / `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.Ocorrencias.dfm` |
| Estacionamento | Relatórios > Acessos de Veículos | `TFrmEstacionamentoViewsMonitoramentoVeiculosAcessos` | `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.VeiculosAcessos.pas` / `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.VeiculosAcessos.dfm` |
| Estacionamento | Relatórios > Colaborador Vinculado Estacionamento | `TFrmEstacionamentoViewsMonitoramentoColaboradorVinculado` | `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.ColaboradorVinculado.pas` / `Estacionamento/Views/Relatorio/Acessus.Estacionamento.Views.Relatorio.ColaboradorVinculado.dfm` |
| Estacionamento | Consultas >  | `TFrmAuditoriaHistoricoEstacionamento` | `Acesso/UFrmAuditoriaHistoricoEstacionamento.pas` / `Acesso/UFrmAuditoriaHistoricoEstacionamento.dfm` |
| Estacionamento | Ajuda > Sobre... | `TFrmSobre` | ? |
| Estacionamento | Ajuda > Sair | `—` | `Estacionamento/Views/Acessus.Estacionamento.Views.Principal.pas` |
| Modulo | Modulos > Acesso | `Executa Acessus.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Refeitório | `Executa Acessus.Refeitorio.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Portaria | `Executa Acessus.Portaria.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Estacionamento | `Executa Acessus.Estacionamento.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Escola | `Executa Acessus.Escola.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Administração | `Executa Acessus.Administracao.exe` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > LogOff | `—` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Modulos > Sair | `—` | `Modulo/Views/Acessus.Modulo.Views.Principal.pas` |
| Modulo | Ajuda > Novidades | `TFrmModuloViewsNovidades` | `Modulo/Views/Acessus.Modulo.Views.Novidades.pas` / `Modulo/Views/Acessus.Modulo.Views.Novidades.dfm` |
| Portaria | Visita Rápida | `TFrmPortariaViewsVisitaRapida` | `Portaria/Views/Acessus.Portaria.Views.VisitaRapida.pas` / `Portaria/Views/Acessus.Portaria.Views.VisitaRapida.dfm` |
| Portaria | Cadastro > Empresa de Acesso... | `TFrmCadEmpresaAcesso` | `Acesso/UFrmCadEmpresaAcesso.pas` / `Acesso/UFrmCadEmpresaAcesso.dfm` |
| Portaria | Cadastro > Visitantes e Terceiros... | `TFrmCadVisitantesTerceirosDois, TFrmCadVisitantesTerceiros` | `Acesso/UFrmCadVisitantesTerceirosDois.pas` / `Acesso/UFrmCadVisitantesTerceirosDois.dfm`, `Acesso/UFrmCadVisitantesTerceiros.pas` / `Acesso/UFrmCadVisitantesTerceiros.dfm` |
| Portaria | Consultas > Marcações OnLine... | `TFMarcacoesOnline` | `Acesso/UMarcacoesOnline.pas` / `Acesso/UMarcacoesOnline.dfm` |
| Portaria | Consultas > Auditorias/Históricos... | `TFrmAuditoriaHistoricoPortaria` | `Acesso/UFrmAuditoriaHistoricoPortaria.pas` / `Acesso/UFrmAuditoriaHistoricoPortaria.dfm` |
| Portaria | Ferramentas > Etiqueta | `TFrmConfigEtiqueta` | `Acesso/UFrmConfigEtiqueta.pas` / `Acesso/UFrmConfigEtiqueta.dfm` |
| Portaria | Ferramentas > Importação | `TFrmPortariaViewsImportacao` | `Portaria/Views/Acessus.Portaria.Views.Importacao.pas` / `Portaria/Views/Acessus.Portaria.Views.Importacao.dfm` |
| Portaria | Ferramentas > Importação CSV | `TFrmImportadorCSV` | `Acesso/uFrmImportadorCSV.pas` / `Acesso/uFrmImportadorCSV.dfm` |
| Portaria | Relatórios > Digitais e Faces... | `TFrmRelDigitaisFaces` | `Acesso/UFrmRelDigitaisFaces.pas` / `Acesso/UFrmRelDigitaisFaces.dfm` |
| Portaria | Relatórios > Visitantes e Terceiros... | `TFrmRelVisitantesTerceiros` | `Acesso/UFrmRelVisitantesTerceiros.pas` / `Acesso/UFrmRelVisitantesTerceiros.dfm` |
| Portaria | Relatórios > Acesso de Visitantes e Terceiros... | `TFrmRelAcessoVisitantesTerceiros` | `Acesso/UFrmRelAcessoVisitantesTerceiros.pas` / `Acesso/UFrmRelAcessoVisitantesTerceiros.dfm` |
| Portaria | Relatórios > Reservas e Consumos... | `TFrmRelResCon` | `Acesso/UFrmRelResCon.pas` / `Acesso/UFrmRelResCon.dfm` |
| Portaria | Ajuda > Sobre... | `—` | `Portaria/Views/Acessus.Portaria.Views.Principal.pas` |
| Portaria | Ajuda > Sair | `—` | `Portaria/Views/Acessus.Portaria.Views.Principal.pas` |
| Refeitorio | Cadastro > Modelo de Coletores... | `TFrmCadModeloColetores` | `Acesso/uFrmCadModeloColetores.pas` / `Acesso/uFrmCadModeloColetores.dfm` |
| Refeitorio | Cadastro > Coletores | `TFrmCadColetores` | `Acesso/uFrmCadColetores.pas` / `Acesso/uFrmCadColetores.dfm` |
| Refeitorio | Acesso > Regras de Acesso... | `TFRegrasAcesso` | `Acesso/UFrmRegrasAcesso.pas` / `Acesso/UFrmRegrasAcesso.dfm` |
| Refeitorio | Acesso > Gerar Acesso... | `TFGerarAcesso` | `Acesso/UGerarAcesso.pas` / `Acesso/UGerarAcesso.dfm` |
| Refeitorio | Consultas > Marcações Online... | `TFMarcacoesOnline` | `Acesso/UMarcacoesOnline.pas` / `Acesso/UMarcacoesOnline.dfm` |
| Refeitorio | Consultas > Acesso Por Pessoa... | `TFAcessoPorPessoa` | `Acesso/UAcessoPorPessoa.pas` / `Acesso/UAcessoPorPessoa.dfm` |
| Refeitorio | Consultas > Auditorias/Históricos... | `TFrmAuditoriaHistoricoRefeitorio` | `Acesso/UFrmAuditoriaHistoricoRefeitorio.pas` / `Acesso/UFrmAuditoriaHistoricoRefeitorio.dfm` |
| Refeitorio | Refeitório > Importar Refeições | `TFrmGerarRefeicao` | `Refeitorio/Views/Acessus.Refeitorio.Views.UFrmImportarRefeicao.pas` / `Refeitorio/Views/Acessus.Refeitorio.Views.UFrmImportarRefeicao.dfm` |
| Refeitorio | Refeitório > Cadastro... | `TFrmCadRefeitorios` | `Acesso/uFrmCadRefeitorio.pas` / `Acesso/uFrmCadRefeitorio.dfm` |
| Refeitorio | Refeitório > Incluir Refeições... | `TFrmRefeicoes` | `Acesso/UFrmCadRefeicoes.pas` / `Acesso/UFrmCadRefeicoes.dfm` |
| Refeitorio | Refeitório > Cardapios... | `TFrmCadCardapio` | `Acesso/uFrmCadCardapio.pas` / `Acesso/uFrmCadCardapio.dfm` |
| Refeitorio | Refeitório > Créditos... | `TFrmRelCreditos` | `Acesso/UFrmRelCreditos.pas` / `Acesso/UFrmRelCreditos.dfm` |
| Refeitorio | Comunicação > Comandos Por Equipamentos... | `TFrmComunicacaoEquipamentos` | `Acesso/uFrmComunicacaoEquipamentos.pas` / `Acesso/uFrmComunicacaoEquipamentos.dfm` |
| Refeitorio | Reservas > Refeições | `TFrmRefeitorioViewsReservasRefeicoes` | `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.pas` / `Refeitorio/Views/Acessus.Refeitorio.Views.ReservasRefeicoes.dfm` |
| Refeitorio | Relatórios > Operacional > Pessoas... | `TFrmRelPessoas` | `Acesso/UFrmRelPessoas.pas` / `Acesso/UFrmRelPessoas.dfm` |
| Refeitorio | Relatórios > Reservas e Consumos... | `TFrmRelResCon` | `Acesso/UFrmRelResCon.pas` / `Acesso/UFrmRelResCon.dfm` |
| Refeitorio | Relatórios > Créditos... | `TFrmRelCreditos` | `Acesso/UFrmRelCreditos.pas` / `Acesso/UFrmRelCreditos.dfm` |
| Refeitorio | Relatórios > Marcações OnLine... | `TFrmRelMarcacoesOnline` | `Acesso/UFrmRelMarcacoesOnline.pas` / `Acesso/UFrmRelMarcacoesOnline.dfm` |
| Refeitorio | Relatórios > Reservas de Refeições... | `TFrmRelReservasRefeicoes` | `Acesso/UFrmRelReservasRefeicoes.pas` / `Acesso/UFrmRelReservasRefeicoes.dfm` |
| Refeitorio | Relatórios > Refeições Total | `TFrmRelRefeicoesTotal` | `Acesso/UFrmRelRefeicoesTotal.pas` / `Acesso/UFrmRelRefeicoesTotal.dfm` |
| Refeitorio | Ajuda > Sobre | `TFrmSobre` | ? |
| Refeitorio | Ajuda > Sair | `—` | `Refeitorio/Views/Acessus.Refeitorio.Views.Principal.pas` |

**Total:** 140 itens acionáveis nos `TActionManager` de 7 módulos; 90 classes de tela distintas identificadas por `TelaShow` ou criação modal. O módulo Trabalho usa navegação customizada e não entra nessas contagens.

## Vínculos pendentes de inspeção

- **Acesso > Ajuda > Sobre...**: ação `acAjudaSobre`, handler `acAjudaSobreExecute`; vínculo com form/arquivo não resolvido por `TelaShow`.
- **Escola > Ajuda > Sobre...**: ação `actSobre`, handler `actSobreExecute`; vínculo com form/arquivo não resolvido por `TelaShow`.
- **Estacionamento > Ajuda > Sobre...**: ação `acAjuSobre`, handler `acAjuSobreExecute`; vínculo com form/arquivo não resolvido por `TelaShow`.
- **Refeitorio > Ajuda > Sobre**: ação `acAjuSobre`, handler `acAjuSobreExecute`; vínculo com form/arquivo não resolvido por `TelaShow`.

## Limites da extração

- O formulário principal de `Trabalho` não contém `TActionManager`; seus comandos exigem inspeção específica.

## Navegação customizada de Trabalho

`TFrmTrabalhoViewsPrincipal` não usa a árvore `TActionManager` dos demais módulos; oito `TSpeedButton` na lateral chamam procedures diretamente em `Trabalho/Views/Acessus.Trabalho.Views.Principal.pas`:

| Botão/ação | Destino | Unit `.pas/.dfm` |
|---|---|---|
| Painel de Controle / `actPainelDeControleExecute` | Aba `TabPainel` no próprio form | `Trabalho/Views/Acessus.Trabalho.Views.Principal` |
| Cadastro / `actCadastroExecute` | Aba `TabCadastro`; seleciona `TabGridTiposDeEPIs` | mesma unit |
| Controle de EPIs / `actControleDeEPIsExecute` | Aba `TabControleDeEPIs` | mesma unit |
| Acesso / `actAcessoExecute` | Form `TFGerarAcesso`, esconde `PgRight` | `Acesso/UGerarAcesso.pas/.dfm` |
| Segurança e Saúde / `actSegurancaESaudeExecute` | Aba `TabSegurancaESaude` | mesma unit |
| Documentos Fiscais / `actDocumentosFiscaisExecute` | Aba `TabDocumentosFiscais` | mesma unit |
| Contratos Sociais / `actContratosSociaisExecute` | Aba `TabContratosSociais` | mesma unit |
| Sobre / `actSobreExecute` | Aba `TabSobre` | mesma unit |

O DFM declara grades e botões de cadastro de EPIs dentro do próprio form. Nesta cópia, os botões internos não têm `OnClick` ou `Action` no DFM; a implementação funcional deve ser conferida no build instalado. `FormCreate` esconde as abas para navegação pela lateral.
