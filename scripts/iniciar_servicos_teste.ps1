# Executar elevado. Só inicia quando os dois INIs e o projeto apontam ao banco de teste confirmado.
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$cfg = Get-Content -LiteralPath (Join-Path $root 'config\ambiente-teste.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$target = $cfg.sql_destino.banco
if ($cfg.sql_destino.confirmado_como_teste -ne $true -or $target -notmatch '^Acessus_AUTOTEST_[0-9]{8}$') {
    throw 'Banco de destino não é o banco AUTOTEST confirmado.'
}
foreach ($ini in @('C:\acesso\ConexaoConfig.ini','C:\acesso\AccessusComConfig.ini')) {
    $raw = [IO.File]::ReadAllBytes($ini)
    $content = [Text.Encoding]::GetEncoding(1252).GetString($raw)
    if ($content -notmatch '(?m)^Server=desk-tec\r?$' -or $content -notmatch "(?m)^Database=$([regex]::Escape($target))\r?$" ) {
        throw "Destino incompatível no arquivo $ini"
    }
}
$results = @()
foreach ($name in @('SrvAcessusCom','FrmViewsPrincipalService','FrmSyncImpViewsPrincipal')) {
    $service = Get-Service -Name $name -ErrorAction Stop
    try {
        if ($service.Status -ne 'Running') { Start-Service -Name $name -ErrorAction Stop }
        $service = Get-Service -Name $name
        $service.WaitForStatus('Running',[TimeSpan]::FromSeconds(30))
        $results += [pscustomobject]@{nome=$name;resultado='OK';estado='Running'}
    } catch {
        $state = (Get-Service -Name $name -ErrorAction SilentlyContinue).Status
        $results += [pscustomobject]@{nome=$name;resultado='FALHA';estado=[string]$state;erro=$_.Exception.Message}
    }
}
$folder = Join-Path $root 'reports'
New-Item -ItemType Directory -Force -Path $folder | Out-Null
$path = Join-Path $folder ('servicos-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.json')
$results | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $path -Encoding UTF8
$results | Format-Table -AutoSize | Out-String | Write-Output
if ($results.Where({$_.resultado -eq 'FALHA'}).Count -gt 0) { exit 1 }
