import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("380x760")
root.configure(bg="#f5f5f5")

# ===== Header Section =====
header_frame = tk.Frame(root, bg="#11162a", height=120)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)

# Load and display the logo image (using tkinter's PhotoImage - supports PNG/GIF)
try:
    logo_photo = tk.PhotoImage(file="logo.png")
    logo_label = tk.Label(header_frame, image=logo_photo, bg="#11162a")
    logo_label.image = logo_photo  # Keep a reference
    logo_label.pack(pady=10)
except tk.TclError:
    # Fallback if image is not found
    tk.Label(header_frame, text="Logo not found", bg="#11162a", fg="white").pack(pady=10)

# ===== Title Section =====
tk.Label(root, text="Student Management System", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=(10,0))
tk.Label(root, text="New Student Registration", font=("Arial", 11), bg="#f5f5f5").pack()

# ===== Form Frame =====
form_frame = tk.Frame(root, bg="#f5f5f5")
form_frame.pack(pady=15)

# Labels and Entries
labels = ["Student Name", "Mobile Number", "Email Id", "Home Address"]
entries = []

for i, text in enumerate(labels):
    tk.Label(form_frame, text=text, font=("Arial", 10), bg="#f5f5f5").grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, width=30, bg="#d9d9d9")
    entry.grid(row=i, column=1, pady=5, padx=10)
    entries.append(entry)

# Gender Dropdown
tk.Label(form_frame, text="Gender", font=("Arial", 10), bg="#f5f5f5").grid(row=4, column=0, sticky="w", pady=5)
gender_box = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], width=27)
gender_box.grid(row=4, column=1, pady=5, padx=10)

# Course Enrolled
tk.Label(form_frame, text="Course Enrolled", font=("Arial", 10), bg="#f5f5f5").grid(row=5, column=0, sticky="w", pady=5)
course_var = tk.StringVar()
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]

for i, course in enumerate(courses):
    tk.Radiobutton(form_frame, text=course, variable=course_var, value=course, bg="#f5f5f5").grid(row=6+i, column=1, sticky="w")

# Languages Known
tk.Label(form_frame, text="Languages known", font=("Arial", 10), bg="#f5f5f5").grid(row=10, column=0, sticky="w", pady=5)
langs = ["English", "Tagalog", "Hindi/Urdu"]
lang_vars = []

for i, lang in enumerate(langs):
    var = tk.IntVar()
    tk.Checkbutton(form_frame, text=lang, variable=var, bg="#f5f5f5").grid(row=11+i, column=1, sticky="w")
    lang_vars.append(var)

# English Skill
tk.Label(form_frame, text="Rate your English communication skills", font=("Arial", 10), bg="#f5f5f5").grid(row=14, column=0, columnspan=2, pady=(10,5))
scale = tk.Scale(form_frame, from_=0, to=10, orient="horizontal", bg="#f5f5f5")
scale.grid(row=15, column=0, columnspan=2)

# ===== Buttons =====
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Submit", bg="#11162a", fg="white", width=12).grid(row=0, column=0, padx=20)
tk.Button(button_frame, text="Clear", bg="#11162a", fg="white", width=12).grid(row=0, column=1, padx=20)

root.mainloop()