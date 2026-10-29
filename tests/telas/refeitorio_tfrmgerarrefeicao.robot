*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmGerarRefeicao
    [Tags]    smoke    cadastro-tfrmgerarrefeicao    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmgerarrefeicao
    Abrir Tela    refeitorio_tfrmgerarrefeicao
