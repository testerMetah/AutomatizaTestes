*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Run Keywords    Fechar Popup    AND    Fechar Tela

*** Test Cases ***
Refeitorio Rejeita Nome Vazio
    [Tags]    cadastro-refeitorio    regressao    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmcadrefeitorios
    Abrir Tela    refeitorio_tfrmcadrefeitorios
    Clicar Controle    btn_inserir
    Preencher Campo    campo_nome    ${EMPTY}
    Clicar Controle    btn_ok
    ${mensagens}=    Ler Mensagem
    Mensagem Deve Conter    ${mensagens}    O Nome do refeitório deve ser informado.

Cardapio Rejeita Nome Vazio
    [Tags]    cadastro-cardapio    regressao    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmcadcardapio
    Abrir Tela    refeitorio_tfrmcadcardapio
    Clicar Controle    btn_inserir
    Preencher Campo    campo_nome    ${EMPTY}
    Clicar Controle    btn_ok
    ${mensagens}=    Ler Mensagem
    Mensagem Deve Conter    ${mensagens}    O Nome do cardápio deve ser informado.
