*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelInconsistencias
    [Tags]    smoke    cadastro-tfrmescolarelinconsistencias    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelinconsistencias
    Abrir Tela    escola_tfrmescolarelinconsistencias
