*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmModuloViewsNovidades
    [Tags]    smoke    cadastro-tfrmmoduloviewsnovidades    desktop    mapa-estatico
    Mapa Deve Estar Validado    modulo_tfrmmoduloviewsnovidades
    Abrir Tela    modulo_tfrmmoduloviewsnovidades
