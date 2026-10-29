*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmConfigEtiqueta
    [Tags]    smoke    cadastro-tfrmconfigetiqueta    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmconfigetiqueta
    Abrir Tela    portaria_tfrmconfigetiqueta
