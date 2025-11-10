import tkinter as tk
from tkinter import ttk, messagebox

# ===== Stock and prices =====
drinks_amount = {
    "Coke":    10,
    "Sprite":   8,
    "Fanta":   16,
    "Schweps":  7,
    "Pepsi":    7,
    "Mirinda":  9,
    "Water":   12
}

drinks_price = {
    "Coke":    2,
    "Sprite":  4,
    "Fanta":   3,
    "Schweps": 4,
    "Pepsi":   4,
    "Mirinda": 4,
    "Water":   2
}

# ===== Functions =====
def update_menu():
    menu_text = ""
    for drink in drinks_price:
        price = drinks_price[drink]
        stock = drinks_amount[drink]
        status = f"{stock} in stock" if stock > 0 else "SOLD OUT"
        menu_text += f"{drink:8} - AED{price} ({status})\n"
    menu_label.config(text=menu_text)

def purchase():
    drink = drink_var.get()
    if not drink:
        messagebox.showwarning("Warning", "Please select a drink.")
        return

    if drinks_amount[drink] == 0:
        messagebox.showinfo("Sold Out", f"Sorry, {drink} is sold out.")
        return

    money = money_entry.get()
    if not money.isdigit():
        messagebox.showerror("Error", "Please enter a valid amount of money.")
        return
    money = int(money)
    price = drinks_price[drink]

    if money < price:
        messagebox.showinfo("Not enough money", "Inserted money is not enough. Transaction cancelled.")
        return

    drinks_amount[drink] -= 1
    change = money - price
    messagebox.showinfo("Success", f"Dispensing {drink}...\nChange: AED{change}")
    money_entry.delete(0, tk.END)
    update_menu()

# ===== Main Window =====
root = tk.Tk()
root.title("Python Vending Machine")
root.geometry("350x430")
root.config(bg="light blue")
tk.Label(root, text="Welcome to Python Vending Machine", font=("Arial", 12, "bold")).pack(pady=10)

# Menu display
menu_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
menu_label.pack(pady=5)
update_menu()

# Drink selection
tk.Label(root, text="Select your drink:").pack(pady=5)
drink_var = tk.StringVar()
drink_menu = ttk.Combobox(root, textvariable=drink_var, values=list(drinks_price.keys()), state="readonly")
drink_menu.pack(pady=5)

# Money entry
tk.Label(root, text="Insert Money (AED):").pack(pady=5)
money_entry = tk.Entry(root)
money_entry.pack(pady=5)

# Purchase button
tk.Button(root, text="Purchase", bg="#4caf50", fg="white", command=purchase).pack(pady=20)

# Quit button
tk.Button(root, text="Quit", bg="#f44336", fg="white", command=root.destroy).pack(pady=10)

root.mainloop()
