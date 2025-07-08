Write-Host "Building Updater..." -ForegroundColor Green

# Check if a config file exists and copy it to the dist folder
if (Test-Path "config.json") {
    Write-Host "Found config.json - will include in build" -ForegroundColor Yellow
    $ConfigInclude = "--add-data config.json;."
}
else {
    $ConfigInclude = ""
}

# Run PyInstaller with the spec file
pyinstaller scripts/specs/updater.spec $ConfigInclude

Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host "Executable created: dist/updater.exe" -ForegroundColor Cyan
