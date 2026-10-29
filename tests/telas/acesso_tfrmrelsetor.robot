*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelSetor
    [Tags]    smoke    cadastro-tfrmrelsetor    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelsetor
    Abrir Tela    acesso_tfrmrelsetor
