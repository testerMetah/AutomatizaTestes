*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelResponsaveis
    [Tags]    smoke    cadastro-tfrmescolarelresponsaveis    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelresponsaveis
    Abrir Tela    escola_tfrmescolarelresponsaveis
