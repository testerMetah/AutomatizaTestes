@echo off
setlocal
set "PYTHON=C:\python32b\venv32\Scripts\python.exe"
if not exist "%PYTHON%" (
  echo Python 32 bits nao encontrado: %PYTHON%
  exit /b 2
)
call "C:\python32b\venv32\Scripts\activate.bat"
set "PYTHONPATH=%~dp0src;%PYTHONPATH%"
set "SUITE=%~dp0tests"
set "FILTRO=--exclude bloqueado"
:args
if "%~1"=="" goto executar
if /I "%~1"=="--tela" goto tela
if /I "%~1"=="--tag" goto tag
echo Argumento invalido: %~1
exit /b 2
:tela
if "%~2"=="" exit /b 2
set "SUITE=%~dp0tests\telas\%~2.robot"
shift
shift
goto args
:tag
if "%~2"=="" exit /b 2
set "FILTRO=%FILTRO% --include %~2"
shift
shift
goto args
:executar
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd-HHmmss"') do set "RODADA=%%i"
"%PYTHON%" -m robot --outputdir "%~dp0resultados\robot-telas\%RODADA%" %FILTRO% "%SUITE%"
exit /b %ERRORLEVEL%
