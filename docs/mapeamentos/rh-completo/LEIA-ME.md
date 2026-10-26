# Inspeção do RH e do módulo Frequência — 15/10/2026

Atualização: o levantamento foi ampliado para bibliotecas sem prefixo RH.
O total combinado, sem duplicar estruturas iguais, é de 4.782 estruturas e
156.082 componentes, em 1.559 arquivos inspecionados. Veja o
[índice ampliado](INDICE-AMPLIADO.md) e o
[relatório integrado de Acessus, RH e SQL](../../LEVANTAMENTO-ACESSUS-RH-SQL.md).
Os números abaixo descrevem a primeira extração, preservada como evidência.

O inventário estático foi concluído. A inspeção das telas em execução permanece
pendente porque esta sessão não dispõe de desktop interativo para foco, mouse e
teclado. Não considerar este levantamento uma validação completa do sistema.

## Material produzido

- [Índice geral dos formulários](estatico-20261015/INDICE.md).
- [Catálogo com origens, hashes, menus e limites](estatico-20261015/catalogo.json).
- [Formulários candidatos de Frequência](estatico-20261015/frequencia.json).
- [Menus e detalhes de Frequência](FREQUENCIA.md).
- [Manifesto dos mapas](manifesto-sha256.json).

Foram lidos 1.079 arquivos locais com prefixo RH e extensão EXE, BPL ou DLL
na pasta de instalação, totalizando 484.633.888 bytes. Foram extraídas 4.589
estruturas distintas de formulários, frames e diálogos, com 151.337 componentes
declarados, incluindo componentes não visuais. Não ocorreram erros de leitura
ou análise nos recursos selecionados. Isso não garante cobertura de recursos
com outros formatos, outros nomes de classe ou arquivos fora desse conjunto.

RH.exe não apresentou formulários TPF0 selecionados. O painel foi localizado
em RHID.exe. RHPA.exe contém 272 recursos selecionados; o índice de Frequência
inclui 276 estruturas candidatas, considerando também classes TFrm_RHPA em
bibliotecas compartilhadas. Essa associação não comprova disponibilidade em
execução, licença ou permissão. Há formulários compartilhados entre módulos.

Os JSONs de formulário registram classes, nomes Delphi, legendas, campos
declarados, eventos e hierarquia. Os nomes não são automaticamente automation_id.
Propriedades herdadas podem estar em outro recurso. SQL, conexões, textos dos
campos e imagens binárias não são exportados pelo leitor. Nenhum dado de negócio
foi consultado para produzir o inventário.

## Tentativa de inspeção em execução

1. A abertura de C:\meta\rhsis\rh.exe iniciou RHID.exe e apresentou Identificação.
2. A tentativa pelo fluxo existente RhApp falhou em set_focus/SetCursorPos com
   a mensagem de ausência de desktop ativo. Não chegou a preencher nessa tentativa.
3. Uma única submissão foi feita diretamente pelos controles, com credenciais
   locais; confirmou-se que o usuário preenchido era master, sem publicar a senha.
4. Apareceu TMessageForm, título Information, texto “Usuário inválido”. Uma
   captura PrintWindow confirmou a mensagem. O aviso foi fechado por OK.
5. O campo de senha foi limpo. Não houve nova submissão, não foi confirmado
   login, não se chegou ao aviso de configurações nem ao módulo Frequência.

O fluxo direto não validou o evento de saída do campo de operador como uma
digitação real. A mensagem não comprova que a credencial fornecida esteja
errada. A inspeção UIA não respondeu e seu processo de leitura foi interrompido.
O formulário de login ficou aberto ao final; não se deve presumir esse estado
em outra sessão.

Evidência local: reports/inspecao-rh/20261015/aviso-login.png. Não foram acionados
salvamento, exclusão, importação, recálculo, envio a equipamentos ou processamento.
Não foram feitos testes reais de negócio ou de banco.

## Continuidade

Para completar a tarefa, é necessário executar a inspeção em uma sessão com
desktop interativo disponível e usar o login informado pelo usuário. Primeiro
validar operador, senha, aviso e restauração/maximização; depois capturar o painel
e percorrer as rotas de Frequência, abas e formulários seguros. Rotinas de
processamento devem ter apenas sua tela de parâmetros inspecionada, sem execução.
O inventário estático já fornece a base, mas não substitui essa etapa.

O Python da .venv aponta para um executável inacessível nesta sessão. O trabalho
usou C:\Python314\python.exe com os pacotes já presentes em .venv, sem instalação
ou mudança de configuração. O extrator reutiliza o leitor existente e pode ser
executado pelo script scripts/mapear_rh_estatico.py em um ambiente Python válido.
