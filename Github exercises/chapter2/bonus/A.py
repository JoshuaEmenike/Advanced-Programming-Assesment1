import tkinter as tk
from tkinter import messagebox

# Function to convert temperature
def convert():
    try:
        temp = float(entry.get())
        if var.get() == "C to F":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F")
        elif var.get() == "F to C":
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Entry for temperature input
tk.Label(root, text="Enter temperature:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Option to select conversion type
var = tk.StringVar(value="C to F")
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C to F").pack()
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F to C").pack()

# Convert button
tk.Button(root, text="Convert", command=convert).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
