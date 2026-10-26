# Codex dentro da VM

O usuário solicitou instalar o Codex no Windows TESTESVM para continuar o trabalho
diretamente no projeto C:\AutomatizaTestes.

Pacote nativo x64 oficial 0.163.0, publicado em releases.openai.com/codex,
com SHA-256 conferido contra os metadados oficiais. O pacote completo inclui
o executável, o host de código e os recursos auxiliares; não exige Node.js/npm.

O instalador gráfico Instalar-Codex-VM.pyw copia esse pacote para
`%LOCALAPPDATA%\Programs\OpenAI\Codex`, adiciona a pasta bin ao PATH do usuário
e cria o atalho **Codex - AutomatizaTestes** na área de trabalho da VM.
Também corrige o lançador codex.cmd do projeto, com backup do anterior.
Não copia autenticação do computador principal nem altera permissões do Codex.

Depois de instalado:

1. Abra o atalho **Codex - AutomatizaTestes** dentro da VM.
2. Faça login com sua conta quando solicitado.
3. Envie: "Leia CONTEXTO-PARA-CONTINUAR.md, README.md e
   docs/ESTADO-VM-20261019.md. Confira o estado atual da execução e continue a
   automação dos testes dentro desta VM. Atualize os arquivos .md com evidências."

Em um novo CMD da VM, também é possível usar:

```bat
cd /d C:\AutomatizaTestes
codex
```

Terminais abertos antes da instalação podem continuar com o PATH anterior;
feche-os e abra um novo. O atalho usa o caminho completo do executável.

O relatório da instalação fica em `C:\AutomatizaTestes\reports\codex` na VM
e é publicado como `codex-instalacao-*.json` em ResultadoVM. O relatório distingue
arquivos instalados e verificados de execução do aplicativo/login.

Referências oficiais:
- https://learn.chatgpt.com/docs/codex/cli
- https://learn.chatgpt.com/docs/enterprise/windows-deployment
