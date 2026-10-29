*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelRefeicoesTotal
    [Tags]    smoke    cadastro-tfrmrelrefeicoestotal    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmrelrefeicoestotal
    Abrir Tela    refeitorio_tfrmrelrefeicoestotal
