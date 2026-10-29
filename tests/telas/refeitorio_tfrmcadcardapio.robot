*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadCardapio
    [Tags]    smoke    cadastro-tfrmcadcardapio    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmcadcardapio
    Abrir Tela    refeitorio_tfrmcadcardapio
