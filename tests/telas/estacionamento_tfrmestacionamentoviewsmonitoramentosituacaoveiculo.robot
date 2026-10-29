*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsMonitoramentoSituacaoVeiculo
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsmonitoramentosituacaoveiculo    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsmonitoramentosituacaoveiculo
    Abrir Tela    estacionamento_tfrmestacionamentoviewsmonitoramentosituacaoveiculo
