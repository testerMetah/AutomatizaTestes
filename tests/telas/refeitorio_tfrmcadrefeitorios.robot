*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadRefeitorios
    [Tags]    smoke    cadastro-tfrmcadrefeitorios    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmcadrefeitorios
    Abrir Tela    refeitorio_tfrmcadrefeitorios
