*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsMonitoramentoGraficoOcupacaoVagas
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsmonitoramentograficoocupacaovagas    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsmonitoramentograficoocupacaovagas
    Abrir Tela    estacionamento_tfrmestacionamentoviewsmonitoramentograficoocupacaovagas
