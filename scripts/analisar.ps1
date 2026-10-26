param(
    [ValidateSet('seguir', 'gerar', 'status', 'parar', 'registrar', 'exportar', 'referencias')]
    [string]$Acao = 'seguir',
    [ValidateRange(5, 3600)]
    [int]$IntervaloSegundos = 10,
    [string]$Arquivo
)
$ErrorActionPreference = 'Stop'
$project = Split-Path $PSScriptRoot -Parent
$python = Join-Path $project '.venv\Scripts\python.exe'
Set-Location -LiteralPath $project
if (-not (Test-Path -LiteralPath $python)) { throw 'Execute scripts\instalar.ps1 primeiro.' }
if ($Acao -ne 'seguir') {
    $command = switch ($Acao) {
        'gerar' { 'analisar' }
        'status' { 'analise-status' }
        'parar' { 'parar-analise' }
        'registrar' { 'registrar-caso' }
        'exportar' { 'exportar-evidencias' }
        'referencias' { 'atualizar-referencias' }
    }
    $cliArgs = @('-m', 'automatiza.cli', $command)
    if ($Acao -eq 'registrar') {
        if ([string]::IsNullOrWhiteSpace($Arquivo)) { throw 'Informe -Arquivo com o caso preparado.' }
        $cliArgs += @('--arquivo', $Arquivo)
    }
    & $python @cliArgs
    exit $LASTEXITCODE
}
$base = Join-Path $project 'reports\observacao'
if (-not (Test-Path -LiteralPath (Join-Path $base 'ativo.json'))) { throw 'Inicie a coleta com scripts\observar.ps1 primeiro.' }
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$worker = Start-Process -FilePath $python -ArgumentList @('-m', 'automatiza.cli', 'seguir-analise', '--intervalo', "$IntervaloSegundos") `
    -WorkingDirectory $project -WindowStyle Hidden -RedirectStandardOutput (Join-Path $base "analise-$stamp.out.log") `
    -RedirectStandardError (Join-Path $base "analise-$stamp.err.log") -PassThru
if ($worker.WaitForExit(1000)) {
    Get-Content -LiteralPath (Join-Path $base "analise-$stamp.out.log") -ErrorAction SilentlyContinue
    Get-Content -LiteralPath (Join-Path $base "analise-$stamp.err.log") -ErrorAction SilentlyContinue
    if ($worker.ExitCode -ne 0) { throw 'A análise não iniciou. Verifique a saída acima.' }
}
Write-Output "Análise iniciada em segundo plano (PID $($worker.Id)). Usa arquivos locais e consulta estados dos serviços."
Write-Output 'Status: .\scripts\analisar.ps1 -Acao status'
