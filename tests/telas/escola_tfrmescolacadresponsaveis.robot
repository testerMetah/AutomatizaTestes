*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadResponsaveis
    [Tags]    smoke    cadastro-tfrmescolacadresponsaveis    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacadresponsaveis
    Abrir Tela    escola_tfrmescolacadresponsaveis
