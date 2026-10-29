*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelVisitantesTerceiros
    [Tags]    smoke    cadastro-tfrmrelvisitantesterceiros    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmrelvisitantesterceiros
    Abrir Tela    portaria_tfrmrelvisitantesterceiros
