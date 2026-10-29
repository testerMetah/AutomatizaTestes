*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAdministracaoViewsCadUsuarios
    [Tags]    smoke    cadastro-tfrmadministracaoviewscadusuarios    desktop    mapa-estatico
    Mapa Deve Estar Validado    administracao_tfrmadministracaoviewscadusuarios
    Abrir Tela    administracao_tfrmadministracaoviewscadusuarios
