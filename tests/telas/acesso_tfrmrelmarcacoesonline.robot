*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelMarcacoesOnline
    [Tags]    smoke    cadastro-tfrmrelmarcacoesonline    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelmarcacoesonline
    Abrir Tela    acesso_tfrmrelmarcacoesonline
