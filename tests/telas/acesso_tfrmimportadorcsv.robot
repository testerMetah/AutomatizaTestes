*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmImportadorCSV
    [Tags]    smoke    cadastro-tfrmimportadorcsv    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmimportadorcsv
    Abrir Tela    acesso_tfrmimportadorcsv
