*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelDigitaisFaces
    [Tags]    smoke    cadastro-tfrmreldigitaisfaces    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmreldigitaisfaces
    Abrir Tela    acesso_tfrmreldigitaisfaces
