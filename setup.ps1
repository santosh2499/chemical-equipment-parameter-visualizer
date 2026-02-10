# Setup Script for Chemical Equipment Visualizer
# This script sets up the entire project

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Chemical Equipment Visualizer" -ForegroundColor Cyan
Write-Host "Setup Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Backend Setup
Write-Host "Setting up Django Backend..." -ForegroundColor Yellow
Set-Location backend

Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv venv

Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1

Write-Host "Installing Python dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Running migrations..." -ForegroundColor Green
python manage.py migrate

Write-Host "Creating superuser (follow prompts)..." -ForegroundColor Green
python manage.py createsuperuser

Write-Host "Backend setup complete!" -ForegroundColor Green
Write-Host ""

Set-Location ..

# Frontend Web Setup
Write-Host "Setting up React Web Frontend..." -ForegroundColor Yellow
Set-Location frontend-web

Write-Host "Installing npm dependencies..." -ForegroundColor Green
npm install

Write-Host "Web frontend setup complete!" -ForegroundColor Green
Write-Host ""

Set-Location ..

# Frontend Desktop Setup
Write-Host "Setting up PyQt5 Desktop Frontend..." -ForegroundColor Yellow
Set-Location frontend-desktop

Write-Host "Installing Python dependencies..." -ForegroundColor Green
..\backend\venv\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Host "Desktop frontend setup complete!" -ForegroundColor Green
Write-Host ""

Set-Location ..

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Start backend: cd backend && .\venv\Scripts\Activate.ps1 && python manage.py runserver" -ForegroundColor White
Write-Host "2. Start web frontend: cd frontend-web && npm start" -ForegroundColor White
Write-Host "3. Start desktop app: cd frontend-desktop && ..\backend\venv\Scripts\Activate.ps1 && python main.py" -ForegroundColor White
Write-Host ""
