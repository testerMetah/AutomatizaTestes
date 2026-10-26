# Base de dados de cada teste

A base pode mudar. `bras1` foi o destino autorizado para o levantamento atual;
não é mais um nome obrigatório nas ferramentas. A base do RH pode ser outra:
não presumir que seu banco de origem seja a mesma base de destino do Acessus.

## Seleção por execução

Os exemplos abaixo são comandos para uso posterior. Substitua `NOME_DA_BASE`
pelo nome real do banco de teste; nenhum desses exemplos foi executado agora.

```powershell
# Inventário de metadados da base escolhida:
.\.venv\Scripts\python.exe .\scripts\mapear_banco.py --base NOME_DA_BASE

# Consulta filtrada usando o mesmo formato de filtros do projeto:
.\.venv\Scripts\python.exe .\scripts\conferir.py consultar --base NOME_DA_BASE --filtros .\meus-filtros.json --saida .\reports\conferencia\nova-amostra.json

# Observação durante dez minutos, sem controlar janelas:
.\.venv\Scripts\python.exe -m automatiza.cli observar --base NOME_DA_BASE --duracao 600 --intervalo 15

# Referências de pessoas da sessão ativa, na mesma base da coleta:
.\.venv\Scripts\python.exe -m automatiza.cli atualizar-referencias --base NOME_DA_BASE
```

`--base` não modifica o `.env`, os sistemas instalados nem serviços. Quando ele
não é informado, vale `SQL_DATABASE` da configuração. Para os atalhos PowerShell,
é possível usar a variável de ambiente na sessão do terminal:

```powershell
$env:SQL_DATABASE = 'NOME_DA_BASE'
.\scripts\observar.ps1
```

A variável continua valendo nesse terminal e seus processos filhos até ser
alterada ou removida. Para voltar a usar o `.env`:

```powershell
Remove-Item Env:SQL_DATABASE
```

Servidor, driver e autenticação continuam definidos na configuração existente.
Trocar apenas a base não muda o servidor nem as credenciais.

## Identificação das evidências

- Observação, conferência, referências, inventário e inspeção da integração
  conferem `DB_NAME()` contra o destino configurado antes da leitura.
- As sessões, amostras e relatórios identificam a base usada.
- Comparações exigem servidor, base e filtros idênticos.
- Referências de pessoas recusam mistura com uma sessão ou arquivo de outra origem.
- Uma coleta nova usa uma pasta de sessão nova. Não reaproveite amostras de
  outra base. A troca da configuração não redireciona um observador já iniciado.

As consultas de negócio continuam dependendo das estruturas de destino do
Acessus, como `dbo.Afastamentos` e `dbo.Pessoas`. Aceitar outro nome de banco não
significa que qualquer esquema SQL seja compatível. Inspecione a estrutura antes
de usar uma cópia com outra versão. SQL livre continua aceitando comandos
arbitrários: a seleção da base e o rollback não tornam qualquer consulta segura.

Os relatórios antigos continuam identificados como `bras1`; são evidências daquela
execução. A análise usa `bras1` como compatibilidade apenas em arquivos históricos
que não registravam o nome da base.
