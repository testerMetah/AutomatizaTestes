$ErrorActionPreference = 'Stop'
Write-Host 'Verificando o Windows da VM e as pastas de origem...'

# Execute somente no Windows convidado. As origens sao compartilhamentos readonly.
if ($env:COMPUTERNAME -ne 'TESTESVM' -or -not (Get-Service VBoxService -ErrorAction SilentlyContinue)) {
    throw 'Este script deve ser executado dentro da VM TESTESVM, nunca na maquina principal.'
}

if (Get-Process -Name robocopy -ErrorAction SilentlyContinue) {
    Write-Host 'Uma copia ja esta em andamento. Acompanhando sem iniciar outra...'
    & (Join-Path $PSScriptRoot 'acompanhar-copia-vm.ps1') -AteEncerrar
    return
}

$copias = @(
    @{ Origem = '\\VBOXSVR\OrigemAcessus'; Destino = 'C:\acesso' },
    @{ Origem = '\\VBOXSVR\OrigemRH'; Destino = 'C:\meta' },
    @{ Origem = '\\VBOXSVR\OrigemMetahConnect'; Destino = 'C:\MetahConnect' },
    @{ Origem = '\\VBOXSVR\OrigemAutomatiza'; Destino = 'C:\AutomatizaTestes' }
)

foreach ($copia in $copias) {
    if (-not (Test-Path -LiteralPath $copia.Origem)) {
        throw "Compartilhamento indisponivel: $($copia.Origem). Avise para reativarmos as pastas no VirtualBox."
    }
}
if ((Get-PSDrive C).Free -lt 12GB) {
    throw 'Libere pelo menos 12 GB no disco C: da VM antes de copiar.'
}

$pastaLog = 'C:\AutomatizaPreparacao'
New-Item -ItemType Directory -Path $pastaLog -Force | Out-Null
$log = Join-Path $pastaLog ('copia-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.log')

$etapa = 0
foreach ($copia in $copias) {
    $etapa++
    Write-Host "Copiando $($copia.Origem) para $($copia.Destino)..."
    $argumentos = @(
        $copia.Origem, $copia.Destino,
        '/E', '/XJ', '/XC', '/XN', '/XO', '/R:1', '/W:1', '/NP', '/NFL', '/NDL', '/TEE',
        "/LOG+:$log"
    )
    if ($copia.Destino -eq 'C:\AutomatizaTestes') {
        $argumentos += @('/XD', '.venv', '.git', '__pycache__', '.pytest_cache', 'reports', 'artifacts')
        $argumentos += @('/XF', '.env', '*.pyc')
    }
    $linhaArgumentos = ($argumentos | ForEach-Object { '"' + $_ + '"' }) -join ' '
    $inicioEtapa = Get-Date
    $processoCopia = Start-Process -FilePath "$env:SystemRoot\System32\robocopy.exe" -ArgumentList $linhaArgumentos -WindowStyle Hidden -PassThru
    $null = $processoCopia.Handle
    while (-not $processoCopia.WaitForExit(10000)) {
        $decorrido = (Get-Date) - $inicioEtapa
        $mensagem = '[{0}] Etapa {1}/4: {2} -> {3}. Copia em execucao ha {4:n0} segundos.' -f (Get-Date -Format 'HH:mm:ss'), $etapa, $copia.Origem, $copia.Destino, $decorrido.TotalSeconds
        Write-Host $mensagem
        Add-Content -LiteralPath (Join-Path $pastaLog 'progresso.log') -Value $mensagem
    }
    $processoCopia.WaitForExit()
    if ($null -eq $processoCopia.ExitCode) {
        throw "Nao foi possivel confirmar o resultado da copia. Consulte $log."
    }
    if ($processoCopia.ExitCode -ge 8) {
        Get-Content -LiteralPath $log -Tail 25
        throw "Falha de copia. Consulte $log. Pode repetir o script para copiar os arquivos faltantes."
    }
    Write-Host "Etapa $etapa/4 concluida: $($copia.Destino)."
}

Write-Host ''
Write-Host 'COPIA CONCLUIDA. Os arquivos da maquina principal foram apenas lidos.' -ForegroundColor Green
Write-Host 'Arquivos que ja existiam na VM foram preservados.'
Write-Host 'Nao abra os sistemas nem inicie integracoes ainda: as conexoes copiadas precisam apontar para as bases de teste.'
Write-Host 'SQL Server, bases e dependencias ainda precisam ser preparados.'
Write-Host "Log: $log"
