*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAcessosAutorizados
    [Tags]    smoke    cadastro-tfrmacessosautorizados    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmacessosautorizados
    Abrir Tela    acesso_tfrmacessosautorizados
