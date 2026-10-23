*** Settings ***
Library    automatiza.sequencias.robot_library.SequenceLibrary

*** Test Cases ***
Checagem leitura
    [Tags]    smoke    regressao    sequencia-fixa
    Executar Sequencia    tests/sequencias/checagem_leitura.yaml

Ciclo pessoa
    [Tags]    smoke    regressao    sequencia-fixa    bloqueado
    Executar Sequencia    tests/sequencias/ciclo_pessoa.yaml

Fluxo importacao
    [Tags]    mudanca-atual    regressao    sequencia-fixa    bloqueado
    Executar Sequencia    tests/sequencias/fluxo_importacao.yaml

Volume baixo
    [Tags]    lento    regressao    sequencia-fixa    bloqueado
    Executar Sequencia    tests/sequencias/volume_baixo.yaml

Aleatoria reproduzivel
    [Tags]    regressao    sequencia-aleatoria    bloqueado
    Executar Sequencia Com Seed    4242    8
