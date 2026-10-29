*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadSetores
    [Tags]    smoke    cadastro-tfrmcadsetores    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadsetores
    Abrir Tela    acesso_tfrmcadsetores
