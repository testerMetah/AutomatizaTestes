*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRelResCon
    [Tags]    smoke    cadastro-tfrmrelrescon    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmrelrescon
    Abrir Tela    acesso_tfrmrelrescon
