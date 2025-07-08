# App Updater

A modular, GitHub-based application updater that downloads and replaces files from a GitHub repository.

## Features

- **GitHub Integration**: Downloads files directly from GitHub repositories
- **Process Management**: Automatically closes running applications before updating
- **Safe Updates**: Creates backups and handles rollback on failure
- **Clean GUI**: Simple, user-friendly interface
- **Error Handling**: Comprehensive error reporting and recovery

## Structure

```
src/
  updater.py          # Main updater application
scripts/
  build.ps1           # Build script
  updater.spec        # PyInstaller specification
dist/
  updater.exe         # Compiled executable
```

## Configuration

Edit the `AppUpdater` class in `src/updater.py` to configure:

- `target_file`: The file to be replaced (default: "app.exe")
- `github_repo`: GitHub repository in format "owner/repo" (default: "facufierro/Updater")
- `github_file_path`: Path to file in the repository (default: "dist/app.exe")

## How It Works

1. **Launch**: User runs `updater.exe`
2. **Close**: Automatically closes any running instances of the target app
3. **Download**: Downloads the latest version from GitHub
4. **Replace**: Safely replaces the target file with backup/rollback support
5. **Launch**: Starts the updated application

## Building

Run the build script:
```powershell
.\scripts\build.ps1
```

## Dependencies

- `psutil`: Process management
- `requests`: HTTP downloads
- `tkinter`: GUI (included with Python)

## Usage

1. Place `updater.exe` in the same directory as the app you want to update
2. Configure the GitHub repository settings in the source code
3. Run `updater.exe`
4. Click "Update & Launch"

The updater will handle the rest automatically.
