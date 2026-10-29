*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelCracha
    [Tags]    smoke    cadastro-tfrmrelcracha    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelcracha
    Abrir Tela    acesso_tfrmrelcracha
