*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFExportadorMetadados
    [Tags]    smoke    cadastro-tfexportadormetadados    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfexportadormetadados
    Abrir Tela    acesso_tfexportadormetadados
