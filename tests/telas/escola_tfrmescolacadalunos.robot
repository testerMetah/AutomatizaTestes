*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaCadAlunos
    [Tags]    smoke    cadastro-tfrmescolacadalunos    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolacadalunos
    Abrir Tela    escola_tfrmescolacadalunos
