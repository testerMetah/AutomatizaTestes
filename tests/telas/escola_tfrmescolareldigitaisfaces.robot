*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelDigitaisFaces
    [Tags]    smoke    cadastro-tfrmescolareldigitaisfaces    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolareldigitaisfaces
    Abrir Tela    escola_tfrmescolareldigitaisfaces
