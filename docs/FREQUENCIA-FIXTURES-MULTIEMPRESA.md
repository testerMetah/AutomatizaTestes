# Fixtures multiempresa do Frequência (22/10/2026)

## Regra operacional

Todos os cadastros desta massa são feitos pela interface do **Frequência Essencial**, iniciado pelo SIRH Metadados. O SQL Server é usado somente para consultas de conferência. Não criar nem alterar registros diretamente nos bancos e não alterar o Acessus nesta etapa.

Banco fonte: `RHFagundes` no servidor `desk-tec`. Banco Acessus: `novo123` (consulta apenas). Configuração e credenciais ficam no `.env`; não copiá-las para relatórios. A aplicação usa o operador `MASTER`.

## Identificadores reservados

| Empresa | Nome | Unidades | Estabelecimento |
| --- | --- | --- | --- |
| 9001 | AUTOTESTE ACESSUS ALFA | 9101, 9102 | 9001 (criado) |
| 9002 | AUTOTESTE ACESSUS BETA | 9201, 9202 | 9002 (criado) |
| 9003 | AUTOTESTE ACESSUS GAMA | 9301, 9302 | 9003 (criado) |

Nomes e códigos são exclusivos da massa de testes. As seis unidades foram criadas e conferidas em `RHUNIDADES`, cada uma vinculada à empresa correta. As três empresas foram criadas e conferidas em `RHEMPRESAS`. Empresas e unidades estão ativas.

Pessoa compartilhada: `990001`, `TESTE COMPARTILHADO ALEX`, CPF de teste `90000000175`, mesma identidade em cada empresa. Cada empresa tem seu próprio registro em `RHPESSOAS`; a pessoa participa das duas unidades da empresa por dois registros em `RHCONTRATOS`.

Pessoas exclusivas por unidade: códigos `910101`, `910201`, `920101`, `920201`, `930101`, `930201`, com nome `TESTE EXCLUSIVO <EMPRESA> UNIDADE <N>`. Cada uma recebe somente um contrato na unidade correspondente. Os CPFs fictícios com dígitos válidos são, na mesma ordem: `90000100129`, `90000200182`, `90000300136`, `90000400190`, `90000500143`, `90000600105`. Esses números são dados sintéticos de teste.

Contratos: `910101` e `910102` na unidade 9101 (ALEX e exclusivo), `910201` e `910202` na 9102, e assim por diante. Situação `Ativo` (`SITUACAO='1'`). Valores de apoio já existentes no Frequência: vínculo empregatício `C.L.T. com Prazo Indeterminado`, previdência `Empregado`, cargo `0020`, sindicato `0006`, escala ativa `5151`.

## Estado confirmado

- Empresas 9001, 9002, 9003: gravadas.
- Unidades 9101, 9102, 9201, 9202, 9301, 9302: gravadas e vinculadas corretamente.
- Estabelecimentos 9001, 9002 e 9003: gravados via Frequência. O CNPJ do 9003 é sintético: `90.000.000/0301-72` (no banco `90000000/0301-72`).
- Pessoa compartilhada 990001: gravada nas três empresas.
- Exclusivos 910101, 910201, 920101, 920201, 930101 e 930201: gravados nas empresas correspondentes.
- Contratos das seis unidades: doze gravados e ativos, com as pessoas correspondentes. Validação completa em 22/10/2026 às 14:14: `APROVADO`.
- Em 22/10/2026, a janela de busca `TFrm_Procura` para estabelecimento no formulário de contrato abriu vazia, com os controles internos invisíveis. A falha se repetiu após reiniciar somente o módulo Frequência. A janela não respondeu a Escape nem a fechar; foi necessário reiniciar o módulo. Como alternativa, digitar o código do estabelecimento no campo, sair com Tab e conferir a descrição preenchida. O mesmo funcionou para sindicato `0006`, cargo `0020` e escala `5151`; todos os contratos foram validados no banco após salvar.
- A diretriz `Iniciar sempre na Empresa` está em 9001. O valor original era vazio. Foi tentada a restauração pela interface, mas o Frequência recusou o valor vazio com `Código inexistente.`; a edição foi cancelada e 9001 permanece salvo. Encontrar um caminho válido pela interface antes de considerar a restauração concluída.

Conferir o estado vivo antes de retomar: a sessão pode desconectar por inatividade, e o último cadastro pode ter sido salvo depois deste documento.

Validação automatizada somente leitura: `scripts/validar_fixtures_frequencia.py`. Executar com `.\\.venv\\Scripts\\python.exe .\\scripts\\validar_fixtures_frequencia.py`; o relatório é gravado em `reports/frequencia_fixtures_validacao.json`. Retorna código 0 somente quando todas as empresas, unidades, estabelecimentos, pessoas e contratos esperados existirem e os contratos estiverem ativos. A última execução retornou código 0 e `APROVADO`.

## Caminho da interface e validações

- Menu `Cadastramento > Empresas`, `Unidades`, `Estabelecimentos`, `Pessoas e Contratos`.
- Para alternar empresa: `Arquivo > Diretrizes > Diretrizes do Operador > Iniciar sempre na Empresa`; escolher no botão de busca, salvar, fechar o módulo Frequência e reabrir pelo SIRH. Valor original dessa diretriz era vazio: restaurar ao final. `Editar > Trocar Unidade/Empresa` apareceu desabilitado.
- Unidade nova herda a empresa corrente. Validar `RHUNIDADES.EMPRESA` após cada gravação.
- Em Pessoas e Contratos, cadastrar dados pessoais antes do contrato. O CPF exige máscara formatada, por exemplo `900.000.001-75`. Para cada contrato, preencher unidade e código e aguardar o formulário carregar. Situação padrão é `Ativo`.
- Estabelecimento e sindicato precisam ser escolhidos na janela de busca (lupa); digitar o código e sair do campo pode limpá-lo. Escala ativa `5151` pode ser escolhida pela busca. Cargo `0020` funciona digitando e saindo com Tab, mas às vezes é limpo após selecionar a escala: conferir antes de salvar e, se necessário, preencher mais uma vez.
- Ao salvar contrato, o Frequência informa o próximo campo obrigatório. Os campos que exigiram preenchimento foram: Vínculo Previdência, Cargo, Sindicato, Estabelecimento, Escala. Vínculo Empregatício também foi definido explicitamente. A consulta no banco é a confirmação final; ausência de mensagem na UI não basta.
- Para criar estabelecimento, no formulário `Estabelecimentos` usar código da empresa, nome reduzido de teste, tipo `Único`, natureza jurídica `Sociedade Empresária Limitada`, categoria `Outros`, inscrição `CNPJ` e CNPJ sintético válido, data de início de atividades `22/10/2026`. As máscaras de CNPJ e data aceitaram entrada com teclado no início do campo; `set_edit_text` não persistiu na máscara.

Consultas somente leitura:

```sql
SELECT EMPRESA, RAZAOSOCIAL, ATIVADESATIVADA FROM RHEMPRESAS WHERE EMPRESA IN ('9001','9002','9003');
SELECT UNIDADE, EMPRESA, DESCRICAO40, ATIVADESATIVADA FROM RHUNIDADES WHERE UNIDADE IN ('9101','9102','9201','9202','9301','9302');
SELECT EMPRESA, PESSOA, NOME, CPF FROM RHPESSOAS WHERE EMPRESA IN ('9001','9002','9003') AND (PESSOA=990001 OR PESSOA IN (910101,910201,920101,920201,930101,930201));
SELECT EMPRESA, UNIDADE, CONTRATO, PESSOA, SITUACAO, ESTABELECIMENTO, ESCALA FROM RHCONTRATOS WHERE UNIDADE IN ('9101','9102','9201','9202','9301','9302');
```

## Arquitetura do projeto

`src/automatiza/config.py` carrega `.env`; `database.py` fornece consultas SQL com rollback; `rh.py` inicia e controla o Frequência via pywinauto; `crachas_sirh.py` executa o fluxo automatizado de crachás. Mapas das telas RH e Acessus estão em `docs/mapeamentos/`. Os scripts de testes e relatórios ficam em `src/automatiza/` e `reports/`. A versão Acessus visível é 2.11.1. Este preparo da massa não dispara sincronização nem modifica o banco Acessus.
