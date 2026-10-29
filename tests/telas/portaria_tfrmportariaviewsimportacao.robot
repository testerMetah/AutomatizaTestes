*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmPortariaViewsImportacao
    [Tags]    smoke    cadastro-tfrmportariaviewsimportacao    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmportariaviewsimportacao
    Abrir Tela    portaria_tfrmportariaviewsimportacao
