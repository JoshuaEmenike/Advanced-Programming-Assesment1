import tkinter as tk
from tkinter import ttk

# Function to update the greeting
def update_greeting():
    name = name_entry.get()
    color = color_var.get()
    if name and color:
        greeting_label.config(text=f"Hello, {name}!", fg=color)
    else:
        greeting_label.config(text="Please enter your name and select a color.", fg="red")

# Main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("400x350")

# ===== Input Frame =====
input_frame = tk.Frame(root, bg="#d0e1f9", padx=10, pady=10)
input_frame.pack(fill="x", padx=10, pady=10)

# Title label
tk.Label(input_frame, text="Welcome to Greeting App", font=("Arial", 14, "bold"), fg="blue", bg="#d0e1f9").pack(pady=5)

# Name entry
tk.Label(input_frame, text="Enter your name:", bg="#d0e1f9").pack(anchor="w", pady=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.pack(pady=5)

# Color dropdown
tk.Label(input_frame, text="Select a color:", bg="#d0e1f9").pack(anchor="w", pady=5)
color_var = tk.StringVar()
color_dropdown = ttk.Combobox(input_frame, textvariable=color_var, values=["red", "green", "blue", "purple", "orange"], width=27)
color_dropdown.pack(pady=5)

# Update button
tk.Button(input_frame, text="Update Greeting", command=update_greeting).pack(pady=10)

# ===== Display Frame =====
display_frame = tk.Frame(root, bg="#f9e0d0", padx=10, pady=10)
display_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Greeting label (initially empty)
greeting_label = tk.Label(display_frame, text="", font=("Arial", 14, "bold"), bg="#f9e0d0")
greeting_label.pack(expand=True)

root.mainloop()
