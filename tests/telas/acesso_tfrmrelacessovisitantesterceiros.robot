*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelAcessoVisitantesTerceiros
    [Tags]    smoke    cadastro-tfrmrelacessovisitantesterceiros    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelacessovisitantesterceiros
    Abrir Tela    acesso_tfrmrelacessovisitantesterceiros
