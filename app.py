import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Simple App")

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


# Create a button with larger font
button = tk.Button(root, text="Press Me", command=on_button_press, font=("Arial", 16), width=12, height=2)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
