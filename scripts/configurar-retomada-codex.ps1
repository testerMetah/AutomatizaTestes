param(
    [ValidateSet('Instalar', 'Status', 'Desativar', 'Ativar', 'Remover')]
    [string]$Acao = 'Status'
)
$ErrorActionPreference = 'Stop'
$pastaControle = Join-Path $env:LOCALAPPDATA 'CodexAutoResume'
$configuracaoControle = Join-Path $pastaControle 'config.json'
$nomeTarefaControle = 'CodexAutoResume-AutomatizaTestes'
$pythonControle = 'C:\Program Files\Python312\python.exe'
$pythonOcultoControle = 'C:\Program Files\Python312\pythonw.exe'
$scriptControle = Join-Path $pastaControle 'controller.py'
if ($Acao -eq 'Instalar') {
    New-Item -ItemType Directory -Path $pastaControle -Force | Out-Null
    if (-not (Test-Path -LiteralPath $configuracaoControle)) {
        throw 'Preparar config.json com o ID exato da conversa antes de instalar a tarefa.'
    }
    if (-not (Test-Path -LiteralPath $pythonOcultoControle)) { throw 'Python existente não encontrado.' }
    $acaoControle = New-ScheduledTaskAction -Execute $pythonOcultoControle -Argument "`"$scriptControle`" watch --config `"$configuracaoControle`"" -WorkingDirectory 'C:\AutomatizaTestes'
    $identidadeControle = [Security.Principal.WindowsIdentity]::GetCurrent().Name
    $principalControle = New-ScheduledTaskPrincipal -UserId $identidadeControle -LogonType Interactive -RunLevel Limited
    $gatilhoLoginControle = New-ScheduledTaskTrigger -AtLogOn -User $identidadeControle
    $gatilhoRecorrenteControle = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 5)
    $ajustesControle = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit ([TimeSpan]::Zero) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
    $tarefaExistenteControle = Get-ScheduledTask -TaskName $nomeTarefaControle -ErrorAction SilentlyContinue
    if ($tarefaExistenteControle -and $tarefaExistenteControle.Description -notlike '*CodexAutoResume*') {
        throw 'Nome de tarefa ocupado por tarefa não reconhecida; preservado.'
    }
    # Atualiza somente o supervisor; não encerra o daemon nem o turno do Codex.
    if ($tarefaExistenteControle) {
        Stop-ScheduledTask -TaskName $nomeTarefaControle
        Start-Sleep -Seconds 2
    }
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'codex_auto_resume.py') -Destination $scriptControle -Force
    Register-ScheduledTask -TaskName $nomeTarefaControle -Action $acaoControle -Trigger @($gatilhoLoginControle, $gatilhoRecorrenteControle) -Principal $principalControle -Settings $ajustesControle -Description 'CodexAutoResume: retoma somente esta conversa após falha real de cota; sem alterar autenticação/permissões.' -Force | Out-Null
    Start-ScheduledTask -TaskName $nomeTarefaControle
}
elseif ($Acao -eq 'Desativar' -or $Acao -eq 'Remover') {
    & $pythonControle $scriptControle disable --config $configuracaoControle
    Disable-ScheduledTask -TaskName $nomeTarefaControle | Out-Null
    Stop-ScheduledTask -TaskName $nomeTarefaControle -ErrorAction SilentlyContinue
    if ($Acao -eq 'Remover') {
        Unregister-ScheduledTask -TaskName $nomeTarefaControle -Confirm:$false
        Write-Output 'Tarefa removida. Arquivos de configuração/diagnóstico preservados para auditoria.'
        exit 0
    }
}
elseif ($Acao -eq 'Ativar') {
    & $pythonControle $scriptControle arm --config $configuracaoControle
    Enable-ScheduledTask -TaskName $nomeTarefaControle | Out-Null
    Start-ScheduledTask -TaskName $nomeTarefaControle
}
Get-ScheduledTask -TaskName $nomeTarefaControle | Select-Object TaskName,State
if (Test-Path -LiteralPath (Join-Path $pastaControle 'state.json')) {
    Get-Content -LiteralPath (Join-Path $pastaControle 'state.json') -Encoding UTF8
}
