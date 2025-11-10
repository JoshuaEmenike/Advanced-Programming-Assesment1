import tkinter as tk

# Function to convert text to uppercase
def to_uppercase():
    text = entry.get()
    result_label.config(text=text.upper())

# Main window
root = tk.Tk()
root.title("Uppercase Converter")
root.geometry("300x150")

# Entry widget
tk.Label(root, text="Enter text:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to convert
tk.Button(root, text="Convert to Uppercase", command=to_uppercase).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
