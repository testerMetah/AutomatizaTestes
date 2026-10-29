*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelPessoas
    [Tags]    smoke    cadastro-tfrmrelpessoas    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelpessoas
    Abrir Tela    acesso_tfrmrelpessoas
