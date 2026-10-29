*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadColetores
    [Tags]    smoke    cadastro-tfrmcadcoletores    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadcoletores
    Abrir Tela    acesso_tfrmcadcoletores
