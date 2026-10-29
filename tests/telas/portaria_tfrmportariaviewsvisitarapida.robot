*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmPortariaViewsVisitaRapida
    [Tags]    smoke    cadastro-tfrmportariaviewsvisitarapida    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmportariaviewsvisitarapida
    Abrir Tela    portaria_tfrmportariaviewsvisitarapida
