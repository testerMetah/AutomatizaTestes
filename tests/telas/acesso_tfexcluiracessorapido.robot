*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFExcluirAcessoRapido
    [Tags]    smoke    cadastro-tfexcluiracessorapido    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfexcluiracessorapido
    Abrir Tela    acesso_tfexcluiracessorapido
