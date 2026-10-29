*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistorico
    [Tags]    smoke    cadastro-tfrmauditoriahistorico    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmauditoriahistorico
    Abrir Tela    acesso_tfrmauditoriahistorico
