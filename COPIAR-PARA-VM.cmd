@echo off
setlocal
title Copiar programas para a VM de testes
if /I not "%COMPUTERNAME%"=="TESTESVM" (
  echo Abra este arquivo DENTRO da VM, pela pasta compartilhada OrigemAutomatiza.
  pause
  exit /b 1
)
echo Preparando acesso a pasta compartilhada...
pushd "%~dp0"
if errorlevel 1 (
  echo Nao foi possivel acessar a pasta compartilhada.
  pause
  exit /b 1
)
echo Iniciando ou acompanhando a copia. Atualizacao a cada 10 segundos.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\copiar-para-vm.ps1"
if errorlevel 1 (
  popd
  echo.
  echo A copia encontrou um erro. Mantenha esta janela aberta e informe a mensagem.
  pause
  exit /b 1
)
popd
echo.
echo Execucao encerrada. Confira o resultado acima. Bancos e dependencias ainda precisam ser configurados.
pause
