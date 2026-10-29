*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadEmpresas
    [Tags]    smoke    cadastro-tfrmcadempresas    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadempresas
    Abrir Tela    acesso_tfrmcadempresas
