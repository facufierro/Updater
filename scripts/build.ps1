Write-Host "Building App 1..." -ForegroundColor Green
pyinstaller app.spec

Write-Host "Building App 2..." -ForegroundColor Green
pyinstaller app2.spec

Write-Host ""
Write-Host "Build complete!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Executables created:" -ForegroundColor Cyan
Write-Host "- dist\app.exe (Main app)" -ForegroundColor White
Write-Host "- dist\app2.exe (Second app)" -ForegroundColor White
Write-Host ""
Write-Host "To run: Execute dist\app.exe" -ForegroundColor Green
Read-Host "Press Enter to continue"
