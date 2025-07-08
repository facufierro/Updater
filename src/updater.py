import tkinter as tk
import subprocess
import os
import sys
import shutil

def launch_app():
    # Get the directory where the executable or script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as Python script
        base_dir = os.path.dirname(__file__)
    
    exe = os.path.join(base_dir, "app.exe")
    new_exe = os.path.join(base_dir, "new", "app.exe")
    py = os.path.join(base_dir, "app.py")
    
    # Check if there's a new version to update to
    if os.path.exists(new_exe):
        try:
            # Replace the old app with the new one
            if os.path.exists(exe):
                os.remove(exe)  # Remove old version
            shutil.copy2(new_exe, exe)  # Copy new version to main location
            print(f"Updated app.exe with new version from {new_exe}")
        except Exception as e:
            print(f"Error updating app: {e}")
            # If update fails, try to launch the new version directly
            if os.path.exists(new_exe):
                subprocess.Popen([new_exe])
                root.destroy()
                return
    
    # Launch the (possibly updated) app
    if os.path.exists(exe):
        subprocess.Popen([exe])
        root.destroy()
    elif os.path.exists(py):
        subprocess.Popen([sys.executable, py])
        root.destroy()

root = tk.Tk()
root.title("Updater")
tk.Button(root, text="Update", command=launch_app, width=20, height=2).pack(padx=40, pady=40)
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.mainloop()
