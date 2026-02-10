$ErrorActionPreference = "Stop"

Write-Host "Starting application setup..."

# Frontend
Write-Host "Building Frontend..."
Push-Location "frontend-web"
if (!(Test-Path "node_modules")) {
    Write-Host "Installing frontend dependencies..."
    npm install
}
npm run build
if ($LASTEXITCODE -ne 0) {
    Write-Error "Frontend build failed."
    exit 1
}
Pop-Location

# Backend
Write-Host "Setting up Backend..."
Push-Location "backend"

# Ensure venv exists
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Determine venv paths
$CheckWindows = $env:OS -like "*Windows*"
if ($CheckWindows) {
    $VenvPython = ".\venv\Scripts\python.exe"
    $VenvPip = ".\venv\Scripts\pip.exe"
}
else {
    $VenvPython = "./venv/bin/python"
    $VenvPip = "./venv/bin/pip"
}

if (!(Test-Path $VenvPython)) {
    Write-Error "Could not find python in venv at $VenvPython."
    exit 1
}

Write-Host "Installing backend dependencies..."
& $VenvPip install -r requirements.txt

Write-Host "Running migrations..."
& $VenvPython manage.py migrate

Write-Host "Opening browser..."
Start-Process "http://localhost:8000"

Write-Host "Starting Django Server..."
& $VenvPython manage.py runserver

Pop-Location
