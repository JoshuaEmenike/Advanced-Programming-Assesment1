import tkinter as tk
from tkinter import messagebox
import random

# ===== Word List =====
words = ["python", "computer", "program", "keyboard", "algorithm", "developer", "variable", "function"]

# ===== Game Variables =====
score = 0
current_word = ""
time_left = 15  # seconds per word

# ===== Functions =====
def shuffle_word(word):
    shuffled = list(word)
    random.shuffle(shuffled)
    return ''.join(shuffled)

def next_word():
    global current_word, time_left
    if not words:
        messagebox.showinfo("Game Over", f"Game Over! Your final score is: {score}")
        root.destroy()
        return
    current_word = random.choice(words)
    words.remove(current_word)
    shuffled = shuffle_word(current_word)
    word_label.config(text=shuffled)
    guess_entry.delete(0, tk.END)
    time_left = 15
    update_timer()

def check_guess():
    global score
    guess = guess_entry.get().strip().lower()
    if guess == current_word:
        score += 1
        score_label.config(text=f"Score: {score}")
        messagebox.showinfo("Correct!", "Well done! That's correct.")
        next_word()
    else:
        messagebox.showwarning("Incorrect", "Try again!")

def update_timer():
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left} sec")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's up!", f"Time's up! The word was: {current_word}")
        next_word()

# ===== Main Window =====
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x300")

tk.Label(root, text="Guess the Word!", font=("Arial", 16, "bold")).pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="blue")
word_label.pack(pady=10)

tk.Label(root, text="Your Guess:").pack()
guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack(pady=5)

tk.Button(root, text="Submit Guess", bg="#4caf50", fg="white", command=check_guess).pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
score_label.pack()

timer_label = tk.Label(root, text=f"Time Left: {time_left} sec", font=("Arial", 12))
timer_label.pack(pady=5)

# Start the first word
next_word()

root.mainloop()
