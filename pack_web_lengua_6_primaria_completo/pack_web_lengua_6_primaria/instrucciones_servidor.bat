@echo off
echo ========================================
echo    SERVIDOR PACK ESTUDIO LENGUA 6º
echo ========================================
echo.
echo Iniciando servidor web local...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no está instalado
    echo Descarga Python desde: https://python.org
    pause
    exit /b 1
)

REM Verificar si existe el directorio del pack
if not exist "pack_final_lengua_6_primaria_completo" (
    echo ERROR: Directorio del pack no encontrado
    echo Asegurate de descomprimir el archivo ZIP primero
    pause
    exit /b 1
)

echo Python encontrado. Iniciando servidor...
echo.
python servidor_local.py

pause