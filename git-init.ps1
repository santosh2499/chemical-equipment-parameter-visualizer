# Git Initialization and GitHub Setup Script

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Git Repository Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Initialize Git repository
Write-Host "Initializing Git repository..." -ForegroundColor Yellow
git init

# Add all files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .

# Create initial commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Chemical Equipment Parameter Visualizer

- Django backend with REST API
- React web frontend with Chart.js
- PyQt5 desktop frontend with Matplotlib
- User authentication
- CSV upload and processing
- Data visualization
- PDF report generation
- Dataset history management
- Comprehensive documentation"

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "Git repository initialized!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a new repository on GitHub" -ForegroundColor White
Write-Host "2. Copy the repository URL" -ForegroundColor White
Write-Host "3. Run the following commands:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin <your-github-repo-url>" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "Example:" -ForegroundColor Yellow
Write-Host "   git remote add origin https://github.com/yourusername/chemical-equipment-visualizer.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
