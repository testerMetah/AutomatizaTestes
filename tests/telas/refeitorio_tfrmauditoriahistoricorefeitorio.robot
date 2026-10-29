*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistoricoRefeitorio
    [Tags]    smoke    cadastro-tfrmauditoriahistoricorefeitorio    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmauditoriahistoricorefeitorio
    Abrir Tela    refeitorio_tfrmauditoriahistoricorefeitorio
