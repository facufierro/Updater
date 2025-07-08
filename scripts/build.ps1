Write-Host "Building Launcher..." -ForegroundColor Green
pyinstaller scripts/app.spec

Write-Host "Building Updater..." -ForegroundColor Green
pyinstaller scripts/updater.spec

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Executables created:" -ForegroundColor Cyan
Write-Host "- dist\\app.exe (Launcher)" -ForegroundColor White
Write-Host "- dist\\updater.exe (Updater)" -ForegroundColor White
Write-Host ""
Write-Host "To run: Execute dist\\app.exe" -ForegroundColor Green
Read-Host "Press Enter to continue"
