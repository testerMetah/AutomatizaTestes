*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadEmpresaAcesso
    [Tags]    smoke    cadastro-tfrmcadempresaacesso    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadempresaacesso
    Abrir Tela    acesso_tfrmcadempresaacesso
