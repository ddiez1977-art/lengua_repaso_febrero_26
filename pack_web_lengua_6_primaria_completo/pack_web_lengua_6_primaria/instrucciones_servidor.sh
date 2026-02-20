#!/bin/bash

echo "========================================"
echo "   SERVIDOR PACK ESTUDIO LENGUA 6º"
echo "========================================"
echo

echo "Iniciando servidor web local..."
echo

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no está instalado"
    echo "Instala Python3 desde tu gestor de paquetes"
    exit 1
fi

# Verificar si existe el directorio del pack
if [ ! -d "pack_final_lengua_6_primaria_completo" ]; then
    echo "ERROR: Directorio del pack no encontrado"
    echo "Asegúrate de descomprimir el archivo ZIP primero"
    exit 1
fi

echo "Python3 encontrado. Iniciando servidor..."
echo

python3 servidor_local.py