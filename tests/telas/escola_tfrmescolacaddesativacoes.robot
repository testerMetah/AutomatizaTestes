*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadDesativacoes
    [Tags]    smoke    cadastro-tfrmescolacaddesativacoes    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacaddesativacoes
    Abrir Tela    escola_tfrmescolacaddesativacoes
