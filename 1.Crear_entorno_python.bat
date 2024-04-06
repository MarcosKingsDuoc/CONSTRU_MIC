@echo off
setlocal enabledelayedexpansion

REM Definir ruta del proyecto
set "script_path=%~dp0"

REM Crear entorno virtual Python "venv"
python -m venv "%script_path%venv"

REM Activar el entorno virtual
call "%script_path%venv\Scripts\activate"

REM Instalar las dependencias pip mediante archivo de dependencias "requirements.txt"
pip install -r "%script_path%requirements.txt"

echo "Entorno virtual creado exitosamente."
pause