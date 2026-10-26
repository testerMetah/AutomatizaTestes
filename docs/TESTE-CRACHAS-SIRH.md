# Teste automatizado de crachás: Frequência → API → Acessus

Execute na sessão interativa do Windows, com o RH e o banco configurados:

```powershell
.\.venv\Scripts\python.exe -m automatiza.crachas_sirh --arquivo examples\crachas-sirh.json --saida reports\crachas-sirh\minha-execucao
```

O plano contém pelo menos dois contratos. Para cada um, o teste confere a pessoa, o contrato, o crachá anterior, a API e o banco de destino antes de alterar dados. No Frequência, registra o crachá anterior como **Cancelado**, espera o horário necessário e registra o novo como **Ativo**. Confere `SITUACAOCRACHA=01` e o crachá novo na origem. Em seguida, assegura que `FrmSyncImpViewsPrincipal` esteja executando, observa um ciclo `GetContratos` e compara os novos crachás por código e pessoa entre origem, API e `RegCrachas`.

Cada passo fica em `passos.log` e `passos.jsonl`. `resultado.json` mostra `IMPORTADO_EXATO`, `NAO_IMPORTADO`, `NAO_PUBLICADO_API`, `NAO_GRAVADO_ORIGEM` ou `DIVERGENTE_DESTINO` por contrato. Uma mensagem inesperada da tela gera `erro-cadastro-<contrato>.png` e interrompe o teste. O mesmo plano pode ser executado novamente para concluir ou conferir casos já gravados, sem repetir o cadastro deles.

Os crachás do exemplo foram usados em 22/10/2026. Para um novo ciclo de cadastro, forneça novos códigos ainda livres e os crachás anteriores atuais no plano; use uma pasta de saída nova.
