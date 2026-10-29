*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadFuncionario
    [Tags]    smoke    cadastro-tfrmescolacadfuncionario    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacadfuncionario
    Abrir Tela    escola_tfrmescolacadfuncionario
