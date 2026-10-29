*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRegCrachas
    [Tags]    smoke    cadastro-tfrmregcrachas    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmregcrachas
    Abrir Tela    acesso_tfrmregcrachas
