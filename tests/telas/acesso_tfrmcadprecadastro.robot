*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadPreCadastro
    [Tags]    smoke    cadastro-tfrmcadprecadastro    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadprecadastro
    Abrir Tela    acesso_tfrmcadprecadastro
