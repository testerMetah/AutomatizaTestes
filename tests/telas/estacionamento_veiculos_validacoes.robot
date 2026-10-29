*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Run Keywords    Fechar Popup    AND    Fechar Tela

*** Test Cases ***
Validacoes de Veiculos
    [Tags]    cadastro-veiculos    regressao    mapa-estatico
    [Template]    Validar Campos Sem Gravar
    ${EMPTY}    ABC1234    O Nome do veículo deve ser informado.
    AUTOTEST_SEM_PLACA    ${EMPTY}    A placa do veículo deve ser informada.
    AUTOTEST_PLACA_INVALIDA    ABC1    Placa inválida!

*** Keywords ***
Validar Campos Sem Gravar
    [Arguments]    ${nome}    ${placa}    ${mensagem_esperada}
    Mapa Deve Estar Validado    estacionamento_cadastro_veiculos
    Abrir Tela    estacionamento_cadastro_veiculos
    Clicar Controle    btn_incluir
    Preencher Campo    campo_nome    ${nome}
    Preencher Campo    campo_placa    ${placa}
    Clicar Controle    btn_salvar
    ${mensagens}=    Ler Mensagem
    Mensagem Deve Conter    ${mensagens}    ${mensagem_esperada}
    Fechar Popup
    Clicar Controle    btn_cancelar
    Fechar Tela
