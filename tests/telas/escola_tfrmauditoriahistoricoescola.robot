*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistoricoEscola
    [Tags]    smoke    cadastro-tfrmauditoriahistoricoescola    desktop    mapa-estatico
    Mapa Deve Estar Validado    escola_tfrmauditoriahistoricoescola
    Abrir Tela    escola_tfrmauditoriahistoricoescola
