*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelFuncionarios
    [Tags]    smoke    cadastro-tfrmescolarelfuncionarios    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelfuncionarios
    Abrir Tela    escola_tfrmescolarelfuncionarios
