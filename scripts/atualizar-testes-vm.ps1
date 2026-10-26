$ErrorActionPreference = 'Stop'
if ($env:COMPUTERNAME -ne 'TESTESVM' -or -not (Get-Service VBoxService -ErrorAction SilentlyContinue)) {
    throw 'Execute somente dentro da VM TESTESVM.'
}
$origem = '\\VBOXSVR\OrigemAutomatiza'
$destino = 'C:\AutomatizaTestes'
$pythonVM = Join-Path $destino '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $pythonVM)) { throw 'Python da VM ausente. Execute primeiro COPIAR-PARA-VM.cmd.' }
if (-not (Test-Path -LiteralPath (Join-Path $destino '.env'))) { throw 'Configuracao .env da VM ausente. Nao copiar credenciais automaticamente.' }
$idAtualizacao = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$backup = Join-Path $destino "reports\atualizacao\$idAtualizacao\backup"
New-Item -ItemType Directory -Path $backup -Force | Out-Null

# Copia apenas o projeto, preservando .env, perfis, amostras e configuracoes dos sistemas.
foreach ($subpasta in @('src', 'scripts', 'examples', 'tests', 'docs')) {
    $raizOrigem = Join-Path $origem $subpasta
    if (-not (Test-Path -LiteralPath $raizOrigem)) { throw "Origem indisponivel: $raizOrigem" }
    foreach ($arquivo in Get-ChildItem -LiteralPath $raizOrigem -File -Recurse) {
        if ($arquivo.FullName -match '\\(__pycache__|\.pytest_cache)\\' -or $arquivo.Extension -eq '.pyc') { continue }
        $relativo = $arquivo.FullName.Substring($origem.Length).TrimStart('\')
        $alvo = Join-Path $destino $relativo
        if (Test-Path -LiteralPath $alvo) {
            if ((Get-FileHash -LiteralPath $arquivo.FullName).Hash -eq (Get-FileHash -LiteralPath $alvo).Hash) { continue }
            $copiaAnterior = Join-Path $backup $relativo
            New-Item -ItemType Directory -Path (Split-Path -Parent $copiaAnterior) -Force | Out-Null
            Copy-Item -LiteralPath $alvo -Destination $copiaAnterior
        }
        New-Item -ItemType Directory -Path (Split-Path -Parent $alvo) -Force | Out-Null
        Copy-Item -LiteralPath $arquivo.FullName -Destination $alvo -Force
    }
}
foreach ($documentoRaiz in @('README.md', 'CONTEXTO-PARA-CONTINUAR.md')) {
    $origemDocumento = Join-Path $origem $documentoRaiz
    $alvoDocumento = Join-Path $destino $documentoRaiz
    if (Test-Path -LiteralPath $origemDocumento) {
        if (Test-Path -LiteralPath $alvoDocumento) {
            if ((Get-FileHash -LiteralPath $origemDocumento).Hash -eq (Get-FileHash -LiteralPath $alvoDocumento).Hash) { continue }
            Copy-Item -LiteralPath $alvoDocumento -Destination (Join-Path $backup $documentoRaiz)
        }
        Copy-Item -LiteralPath $origemDocumento -Destination $alvoDocumento -Force
    }
}
Push-Location $destino
try {
    $temporarioTestes = Join-Path (Split-Path $backup -Parent) 'pytest-temp'
    & $pythonVM -m pytest tests\unit -q "--basetemp=$temporarioTestes"
    if ($LASTEXITCODE -ne 0) { throw 'Testes unitarios falharam. Confira a saida; os arquivos anteriores estao no backup.' }
    $arquivoPerfis = Join-Path (Split-Path $backup -Parent) 'perfis.json'
    & $pythonVM scripts\preparar-perfis-vm.py $arquivoPerfis
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao conferir/criar os perfis do RH.' }
    & $pythonVM scripts\verificar_preparacao.py --sql
    $codigoDiagnostico = $LASTEXITCODE
    if ($codigoDiagnostico -notin @(0, 2)) { throw 'Nao foi possivel concluir o diagnostico.' }
    Write-Host 'Atualizacao concluida. Feche e reabra a Central para carregar os novos comandos.' -ForegroundColor Green
    Write-Host 'O relatorio informa as pendencias. Nenhum teste de negocio foi executado.'
    Write-Host "Backup: $backup"
    Write-Host 'Nao e necessario executar este atualizador como administrador.'
} finally { Pop-Location }
