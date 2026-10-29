*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFRegrasAcesso
    [Tags]    smoke    cadastro-tfregrasacesso    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfregrasacesso
    Abrir Tela    acesso_tfregrasacesso
