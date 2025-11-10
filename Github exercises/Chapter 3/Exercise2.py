import tkinter as tk
from tkinter import ttk, messagebox

# Prices for each coffee
coffee_prices = {
    "Espresso": 50,
    "Cappuccino": 60,
    "Latte": 70,
    "Americano": 55
}

# Function to place order
def place_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    try:
        money = float(money_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount of money.")
        return

    if not coffee:
        messagebox.showwarning("Warning", "Please select a coffee type!")
        return

    price = coffee_prices[coffee]

    if money < price:
        messagebox.showwarning("Insufficient Money", f"Coffee price is {price}. You inserted {money}.")
        return
    change = money - price
    message = (
        f"You have ordered:\n"
        f"Coffee: {coffee}\n"
        f"Sugar: {sugar}\n"
        f"Milk: {milk}\n"
        f"Price: {price}\n"
        f"Inserted Money: {money}\n"
        f"Change: {change:.2f}"
    )
    messagebox.showinfo("Order Placed", message)

# Main window
root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("400x590")

# ===== Coffee Image =====
try:
    coffee_photo = tk.PhotoImage(file="coffee.png")  # Only PNG/GIF
    tk.Label(root, image=coffee_photo).pack(pady=10)
except:
    tk.Label(root, text="[Coffee Image Here]", font=("Arial", 12)).pack(pady=10)

# ===== Coffee Selection =====
tk.Label(root, text="Select Coffee Type:", font=("Arial", 12)).pack(pady=5)
coffee_var = tk.StringVar()
coffee_menu = ttk.Combobox(root, textvariable=coffee_var, values=list(coffee_prices.keys()), width=30)
coffee_menu.pack(pady=5)

# ===== Sugar Selection =====
tk.Label(root, text="Sugar (0-3 tsp):", font=("Arial", 12)).pack(pady=5)
sugar_var = tk.StringVar(value="1")
sugar_menu = ttk.Combobox(root, textvariable=sugar_var, values=["0", "1", "2", "3"], width=30)
sugar_menu.pack(pady=5)

# ===== Milk Selection =====
tk.Label(root, text="Milk Option:", font=("Arial", 12)).pack(pady=5)
milk_var = tk.StringVar(value="Normal")
milk_options = ["Normal", "Soy", "Almond", "None"]
milk_menu = ttk.Combobox(root, textvariable=milk_var, values=milk_options, width=30)
milk_menu.pack(pady=5)

# ===== Money Entry =====
tk.Label(root, text="Insert Money:", font=("Arial", 12)).pack(pady=5)
money_entry = tk.Entry(root, width=30)
money_entry.pack(pady=5)

# ===== Place Order Button =====
tk.Button(root, text="Place Order", font=("Arial", 12), bg="#a52a2a", fg="white", command=place_order).pack(pady=20)

root.mainloop()
