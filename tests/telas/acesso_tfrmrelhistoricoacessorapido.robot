*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelHistoricoAcessoRapido
    [Tags]    smoke    cadastro-tfrmrelhistoricoacessorapido    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelhistoricoacessorapido
    Abrir Tela    acesso_tfrmrelhistoricoacessorapido
