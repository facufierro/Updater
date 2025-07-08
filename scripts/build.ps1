Write-Host "Building Launcher..." -ForegroundColor Green
pyinstaller scripts/app.spec

Write-Host "Building Launcher..." -ForegroundColor Green
pyinstaller scripts/app_new.spec

Write-Host "Building Updater..." -ForegroundColor Green
pyinstaller scripts/updater.spec

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Executables created:" -ForegroundColor Cyan
Write-Host "- dist\\app.exe (Launcher)" -ForegroundColor White
Write-Host "- dist\\updater.exe (Updater)" -ForegroundColor White
Write-Host "- dist\\app_new.exe (New Launcher)" -ForegroundColor White
