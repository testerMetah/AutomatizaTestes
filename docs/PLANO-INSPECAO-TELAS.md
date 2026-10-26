# Inspeção do painel e das telas dos módulos

## Nova inspeção autorizada em 19/10/2026

Usuário pediu percorrer todos os módulos, inspecionar e salvar cada tela antes
de passar à seguinte. Sessão atual em `reports/inspecao-telas/vm-20261019`,
com mapas por tela em JSON e Markdown. Índice de cobertura em
[vm-20261019/LEIA-ME.md](mapeamentos/vm-20261019/LEIA-ME.md).
Essa sessão é da versão instalada 2.10.0 e ainda está em andamento.

O usuário também informou a release 2.11.0 no Dexter. A ordem atualização/
inspeção está pendente de escolha; o compartilhamento requer autenticação.
Ao atualizar a versão ou trocar o banco Acessus, executar o Atualizador no
destino antes dos testes. Guia: [ATUALIZACAO-ACESSUS.md](ATUALIZACAO-ACESSUS.md).

Solicitação registrada em 15/10/2026: inspecionar o Painel de Módulos e as
telas dentro de cada módulo, salvando o mapeamento para uso posterior no código.

Estado: inspeção executada após autorização explícita do usuário para controlar
as telas e prosseguir sem sua presença. Resultado em
[Inspeção do painel e dos módulos](mapeamentos/acessus-completo/LEIA-ME.md).

Foram inspecionadas 120 rotas dos seis módulos, além do painel e Ajuda → Novidades,
com formulários vazios e abas quando acessíveis. A opção Opções do Sistema da
Administração não apareceu em execução; a causa não foi confirmada. Opções de
saída foram inventariadas sem acionamento.

Foram extraídas 157 estruturas distintas dos executáveis, com 11.272 componentes
declarados, incluindo não visuais. Isso não equivale a 157 telas testadas ao vivo.
As funções de negócio e os botões de processamento não foram executados.

## Cobertura solicitada

1. Mapear o painel: módulos disponíveis, menus, botões, títulos e caminhos de abertura.
2. Enumerar os módulos realmente disponíveis nessa instalação, sem presumir nomes.
3. Em cada módulo, inventariar menus, submenus e telas acessíveis.
4. Em cada tela, registrar abas, campos, rótulos, botões, atalhos e diálogos.
5. Registrar seletores candidatos e, separadamente, os seletores confirmados em execução.
6. Salvar os mapas para que as rotas e os controles possam ser incorporados ao código.

## O que salvar

Manter um índice em `docs/mapeamentos` com módulo, rota da tela, arquivo do mapa,
data, versão observada e situação: pendente, extraído estaticamente,
inspecionado em execução ou seletor validado.

Para cada tela, salvar uma árvore estruturada de controles em JSON e um resumo
legível com a rota de navegação. Registrar classe, título, hierarquia, tipo,
identificador acessível quando existir, atalhos e estados relevantes.
IDs de sessão, handles e coordenadas observadas não são seletores permanentes.
Nomes Delphi extraídos de recursos não são automaticamente `automation_id`.

Registrar também telas indisponíveis, bloqueadas por permissão ou dependentes
de dados, para não declarar cobertura completa indevidamente.

## Execução e limites

- A navegação em janelas deve ocorrer com o computador liberado pelo usuário.
- Este pedido é de mapeamento; não inclui salvar cadastros, excluir registros,
  importar dados, disparar processamento ou alterar configurações e serviços.
- Formulários novos devem ser cancelados sem salvar. Ações cujo efeito não
  esteja claro ficam pendentes, com o motivo registrado.
- Evitar salvar senhas e valores de dados pessoais nas árvores e evidências.
  Capturas de tela só devem ser guardadas quando necessárias e sem segredos.
- A leitura estática de executáveis pode complementar o inventário, mas não
  comprova o estado da tela nem valida a navegação em execução.

## Material já existente

- `docs/mapeamentos/ACESSO.md`: mapa parcial do Módulo de Acesso.
- `docs/mapeamentos/rh/LEIA-ME.md`: nove formulários extraídos estaticamente do RH.
- `src/automatiza/delphi_resources.py`: extrator estático de recursos Delphi.
- `src/automatiza/cli.py`: inspeção da janela configurada; ainda não percorre
  automaticamente todos os módulos e suas telas.

Depois da inspeção, usar os mapas para implementar as rotas por módulo e os
seletores das telas, documentando o que ainda precisa de validação real.
