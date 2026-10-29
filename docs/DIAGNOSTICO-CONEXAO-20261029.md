# Diagnóstico de abertura do Estacionamento — 29/10/2026

Ao iniciar `C:\acesso\Acessus.Estacionamento.exe` diretamente, apareceu `A Entrada no Sistema é irregular. Utilize o Acessus.Modulo.Exe`. Uma instância aberta dessa forma permaneceu com erro FireDAC/ODBC de conexão SQL (`Provedor de Pipes Nomeados: Não foi possível abrir uma conexão com o SQL Server [2]`). Encerrei essa instância. Em seguida, o painel `Acessus.Modulo.exe` aceitou o login de teste e abriu Estacionamento normalmente pelo menu `Módulos > Estacionamento`; Cadastro de Veículos ficou acessível.

`Acesso/UDMConexaoBD.pas`, procedure `SetConfigBD`, carrega o INI e decripta a senha com `UFEncrypt.DesCriptografa(..., 99)`. `scripts/diagnosticar_conexao_acessus.py` fez somente `SELECT DB_NAME()` com as duas configurações após essa transformação, sem imprimir credenciais:

| Origem da configuração | Resultado |
|---|---|
| `.env` da venv 32 bits | Conectou a `Acessus_AUTOTEST_20261023` |
| `C:\acesso\ConexaoConfig.ini`, senha decriptada | Conectou a `Acessus_AUTOTEST_20261023` |

Servidor, banco, usuário e senha decriptada são iguais nas duas configurações. A causa exata da mensagem SQL na instância irregular não foi isolada. Nenhum INI foi alterado. A fumaça de Veículos e três validações negativas passaram no build 2.11.1 após a abertura correta pelo painel.
