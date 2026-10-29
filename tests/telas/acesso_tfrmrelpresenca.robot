*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelPresenca
    [Tags]    smoke    cadastro-tfrmrelpresenca    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelpresenca
    Abrir Tela    acesso_tfrmrelpresenca
