*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsMonitoramentoVeiculosAcessos
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsmonitoramentoveiculosacessos    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsmonitoramentoveiculosacessos
    Abrir Tela    estacionamento_tfrmestacionamentoviewsmonitoramentoveiculosacessos
