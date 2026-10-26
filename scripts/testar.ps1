param(
    [ValidateSet('base', 'banco', 'desktop', 'todos')]
    [string]$Grupo = 'base',
    [switch]$ConectarApenas
)
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
    throw 'Execute scripts\instalar.ps1 primeiro.'
}
New-Item -ItemType Directory -Path reports -Force | Out-Null
$report = 'reports\' + $Grupo + '-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff') + '.html'
$testArgs = @('-m', 'pytest', "--html=$report", '--self-contained-html')
if ($ConectarApenas) { $testArgs += '--conectar-apenas' }
switch ($Grupo) {
    'base' { $testArgs += @('tests\unit') }
    'banco' { $testArgs += @('tests\integration', '--real', '-m', 'banco') }
    'desktop' { $testArgs += @('tests\integration', '--real', '-m', 'desktop') }
    'todos' { $testArgs += @('--real') }
}
& .\.venv\Scripts\python.exe @testArgs
exit $LASTEXITCODE
