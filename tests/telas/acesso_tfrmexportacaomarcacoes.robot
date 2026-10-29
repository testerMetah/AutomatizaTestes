*** Settings ***
Library    automatiza.biblioteca_telas.BibliotecaTelas
Test Teardown    Fechar Tela

*** Test Cases ***
Fumaca TFrmExportacaoMarcacoes
    [Tags]    smoke    cadastro-tfrmexportacaomarcacoes    desktop    mapa-estatico
    Mapa Deve Estar Validado    acesso_tfrmexportacaomarcacoes
    Abrir Tela    acesso_tfrmexportacaomarcacoes
