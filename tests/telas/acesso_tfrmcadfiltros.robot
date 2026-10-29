*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadFiltros
    [Tags]    smoke    cadastro-tfrmcadfiltros    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadfiltros
    Abrir Tela    acesso_tfrmcadfiltros
