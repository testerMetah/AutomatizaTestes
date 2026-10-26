# Acesso necessário para testar RH → Acessus

Diagnóstico em 15/10/2026, nesta sessão. Nenhum cadastro foi feito.

## Resultado técnico

- Python e bibliotecas de automação estão disponíveis. O Python configurado na
  .venv não é executável nesta sessão; o diagnóstico consegue usar o Python já
  instalado em C:\Python314 com os pacotes locais, sem reinstalação.
- O processo está em CodexSandboxDesktop; o desktop de entrada é Default.
- desk-tec:1433 aceita conexão TCP.
- A inicialização local do Schannel retorna 0x8009030E (SEC_E_NO_CREDENTIALS)
  mesmo sem abrir rede, apresentar senha ou contactar o SQL Server.
- O ODBC retorna 08001 na negociação criptográfica. A falha local do Schannel
  reforça a necessidade de comparar os contextos de execução; não comprova uma
  senha SQL errada nem um defeito no certificado do servidor.

O teste Schannel apenas solicita e libera um contexto TLS local. Não captura
credenciais de usuários, não valida o certificado remoto e não muda protocolos.
Seu resultado não substitui uma conexão real.

## Correções feitas no projeto

- RH e Acessus verificam o desktop antes de iniciar ou controlar os aplicativos.
  Uma sessão isolada agora falha cedo, sem abrir novas janelas ocultas ou tentar
  preencher login por um fluxo incompleto.
- Novo diagnóstico único verifica desktop, bibliotecas, Schannel, TCP e uma
  leitura de DB_NAME(). Não altera os sistemas, dados ou configurações.
- O atalho PowerShell seleciona um Python acessível e reutiliza os pacotes já
  instalados. Não instala nada nem muda o ambiente virtual.

```powershell
cd C:\AutomatizaTestes
.\scripts\diagnosticar-acessos.ps1 -Base bras1
```

Esse comando é somente de diagnóstico. Não inicia cadastro automaticamente.
Gera JSON com nome novo em reports/diagnostico-acessos. Código de saída 0 indica
pré-condições técnicas disponíveis; 2 indica bloqueio ou diagnóstico incompleto.
Nenhum deles comprova o funcionamento da importação.

## Limite que depende do controle da sessão

A conversa atual usa workspace-write com pedidos de saída do sandbox
desabilitados. O agente não pode mudar essa política, editar configurações fora
do projeto ou transferir processos para Default para contornar o isolamento.
Não foi criada tarefa agendada, serviço, worker externo ou ponte de comandos.

O caminho suportado é o responsável pela sessão revisar o perfil no controle de
permissões do aplicativo, abaixo da caixa de mensagem, ou em `/permissions` na
CLI. Se disponível, um perfil que permita solicitar aprovações pontuais é
preferível a conceder acesso irrestrito. Isso não garante que a política da
organização ou as capacidades de controle de desktop permitam a operação;
o acesso efetivo deve ser revalidado depois. Restrições gerenciadas exigem revisão
do administrador.

Uma comparação do diagnóstico na sessão normal do usuário também pode distinguir
problema geral de Windows/SQL de limitação do contexto isolado, se o usuário ou
administrador optar por executá-lo. O agente não executou nada fora do sandbox.

Não se deve reduzir Encrypt, aceitar certificados indiscriminadamente,
desabilitar firewall ou reiniciar serviços como tentativa de resolver esse
problema sem evidências adicionais. As opções originais foram preservadas.

## Depois que as pré-condições estiverem disponíveis

Confirmar o banco de origem do RH, um contrato/pessoa de teste vinculado ao
Acessus e um código de ocorrência com GERAAFASTAMENTO='S'. Capturar o destino
antes, cadastrar pela tela, registrar os dados exatos e acompanhar a importação.
Sem leitura anterior e posterior e identificação do registro novo, não aprovar
o teste. O cadastro em tela por cenário ainda depende de implementação e
validação no aplicativo; o inventário de formulários não concluiu essa etapa.

## Fontes oficiais consultadas

- [Windows sandbox do Codex](https://learn.chatgpt.com/docs/windows/windows-sandbox):
  isolamento de desktop e diagnóstico de permissões.
- [Controles de permissões](https://learn.chatgpt.com/docs/sandboxing):
  seletor no aplicativo e /permissions na CLI.
- [AcquireCredentialsHandle — Schannel](https://learn.microsoft.com/en-us/windows/win32/secauthn/acquirecredentialshandle--schannel):
  inicialização do contexto local e significado dos retornos.
- [SCHANNEL_CRED](https://learn.microsoft.com/en-us/windows/win32/api/schannel/ns-schannel-schannel_cred):
  parâmetros do teste do provedor legado, com protocolos padrão do Windows.
