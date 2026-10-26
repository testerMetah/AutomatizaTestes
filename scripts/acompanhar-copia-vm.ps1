param([switch]$AteEncerrar)
$ErrorActionPreference = 'Stop'
if ($env:COMPUTERNAME -ne 'TESTESVM') {
    throw 'Execute este monitor dentro da VM TESTESVM.'
}
Write-Host 'Monitor da copia. Atualiza a cada 10 segundos. Pode fechar esta janela sem interromper a copia.'
Write-Host 'As mensagens mostram a etapa ativa; nao representam uma porcentagem de conclusao.'
$semProcesso = 0
while ($true) {
    $log = Get-ChildItem -LiteralPath 'C:\AutomatizaPreparacao' -Filter 'copia-*.log' -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 1
    $processos = @(Get-Process -Name robocopy -ErrorAction SilentlyContinue)
    if ($log) {
        $destino = Get-Content -LiteralPath $log.FullName -Tail 100 |
            Select-String -Pattern '^\s*Destino\s*:' | Select-Object -Last 1
        $etapa = if ($destino) { $destino.Line.Trim() } else { 'Verificando a etapa no log' }
        $estado = if ($processos.Count) { 'Robocopy ativo' } else { 'Robocopy nao esta ativo; confira o resultado na janela da copia' }
        $mensagem = '[{0}] {1} | {2}' -f (Get-Date -Format 'HH:mm:ss'), $etapa, $estado
        Write-Host $mensagem
        Add-Content -LiteralPath 'C:\AutomatizaPreparacao\monitor.log' -Value $mensagem
    } else {
        Write-Host ('[{0}] Aguardando o arquivo de log da copia...' -f (Get-Date -Format 'HH:mm:ss'))
    }
    if ($processos.Count) { $semProcesso = 0 } else { $semProcesso++ }
    if ($AteEncerrar -and $semProcesso -ge 3) {
        Write-Host 'A copia deixou de executar. Confira o resultado na janela que iniciou a transferencia.'
        return
    }
    Start-Sleep -Seconds 10
}
