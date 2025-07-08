Write-Host "Building Updater..." -ForegroundColor Green
pyinstaller scripts/specs/updater.spec

Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host "Executable created: dist/updater.exe" -ForegroundColor Cyan
