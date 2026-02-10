# Cleanup Script for GitHub Submission
# This script removes unnecessary files before pushing to GitHub

Write-Host "================================" -ForegroundColor Cyan
Write-Host "GitHub Submission Cleanup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Removing unnecessary documentation files..." -ForegroundColor Yellow

# Remove internal documentation
$filesToRemove = @(
    "setup.ps1",
    "git-init.ps1",
    "NO_AUTH_VERSION.md",
    "DESKTOP_APP_GUIDE.md",
    "DESKTOP_APP_UPDATED.md",
    "GETTING_STARTED.md",
    "REQUIREMENTS_CHECK.md"
)

foreach ($file in $filesToRemove) {
    if (Test-Path $file) {
        Remove-Item $file
        Write-Host "✓ Removed: $file" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "Keeping essential files:" -ForegroundColor Yellow
Write-Host "✓ README.md" -ForegroundColor Green
Write-Host "✓ QUICKSTART.md" -ForegroundColor Green
Write-Host "✓ PROJECT_STRUCTURE.md" -ForegroundColor Green
Write-Host "✓ TESTING_GUIDE.md" -ForegroundColor Green
Write-Host "✓ DEMO_SCRIPT.md" -ForegroundColor Green
Write-Host "✓ IMPLEMENTATION_SUMMARY.md" -ForegroundColor Green
Write-Host "✓ TROUBLESHOOTING.md" -ForegroundColor Green
Write-Host "✓ sample_equipment_data.csv" -ForegroundColor Green
Write-Host "✓ .gitignore" -ForegroundColor Green
Write-Host ""

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Cleanup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Review remaining files" -ForegroundColor White
Write-Host "2. Initialize Git: git init" -ForegroundColor White
Write-Host "3. Add files: git add ." -ForegroundColor White
Write-Host "4. Commit: git commit -m 'Initial commit: Chemical Equipment Visualizer'" -ForegroundColor White
Write-Host "5. Create GitHub repo and push" -ForegroundColor White
Write-Host ""
