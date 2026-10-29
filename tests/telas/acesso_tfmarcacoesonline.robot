*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFMarcacoesOnline
    [Tags]    smoke    cadastro-tfmarcacoesonline    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfmarcacoesonline
    Abrir Tela    acesso_tfmarcacoesonline
