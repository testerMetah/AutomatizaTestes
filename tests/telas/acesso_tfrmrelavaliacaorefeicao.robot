*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelAvaliacaoRefeicao
    [Tags]    smoke    cadastro-tfrmrelavaliacaorefeicao    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelavaliacaorefeicao
    Abrir Tela    acesso_tfrmrelavaliacaorefeicao
