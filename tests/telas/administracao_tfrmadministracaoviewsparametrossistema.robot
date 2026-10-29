*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAdministracaoViewsParametrosSistema
    [Tags]    smoke    cadastro-tfrmadministracaoviewsparametrossistema    desktop    mapa-estatico
    Mapa Deve Estar Validado    administracao_tfrmadministracaoviewsparametrossistema
    Abrir Tela    administracao_tfrmadministracaoviewsparametrossistema
