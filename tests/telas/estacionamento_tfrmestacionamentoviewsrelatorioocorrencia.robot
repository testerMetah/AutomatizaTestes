*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmEstacionamentoViewsRelatorioOcorrencia
    [Tags]    smoke    cadastro-tfrmestacionamentoviewsrelatorioocorrencia    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmestacionamentoviewsrelatorioocorrencia
    Abrir Tela    estacionamento_tfrmestacionamentoviewsrelatorioocorrencia
