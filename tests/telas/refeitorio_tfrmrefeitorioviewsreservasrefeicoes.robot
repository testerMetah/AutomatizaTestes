*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmRefeitorioViewsReservasRefeicoes
    [Tags]    smoke    cadastro-tfrmrefeitorioviewsreservasrefeicoes    desktop    mapa-estatico
    Mapa Deve Estar Validado    refeitorio_tfrmrefeitorioviewsreservasrefeicoes
    Abrir Tela    refeitorio_tfrmrefeitorioviewsreservasrefeicoes
    Clicar Controle    btn_inserir
    Clicar Controle    btn_cancelar
