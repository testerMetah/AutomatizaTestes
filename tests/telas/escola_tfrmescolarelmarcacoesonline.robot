*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelMarcacoesOnline
    [Tags]    smoke    cadastro-tfrmescolarelmarcacoesonline    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelmarcacoesonline
    Abrir Tela    escola_tfrmescolarelmarcacoesonline
