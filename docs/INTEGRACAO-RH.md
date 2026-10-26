Current evidence (2026-10-20): reports/integracao-api/20261020/auditoria-103518/COMPLEMENTO.md and diario-testes.txt. Historical preparation below is superseded by this audit.

# RH Metadados → Acessus

Atualização de 19/10/2026: abertura real de Frequência, Ocorrências e Férias
Cedidas aprovada em RHFagundes. Relatório do lote:
`reports/lotes/20261019-145247-757fa142/indice.html`. Não valida inclusão,
exclusão, recadastro ou integração completa. Veja o estado atual em
[ESTADO-VM-20261019.md](ESTADO-VM-20261019.md); os achados de 15/10 abaixo são históricos.

Para acompanhar seus testes manuais sem controlar a tela, use o
[observador SQL em segundo plano](OBSERVACAO-EM-SEGUNDO-PLANO.md).
O [mapa estático do RH](mapeamentos/rh/LEIA-ME.md) agora inclui os formulários
de ocorrências e férias, além do login. A validação nas janelas reais continua pendente.

## Inicialização

No PowerShell, dentro de `C:\AutomatizaTestes`:

```powershell
.\scripts\iniciar.ps1
# Somente um dos sistemas:
.\scripts\iniciar.ps1 -Sistema acesso
.\scripts\iniciar.ps1 -Sistema rh
```

O primeiro comando reutiliza ou abre o painel Acessus.Modulo, abre o Módulo de
Acesso, inicia o RH com sua pasta de trabalho e trata o login quando necessário.
Se Frequência já estiver aberta, ela é reutilizada. Janelas minimizadas são
restauradas. Não há repetição automática de senha em caso de falha.

As credenciais ficam no `.env` local: `RH_USER`, `RH_PASSWORD`, `SQL_USER` e
`SQL_PASSWORD`. Nenhuma senha é colocada nos exemplos ou nos relatórios.

`RH_CONTINUE_INVALID_CONFIG=yes` permite confirmar exclusivamente a janela
`TFrm_ConfiguracoesInvalidas` do RHID da pasta configurada, pelo botão
Continuar/OK. Conforme autorização posterior do usuário, avisos informativos
de entrada do RHPA com um único botão OK também são confirmados; o executor
continua exigindo módulo disponível depois. Confirmações com Sim não são
tratadas como avisos de entrada. A ocorrência
desse aviso é informada no console e não implica que as configurações foram corrigidas.

## Evidência disponível em 15/10/2026

- Conexão real ao SQL Server `desk-tec`, banco `bras1`, autenticação SQL: validada.
- Tabela de destino confirmada: `dbo.Afastamentos`, com `Id`, `IdPessoa`,
  `DataInicio`, `DataTermino`, `Causa` e `IdFreq`.
- Estrutura das tabelas relacionadas salva em `docs/mapeamentos/sql-bras1.json`.
- Formulário de login identificado nos recursos binários locais de
  `C:\meta\rhsis\RHLogin.bpl`: `TFrm_Login`, campos `TEdit` (login e senha)
  e botão `TBitBtn` com legenda `&OK`. Campos AD desabilitados são ignorados.
- Painel identificado nos recursos de `RHID.exe`: `TFrm_RHID0010`,
  menu `Módulos → Frequência`.
- Aviso identificado em `RHLogin.bpl`: `TFrm_ConfiguracoesInvalidas`,
  botões Continuar e Sair do Sistema.

**Essas definições vieram dos arquivos instalados, não de uma inspeção visual
concluída. O login, o aviso e a abertura de Frequência ainda precisam de uma
execução real de validação.** A ferramenta de controle de janelas não expôs as
janelas do RH, embora seu processo estivesse na mesma sessão Windows.

## Acompanhamento SQL e relatório

O acompanhamento já implementado consulta o destino periodicamente e grava
`amostras.jsonl`, `resultado.json` e `relatorio.html` a cada etapa em
`reports/importacao/<execucao>`. Pode ser executado depois de uma ação no RH:

```powershell
.\.venv\Scripts\automatiza.exe acompanhar --cenario .\examples\integracao-rh.modelo.json --caso ferias-incluir
```

O modelo vem com `preparado=false`, tanto no arquivo quanto em cada caso, para
evitar conclusões com pessoas, causas e datas ilustrativas. Copie o arquivo
na mesma pasta, preencha os dados reais, valide a consulta manualmente e só
então use `preparado=true` no arquivo e no caso escolhido. Os demais casos
podem continuar desabilitados.
O caminho de cada arquivo SQL é relativo ao JSON. Você pode editar as consultas.
Cada consulta de verificação deve retornar uma única contagem inteira, como `COUNT(*)`.

`id_pessoa` deve conter o ID interno positivo no Acessus. O parâmetro
`{"campo_caso": "id_pessoa"}` usa esse mesmo valor na consulta, evitando
duplicar o identificador em dois lugares. Outros parâmetros podem continuar
como valores literais. Parâmetros `PREENCHER` não são aceitos na execução.
O modelo inclui oito casos de inclusão, exclusão, recadastro e períodos antigos;
as expectativas sobre períodos antigos dependem da regra do serviço, ainda não confirmada.

Modos disponíveis:

- `convergencia`: aguarda a contagem esperada e exige amostras estáveis. Serve
  tanto para inclusão (um registro) quanto para exclusão propagada (zero).
- `na_janela`: espera zero e acompanha até o tempo limite. Qualquer presença
  amostrada reprova o caso, mesmo que depois desapareça. Serve para uma regra
  esperada de não importar determinado período.

Ausência nas amostras não comprova que o serviço rodou ou que nunca houve
registro entre duas consultas. O ciclo e a regra de corte do serviço ainda
precisam ser confirmados. O tempo limite padrão do modelo é apenas inicial.

Para validar exclusão, registre primeiro a existência do afastamento exato;
encontrar zero desde o início não comprova remoção. Para recadastro, use duas
verificações no mesmo caso: período antigo com zero e período novo com um.
Identifique a pessoa pelo `IdPessoa` interno do Acessus e confirme o contrato
correspondente no RH. Não confunda esse ID com matrícula ou `IdExportacao`.

As consultas de exemplo filtram pessoa, causa e datas/horários completos.
Não há ainda uma regra confirmada de conversão entre as datas do RH e os
horários de início/término do afastamento importado.

## O que ainda falta para executar tudo sozinho

1. Validar a inicialização e o login reais com o comando acima.
2. Mapear em Frequência → Programações os formulários de Registro de
   Ocorrências e Férias Cedidas, incluindo gravação, exclusão e confirmações.
3. Identificar pessoas/contratos em ambos os sistemas, uma ocorrência que gere
   afastamento, sua causa no destino e o ciclo/regra de corte do serviço.
4. Implementar as ações de cada caso e suas pré-condições, preservar os IDs
   criados e reunir os resultados no relatório da sequência completa.

O acompanhamento SQL atual **não executa as ações do RH**. Nenhum cadastro ou
exclusão de férias/ocorrências foi feito pelo projeto nesta preparação.
