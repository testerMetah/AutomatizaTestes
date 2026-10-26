# Atualização do Acessus e do banco de destino

## Resultado de 21/10/2026 — versão 2.11.1

Release 2.11.1 copiada do Dexter para `C:\acesso`: 653 arquivos conferidos por
SHA-256, sem divergências. Backup SQL de `desk-tec/novo123` verificado antes da
cópia; 652 arquivos locais anteriores preservados. O Atualizador exibiu conclusão,
e a tabela `VERSOES` do banco `novo123` registra 2.11.1.0. O serviço de importação
foi restaurado para `Running`. Evidências em
`reports/atualizacao/20261021-2111/LEIA-ME.md`. Testes de negócio ainda não foram
revalidados na nova versão. A credencial Dexter está no Gerenciador de Credenciais
do Windows, sem senha registrada neste projeto.

## Confer?ncia posterior ao login ? 20/10/2026

Seis m?dulos abertos na 2.11.0. As 20 rotas antes pendentes/falhas de Acesso foram inspecionadas. Nove inclus?es vazias de coletores/regras/programa??o foram capturadas e canceladas. Administra??o: incluir usu?rio provoca Access violation 015C537D / leitura 000001E4; aviso fechado e inclus?o cancelada. Op??es do Sistema permanece ausente. Refeit?rio: Importar Reservas bloqueado por falta de conex?o SIRH cadastrada; di?logo de configura??o n?o abre. Servi?o Running, mas log atual mostra erro de conex?o 12029 ao obter token. API 192.168.50.105 n?o responde em 443/80; confirma??o de endere?o para RHFagundes solicitada. Baseline destino: zero reservas e zero refeit?rios, 10 pessoas. Nenhuma grava??o de neg?cio pela inspe??o. 176 testes unit?rios passaram ap?s ajustes de captura. Mapas: docs/mapeamentos/vm-211-20261020/LEIA-ME.md. Esta sess?o inspecionou 31 rotas e registrou 3 bloqueios/indisponibilidades; n?o revalidou as 90 rotas restantes j? inspecionadas ou inventariadas na 2.10. Fluxos de neg?cio permanecem pendentes de infraestrutura, dados e expectativas confirmados.


## Resultado de 20/10/2026

Atualiza??o conclu?da em C:\acesso, vers?o 2.11.0.0. Atualizador conclu?do em desk-tec/novo123. 661 arquivos conferidos por hash, zero diverg?ncias. Servi?o de importa??o restaurado para Running. 176 testes unit?rios passaram. Confer?ncia real das telas aguarda login no painel; documenta??o e evid?ncias em reports/atualizacao/20261020-211-preparacao/LEIA-ME.md. As se??es de descoberta abaixo s?o hist?ricas.

## Autorizacao de 20/10/2026

Usuario autorizou atualizar agora para 2.11.0, copiando todos os arquivos da release do Dexter para C:\acesso e executando o Atualizador. Depois, conferir todas as pendencias. Copiar preservando a release original no servidor.

Sempre executar o Atualizador ao mudar o banco do Acessus, mesmo sem mudar a versao. Destino confirmado nesta preparacao: desk-tec/novo123; origem RHFagundes nao e destino da migracao.

Backup COPY_ONLY/CHECKSUM de novo123 criado em E:\SQL Server\Backup\novo123_pre_211_20261020.bak e RESTORE VERIFYONLY aprovado. Evidencia: reports/atualizacao/20261020-211-preparacao/backup-banco.json.

Estado abaixo e historico; a conclusao da atualizacao exige nova evidencia. Credenciais de rede nao devem ser registradas.

## Regra informada pelo usuário em 19/10/2026

Depois de atualizar os executáveis do Acessus, é obrigatório executar o
**Atualizador no banco do Acessus que será usado nos testes**. Ao trocar esse
banco, executar o Atualizador novamente no novo destino. Selecionar um perfil
na Central ou validar a conexão SQL não substitui esse procedimento.

## Release informada

`\\dexter\Arquivos\Sistemas\Acessus Release\Versões\v2.0\2.11.0`

A instalação em uso foi observada como **2.10.0**. A release 2.11.0 ainda não
foi inspecionada nem instalada. Dexter resolve nesta VM para 192.168.50.220;
porta SMB 445 acessível. A tentativa de listar o compartilhamento retornou
**WinError 1326** (falha de autenticação); `net view` retornou acesso negado.
O Explorador foi aberto em `\\dexter\Arquivos` para autenticação pelo Windows,
sem reutilizar credenciais do RH/Acessus ou registrar senhas nos documentos.

Foi perguntado ao usuário se prefere atualizar agora e mapear a 2.11.0, ou
concluir primeiro o inventário da 2.10.0. A escolha ainda está pendente.

## Procedimento a executar após liberar a release e definir a sequência

1. Conferir o conteúdo da release, versão dos executáveis e instruções do
   fornecedor. Comparar com a instalação; não presumir formato do pacote.
2. Confirmar servidor/base de destino do Acessus. O destino usado até aqui
   é **desk-tec / novo123**. RHFagundes é a origem RH, não o banco a migrar
   com o Atualizador do Acessus.
3. Preparar recuperação dos executáveis e configurações locais e do banco
   de destino antes da migração. Não publicar arquivos com credenciais nem
   sobrescrever .env, perfis ou arquivos de conexão por cópias da release.
4. Encerrar módulos antes da substituição e conferir o serviço de importação.
   O serviço instalado nesta VM estava parado; não iniciar importação de uma
   API cuja origem ainda não foi confirmada.
5. Aplicar a release conforme o pacote real e rodar seu Atualizador no destino
   confirmado. Registrar versão, servidor, banco, data/hora e resultado real,
   incluindo evidência de conclusão ou falha. Não marcar executado sem evidência.
6. Conferir novamente estrutura SQL, abertura dos módulos e rotas relevantes.
   A inspeção da 2.10.0 permanece histórica; não vale automaticamente para 2.11.0.
7. Ao mudar de banco do Acessus, repetir o Atualizador nessa base e registrar
   nova evidência antes de realizar os testes de negócio.

Não houve atualização de executáveis, execução do Atualizador ou migração de
banco nesta etapa de descoberta da release.
