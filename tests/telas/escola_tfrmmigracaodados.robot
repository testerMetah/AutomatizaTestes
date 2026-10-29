*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TfrmMigracaoDados
    [Tags]    smoke    cadastro-tfrmmigracaodados    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmmigracaodados
    Abrir Tela    escola_tfrmmigracaodados
