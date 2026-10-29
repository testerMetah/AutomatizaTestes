*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelPreCadastro
    [Tags]    smoke    cadastro-tfrmrelprecadastro    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelprecadastro
    Abrir Tela    acesso_tfrmrelprecadastro
