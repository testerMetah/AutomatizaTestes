*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistoricoEstacionamento
    [Tags]    smoke    cadastro-tfrmauditoriahistoricoestacionamento    desktop    mapa-estatico
    Mapa Deve Estar Validado    estacionamento_tfrmauditoriahistoricoestacionamento
    Abrir Tela    estacionamento_tfrmauditoriahistoricoestacionamento
