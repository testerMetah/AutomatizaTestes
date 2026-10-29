*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadDigitaisFaces
    [Tags]    smoke    cadastro-tfrmcaddigitaisfaces    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcaddigitaisfaces
    Abrir Tela    acesso_tfrmcaddigitaisfaces
