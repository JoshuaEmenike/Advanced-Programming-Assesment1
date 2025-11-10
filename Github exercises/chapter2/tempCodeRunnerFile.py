import tkinter as tk
from tkinter import BOTH, YES, NO, TOP, BOTTOM, LEFT, RIGHT, X, RAISED

# Create main window
root = tk.Tk()
root.title("Pack Layout Example")
root.geometry("250x95")

# Create label A (top, full width with border)
label_a = tk.Label(root, text="A", bg="red", fg="white", font=("Arial", 16, "bold"), 
                   relief=RAISED, bd=3, height=1)
label_a.pack(side=TOP, fill=X, expand=NO)

# Create a frame to hold C and D side by side
middle_frame = tk.Frame(root)
middle_frame.pack(side=TOP, fill=X, expand=NO)

# Create label C (left side with border, equal width with D)
label_c = tk.Label(middle_frame, text="C", bg="blue", fg="white", font=("Arial", 16, "bold"),
                   relief=RAISED, bd=3, height=1)
label_c.pack(side=LEFT, fill=BOTH, expand=YES)

# Create label D (right side with border, equal width with C)
label_d = tk.Label(middle_frame, text="D", bg="white", fg="black", font=("Arial", 16, "bold"),
                   relief=RAISED, bd=3, height=1)
label_d.pack(side=LEFT, fill=BOTH, expand=YES)

# Create label B (bottom center with border, small box)
label_b = tk.Label(root, text="B", bg="yellow", fg="black", font=("Arial", 16, "bold"),
                   relief=RAISED, bd=3, width=10, height=1)
label_b.pack(side=BOTTOM, expand=NO)

# Start the GUI event loop
root.mainloop()