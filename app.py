import tkinter as tk
import sys
import os
import subprocess
import requests
from packaging import version
from tkinter import messagebox


# Create the main window
root = tk.Tk()
root.title("Simple App")

CURRENT_VERSION = "v1.0.0"

# Set window size
window_width = 400
window_height = 200
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Create a label with larger font
label = tk.Label(root, text="Press the button", font=("Arial", 18))
label.pack(pady=20)


# Button callback
def on_button_press():
    label.config(text="Button pressed")

def relaunch_app():
    subprocess.Popen([sys.executable, __file__])
    root.quit()

def check_for_updates():
    try:
        response = requests.get("https://api.github.com/repos/facufierro/Updater/releases/latest")
        latest_version = response.json()["tag_name"]
        
        if version.parse(latest_version.lstrip('v')) > version.parse(CURRENT_VERSION.lstrip('v')):
            result = messagebox.askyesno("Update Available", f"New version {latest_version} available. Update now?")
            if result:
                subprocess.Popen([sys.executable, "update.py"])
                root.quit()
    except:
        pass

root.after(1000, check_for_updates)


# Create a button with larger font
button = tk.Button(root, text="Press Me", command=on_button_press, font=("Arial", 16), width=12, height=2)
button.pack(pady=10)

relaunch_button = tk.Button(root, text="Relaunch", command=relaunch_app)
relaunch_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
