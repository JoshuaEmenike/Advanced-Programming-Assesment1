import tkinter as tk

# Function to count letters, vowels, consonants, and special characters
def count_letters():
    text = entry.get()
    total_letters = len(text)
    vowels = 0
    consonants = 0
    special_chars = 0
    
    for char in text:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif not char.isspace():
            special_chars += 1

    result_label.config(text=f"Total letters: {total_letters}\n"
                             f"Number of vowels: {vowels}\n"
                             f"Number of consonants: {consonants}\n"
                             f"Number of special characters: {special_chars}")

# Main window
root = tk.Tk()
root.title("Vowel & Consonant Counter")
root.geometry("350x250")

# Entry widget
tk.Label(root, text="Enter a string:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to count letters
tk.Button(root, text="Count", command=count_letters).pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
