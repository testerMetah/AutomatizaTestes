*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAfastamentos
    [Tags]    smoke    cadastro-tfrmafastamentos    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmafastamentos
    Abrir Tela    acesso_tfrmafastamentos
