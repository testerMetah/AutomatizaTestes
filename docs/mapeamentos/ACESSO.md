# Mapeamento inicial — Módulo de Acesso

Observado automaticamente em 14/10/2026, versão 2.10.0.

## Abertura

Entrada: C:\acesso\Acessus.Modulo.exe. Pasta de trabalho: C:\acesso.
O painel abriu normalmente ao executar pela pasta no Explorer, sem solicitar nova configuração do banco.
O botão Acesso abriu C:\acesso\Acessus.exe, com título Módulo de Acesso - v2.10.0.
Também foi identificado o menu Modulos > Acesso no painel.
A hipótese de diferença de pasta de trabalho é compatível com o observado, mas a causa exata
da tela anterior de configuração não foi comprovada.

## Cobertura deste primeiro mapa

- Inventário dos menus e submenus da janela principal: acesso-principal.txt.
- Cadastro de Pessoas, pesquisa e ações: acesso-pessoas.txt.
- Inclusão de Pessoas, Dados Gerais: acesso-pessoas-dados-gerais.txt.
- Inclusão de Pessoas, Dados Cadastrais: acesso-pessoas-dados-cadastrais.txt.
- Consulta Acesso por Pessoa: acesso-consulta-pessoa.txt.

O inventário contém opções das demais telas; seus formulários ainda não foram inspecionados.
Os índices e IDs numéricos dos arquivos são dados da sessão de inspeção, não seletores permanentes.
Alguns campos não possuem nome acessível. Sua associação aos rótulos foi observada visualmente;
os seletores de preenchimento precisam ser refinados por posição relativa/estrutura do formulário.

## Pessoas

Rota: Cadastros > Pessoas...; título interno: Cadastro de Pessoas.

| Área | Campos/ações observados |
|---|---|
| Lista | Código, Nome, Situação, Afastamento |
| Pesquisa | Nome (Ctrl+B), Exibir tudo (Ctrl+T) |
| Ações | Incluir (Ctrl+I), Alterar (Ctrl+E), Excluir (Ctrl+Del), Importar Pessoas (Ctrl+F5) |
| Dados Gerais | Nome, CPF, Nascimento, Sexo, Fone, Email, Setor, Unidade, Código de Exportação / Matrícula, Situação, Gestor |
| Crachás | Fixo, Provisório, Mestre |
| Acesso para o Aplicativo | Usuário, Senha |
| Dados Cadastrais | CEP, Endereço, Número, Bairro, Complemento, Cidade, UF |
| Endereço | Pesquisar Rua (F5), Limpar Endereço (F6) |
| Formulário | Salvar (Ctrl+S), Cancelar (Ctrl+D) |

Foram verificadas a abertura, inclusão de formulário vazio, troca de aba e cancelamento.
Não foi salvo cadastro. Campos de acesso ao aplicativo foram apenas identificados.

## Acesso por Pessoa

Rota: Consultas > Acesso por Pessoa...; título interno: Acesso por Pessoa.
Filtros observados: tipo (Pessoas), código/pesquisa de pessoa, Coletor, Crachá,
data/hora inicial e final. Ação: Consultar (F5); área de Período Calculado e resultados.
Os controles de datas, horas, código e combinações aparecem na árvore acessível.
Foi verificada a abertura do formulário, sem executar consulta com parâmetros inventados.

## Uso no projeto

```python
from automatiza.acesso import Acesso

acesso = Acesso(desktop)  # fixture conectada ao módulo já aberto
pessoas = acesso.open_screen("pessoas")
consulta = acesso.open_screen("acesso_por_pessoa")
```

Essas rotas usam os menus/títulos observados; a resolução delas pelo pywinauto ainda
precisa de uma execução real. O mapeamento nesta sessão usou Computer Use.
Próximas etapas: validar os seletores pywinauto e definir um caso de teste com dados e resultado esperado.
