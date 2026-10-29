"""Análise manual dos relatórios do menu Refeitório para fichas geradas."""

BASE = "O fluxo herdado de seleção, consulta, geração e fechamento está em [base_relatorio_padrao.md](base_relatorio_padrao.md). Salvar, Excluir e Cancelar de cadastro não se aplicam a este formulário."

NOTAS = {
    "tfrmrelcreditos": [
        "`ActRelatorioExecute` separa mês e ano de `MEdMesAno.Text` por posição (`Copy`), lê `cmbOrdenar`/`cmbOrdem`, chama `ReceberDadosRelCreditos` e depois o relatório herdado. Esta procedure não valida o mês/ano; conferir a base e o controller antes de definir resultados esperados para entradas inválidas.",
        "`FormShow` foca `MEdMesAno`. O método `RgbSelecaoClick` fixa `ModeloRelatorio=RelCreditos`.",
    ],
    "tfrmrelpessoas": [
        "`ActRelatorioExecute` usa `cbSituacao.ItemIndex`, `cmbOrdenar.ItemIndex` e `cmbOrdem.ItemIndex`, chama `ReceberDadosRelPessoas` e depois o relatório herdado. Não há validação específica desses índices no form filho.",
        "`FormShow` e `RgbSelecaoClick` fixam `ModeloRelatorio=RelPessoas`.",
    ],
    "tfrmrelrescon": [
        "`ActRelatorioExecute` valida data/hora inicial e final com `ValidaCamposDataHoraIniFim`; em erro mostra a mensagem retornada e aborta. Depois usa múltiplos coletores de `GetIdsColetor`, código de `EdCardapio`, `ChkInconsistencias`, ordenação e ordem. Chama `ReceberDadosRelResCon` e a geração herdada.",
        "`btnExcluiFiltroClick` mostra `Selecione um item para excluí-lo.` quando `lbColetor` não está focado; caso contrário remove o item selecionado.",
    ],
    "tfrmrelmarcacoesonline": [
        "`ActRelatorioExecute` rejeita período com `DaysBetween > 3650` e mostra `O período informado excede o limite de 3650 dias (10 anos).`. **Dúvida:** chama `StrToDateTime` antes da validação que retornaria mensagem amigável; data malformada pode provocar exceção primeiro.",
        "Após validar o período, usa `ChkSepararDia`, múltiplos coletores (`GetIdsColetor`), coleta, situação, crachá, sentido, função, pré-cadastro (`True`), ordenação e ordem. Chama `ReceberDadosRelMarcacoesOnline` e a geração herdada.",
    ],
    "tfrmrelreservasrefeicoes": [
        "`ActRelatorioExecute` valida `MEdDataIni` e `MEdDataFim` com horas fixas `00:00` e `23:59`, mostra a mensagem e aborta se falhar. Passa cardápio (`EdCardapio`), situação (`cbSituacao`), ordenação e ordem a `ReceberDadosRelReservasRefeicoes`; depois chama a geração herdada.",
        "`FormCreate` preenche as duas datas com o dia atual. O período do relatório é inclusivo até 23:59 do fim informado no form.",
    ],
    "tfrmrelrefeicoestotal": [
        "`ActRelatorioExecute` valida data/hora inicial e final, mostra mensagem e aborta se falhar. Usa `GetIdsColetor` para múltiplos coletores, `StrToIntDef(EdCardapio.Text, 0)` para cardápio, seleção, ordenação e ordem. Chama `ReceberDadosRelRefeicoesTotal` e a geração herdada.",
        "`btnExcluiFiltroClick` mostra `Selecione um item para excluí-lo.` se `lbColetor` não está focado; caso contrário remove o item selecionado.",
    ],
}
