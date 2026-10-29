*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmMensagemColetores
    [Tags]    smoke    cadastro-tfrmmensagemcoletores    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmmensagemcoletores
    Abrir Tela    acesso_tfrmmensagemcoletores
