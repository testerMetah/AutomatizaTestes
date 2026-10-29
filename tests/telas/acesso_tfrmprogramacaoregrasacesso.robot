*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmProgramacaoRegrasAcesso
    [Tags]    smoke    cadastro-tfrmprogramacaoregrasacesso    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmprogramacaoregrasacesso
    Abrir Tela    acesso_tfrmprogramacaoregrasacesso
