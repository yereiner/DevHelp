Write-Host "🚀 Iniciando instalación de DevHelp..." -ForegroundColor Cyan

# 1. Verificar/Instalar Python y Git vía Winget
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Instalando Python..." -ForegroundColor Yellow
    winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
}

if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Instalando Git..." -ForegroundColor Yellow
    winget install -e --id Git.Git --accept-package-agreements --accept-source-agreements
}

# 2. Instalar Pipx
Write-Host "🛠️ Configurando entorno de paquetes..." -ForegroundColor Cyan
python -m pip install --user pipx
python -m pipx ensurepath

# 3. Instalación del proyecto
Write-Host "⚙️ Instalando DevHelp..." -ForegroundColor Cyan
pipx install . --force
pipx inject devhelp rich  # <--- Esto soluciona el error que vimos ayer

Write-Host "✅ ¡Instalación completada! Reinicia tu terminal y escribe 'devhelp --all'" -ForegroundColor Green