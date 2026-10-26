# Levantamento de Acessus, RH e SQL Server

Inspeção em 15/10/2026. Escopo: maximizar informações úteis para preparar testes,
mantendo dados e configurações dos sistemas. A base deste levantamento foi
`bras1`; o nome da base poderá mudar em outras execuções.

## O que foi confirmado nesta sessão

| Área | Resultado | Evidência |
|---|---|---|
| Acessus | 32 EXE/BPL lidos; 223 estruturas distintas; 16.744 componentes declarados | [Catálogo ampliado](mapeamentos/acessus-completo/estatico-20261015-ampliado/catalogo.json) |
| RH | 1.559 EXE/BPL/DLL lidos; 4.782 estruturas distintas; 156.082 componentes declarados | [Índice ampliado](mapeamentos/rh-completo/INDICE-AMPLIADO.md) |
| Frequência | 175 caminhos terminais declarados; 276 estruturas candidatas no levantamento inicial | [Menus e formulários](mapeamentos/rh-completo/FREQUENCIA.md) |
| Integração | 101 trechos SQL estáticos selecionados em cinco executáveis, com literais omitidos | [Trechos e offsets](PISTAS-SQL-INTEGRACAO.md) |
| Arquivos instalados | Versões, arquitetura PE, tamanhos, hashes e estrutura de 49 configurações | [Inventário local](../reports/levantamento-20261015/ambiente/ambiente.json) |
| Rede SQL | desk-tec resolveu para 192.168.50.61; conexão TCP à porta 1433 foi possível | [Diagnóstico TCP](../reports/levantamento-20261015/rede-sql.json) |
| Acesso SQL | Negociação criptográfica falhou com ODBC 17 e Native Client 11; nenhuma consulta desta sessão foi concluída | [Tentativas](../reports/levantamento-20261015/sql-conexao.json) |
| Serviços | Importação API executando; AcessusSync, MetahConnect e Comunicação parados na consulta | [Estados observados](../reports/levantamento-20261015/servicos.json) |
| Desktop | Processo no desktop isolado CodexSandboxDesktop; desktop de entrada do usuário é Default | [Diagnóstico](../reports/levantamento-20261015/desktop.json) |

Não houve falha de análise nos recursos selecionados dos inventários estáticos.
Os números são estruturas declaradas, incluindo frames e diálogos; componentes
podem ser não visuais. Eles não equivalem a telas navegadas ou regras validadas.
Arquivos de bibliotecas podem compartilhar a mesma estrutura, deduplicada por
conteúdo. Recursos sem TPF0, nomes fora do filtro e telas criadas dinamicamente
podem não estar representados.

## Acessus: instalação e telas

`Acessus.exe`, `Acessus.Modulo.exe` e `AcessusSyncImportacao.exe` são x86 e têm
versão de arquivo 2.10.0.0. Os hashes individuais permitem reconhecer uma mudança
de executável antes de reaproveitar seletores ou conclusões.

A inspeção anterior de 120 rotas nos seis módulos está preservada no
[catálogo de telas](mapeamentos/acessus-completo/LEIA-ME.md). Ela não foi repetida
nem revalidada na área de trabalho do usuário nesta sessão. O inventário novo
acrescenta os executáveis auxiliares e os componentes de integração.

Foram localizados, entre outros:

- `TFConfigAPI`: configuração de API.
- `TFImportadorExportadorMetadados`: importador Metadados.
- `TFImportadorMetadadosSelecao`: seleção de pessoas.
- `TFrmPrincipalSync`: gerenciador de tarefas.
- `TFrmViewsTarefas`: montagem de tarefa.
- `TFrmMetahConnectAgendamentos`: agendamentos.
- `TFrmAfastamentos`: afastamentos.
- `TFrmBDConfig` e `TFrmViewsConfigDB`: configurações de banco.

Sua presença em vários executáveis não comprova que todos os processos usam os
mesmos fluxos. Não foram abertos serviços ou utilitários de processamento para
descobrir isso por tentativa.

Os arquivos `ConexaoConfig.ini` e `AccessusComConfig.ini` indicavam desk-tec/BRAS1.
Isso é configuração em arquivo, sem confirmação de que todo processo a tenha
carregado. Outro `config.ini` aponta para uma base de licenciamento; não deve
ser confundido com o banco dos testes. Credenciais e strings de conexão não foram
publicadas.

## RH e Frequência

`rh.exe` inicia o sistema; não foram encontrados formulários TPF0 selecionados
nesse lançador. O painel está em `RHID.exe`, x86, versão de arquivo 6.0.2.0.
Frequência está em `RHPA.exe`, também x86. Não foi inferida uma versão de produto
para todo o RH a partir de apenas um arquivo.

O painel declara módulos de Administração, Folha, Frequência, Benefícios,
Integração Bancária, Jurídico, Cargos e Salários, Avaliação, Treinamento,
Recrutamento, Saúde, Segurança, Acesso, Portaria, eSocial e Easy MOB.

O levantamento de Frequência inclui diretrizes; tabelas diversas, do ponto e de
pessoas/contratos; cadastramento; programações; refeitório; gorjetas; apuração;
integração; relatórios e consultas. Foram preservados os detalhes declarados de
Registro de Ocorrências e Férias Cedidas.

O arquivo `dbxconnections.ini` contém seções Firebird, Oracle e SQL Server, com
valores que podem ser modelos ou configurações antigas. A presença dessas seções
não confirma o backend ativo do RH. Em particular, não há evidência de que o RH
use a própria bras1 como origem.

Bibliotecas sem prefixo RH também foram inventariadas no
[catálogo complementar](mapeamentos/rh-completo/estatico-complementar-20261015/catalogo.json).
As [dependências PE](../reports/levantamento-20261015/binarios-integracao.json)
ajudam a localizar formulários ancestrais e bibliotecas carregáveis. Imports
estáticos não garantem carregamento em cada sessão.

## Pistas novas sobre a integração

As evidências abaixo vêm de textos SQL dos executáveis instalados, especialmente
`AcessusSyncImportacao.exe`. Não são resultados de consultas executadas agora.

| Informação | Trecho encontrado | Limite |
|---|---|---|
| Férias | `RHFERIASCEDIDASPA`, campos UNIDADE, CONTRATO, INICIOGOZOFERIAS, TERMINOGOZOFERIAS; junção com RHCONTRATOS | Não confirma a chave final de vínculo com Pessoas |
| Ocorrências | `RHREGOCORRENCIAS`, campos UNIDADE, CONTRATO, OCORRENCIA, DATAINICIOOCORRENCIA e DATATERMINOOCORRENCIA | Não confirma que todo registro seja importado |
| Causa | `RHOCORRENCIAS.DESCRICAO40` aparece como alias `causa` | Transformações posteriores podem existir |
| Afastamento | Consultas filtram `GERAAFASTAMENTO = 'S'` | Não comprova que seja a única condição efetiva |
| Corte por início | `INICIOGOZOFERIAS >= :Ini` e `DATAINICIOOCORRENCIA >= :Ini` | O valor de `:Ini` não foi obtido |
| Vigência de ocorrência | `:Hoje BETWEEN DATAINICIOOCORRENCIA AND COALESCE(DATATERMINOOCORRENCIA, :Hoje)` | O valor/horário de `:Hoje` e o fluxo usado permanecem pendentes |
| Situação do contrato | Há consulta de férias com `SITUACAO = 1` e outras com `SITUACAO IN (1,2)` | Não definir os significados de 1 e 2 sem confirmação |
| Férias ainda vigentes | Outra consulta usa término nulo ou término maior/igual a `:Hoje` | Pode ser outra etapa; não substitui automaticamente a consulta por `:Ini` |
| Término especial | Consultas de destino aceitam `DataTermino = 0` ou usam parâmetro `:DataZero` | Reforça hipótese de sentinela; não autoriza normalizar 1899-12-30 para NULL |
| Chave de origem | Consultas usam `IdFreq`, `LIKE :prefixo`, comparação por pessoa/causa/início e exclusões de padrões | A formação completa da chave não foi confirmada |
| Exclusão | Existe texto de `DELETE` de Afastamentos filtrado por pessoa | Não foi executado; não comprova quando o serviço chama essa operação |

Também há diferença textual em `MetahConnect.exe`: um trecho une
`r.CONTRATO = c.PESSOA`, enquanto outros usam `r.CONTRATO = c.CONTRATO`.
Isso deve orientar uma verificação posterior; não é diagnóstico de defeito,
pois não sabemos se esse trecho participa da integração atual.

Essas pistas explicam por que testes de períodos antigos, registros fora da
vigência, término nulo e diferentes situações do contrato precisam de expectativas
separadas. A configuração histórica `contratos_alterados=2000-01-01` não foi
comprovada como o valor de `:Ini` dessas consultas.

## SQL Server e bras1

O servidor remoto estava acessível por TCP, mas os clientes não concluíram o
login por erro de criptografia/provedor de segurança, SQLSTATE 08001. Não foram
relaxadas opções de segurança, alterados serviços ou testadas outras credenciais.
Não foi obtida uma versão atual do motor SQL Server. A instalação local de uma
instância SQLEXPRESS parada não identifica a versão do servidor remoto desk-tec.

O inventário de metadados já existente, observado em **15/10/2026 às 12:57:41 UTC**
(09:57:41 em São Paulo), contém:

- 142 tabelas, duas views, um procedimento e um gatilho.
- 1.373 colunas.
- 268 índices distintos; as 343 linhas do arquivo de índices são participações
  de colunas, incluindo colunas incluídas.
- 176 chaves estrangeiras e 176 vínculos de colunas nesse inventário.

Todos esses objetos foram organizados em um
[dicionário completo da coleta histórica](DICIONARIO-BRAS1-HISTORICO.md), com
tipos, nulabilidade, identidade, índices e relacionamentos. Não são uma nova
leitura do servidor.

O destino relevante continua sendo `dbo.Afastamentos`: Id, IdPessoa, DataInicio,
DataTermino, Causa e IdFreq. O inventário registra PK_Ferias em Id, unicidade
de IdFreq e FK para Pessoas.id. O nome da PK não limita a tabela a férias.

Também foram identificados Pessoas, Ocorrencias, DADOS_IMPORTACAO_API,
AcessusSyncTarefas, AcessusSyncAgendamento, estruturas de histórico e filtros.
Os nomes sugerem funções; não comprovam que todas participem do mesmo fluxo.

## Troca de base e ferramentas

As ferramentas de observação, conferência, referências e inventário deixaram de
exigir o nome bras1. Use `SQL_DATABASE` ou `--base` conforme o
[guia de bases de teste](BASES-DE-TESTE.md). Nenhuma base foi trocada nos sistemas
instalados; o `.env` foi preservado.

As leituras de coleta conferem `DB_NAME()` contra o nome configurado. Relatórios
e pacotes identificam a base; amostras de bases diferentes não são comparadas;
referências de pessoas de outra origem são recusadas. O esquema das consultas
continua sendo o de destino do Acessus, não um esquema SQL arbitrário.

O inventário SQL foi ampliado para opções do servidor/base, estimativas de linhas
dos catálogos, restrições, dependências, parâmetros, sinônimos e arquivos lógicos.
Essas consultas novas estão preparadas, mas não foram validadas no servidor nesta
sessão. Falhas por permissão/versão ficam explícitas, em vez de virar listas vazias.

## Limites da navegação e próximos pontos a confirmar

Sua autorização para usar o computador foi recebida. O processo desta ferramenta
está, porém, no desktop isolado `CodexSandboxDesktop`, diferente de `Default`.
Não foi tentada troca de desktop ou outra forma de contornar esse isolamento.
Isso explica por que os aplicativos iniciados aqui não permitem a inspeção normal
da área de trabalho que você usa. A biblioteca UIA não respondeu na tentativa
anterior; as novas capturas usaram somente controles Win32, sem valores de dados.

O RH continuou sem login confirmado. Surgiu também um diálogo de Diretório do
Sistema apontando C:\META\RHSIS; foi acionado Cancelar, sem salvar configuração.
O painel Acessus foi chamado, mas não expôs uma janela navegável nesta área
isolada. O índice de janelas e os processos observados estão nos
[arquivos da sessão](../reports/levantamento-20261015/janelas/indice.json).

Falta confirmar em ambiente interativo e com conexão SQL funcional: login do RH,
aviso e restauração; seletores e telas efetivas; banco de origem do RH; valores de
`Ini`/`Hoje`; construção de IdFreq; correspondência de pessoa, unidade e contrato;
significado de situação e término sentinela; qual serviço e qual fluxo são usados;
e comportamento observado de inclusão, exclusão e recadastro.

Não foram feitas operações de negócio, mudanças no banco, instalações ou
reconfigurações de serviço. A documentação distingue evidência estática, histórico
SQL e observação atual. Os testes de código têm relatório em
[testes-unitarios.html](../reports/levantamento-20261015/testes-unitarios.html).

A validação final teve **127 testes unitários aprovados**. A checagem dos
artefatos gerados não encontrou as senhas locais de RH/SQL nos arquivos
inspecionados; ela não substitui uma revisão do conteúdo antes de compartilhar.

O [pacote local de evidências](../reports/levantamento-20261015/levantamento-acessus-rh-sql.zip)
reúne mapas estáticos, dicionário histórico, evidências atuais, documentação e
código do projeto. Ele não inclui `.env` nem os executáveis instalados.
O manifesto SHA-256 identifica os arquivos; a
[verificação do pacote](../reports/levantamento-20261015/verificacao-pacote.json)
confere os hashes após a compactação. O pacote permanece neste computador.
