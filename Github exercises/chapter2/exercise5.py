import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        elif operation == "mod":
            if num2 != 0:
                result = num1 % num2
            else:
                messagebox.showerror("Error", "Cannot modulo divide by zero")
                return
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.config(bg="gray")
# Labels and Entry widgets
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Buttons for operations
tk.Button(root, text="Add", width=12, command=lambda: calculate("add")).pack(pady=3)
tk.Button(root, text="Subtract", width=12, command=lambda: calculate("subtract")).pack(pady=3)
tk.Button(root, text="Multiply", width=12, command=lambda: calculate("multiply")).pack(pady=3)
tk.Button(root, text="Divide", width=12, command=lambda: calculate("divide")).pack(pady=3)
tk.Button(root, text="Modulo", width=12, command=lambda: calculate("mod")).pack(pady=3)

# Label to show result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
