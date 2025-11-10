import tkinter as tk
from tkinter import ttk, messagebox

# Function to draw the selected shape
def draw_shape():
    canvas.delete("all")  # Clear previous drawings
    shape = shape_var.get()
    
    try:
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer coordinates")
        return
    
    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, fill="lightblue")
    elif shape == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen")
    elif shape == "Square":
        # Ensure square by taking min of width and height
        side = min(abs(x2 - x1), abs(y2 - y1))
        canvas.create_rectangle(x1, y1, x1 + side, y1 + side, fill="pink")
    elif shape == "Triangle":
        # Draw triangle using three points
        # Using x1,y1 and x2,y2 as two points, third point calculated
        x3 = x1
        y3 = y2
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="yellow")
    else:
        messagebox.showwarning("Warning", "Please select a shape")

# Main window
root = tk.Tk()
root.title("Shape Drawer")
root.geometry("500x500")
root.config(bg="black")
# Shape selection
tk.Label(root, text="Select Shape:").pack(pady=5)
shape_var = tk.StringVar()
shape_menu = ttk.Combobox(root, textvariable=shape_var, values=["Oval", "Rectangle", "Square", "Triangle"])
shape_menu.pack(pady=5)

# Coordinate inputs
coord_frame = tk.Frame(root)
coord_frame.pack(pady=10)

tk.Label(coord_frame, text="x1:").grid(row=0, column=0, padx=5)
x1_entry = tk.Entry(coord_frame, width=5)
x1_entry.grid(row=0, column=1, padx=5)

tk.Label(coord_frame, text="y1:").grid(row=0, column=2, padx=5)
y1_entry = tk.Entry(coord_frame, width=5)
y1_entry.grid(row=0, column=3, padx=5)

tk.Label(coord_frame, text="x2:").grid(row=1, column=0, padx=5)
x2_entry = tk.Entry(coord_frame, width=5)
x2_entry.grid(row=1, column=1, padx=5)

tk.Label(coord_frame, text="y2:").grid(row=1, column=2, padx=5)
y2_entry = tk.Entry(coord_frame, width=5)
y2_entry.grid(row=1, column=3, padx=5)

# Draw button
tk.Button(root, text="Draw Shape", command=draw_shape).pack(pady=10)

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

root.mainloop()
