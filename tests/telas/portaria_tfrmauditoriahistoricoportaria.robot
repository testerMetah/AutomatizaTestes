*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistoricoPortaria
    [Tags]    smoke    cadastro-tfrmauditoriahistoricoportaria    desktop    mapa-estatico
    Mapa Deve Estar Validado    portaria_tfrmauditoriahistoricoportaria
    Abrir Tela    portaria_tfrmauditoriahistoricoportaria
