import tkinter as tk
import subprocess
import os
import sys

def launch_updater():
    # Get the directory where the executable or script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as Python script
        base_dir = os.path.dirname(__file__)
    
    exe = os.path.join(base_dir, "updater.exe")
    py = os.path.join(base_dir, "updater.py")
    
    if os.path.exists(exe):
        subprocess.Popen([exe])
        root.destroy()
    elif os.path.exists(py):
        subprocess.Popen([sys.executable, py])
        root.destroy()

root = tk.Tk()
root.title("v1.0.1")
tk.Button(root, text="Launch Updater", command=launch_updater, width=20, height=2).pack(padx=40, pady=40)
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.mainloop()
