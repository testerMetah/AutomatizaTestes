*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsMonitoramentoVeiculosOcorrencias
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsmonitoramentoveiculosocorrencias    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsmonitoramentoveiculosocorrencias
    Abrir Tela    estacionamento_tfrmestacionamentoviewsmonitoramentoveiculosocorrencias
