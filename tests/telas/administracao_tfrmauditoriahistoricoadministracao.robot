*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmAuditoriaHistoricoAdministracao
    [Tags]    smoke    cadastro-tfrmauditoriahistoricoadministracao    desktop    mapa-estatico
    Mapa Deve Estar Validado    administracao_tfrmauditoriahistoricoadministracao
    Abrir Tela    administracao_tfrmauditoriahistoricoadministracao
