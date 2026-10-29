*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadVisitantesTerceiros
    [Tags]    smoke    cadastro-tfrmcadvisitantesterceiros    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmcadvisitantesterceiros
    Abrir Tela    portaria_tfrmcadvisitantesterceiros
