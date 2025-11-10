import tkinter as tk
from tkinter import ttk, messagebox
import math

# Function to calculate circle area
def calc_circle_area():
    try:
        r = float(circle_radius_entry.get())
        area = math.pi * r**2
        circle_result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid radius")

# Function to calculate square area
def calc_square_area():
    try:
        side = float(square_side_entry.get())
        area = side**2
        square_result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid side length")

# Function to calculate rectangle area
def calc_rectangle_area():
    try:
        length = float(rect_length_entry.get())
        width = float(rect_width_entry.get())
        area = length * width
        rectangle_result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid length and width")

# Main window
root = tk.Tk()
root.title("Shape Area Calculator")
root.geometry("400x300")

# Tabbed interface
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ===== Circle Tab =====
circle_tab = ttk.Frame(notebook)
notebook.add(circle_tab, text="Circle")

tk.Label(circle_tab, text="Radius:").pack(pady=5)
circle_radius_entry = tk.Entry(circle_tab)
circle_radius_entry.pack(pady=5)
tk.Button(circle_tab, text="Calculate Area", command=calc_circle_area).pack(pady=5)
circle_result_label = tk.Label(circle_tab, text="")
circle_result_label.pack(pady=5)

# ===== Square Tab =====
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text="Square")

tk.Label(square_tab, text="Side Length:").pack(pady=5)
square_side_entry = tk.Entry(square_tab)
square_side_entry.pack(pady=5)
tk.Button(square_tab, text="Calculate Area", command=calc_square_area).pack(pady=5)
square_result_label = tk.Label(square_tab, text="")
square_result_label.pack(pady=5)

# ===== Rectangle Tab =====
rectangle_tab = ttk.Frame(notebook)
notebook.add(rectangle_tab, text="Rectangle")

tk.Label(rectangle_tab, text="Length:").pack(pady=5)
rect_length_entry = tk.Entry(rectangle_tab)
rect_length_entry.pack(pady=5)

tk.Label(rectangle_tab, text="Width:").pack(pady=5)
rect_width_entry = tk.Entry(rectangle_tab)
rect_width_entry.pack(pady=5)

tk.Button(rectangle_tab, text="Calculate Area", command=calc_rectangle_area).pack(pady=5)
rectangle_result_label = tk.Label(rectangle_tab, text="")
rectangle_result_label.pack(pady=5)

root.mainloop()
