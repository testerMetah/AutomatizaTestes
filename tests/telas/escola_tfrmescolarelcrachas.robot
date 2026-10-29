*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelCrachas
    [Tags]    smoke    cadastro-tfrmescolarelcrachas    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelcrachas
    Abrir Tela    escola_tfrmescolarelcrachas
