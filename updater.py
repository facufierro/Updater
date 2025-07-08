import tkinter as tk
import subprocess
import os
import sys

def launch_app():
    exe = os.path.join(os.path.dirname(__file__), "app.exe")
    py = os.path.join(os.path.dirname(__file__), "app.py")
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
