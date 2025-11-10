import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("200x200")
root.configure(bg='navy blue', )

# Labels
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e") # Aligns to the right of its column

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Entry fields
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew") # Expands horizontally

password_entry = tk.Entry(root, show="*") # Obscures password
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Login Button
login_button = tk.Button(root, text="Sign In")
login_button.grid(row=2, column=0, columnspan=2, pady=10) # Spans both columns

# Optional: Configure column weights for resizing
root.grid_columnconfigure(1, weight=1) # Makes the second column expand
root.mainloop()