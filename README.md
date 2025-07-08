# Dual App Project

This project contains two simple tkinter applications that work together.

## Files Structure

- `app.py` - Main application source code
- `app2.py` - Second application source code  
- `app.spec` - PyInstaller spec file for main app
- `app2.spec` - PyInstaller spec file for second app
- `build.bat` - Windows batch build script
- `build.ps1` - PowerShell build script
- `dist/app.exe` - Main application executable
- `dist/app2.exe` - Second application executable

## How it Works

1. **Main App (`app.exe`)**: 
   - Contains a "Press Me" button that changes the label text
   - Contains a "Launch App 2" button that opens the second application and closes itself after 1 second
   - Shows status messages when launching the second app

2. **Second App (`app2.exe`)**:
   - Opens as a separate window when launched from the main app
   - Contains an "Execute Action" button that updates the interface
   - Contains a "Launch App 1" button that opens the main application and closes itself after 1 second
   - Contains a "Close App" button to exit the application

## Usage

1. Run `dist/app.exe` to start the main application
2. Click "Launch App 2" to open the second application (the first app will close automatically)
3. Click "Launch App 1" from the second app to return to the main app (the second app will close automatically)
4. This creates a continuous cycle where each app launches the other and closes itself

## Building

To rebuild the executables:

### Using PowerShell:
```powershell
.\build.ps1
```

### Using Command Prompt:
```cmd
build.bat
```

### Manual Build:
```cmd
pyinstaller app.spec
pyinstaller app2.spec
```

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- PyInstaller (`pip install pyinstaller`)

## Features

- Both apps have centered windows
- Clean GUI with large, readable fonts
- Error handling for launching the second app
- Fallback to Python script if executable is not found
- Status feedback for user actions
