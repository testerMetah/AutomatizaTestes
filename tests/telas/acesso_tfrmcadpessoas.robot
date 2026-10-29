*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadPessoas
    [Tags]    smoke    cadastro-tfrmcadpessoas    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadpessoas
    Abrir Tela    acesso_tfrmcadpessoas
