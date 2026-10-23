# Diagnostico somente leitura. Nunca inicia servicos nem executa SQL de escrita.
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$config = Get-Content -LiteralPath (Join-Path $root 'config\ambiente-teste.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$results = New-Object System.Collections.Generic.List[object]
function Report($item, $ok, $detail) {
    $results.Add([pscustomobject]@{ Item=$item; Resultado=$(if($ok){'OK'}else{'FALHA'}); Detalhe=$detail })
}
function PythonBits($path) {
    $bytes = [IO.File]::ReadAllBytes($path)
    $offset = [BitConverter]::ToInt32($bytes, 0x3c)
    $machine = [BitConverter]::ToUInt16($bytes, $offset + 4)
    if ($machine -eq 0x14c) { return 32 }
    if ($machine -eq 0x8664) { return 64 }
    return 0
}
$python = Join-Path $config.python32_venv 'Scripts\python.exe'
$present = Test-Path -LiteralPath $python
Report 'venv Python' $present $python
$bits = if ($present) { PythonBits $python } else { 0 }
Report 'Python 32 bits' ($bits -eq 32) "arquitetura: $bits bits"
$app = 'C:\acesso\Acessus.exe'
Report 'Acessus.exe' (Test-Path -LiteralPath $app) $app
$drive = Get-PSDrive -Name C -ErrorAction SilentlyContinue
Report 'Espaco em disco C:' ($null -ne $drive -and $drive.Free -gt 1GB) $(if($drive){"$([math]::Round($drive.Free / 1GB, 2)) GB livres"}else{'Indisponivel'})
$git = Get-Command git -ErrorAction SilentlyContinue
if (!$git -and (Test-Path -LiteralPath 'C:\Program Files\Git\cmd\git.exe')) { $git = Get-Item -LiteralPath 'C:\Program Files\Git\cmd\git.exe' }
Report 'Git' ($null -ne $git) $(if($git){if($git.Source){$git.Source}else{$git.FullName}}else{'Nao encontrado'})
foreach ($entry in $config.servicos.PSObject.Properties) {
    $name = $entry.Value.nome_windows
    if (!$name) { Report "Servico $($entry.Name)" $false 'Nome interno pendente'; continue }
    $service = Get-CimInstance Win32_Service -Filter "Name='$name'" -ErrorAction SilentlyContinue
    Report "Servico $($entry.Name)" ($null -ne $service) $(if($service){"$($service.Name): $($service.State); inicio $($service.StartMode)"}else{"$name nao instalado"})
}
foreach ($dbConfig in @(@{Name='destino'; Value=$config.sql_destino}, @{Name='origem'; Value=$config.sql_origem})) {
    $server = $dbConfig.Value.servidor
    $database = $dbConfig.Value.banco
    Report "Banco declarado $($dbConfig.Name)" (![string]::IsNullOrWhiteSpace($server) -and ![string]::IsNullOrWhiteSpace($database) -and $dbConfig.Value.confirmado_como_teste) "$server / $database; teste confirmado: $($dbConfig.Value.confirmado_como_teste)"
if ($bits -eq 32) {
    $env:AUTOTEST_SQL_SERVER = $server
    $env:AUTOTEST_SQL_DATABASE = $database
    $env:PYTHONPATH = Join-Path $root 'src'
    $code = @'
from dataclasses import replace
from automatiza.config import Settings
from automatiza.database import SqlServer
import os
c = Settings.load()
c = replace(c, sql_server=os.environ['AUTOTEST_SQL_SERVER'], sql_database=os.environ['AUTOTEST_SQL_DATABASE'])
db = SqlServer(c)
actual = db.assert_database()
assert db.scalar('SELECT 1') == 1
print('SELECT 1 OK em ' + actual)
'@
    try {
        $output = & $python -c $code 2>&1
        Report "Conexao SQL $($dbConfig.Name) somente leitura" ($LASTEXITCODE -eq 0) $(if($LASTEXITCODE -eq 0){($output | Out-String).Trim()}else{'Falhou; conferir credenciais, driver e conectividade sem exibir segredos'})
    } catch { Report "Conexao SQL $($dbConfig.Name) somente leitura" $false 'Falhou; conferir credenciais, driver e conectividade' }
} else { Report "Conexao SQL $($dbConfig.Name) somente leitura" $false 'Nao executada: Python 32 bits indisponivel' }
}
$results | Format-Table -AutoSize | Out-String -Width 240 | Write-Output
if ($results.Where({$_.Resultado -eq 'FALHA'}).Count -gt 0) { exit 1 }
