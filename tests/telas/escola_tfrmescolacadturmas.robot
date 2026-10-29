*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadTurmas
    [Tags]    smoke    cadastro-tfrmescolacadturmas    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacadturmas
    Abrir Tela    escola_tfrmescolacadturmas
