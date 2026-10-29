*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelUnidade
    [Tags]    smoke    cadastro-tfrmrelunidade    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelunidade
    Abrir Tela    acesso_tfrmrelunidade
