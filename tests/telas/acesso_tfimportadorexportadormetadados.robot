*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFImportadorExportadorMetadados
    [Tags]    smoke    cadastro-tfimportadorexportadormetadados    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfimportadorexportadormetadados
    Abrir Tela    acesso_tfimportadorexportadormetadados
