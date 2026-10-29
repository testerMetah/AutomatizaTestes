"""Notas de leitura manual das procedures dos cadastros de coletores."""

NOTAS = {
    "tfrmcadmodelocoletores": [
        "`ValidarCampos`: Nome vazio mostra `O Nome do Modelo de coletores é obrigatório.`; Marca convertida para inteiro <= 0 mostra `A Marca do Modelo de coletores é obrigatório.`; formato por caractere sem separador mostra `Para este tipo de Formato de Campo é obrigatório informar o Caracter.`. Cada caso aborta o salvamento.",
        "`GravaCampos`: grava Nome e ID da Marca por `FModeloColetoresController.Inserir/Atualizar`. Após isso chama `GravaCamposLayout`, que insere/atualiza linhas de layout e exclui as marcadas. O retorno de `GravaCamposLayout` não é verificado em `GravaCampos`: dúvida sobre consistência em falha parcial.",
        "`ActExcluirExecute`: confirma `Excluir o registro?`, chama `FModeloColetoresController.Excluir` e retira a linha do dataset se bem-sucedido. Em falha mostra `Problemas com a exclusão no Banco de Dados!` seguido de CR e `Certifique-se de que o servidor esteja ligado e a rede não esteja congestionada!`.",
        "`ActCancelarExecute`: cancela edição do dataset de layout, libera lista de exclusão de layout e chama o Cancelar herdado. Não há relatório nesta unit.",
        "Fonte: `Acesso/uFrmCadModeloColetores.pas`, procedures `ValidarCampos`, `GravaCampos`, `GravaCamposLayout`, `ActExcluirExecute` e `ActCancelarExecute`. Dúvida: verificar no DAO se exclusão do modelo afeta coletores já associados.",
    ],
    "tfrmcadcoletores": [
        "`ValidarCampos`: Nome e Modelo obrigatórios; IP precisa passar `ValidarIP` e ser único entre coletores. Mensagens: `O Nome do coletor é obrigatório.`, `O Modelo do coletor é obrigatório.`, `Endereço IP inválido!`. IP duplicado mostra `Este endereço IP está sendo usado pelo coletor: ` + CR + ID/Nome + CR + `Informe outro endereço IP.`.",
        "`ValidarCampos`: Dimep Micropoint, Biopoint e TopData Fit exigem Terminal positivo e exclusivo por marca. Micropoint exige Sentido de Entrada, Acionamento e Nº de Funis; as mensagens literais são `O Sentido de Entra da do coletor deve ser informado.`, `O Acionamento do coletor deve ser informado.` e `O Nº de Funis do coletor deve ser informado.`.",
        "`ValidarCampos`: TopData Fit exige TimeOut de 1 a 65 com `O TimeOut do coletor deve ser de 1 até 65.`. Em Micropoint/Biopoint a condição usa `> 65 and < 1`, impossível para um único valor: dúvida/possível defeito; não usar como asserção de faixa nessas marcas sem confirmar o build.",
        "`ValidarCampos`: Função de Acesso obrigatória (`É necessário informar a Função de Acesso.`); funções de Acesso, Reserva e Consumo não podem repetir o mesmo valor (`Funções não podem ter o mesmo valor.`). Campos obrigatórios por marca são selecionados pela aba de configuração.",
        "`ActExcluirExecute`: aviso exato fixo `ATENÇÃO! Ao fazer exclusão de um coletor todos os dados relacionados a ele, incluindo MARCAÇÕES ONLINE, serão PERDIDOS PERMANENTEMENTE.` seguido de quebra de linha e `Tem certeza que deseja excluir este coletor?`; só exclui após Sim. O código declara perda permanente; confirmar no DAO e no banco de teste antes de automatizar.",
        "`ActCancelarExecute`: chama o Cancelar herdado e seleciona aba Geral. `GravaCampos` primeiro chama `EdModelo.OnExit`, valida/monta IP e preenche `FColetoresModel` com dados das abas antes de persistir via controller. Não há relatório nesta unit.",
        "Fonte: `Acesso/uFrmCadColetores.pas`, procedures `ValidarCampos`, `GravaCampos`, `ActExcluirExecute` e `ActCancelarExecute`.",
    ],
}
