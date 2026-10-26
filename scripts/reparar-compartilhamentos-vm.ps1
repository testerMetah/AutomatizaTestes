param([string]$NomeVM = 'AutomatizaTestes')
$ErrorActionPreference = 'Stop'
$raizProjeto = Split-Path $PSScriptRoot -Parent
if ($env:COMPUTERNAME -ieq 'TESTESVM') { throw 'Execute no computador principal.' }
$saidaResultados = Join-Path $raizProjeto 'reports\vm\TESTESVM'
New-Item -ItemType Directory -Path $saidaResultados -Force | Out-Null
$pastaReparo = Join-Path $raizProjeto ('reports\vm\reparo-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
New-Item -ItemType Directory -Path $pastaReparo -Force | Out-Null
$vboxReparo = New-Object -ComObject VirtualBox.VirtualBox
$sessaoReparo = New-Object -ComObject VirtualBox.Session
$maquinaReparo = $vboxReparo.FindMachine($NomeVM)
Copy-Item -LiteralPath $maquinaReparo.SettingsFilePath -Destination (Join-Path $pastaReparo 'maquina.vbox.backup')
$pastasReparo = @(
    @{Nome='OrigemAutomatiza'; Caminho=$raizProjeto; Escrita=$false},
    @{Nome='ResultadoVM'; Caminho=$saidaResultados; Escrita=$true}
)
try {
    # Shared lock permite salvar as pastas permanentes com a VM já ligada.
    $maquinaReparo.LockMachine($sessaoReparo, 1)
    $maquinaMutavel = $sessaoReparo.Machine
    foreach ($pastaReparoItem in $pastasReparo) {
        $existenteReparo = @($maquinaMutavel.SharedFolders | Where-Object Name -eq $pastaReparoItem.Nome)
        if ($existenteReparo.Count) {
            if ($existenteReparo.Count -ne 1 -or
                $existenteReparo[0].HostPath.TrimEnd('\') -ine $pastaReparoItem.Caminho.TrimEnd('\') -or
                [bool]$existenteReparo[0].Writable -ne $pastaReparoItem.Escrita -or
                -not $existenteReparo[0].AutoMount) {
                throw ('Compartilhamento existente diverge: ' + $pastaReparoItem.Nome + '. Nenhum existente foi substituido.')
            }
        }
    }
    foreach ($pastaReparoItem in $pastasReparo) {
        if (-not @($maquinaMutavel.SharedFolders | Where-Object Name -eq $pastaReparoItem.Nome).Count) {
            $maquinaMutavel.CreateSharedFolder($pastaReparoItem.Nome, $pastaReparoItem.Caminho, $pastaReparoItem.Escrita, $true, '')
        }
    }
    $maquinaMutavel.SaveSettings()
    $maquinaMutavel.SharedFolders | Select-Object Name, HostPath, Writable, AutoMount |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $pastaReparo 'compartilhamentos.json') -Encoding UTF8
    Write-Host 'Compartilhamentos permanentes conferidos. A VM nao foi desligada.'
    Write-Host "Evidencias: $pastaReparo"
} finally {
    if ($sessaoReparo.State -eq 1) { $sessaoReparo.UnlockMachine() }
}
