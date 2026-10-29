*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmLayoutExportacao
    [Tags]    smoke    cadastro-tfrmlayoutexportacao    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmlayoutexportacao
    Abrir Tela    acesso_tfrmlayoutexportacao
