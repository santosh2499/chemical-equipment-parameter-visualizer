# Run Desktop Application
# This script activates the backend virtual environment and runs the desktop app

Write-Host "Starting Desktop Application..." -ForegroundColor Cyan
Write-Host ""

# Activate backend virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "..\backend\venv\Scripts\Activate.ps1"

# Run desktop app
Write-Host "Launching desktop application..." -ForegroundColor Green
python main.py
