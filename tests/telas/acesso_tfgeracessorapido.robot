*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFGerAcessoRapido
    [Tags]    smoke    cadastro-tfgeracessorapido    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfgeracessorapido
    Abrir Tela    acesso_tfgeracessorapido
