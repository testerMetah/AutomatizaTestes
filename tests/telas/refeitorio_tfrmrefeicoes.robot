*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRefeicoes
    [Tags]    smoke    cadastro-tfrmrefeicoes    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmrefeicoes
    Abrir Tela    refeitorio_tfrmrefeicoes
