@echo off
cd /d "%~dp0"
if not exist "C:\python32b\venv32\Scripts\python.exe" (
  echo O painel nao abriu: falta o Python 32 bits em C:\python32b\venv32.
  echo O Acessus precisa dessa versao do Python para funcionar.
  echo Confira a instalacao da venv e depois abra este arquivo novamente.
  pause
  exit /b 1
)
"C:\python32b\venv32\Scripts\python.exe" -m automatiza.nova_cli painel
if errorlevel 1 (
  echo O painel parou por um erro. Leia a mensagem acima, confira a venv e tente de novo.
) else (
  echo Painel encerrado. Abra este arquivo novamente para voltar ao site.
)
pause
