*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelReservasRefeicoes
    [Tags]    smoke    cadastro-tfrmrelreservasrefeicoes    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmrelreservasrefeicoes
    Abrir Tela    refeitorio_tfrmrelreservasrefeicoes
