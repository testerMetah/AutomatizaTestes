param(
    [ValidateSet('ambos', 'acesso', 'rh')]
    [string]$Sistema = 'ambos'
)
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
    throw 'Execute scripts\instalar.ps1 primeiro.'
}
$command = switch ($Sistema) {
    'ambos' { 'iniciar' }
    'acesso' { 'abrir' }
    'rh' { 'rh' }
}
& .\.venv\Scripts\python.exe -m automatiza.cli $command
exit $LASTEXITCODE
