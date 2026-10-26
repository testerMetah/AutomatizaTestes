@echo off
cd /d "%~dp0"
if not exist "C:\python32b\venv32\Scripts\python.exe" (
  echo ERRO: Python 32 bits ausente em C:\python32b\venv32.
  pause
  exit /b 1
)
"C:\python32b\venv32\Scripts\python.exe" -m automatiza.nova_cli painel
echo Painel encerrado. Se houve erro, leia a mensagem acima.
pause
