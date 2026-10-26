$ErrorActionPreference = 'Stop'
if ($env:COMPUTERNAME -ne 'TESTESVM' -or -not (Get-Service VBoxService -ErrorAction SilentlyContinue)) {
    throw 'Execute apenas dentro da VM TESTESVM.'
}
$pasta = 'C:\AutomatizaPreparacao'
$idExecucao = Get-Date -Format 'yyyyMMdd-HHmmss'
$resultado = [ordered]@{computador=$env:COMPUTERNAME;data=(Get-Date).ToString('o');aplicativos=@();integracoes_iniciadas=$false;login_automatico_executado=$false}
$programas = @(
    @{Nome='Painel Acessus';Executavel='C:\acesso\Acessus.Modulo.exe';Pasta='C:\acesso';Processos=@('Acessus.Modulo.exe')},
    @{Nome='Modulo de Acesso';Executavel='C:\acesso\Acessus.exe';Pasta='C:\acesso';Processos=@('Acessus.exe')},
    @{Nome='RH Metadados';Executavel='C:\meta\rhsis\rh.exe';Pasta='C:\meta\rhsis';Processos=@('rh.exe','RHID.exe','RHPA.exe')}
)
foreach ($programa in $programas) {
    try {
        if (-not (Test-Path -LiteralPath $programa.Executavel)) { throw 'Executavel nao encontrado.' }
        $processos = @(Get-CimInstance Win32_Process | Where-Object {
            $_.Name -in $programa.Processos -and $_.ExecutablePath -and
            ([IO.Path]::GetDirectoryName($_.ExecutablePath) -eq $programa.Pasta)
        })
        if ($processos.Count) {
            $estado = 'ja estava em execucao'
        } else {
            $aberto = Start-Process -FilePath $programa.Executavel -WorkingDirectory $programa.Pasta -PassThru
            $estado = 'abertura solicitada'
        }
        Write-Host "$($programa.Nome): $estado"
        $resultado.aplicativos += [ordered]@{nome=$programa.Nome;executavel=$programa.Executavel;estado=$estado}
    } catch {
        Write-Host "$($programa.Nome): falha - $($_.Exception.Message)" -ForegroundColor Red
        $resultado.aplicativos += [ordered]@{nome=$programa.Nome;estado='falha';erro=$_.Exception.Message}
    }
}
try {
    $central = 'C:\AutomatizaTestes\scripts\central_testes.py'
    $pythonw = 'C:\AutomatizaTestes\.venv\Scripts\pythonw.exe'
    if (-not (Test-Path -LiteralPath $central) -or -not (Test-Path -LiteralPath $pythonw)) { throw 'Central ou Python nao encontrado.' }
    $jaAberta = Get-CimInstance Win32_Process -Filter "Name='pythonw.exe' OR Name='python.exe'" | Where-Object {
        $_.CommandLine -match 'C:\\AutomatizaTestes\\scripts\\central_testes\.py'
    }
    if (-not $jaAberta) {
        Start-Process -FilePath $pythonw -ArgumentList @($central) -WorkingDirectory 'C:\AutomatizaTestes' -RedirectStandardOutput (Join-Path $pasta "central-$idExecucao.stdout.log") -RedirectStandardError (Join-Path $pasta "central-$idExecucao.stderr.log") | Out-Null
    }
    $resultado.aplicativos += [ordered]@{nome='Central de testes';estado='abertura solicitada ou ja estava em execucao'}
} catch {
    $resultado.aplicativos += [ordered]@{nome='Central de testes';estado='falha';erro=$_.Exception.Message}
}
Write-Host 'Aguardando 10 segundos para conferir os processos...'
Start-Sleep -Seconds 10
$resultado.processos = @(Get-Process -Name 'Acessus','Acessus.Modulo','rh','RHID','RHPA','pythonw' -ErrorAction SilentlyContinue | Select-Object ProcessName,Id,MainWindowTitle,Responding)
$arquivo = Join-Path $pasta "abertura-$idExecucao.json"
$resultado | ConvertTo-Json -Depth 7 | Set-Content -LiteralPath $arquivo -Encoding UTF8
if (Test-Path -LiteralPath '\\VBOXSVR\ResultadoVM') {
    try {
        Get-ChildItem -LiteralPath $pasta -File -Filter "*$idExecucao*" | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination '\\VBOXSVR\ResultadoVM' -Force
        }
    } catch { Write-Warning 'Os logs de abertura ficaram apenas em C:\AutomatizaPreparacao.' }
}
Write-Host 'Abertura concluida. O relatorio distingue programas iniciados de login validado.' -ForegroundColor Green
Write-Host 'Se houver tela de login ou licenca, ela permanecera aberta para verificacao.'
exit 0
