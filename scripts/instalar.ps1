param([string]$PythonExecutable = 'python')
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
    & $PythonExecutable -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar ambiente Python.' }
}
& .\.venv\Scripts\python.exe -m pip install -e .
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependências.' }
if (-not (Test-Path -LiteralPath '.env')) {
    Copy-Item -LiteralPath '.env.example' -Destination '.env'
}
& .\.venv\Scripts\automatiza.exe diagnostico
