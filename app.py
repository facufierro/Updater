import tkinter as tk
import subprocess
import os
import sys


# Create the main window
root = tk.Tk()
root.title("Simple App")

# Set window size
window_width = 400
window_height = 300
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

# Create a status label
status_label = tk.Label(root, text="Ready", font=("Arial", 12))
status_label.pack(pady=5)


# Button callback
def on_button_press():
    label.config(text="Button pressed")


def launch_second_app():
    try:
        # Try to launch the compiled executable first
        exe_path = os.path.join(os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__), "app2.exe")
        if os.path.exists(exe_path):
            subprocess.Popen([exe_path])
            status_label.config(text="App 2 launched! Closing...")
            root.after(1000, close_app)  # Close after 1 second
        else:
            # Fall back to Python script if exe doesn't exist
            script_path = os.path.join(os.path.dirname(__file__), "app2.py")
            if os.path.exists(script_path):
                subprocess.Popen([sys.executable, script_path])
                status_label.config(text="App 2 launched (Python)! Closing...")
                root.after(1000, close_app)  # Close after 1 second
            else:
                status_label.config(text="App 2 not found!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")


def close_app():
    root.quit()
    sys.exit()


# Create a button with larger font
button = tk.Button(root, text="Press Me", command=on_button_press, font=("Arial", 16), width=12, height=2)
button.pack(pady=10)

# Create a button to launch the second app
launch_button = tk.Button(root, text="Launch App 2", command=launch_second_app, font=("Arial", 14), width=15, height=2)
launch_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
