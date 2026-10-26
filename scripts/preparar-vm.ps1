param([switch]$SomenteODBC17, [switch]$DiagnosticarODBC, [switch]$ConectarServidores, [switch]$PrepararAbertura)
$ErrorActionPreference = 'Stop'
if ($env:COMPUTERNAME -ne 'TESTESVM' -or -not (Get-Service VBoxService -ErrorAction SilentlyContinue)) {
    throw 'Execute apenas dentro da VM TESTESVM.'
}
$identidade = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($identidade)
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host 'Confirme Sim na janela do Windows para instalar os componentes na VM.'
    $argumentosElevacao = '-NoProfile -ExecutionPolicy Bypass -File "' + $PSCommandPath + '"'
    if ($SomenteODBC17) { $argumentosElevacao += ' -SomenteODBC17' }
    if ($DiagnosticarODBC) { $argumentosElevacao += ' -DiagnosticarODBC' }
    if ($ConectarServidores) { $argumentosElevacao += ' -ConectarServidores' }
    if ($PrepararAbertura) { $argumentosElevacao += ' -PrepararAbertura' }
    try {
        $elevado = Start-Process -FilePath "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" -Verb RunAs -ArgumentList $argumentosElevacao -WorkingDirectory $env:SystemRoot -PassThru
        $null = $elevado.Handle
        $elevado.WaitForExit()
        if ($null -eq $elevado.ExitCode) { throw 'Nao foi possivel confirmar o resultado da janela de administrador.' }
        exit $elevado.ExitCode
    } catch {
        Write-Host ('Nao foi possivel iniciar a preparacao como administrador: ' + $_.Exception.Message) -ForegroundColor Red
        exit 1
    }
}

Write-Host 'Preparador iniciado dentro da VM.' -ForegroundColor Cyan
$pasta = 'C:\AutomatizaPreparacao'
New-Item -ItemType Directory -Path $pasta -Force | Out-Null
$idExecucao = Get-Date -Format 'yyyyMMdd-HHmmss'
$transcricao = Join-Path $pasta "preparacao-$idExecucao.log"
$script:resultado = [ordered]@{
    computador = $env:COMPUTERNAME
    inicio = (Get-Date).ToString('o')
    estado = 'em_andamento'
    etapa = 'inicio'
    etapas = @()
    bases_restauradas = $false
    sistemas_iniciados = $false
}

function Publicar-Estado {
    $script:resultado.atualizado = (Get-Date).ToString('o')
    $nomeEstado = if ($DiagnosticarODBC) { "estado-diagnostico-$idExecucao.json" } else { 'estado.json' }
    $arquivo = Join-Path $pasta $nomeEstado
    $script:resultado | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $arquivo -Encoding UTF8
    if (Test-Path -LiteralPath '\\VBOXSVR\ResultadoVM') {
        try {
            Copy-Item -LiteralPath $arquivo -Destination (Join-Path '\\VBOXSVR\ResultadoVM' $nomeEstado) -Force
            Get-ChildItem -LiteralPath $pasta -Filter "*$idExecucao*" -File | ForEach-Object {
                Copy-Item -LiteralPath $_.FullName -Destination '\\VBOXSVR\ResultadoVM' -Force -ErrorAction Stop
            }
        } catch {
            Write-Warning 'Nao foi possivel publicar os logs. Eles continuam salvos em C:\AutomatizaPreparacao.'
        }
    }
}

function Executar-Etapa {
    param([string]$Nome, [string]$Executavel, [string[]]$Argumentos, [int[]]$CodigosAceitos = @(0), [int]$LimiteMinutos = 60, [switch]$ExibirSaida)
    $script:resultado.etapa = $Nome
    Write-Host "INICIANDO: $Nome" -ForegroundColor Cyan
    Publicar-Estado
    $indice = $script:resultado.etapas.Count + 1
    $stdout = Join-Path $pasta "etapa-$indice-$idExecucao.stdout.log"
    $stderr = Join-Path $pasta "etapa-$indice-$idExecucao.stderr.log"
    $linha = ($Argumentos | ForEach-Object {
        if ($_ -match '["\r\n]') { throw 'Argumento inesperado no instalador.' }
        if ($_ -match '\s' -or $_ -eq '') { '"' + $_ + '"' } else { $_ }
    }) -join ' '
    $inicio = Get-Date
    $processo = Start-Process -FilePath $Executavel -ArgumentList $linha -WorkingDirectory 'C:\AutomatizaTestes' -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    # PowerShell 5.1 precisa manter o handle aberto para ler ExitCode apos o termino.
    $null = $processo.Handle
    while (-not $processo.WaitForExit(10000)) {
        $decorrido = (Get-Date) - $inicio
        Write-Host ('[{0}] {1} - em execucao ha {2:n0} segundos.' -f (Get-Date -Format 'HH:mm:ss'), $Nome, $decorrido.TotalSeconds)
        Publicar-Estado
        if ($decorrido.TotalMinutes -gt $LimiteMinutos) {
            throw "A etapa $Nome excedeu o tempo esperado. O instalador nao foi encerrado; verifique os logs antes de repetir."
        }
    }
    $processo.WaitForExit()
    $codigo = $processo.ExitCode
    if ($null -eq $codigo) {
        throw "Nao foi possivel ler o codigo de saida de $Nome. Consulte $stdout antes de repetir."
    }
    $script:resultado.etapas += [ordered]@{nome=$Nome; codigo=$codigo; segundos=[math]::Round(((Get-Date)-$inicio).TotalSeconds); log=$stdout}
    Publicar-Estado
    if ($codigo -notin $CodigosAceitos) {
        Get-Content -LiteralPath $stdout -Tail 20
        Get-Content -LiteralPath $stderr -Tail 15
        throw "Falha em $Nome. Codigo: $codigo. Logs em $pasta."
    }
    if ($codigo -eq 3010) { throw 'O Windows precisa ser reiniciado. Reinicie a VM e abra o mesmo arquivo novamente.' }
    if ($ExibirSaida) { Get-Content -LiteralPath $stdout }
    Write-Host "CONCLUIDO: $Nome" -ForegroundColor Green
}

function Coletar-LogsSQL {
    $destino = Join-Path $pasta "sql-$idExecucao"
    New-Item -ItemType Directory -Path $destino -Force | Out-Null
    foreach ($versao in @('170', '160')) {
        $raiz = Join-Path $env:ProgramFiles "Microsoft SQL Server\$versao"
        $bootstrap = Join-Path $raiz 'Setup Bootstrap\Log'
        if (Test-Path -LiteralPath $bootstrap) {
            $arquivos = @(Get-ChildItem -LiteralPath $bootstrap -File -ErrorAction SilentlyContinue)
            $sessoes = Get-ChildItem -LiteralPath $bootstrap -Directory -ErrorAction SilentlyContinue |
                Sort-Object LastWriteTime -Descending | Select-Object -First 2
            foreach ($sessao in $sessoes) {
                $arquivos += Get-ChildItem -LiteralPath $sessao.FullName -File -ErrorAction SilentlyContinue |
                    Where-Object { $_.Name -match '^(Summary.*\.txt|Detail.*\.txt|SystemConfigurationCheck_Report\.htm)$' }
            }
            foreach ($arquivo in $arquivos) {
                Copy-Item -LiteralPath $arquivo.FullName -Destination (Join-Path $destino "$versao-$($arquivo.Directory.Name)-$($arquivo.Name)") -Force
            }
        }
        $ssei = Join-Path $raiz 'SSEI\LogFiles'
        if (Test-Path -LiteralPath $ssei) {
            Get-ChildItem -LiteralPath $ssei -File | Sort-Object LastWriteTime -Descending | Select-Object -First 4 |
                ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $destino "$versao-SSEI-$($_.Name)") -Force }
        }
    }
    Get-ChildItem -LiteralPath $env:TEMP -Filter 'sqlsetup*.log' -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 4 |
        ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $destino $_.Name) -Force }
    if (Get-ChildItem -LiteralPath $destino -File) {
        Compress-Archive -Path (Join-Path $destino '*') -DestinationPath "$destino.zip" -Force
        Write-Host "Logs detalhados do SQL coletados em $destino.zip"
    }
}

function Get-RegistrosODBCSQL {
    # Consulte o registro diretamente: o provedor CIM pode manter a lista antiga.
    foreach ($vista in @([Microsoft.Win32.RegistryView]::Registry64, [Microsoft.Win32.RegistryView]::Registry32)) {
        $base = [Microsoft.Win32.RegistryKey]::OpenBaseKey([Microsoft.Win32.RegistryHive]::LocalMachine, $vista)
        try {
            $lista = $base.OpenSubKey('SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers')
            try {
                foreach ($versao in @(17, 18)) {
                    $nome = "ODBC Driver $versao for SQL Server"
                    $chave = $base.OpenSubKey("SOFTWARE\ODBC\ODBCINST.INI\$nome")
                    try {
                        $registroLista = if ($lista) { $lista.GetValue($nome) } else { $null }
                        if ($chave -or $null -ne $registroLista) {
                            $dll = if ($chave) { [string]$chave.GetValue('Driver') } else { '' }
                            [pscustomobject]@{
                                Name = $nome
                                Platform = if ($vista -eq [Microsoft.Win32.RegistryView]::Registry64) { '64-bit' } else { '32-bit' }
                                Registro = $registroLista
                                Driver = $dll
                                ArquivoPresente = [bool]($dll -and (Test-Path -LiteralPath ([Environment]::ExpandEnvironmentVariables($dll))))
                            }
                        }
                    } finally { if ($chave) { $chave.Dispose() } }
                }
            } finally { if ($lista) { $lista.Dispose() } }
        } finally { $base.Dispose() }
    }
}

function Get-ProdutosODBC18 {
    # ProductsEx inclui os pacotes MSI internos que nao aparecem no Painel de Controle.
    # Nao use Win32_Product: sua consulta pode disparar reparos de outros aplicativos.
    $instaladorMSI = New-Object -ComObject WindowsInstaller.Installer
    try {
        foreach ($produtoMSI in $instaladorMSI.ProductsEx('', '', 7)) {
            $nomeMSI = $produtoMSI.InstallProperty('ProductName')
            if ($nomeMSI -notmatch '^Microsoft ODBC Driver 18(?:\s|$)') { continue }
            # PowerShell 5.1 nao expoe estas propriedades COM por acesso direto.
            $codigoMSI = $produtoMSI.GetType().InvokeMember('ProductCode', [System.Reflection.BindingFlags]::GetProperty, $null, $produtoMSI, $null)
            if ($codigoMSI -notmatch '^\{[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}\}$') {
                throw 'O Windows Installer retornou um codigo inesperado para ODBC 18.'
            }
            [pscustomobject]@{
                Nome = $nomeMSI
                Versao = $produtoMSI.InstallProperty('VersionString')
                ProductCode = $codigoMSI
                Vista = 'WindowsInstaller'
                Idioma = $produtoMSI.InstallProperty('Language')
            }
        }
    } finally { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($instaladorMSI) }
    foreach ($vista in @([Microsoft.Win32.RegistryView]::Registry64, [Microsoft.Win32.RegistryView]::Registry32)) {
        $base = [Microsoft.Win32.RegistryKey]::OpenBaseKey([Microsoft.Win32.RegistryHive]::LocalMachine, $vista)
        try {
            $lista = $base.OpenSubKey('SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
            try {
                if (-not $lista) { continue }
                foreach ($codigoProduto in $lista.GetSubKeyNames()) {
                    $produto = $lista.OpenSubKey($codigoProduto)
                    try {
                        if ($produto -and $produto.GetValue('DisplayName') -eq 'Microsoft ODBC Driver 18 for SQL Server') {
                            if ($codigoProduto -notmatch '^\{[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}\}$') {
                                throw 'Registro do ODBC 18 nao tem um ProductCode MSI reconhecido; nenhuma remocao manual sera feita.'
                            }
                            [pscustomobject]@{Nome=$produto.GetValue('DisplayName'); Versao=$produto.GetValue('DisplayVersion'); ProductCode=$codigoProduto; Vista=[string]$vista}
                        }
                    } finally { if ($produto) { $produto.Dispose() } }
                }
            } finally { if ($lista) { $lista.Dispose() } }
        } finally { $base.Dispose() }
    }
}

$codigoFinal = 0
Start-Transcript -Path $transcricao -Force | Out-Null
try {
    if ($DiagnosticarODBC) {
        Write-Host 'Coletando diagnostico. Nenhuma instalacao sera iniciada ou interrompida.' -ForegroundColor Cyan
        $processos = @(Get-CimInstance Win32_Process -Filter "Name='msiexec.exe' OR Name='winget.exe' OR Name='powershell.exe'" | Where-Object {
            ($_.Name -eq 'powershell.exe' -and $_.CommandLine -match 'preparar-vm\.ps1') -or
            ($_.Name -eq 'winget.exe' -and $_.CommandLine -match 'msodbcsql') -or
            ($_.Name -eq 'msiexec.exe' -and ($_.CommandLine -match 'AA816C7D-E37B-4FD6-BBCF-0657C511993B|msodbcsql18|/V(?:\s|$)|-Embedding'))
        } | Select-Object Name,ProcessId,ParentProcessId,CreationDate,CommandLine)
        $janelas = @(Get-Process -Name msiexec -ErrorAction SilentlyContinue | Select-Object Id,StartTime,MainWindowTitle,Responding,CPU)
        $logsMSI = @(Get-ChildItem -LiteralPath $pasta -Filter '*.msi.log' -File | Select-Object Name,Length,LastWriteTime)
        $diagnostico = [ordered]@{
            data = (Get-Date).ToString('o')
            processos = $processos
            janelas_instalador = $janelas
            drivers = @(Get-RegistrosODBCSQL)
            produtos_odbc18 = @(Get-ProdutosODBC18)
            logs_msi = $logsMSI
            instalacao_em_andamento = Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\InProgress'
            reinicio_pendente = (Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired') -or (Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending')
        }
        $diagnostico | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $pasta "diagnostico-odbc-$idExecucao.json") -Encoding UTF8
        foreach ($logMSI in $logsMSI) {
            try {
                Get-Content -LiteralPath (Join-Path $pasta $logMSI.Name) -Tail 200 -ErrorAction Stop |
                    Set-Content -LiteralPath (Join-Path $pasta "trecho-$idExecucao-$($logMSI.Name).txt") -Encoding UTF8
            } catch { Write-Warning "Log ainda bloqueado: $($logMSI.Name)" }
        }
        $script:resultado.estado = 'diagnostico_odbc_coletado'
        $script:resultado.etapa = 'diagnostico_somente_leitura'
        Write-Host 'DIAGNOSTICO COLETADO. Os resultados serao publicados para verificacao.' -ForegroundColor Green
    } elseif ($PrepararAbertura) {
        foreach ($subpasta in @('src','scripts','tests','examples')) {
            $logCopia = Join-Path $pasta "atualizar-$subpasta-$idExecucao.log"
            Executar-Etapa -Nome "Atualizar $subpasta do projeto na VM" -Executavel "$env:SystemRoot\System32\robocopy.exe" -Argumentos @("\\VBOXSVR\OrigemAutomatiza\$subpasta", "C:\AutomatizaTestes\$subpasta", '/E', '/XJ', '/R:1', '/W:1', '/NP', '/NFL', '/NDL', '/XD', '__pycache__', "/LOG:$logCopia") -CodigosAceitos @(0,1,2,3,4,5,6,7) -LimiteMinutos 10
        }
        Copy-Item -LiteralPath '\\VBOXSVR\OrigemAutomatiza\pyproject.toml' -Destination 'C:\AutomatizaTestes\pyproject.toml' -Force
        $mdeOrigem = '\\VBOXSVR\DiscoC\Users\Dev03\AppData\Local\VirtualStore\Windows\MDE.ini'
        if (-not (Test-Path -LiteralPath $mdeOrigem)) { throw 'A configuracao MDE.ini do RH nao esta acessivel na origem.' }
        $backupMDE = Join-Path $pasta 'config-backups'
        New-Item -ItemType Directory -Path $backupMDE -Force | Out-Null
        $virtualStore = Join-Path $env:LOCALAPPDATA 'VirtualStore\Windows'
        New-Item -ItemType Directory -Path $virtualStore -Force | Out-Null
        foreach ($destinoMDE in @((Join-Path $env:SystemRoot 'MDE.ini'), (Join-Path $virtualStore 'MDE.ini'))) {
            if (Test-Path -LiteralPath $destinoMDE) {
                $identificadorMDE = if ($destinoMDE -like '*VirtualStore*') { 'usuario' } else { 'windows' }
                Copy-Item -LiteralPath $destinoMDE -Destination (Join-Path $backupMDE "MDE-$identificadorMDE-$idExecucao.ini") -Force
            }
            Copy-Item -LiteralPath $mdeOrigem -Destination $destinoMDE -Force
        }
        $pythonVM = 'C:\AutomatizaTestes\.venv\Scripts\python.exe'
        Executar-Etapa -Nome 'Criar perfis dos ambientes RH na VM' -Executavel $pythonVM -Argumentos @('-u', 'C:\AutomatizaTestes\scripts\preparar-perfis-vm.py', (Join-Path $pasta "perfis-$idExecucao.json")) -ExibirSaida
        $componentes = @('C:\meta\rhsis\dbexpsda.dll','C:\meta\rhsis\dbexpoda.dll','C:\meta\rhsis\Oracle.ManagedDataAccess.dll','C:\acesso\Acessus.exe','C:\acesso\Acessus.Modulo.exe','C:\meta\rhsis\rh.exe')
        $script:resultado.componentes = @($componentes | ForEach-Object { [pscustomobject]@{arquivo=$_;presente=(Test-Path -LiteralPath $_)} })
        Executar-Etapa -Nome 'Validar projeto atualizado na VM' -Executavel $pythonVM -Argumentos @('-m', 'pytest', 'tests\unit', '-q') -ExibirSaida
        $script:resultado.estado = 'preparado_para_abrir_sistemas'
        $script:resultado.etapa = 'abrir_sistemas_na_sessao_normal'
        Write-Host 'PREPARACAO CONCLUIDA. O iniciador abrira os sistemas automaticamente na sessao normal.' -ForegroundColor Green
    } elseif ($ConectarServidores) {
        $script:resultado.etapa = 'validar_servidores_remotos'
        $registrosODBC = @(Get-RegistrosODBCSQL)
        $script:resultado.drivers_odbc = $registrosODBC
        if (@($registrosODBC | Where-Object Name -eq 'ODBC Driver 18 for SQL Server').Count) {
            throw 'O ODBC 18 ainda esta registrado na VM; remova-o antes de iniciar o Acessus.'
        }
        $drivers17 = @($registrosODBC | Where-Object { $_.Name -eq 'ODBC Driver 17 for SQL Server' -and $_.ArquivoPresente -and $_.Registro -eq 'Installed' })
        if (@($drivers17 | Select-Object -ExpandProperty Platform -Unique).Count -lt 2) {
            throw 'O ODBC 17 precisa estar disponivel para 32 e 64 bits.'
        }
        $pythonVM = 'C:\AutomatizaTestes\.venv\Scripts\python.exe'
        if (-not (Test-Path -LiteralPath $pythonVM)) { throw 'O ambiente Python da VM nao foi localizado.' }
        $saidaConexoes = Join-Path $pasta "conexoes-$idExecucao.json"
        Executar-Etapa -Nome 'Validar SQL Server e rede Oracle na VM' -Executavel $pythonVM -Argumentos @('-u', (Join-Path $PSScriptRoot 'conectar-servidores-vm.py'), '--saida', $saidaConexoes) -LimiteMinutos 5 -ExibirSaida
        $conexoes = Get-Content -LiteralPath $saidaConexoes -Raw | ConvertFrom-Json
        $script:resultado.estado = $conexoes.estado
        $script:resultado.etapa = 'configurar_oracle_e_validar_sistemas'
        Write-Host 'CONEXOES SQL VALIDADAS. Automacao configurada para desk-tec usando ODBC 17.' -ForegroundColor Green
        Write-Host 'Oracle: confira o resultado de rede acima; o login ainda precisa ser configurado.'
        Write-Host 'Nenhuma base foi copiada e nenhum sistema ou integracao foi iniciado.'
    } else {
    $reinicioPendente = (Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired') -or
        (Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending')
    if ($reinicioPendente) {
        $script:resultado.etapa = 'reinicio_necessario'
        throw 'Ha um reinicio pendente. Reinicie o Windows DENTRO da VM pelo menu Iniciar > Reiniciar e depois abra este mesmo arquivo.'
    }
    $winget = Get-Command winget.exe -ErrorAction SilentlyContinue
    if (-not $winget) { throw 'WinGet nao encontrado na VM.' }
    $script:resultado.etapa = 'configurar_odbc17'
    $script:resultado.odbc_antes = @(Get-RegistrosODBCSQL)
    $produtos18 = @(Get-ProdutosODBC18 | Sort-Object ProductCode -Unique)
    $script:resultado.produtos_odbc18_antes = $produtos18
    Publicar-Estado
    foreach ($produto18 in $produtos18) {
        # Consulte novamente a cada iteracao: outro pacote pode ter removido este cliente.
        if (-not @(Get-ProdutosODBC18 | Where-Object ProductCode -eq $produto18.ProductCode).Count) { continue }
        $codigoEscapado = [regex]::Escape($produto18.ProductCode)
        $chamadaAnterior = Get-CimInstance Win32_Process -Filter "Name='msiexec.exe'" |
            Where-Object { $_.CommandLine -match $codigoEscapado }
        if ($chamadaAnterior) {
            throw 'Uma chamada anterior de remocao do ODBC 18 continua aberta. Reinicie o Windows dentro da VM antes de continuar.'
        }
        $logMSI = Join-Path $pasta "odbc18-$($produto18.ProductCode)-$idExecucao.msi.log"
        Executar-Etapa -Nome "Remover ODBC 18 $($produto18.Versao) $($produto18.Vista) da VM" -Executavel "$env:SystemRoot\System32\msiexec.exe" -Argumentos @('/x', $produto18.ProductCode, '/qn', '/norestart', '/L*v', $logMSI) -CodigosAceitos @(0, 1605, 3010) -LimiteMinutos 10
    }
    $script:resultado.odbc_apos_remocao = @(Get-RegistrosODBCSQL)
    $script:resultado.produtos_odbc18_restantes = @(Get-ProdutosODBC18)
    Publicar-Estado
    if (@($script:resultado.odbc_apos_remocao | Where-Object Name -eq 'ODBC Driver 18 for SQL Server').Count -or $script:resultado.produtos_odbc18_restantes.Count) {
        throw 'O ODBC 18 ainda tem componentes registrados. Consulte os pacotes internos e os logs MSI publicados; nenhum componente do SQL Server foi removido manualmente.'
    }
    $drivers = @(Get-RegistrosODBCSQL | Where-Object { $_.Name -eq 'ODBC Driver 17 for SQL Server' -and $_.ArquivoPresente -and $_.Registro -eq 'Installed' })
    if (@($drivers | Select-Object -ExpandProperty Platform -Unique).Count -lt 2) {
        Executar-Etapa -Nome 'Garantir ODBC 17 para 32 e 64 bits' -Executavel $winget.Source -Argumentos @('install', '--id', 'Microsoft.msodbcsql.17', '--exact', '--source', 'winget', '--silent', '--accept-package-agreements', '--accept-source-agreements', '--disable-interactivity') -CodigosAceitos @(0, -1978335189, 3010)
    }
    $drivers = @(Get-RegistrosODBCSQL | Where-Object { $_.Name -eq 'ODBC Driver 17 for SQL Server' -and $_.ArquivoPresente -and $_.Registro -eq 'Installed' })
    if (@($drivers | Select-Object -ExpandProperty Platform -Unique).Count -lt 2) {
        throw 'O ODBC 17 precisa estar registrado para 32 e 64 bits.'
    }
    $script:resultado.drivers_odbc = $drivers
    $envVM = 'C:\AutomatizaTestes\.env'
    if (Test-Path -LiteralPath $envVM) {
        $conteudoEnv = [IO.File]::ReadAllText($envVM)
        if ($conteudoEnv -match '(?m)^SQL_DRIVER=') {
            $conteudoEnv = [regex]::Replace($conteudoEnv, '(?m)^SQL_DRIVER=.*$', 'SQL_DRIVER=ODBC Driver 17 for SQL Server')
        } else { $conteudoEnv += "`r`nSQL_DRIVER=ODBC Driver 17 for SQL Server`r`n" }
        [IO.File]::WriteAllText($envVM, $conteudoEnv, (New-Object Text.UTF8Encoding($false)))
    }
    if ($SomenteODBC17) {
        $script:resultado.estado = 'odbc17_configurado_bases_pendentes'
        $script:resultado.etapa = 'aguardando_bases_de_teste'
        Write-Host 'ODBC AJUSTADO: driver 18 ausente; driver 17 disponivel para 32 e 64 bits.' -ForegroundColor Green
        Write-Host 'A maquina principal nao foi alterada. A configuracao das bases continua pendente.'
    } else {
    foreach ($arquivo in @('C:\acesso\Acessus.exe', 'C:\meta\rhsis\rh.exe', 'C:\MetahConnect\MetahConnect.exe', 'C:\AutomatizaTestes\pyproject.toml')) {
        if (-not (Test-Path -LiteralPath $arquivo)) {
            & (Join-Path $PSScriptRoot 'copiar-para-vm.ps1')
            if (-not (Test-Path -LiteralPath $arquivo)) { throw "Copia incompleta: $arquivo" }
        }
    }
    $winget = Get-Command winget.exe -ErrorAction SilentlyContinue
    if (-not $winget) { throw 'WinGet nao encontrado. Instale ou atualize o Instalador de Aplicativos pela Microsoft Store da VM e reabra este arquivo.' }
    foreach ($pacote in @('Microsoft.VCRedist.2015+.x64', 'Microsoft.VCRedist.2015+.x86', 'Python.Python.3.12', 'Microsoft.msodbcsql.17')) {
        $argumentosPacote = @('install', '--id', $pacote, '--exact', '--source', 'winget', '--silent', '--accept-package-agreements', '--accept-source-agreements', '--disable-interactivity')
        if ($pacote -eq 'Python.Python.3.12') { $argumentosPacote += @('--scope', 'machine') }
        Executar-Etapa -Nome "Instalar $pacote" -Executavel $winget.Source -Argumentos $argumentosPacote -CodigosAceitos @(0, -1978335189, 3010)
    }
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
    $candidatosPython = @('C:\Program Files\Python312\python.exe', (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312\python.exe'))
    if (Test-Path 'HKLM:\SOFTWARE\Python\PythonCore\3.12\InstallPath') {
        $candidatosPython += Join-Path ((Get-Item 'HKLM:\SOFTWARE\Python\PythonCore\3.12\InstallPath').GetValue('')) 'python.exe'
    }
    $python = $candidatosPython | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if (-not $python) { throw 'Python 3.12 nao localizado depois da instalacao. Confira os logs.' }
    $pythonVenv = 'C:\AutomatizaTestes\.venv\Scripts\python.exe'
    if (-not (Test-Path -LiteralPath $pythonVenv)) {
        Executar-Etapa -Nome 'Criar ambiente Python da VM' -Executavel $python -Argumentos @('-m', 'venv', 'C:\AutomatizaTestes\.venv')
    }
    Executar-Etapa -Nome 'Instalar bibliotecas da automacao' -Executavel $pythonVenv -Argumentos @('-m', 'pip', 'install', '-e', 'C:\AutomatizaTestes')

    $sql = Get-Service -Name 'MSSQL$SQLEXPRESS' -ErrorAction SilentlyContinue
    if (-not $sql) {
        # O manifesto padrao passa /ENU; o bootstrap pode baixar midia no idioma
        # do Windows e falhar com 0x84C4000E ao receber essa opcao.
        # Preserve o idioma do Windows; nao altere configuracoes regionais.
        Executar-Etapa -Nome 'Instalar SQL Server 2025 Express na VM' -Executavel $winget.Source -Argumentos @('install', '--id', 'Microsoft.SQLServer.2025.Express', '--exact', '--source', 'winget', '--silent', '--accept-package-agreements', '--accept-source-agreements', '--disable-interactivity', '--override', '/IACCEPTSQLSERVERLICENSETERMS /ACTION=Install /quiet') -CodigosAceitos @(0, -1978335189, 3010)
        $sql = Get-Service -Name 'MSSQL$SQLEXPRESS' -ErrorAction SilentlyContinue
    }
    if (-not $sql) { throw 'A instalacao nao disponibilizou a instancia SQLEXPRESS. Confira os logs.' }
    if ($sql.Status -ne 'Running') { Start-Service -Name 'MSSQL$SQLEXPRESS' }

    Executar-Etapa -Nome 'Validar testes locais do projeto' -Executavel $pythonVenv -Argumentos @('-m', 'pytest', 'tests\unit', '-q')
    $script:resultado.etapa = 'verificar_sql_local'
    $conexao = New-Object System.Data.SqlClient.SqlConnection('Data Source=.\SQLEXPRESS;Initial Catalog=master;Integrated Security=True;Connect Timeout=15;Encrypt=True;TrustServerCertificate=True')
    try {
        $conexao.Open()
        $consulta = $conexao.CreateCommand()
        $consulta.CommandText = "SELECT CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(128))"
        $script:resultado.sql_versao = $consulta.ExecuteScalar()
        $consulta.CommandText = 'SELECT name FROM sys.databases WHERE database_id > 4'
        $leitor = $consulta.ExecuteReader()
        $bases = @()
        while ($leitor.Read()) { $bases += $leitor.GetString(0) }
        $leitor.Close()
        $script:resultado.bases_locais = $bases
    } finally { $conexao.Dispose() }
    $script:resultado.estado = 'dependencias_concluidas_bases_pendentes'
    $script:resultado.etapa = 'aguardando_bases_de_teste'
    Write-Host ''
    Write-Host 'DEPENDENCIAS CONCLUIDAS. SQL Server local e testes do projeto verificados.' -ForegroundColor Green
    Write-Host 'Falta restaurar as bases e configurar as conexoes dos sistemas.'
    Write-Host 'Acessus, RH e integracoes nao foram iniciados.'
    }
    }
} catch {
    $codigoFinal = 1
    $script:resultado.estado = 'erro'
    $script:resultado.erro = $_.Exception.Message
    Write-Host $_.Exception.Message -ForegroundColor Red
    if (-not $ConectarServidores -and $script:resultado.etapa -match 'SQL Server|sql_local') {
        try { Coletar-LogsSQL } catch { Write-Warning ('Nao foi possivel coletar todos os logs SQL: ' + $_.Exception.Message) }
    }
} finally {
    Stop-Transcript | Out-Null
    Publicar-Estado
}
Write-Host "Logs: $pasta"
if (-not $PrepararAbertura -or $codigoFinal -ne 0) {
    Read-Host 'Pressione Enter para fechar esta janela' | Out-Null
}
exit $codigoFinal
