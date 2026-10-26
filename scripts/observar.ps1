param(
    [ValidateSet('iniciar', 'status', 'parar', 'anotar')]
    [string]$Acao = 'iniciar',
    [ValidateRange(1, 1440)]
    [double]$DuracaoMinutos = 120,
    [ValidateRange(5, 3600)]
    [int]$IntervaloSegundos = 15,
    [int[]]$Pessoas,
    [string]$Nota,
    [string]$DadosArquivo,
    [switch]$SemAnalise
)
$ErrorActionPreference = 'Stop'
$project = Split-Path $PSScriptRoot -Parent
$python = Join-Path $project '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) { throw 'Execute scripts\instalar.ps1 primeiro.' }
Set-Location -LiteralPath $project
if ($Acao -eq 'status') {
    & $python -m automatiza.cli observar-status
    exit $LASTEXITCODE
}
if ($Acao -eq 'parar') {
    & $python -m automatiza.cli parar-observacao
    exit $LASTEXITCODE
}
if ($Acao -eq 'anotar') {
    if ([string]::IsNullOrWhiteSpace($Nota)) { throw 'Informe -Nota com a ação manual e a pessoa/período envolvidos.' }
    $noteArgs = @('-m', 'automatiza.cli', 'anotar', '--nota', $Nota)
    if ($DadosArquivo) { $noteArgs += @('--arquivo', $DadosArquivo) }
    & $python @noteArgs
    exit $LASTEXITCODE
}
$logDir = Join-Path $project 'reports\observacao'
New-Item -ItemType Directory -Path $logDir -Force | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$stdout = Join-Path $logDir "processo-$stamp.out.log"
$stderr = Join-Path $logDir "processo-$stamp.err.log"
$seconds = ($DuracaoMinutos * 60).ToString([System.Globalization.CultureInfo]::InvariantCulture)
$arguments = @('-m', 'automatiza.cli', 'observar', '--duracao', $seconds, '--intervalo', "$IntervaloSegundos")
if ($Pessoas.Count) { $arguments += '--pessoas'; $arguments += ($Pessoas | ForEach-Object { "$_" }) }
$previousFolder = $null
$activePath = Join-Path $logDir 'ativo.json'
if (Test-Path -LiteralPath $activePath) { $previousFolder = (Get-Content -LiteralPath $activePath -Raw -Encoding UTF8 | ConvertFrom-Json).pasta }
$worker = Start-Process -FilePath $python -ArgumentList $arguments -WorkingDirectory $project -WindowStyle Hidden `
    -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
if ($worker.WaitForExit(1000)) {
    Get-Content -LiteralPath $stdout -ErrorAction SilentlyContinue
    Get-Content -LiteralPath $stderr -ErrorAction SilentlyContinue
    if ($worker.ExitCode -ne 0) { throw 'O observador não iniciou. Verifique a saída acima.' }
}
Write-Output "Observador SQL iniciado em segundo plano (PID $($worker.Id)). Não abre janelas dos sistemas."
Write-Output "Duração: $DuracaoMinutos minuto(s). Intervalo: $IntervaloSegundos segundo(s)."
Write-Output 'Status: .\scripts\observar.ps1 -Acao status'
Write-Output 'Parar:  .\scripts\observar.ps1 -Acao parar'
if (-not $SemAnalise) {
    $ready = $false
    for ($attempt = 0; $attempt -lt 40; $attempt++) {
        if (Test-Path -LiteralPath $activePath) {
            $currentFolder = (Get-Content -LiteralPath $activePath -Raw -Encoding UTF8 | ConvertFrom-Json).pasta
            if ($currentFolder -and $currentFolder -ne $previousFolder -and (Test-Path -LiteralPath (Join-Path $currentFolder 'inicial.json'))) {
                $ready = $true
                break
            }
        }
        if ($worker.HasExited) { break }
        Start-Sleep -Milliseconds 250
    }
    if ($ready) {
        & (Join-Path $PSScriptRoot 'analisar.ps1') -Acao seguir
    } else {
        Write-Output 'A primeira amostra ainda não está disponível. Após a coleta iniciar, use .\scripts\analisar.ps1.'
    }
}
