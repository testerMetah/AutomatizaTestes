*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsCadastroOcorrencias
    [Tags]    smoke    cadastro-tfrmestacionamentoviewscadastroocorrencias    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewscadastroocorrencias
    Abrir Tela    estacionamento_tfrmestacionamentoviewscadastroocorrencias
