param(
    [string]$Base,
    [string]$Saida
)
$ErrorActionPreference = 'Stop'
$project = Split-Path $PSScriptRoot -Parent
$venvPython = Join-Path $project '.venv\Scripts\python.exe'
$pythonCandidates = @($venvPython)
$systemPython = Get-Command python -ErrorAction SilentlyContinue
if ($systemPython) { $pythonCandidates += $systemPython.Source }
$selectedPython = $null
foreach ($candidate in ($pythonCandidates | Select-Object -Unique)) {
    if (-not (Test-Path -LiteralPath $candidate)) { continue }
    try {
        & $candidate -c 'import sys; sys.exit(0)' 2>$null
        if ($LASTEXITCODE -eq 0) { $selectedPython = $candidate; break }
    } catch { }
}
if (-not $selectedPython) {
    throw 'Nenhum Python acessível. Nenhuma instalação ou mudança foi feita.'
}
$diagnosticArgs = @()
if ($Base) { $diagnosticArgs += @('--base', $Base) }
if ($Saida) { $diagnosticArgs += @('--saida', $Saida) }
# A chamada direta (&) preserva argumentos; não inicia shell auxiliar ou worker.
$bootstrap = "import pathlib,sys,site,runpy; root=pathlib.Path(sys.argv.pop(1)); site.addsitedir(str(root/'.venv'/'Lib'/'site-packages')); sys.path.insert(0,str(root/'src')); sys.argv[0]=str(root/'scripts'/'diagnosticar_acessos.py'); runpy.run_path(sys.argv[0],run_name='__main__')"
& $selectedPython -c $bootstrap $project @diagnosticArgs
exit $LASTEXITCODE
