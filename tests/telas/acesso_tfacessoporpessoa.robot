*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFAcessoPorPessoa
    [Tags]    smoke    cadastro-tfacessoporpessoa    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfacessoporpessoa
    Abrir Tela    acesso_tfacessoporpessoa
