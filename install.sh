#!/bin/bash
echo "🚀 Iniciando instalación de DevHelp para Linux..."

# 1. Actualizar e instalar dependencias básicas
sudo apt update && sudo apt install -y python3-pip pipx git

# 2. Configurar Path
pipx ensurepath

# 3. Instalación
pipx install . --force
pipx inject devhelp rich

echo "✅ Instalación completada. Reinicia tu terminal y usa 'devhelp --all'"