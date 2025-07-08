Write-Host "Building Updater..." -ForegroundColor Green
pyinstaller scripts/updater.spec

Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host "Executable created: dist/updater.exe" -ForegroundColor Cyan
