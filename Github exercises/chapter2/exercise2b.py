import tkinter as tk
from tkinter import BOTH, YES, TOP, BOTTOM, LEFT, RIGHT, RAISED

# Create main window
root = tk.Tk()
root.title("Pack Layout Example")
root.geometry("400x300")

# Create left frame to contain labels A and B
left_frame = tk.Frame(root, bd=5, relief=RAISED, bg="lightgray")
left_frame.pack(side=LEFT, fill=BOTH, expand=YES)

# Create right frame to contain labels C and D
right_frame = tk.Frame(root, bd=5, relief=RAISED, bg="lightgray")
right_frame.pack(side=RIGHT, fill=BOTH, expand=YES)

# Create label A (top of left frame)
label_a = tk.Label(left_frame, text="A", bg="#1E2235", fg="white", font=("Arial", 24, "bold"))
label_a.pack(side=TOP, fill=BOTH, expand=YES)

# Create label B (bottom of left frame)
label_b = tk.Label(left_frame, text="B", bg="white", fg="#1E2235", font=("Arial", 24, "bold"))
label_b.pack(side=BOTTOM, fill=BOTH, expand=YES)

# Create label C (top of right frame)
label_c = tk.Label(right_frame, text="C", bg="white", fg="#1E2235", font=("Arial", 24, "bold"))
label_c.pack(side=TOP, fill=BOTH, expand=YES)

# Create label D (bottom of right frame)
label_d = tk.Label(right_frame, text="D", bg="#1E2235", fg="white", font=("Arial", 24, "bold"))
label_d.pack(side=BOTTOM, fill=BOTH, expand=YES)

# Start the GUI event loop
root.mainloop()