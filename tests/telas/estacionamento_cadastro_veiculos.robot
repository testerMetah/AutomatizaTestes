*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca Veiculos Sem Gravar
    [Tags]    smoke    cadastro-veiculos    desktop
    Mapa Deve Estar Validado    estacionamento_cadastro_veiculos
    Abrir Tela    estacionamento_cadastro_veiculos
    Clicar Controle    btn_incluir
    Preencher Campo    campo_nome    AUTOTEST_FUMACA_SEM_GRAVAR
    Clicar Controle    btn_cancelar
