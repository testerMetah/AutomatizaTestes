*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFGerarAcesso
    [Tags]    smoke    cadastro-tfgeraracesso    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfgeraracesso
    Abrir Tela    acesso_tfgeraracesso
