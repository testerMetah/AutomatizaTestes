*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsMonitoramentoColaboradorVinculado
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsmonitoramentocolaboradorvinculado    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsmonitoramentocolaboradorvinculado
    Abrir Tela    estacionamento_tfrmestacionamentoviewsmonitoramentocolaboradorvinculado
