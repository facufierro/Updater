Write-Host "Building..." -ForegroundColor Green
pyinstaller scripts/app.spec
pyinstaller scripts/app_new.spec --distpath dist/new
pyinstaller scripts/updater.spec
Write-Host "Build complete!" -ForegroundColor Yellow
