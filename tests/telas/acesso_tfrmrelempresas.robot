*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelEmpresas
    [Tags]    smoke    cadastro-tfrmrelempresas    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelempresas
    Abrir Tela    acesso_tfrmrelempresas
