*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadUnidades
    [Tags]    smoke    cadastro-tfrmcadunidades    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadunidades
    Abrir Tela    acesso_tfrmcadunidades
