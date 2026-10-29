*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEscolaRelAlunos
    [Tags]    smoke    cadastro-tfrmescolarelalunos    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmescolarelalunos
    Abrir Tela    escola_tfrmescolarelalunos
