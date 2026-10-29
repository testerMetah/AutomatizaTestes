*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsCadastro
    [Tags]    smoke    cadastro-tfrmestacionamentoviewscadastro    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewscadastro
    Abrir Tela    estacionamento_tfrmestacionamentoviewscadastro
