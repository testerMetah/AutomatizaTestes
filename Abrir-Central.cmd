@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Ambiente Python nao encontrado. Consulte README.md.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" "scripts\central_testes.py"
if errorlevel 1 pause
