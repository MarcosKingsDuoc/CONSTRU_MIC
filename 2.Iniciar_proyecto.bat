@echo off

REM Definir la ruta del script actual
set "script_path=%~dp0"

REM Activar el entorno virtual (Windows)
call "%script_path%venv\Scripts\activate"

REM Cambiar al directorio base
cd "%script_path%"

REM Ejecutar el servidor

python construmic\manage.py runserver

