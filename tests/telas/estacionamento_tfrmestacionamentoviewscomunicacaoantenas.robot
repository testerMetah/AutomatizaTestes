*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsComunicacaoAntenas
    [Tags]    smoke    cadastro-tfrmestacionamentoviewscomunicacaoantenas    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewscomunicacaoantenas
    Abrir Tela    estacionamento_tfrmestacionamentoviewscomunicacaoantenas
