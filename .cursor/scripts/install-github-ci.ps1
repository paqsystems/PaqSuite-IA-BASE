# Instala la plantilla de CI de PaqSuite en el repositorio de producto actual.
# Uso (desde la raíz del producto, p. ej. PaqSuite-IA-PedidosWeb):
#   powershell -ExecutionPolicy Bypass -File C:\Programacion\PaqSuite-IA-BASE\.cursor\scripts\install-github-ci.ps1
# Guía: docs/_base/00-github-actions-ci-scaffold.md

param(
    [string]$ProjectRoot = (Get-Location).Path,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$baseDocs = Join-Path $ProjectRoot 'docs\_base'
if (-not (Test-Path $baseDocs)) {
    throw "No se encontró docs\_base en $ProjectRoot. Verifique symlinks (docs/_base/symlinks_paqsuite_ia.md)."
}

$templatePath = Join-Path $baseDocs 'templates\github\workflows\ci.yml'
if (-not (Test-Path $templatePath)) {
    throw "Plantilla no encontrada: $templatePath. Actualice PaqSuite-IA-BASE."
}

$destDir = Join-Path $ProjectRoot '.github\workflows'
$destPath = Join-Path $destDir 'ci.yml'

if ((Test-Path $destPath) -and -not $Force) {
    Write-Host "Ya existe $destPath. Use -Force para sobrescribir."
    exit 0
}

New-Item -ItemType Directory -Force -Path $destDir | Out-Null
Copy-Item -Path $templatePath -Destination $destPath -Force

Write-Host "CI instalado: $destPath"
Write-Host "Configure el secret VITE_DEVEXTREME_LICENSE en GitHub (Settings > Secrets) antes del primer build frontend."
