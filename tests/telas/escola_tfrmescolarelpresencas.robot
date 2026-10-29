*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelPresencas
    [Tags]    smoke    cadastro-tfrmescolarelpresencas    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelpresencas
    Abrir Tela    escola_tfrmescolarelpresencas
