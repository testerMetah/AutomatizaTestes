*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmCadModeloColetores
    [Tags]    smoke    cadastro-tfrmcadmodelocoletores    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcadmodelocoletores
    Abrir Tela    acesso_tfrmcadmodelocoletores
