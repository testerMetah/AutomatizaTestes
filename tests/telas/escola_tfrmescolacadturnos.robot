*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadTurnos
    [Tags]    smoke    cadastro-tfrmescolacadturnos    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacadturnos
    Abrir Tela    escola_tfrmescolacadturnos
