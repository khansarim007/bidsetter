@echo off
setlocal

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  py -m pip install -r requirements.txt
  py app.py
  goto :eof
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  python -m pip install -r requirements.txt
  python app.py
  goto :eof
)

echo Python not found.
echo Install Python from https://www.python.org/downloads/windows/
pause
