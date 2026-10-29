*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelCreditos
    [Tags]    smoke    cadastro-tfrmrelcreditos    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmrelcreditos
    Abrir Tela    refeitorio_tfrmrelcreditos
