*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmComunicacaoEquipamentos
    [Tags]    smoke    cadastro-tfrmcomunicacaoequipamentos    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmcomunicacaoequipamentos
    Abrir Tela    acesso_tfrmcomunicacaoequipamentos
