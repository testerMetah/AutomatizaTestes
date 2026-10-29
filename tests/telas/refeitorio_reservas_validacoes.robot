*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Run Keywords    Fechar Popup    AND    Fechar Tela

*** Test Cases ***
Reserva Rejeita Pessoa Ausente
    [Tags]    cadastro-reservas    regressao    desktop
    Mapa Deve Estar Validado    refeitorio_tfrmrefeitorioviewsreservasrefeicoes
    Abrir Tela    refeitorio_tfrmrefeitorioviewsreservasrefeicoes
    Clicar Controle    btn_inserir
    Clicar Controle    btn_ok
    ${mensagens}=    Ler Mensagem
    Mensagem Deve Conter    ${mensagens}    É necessário selecionar uma pessoa.
    Fechar Popup
    Clicar Controle    btn_cancelar
