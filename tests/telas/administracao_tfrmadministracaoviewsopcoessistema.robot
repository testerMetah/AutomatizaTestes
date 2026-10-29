*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAdministracaoViewsOpcoesSistema
    [Tags]    smoke    cadastro-tfrmadministracaoviewsopcoessistema    desktop    mapa-estatico
    Mapa Deve Estar Validado    administracao_tfrmadministracaoviewsopcoessistema
    Abrir Tela    administracao_tfrmadministracaoviewsopcoessistema
