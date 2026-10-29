*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadVisitantesTerceirosDois
    [Tags]    smoke    cadastro-tfrmcadvisitantesterceirosdois    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmcadvisitantesterceirosdois
    Abrir Tela    portaria_tfrmcadvisitantesterceirosdois
