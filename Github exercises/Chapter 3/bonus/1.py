# Burger Shack Ordering System

def select_burger():
    print("\nChoose your burger:")
    for i, (burger, price) in enumerate(burgers.items(), 1):
        print(f"{i}. {burger} - ${price}")
    choice = int(input("Enter number: "))
    burger_name = list(burgers.keys())[choice-1]
    return burger_name, burgers[burger_name]

def select_toppings():
    selected_toppings = []
    total = 0
    print("\nSelect toppings (enter 0 to finish):")
    for i, (topping, price) in enumerate(toppings.items(), 1):
        print(f"{i}. {topping} - ${price}")
    while True:
        choice = int(input("Enter number: "))
        if choice == 0:
            break
        topping_name = list(toppings.keys())[choice-1]
        selected_toppings.append(topping_name)
        total += toppings[topping_name]
    return selected_toppings, total

def select_condiments():
    selected_condiments = []
    print("\nSelect condiments (enter 0 to finish):")
    for i, condiment in enumerate(condiments, 1):
        print(f"{i}. {condiment}")
    while True:
        choice = int(input("Enter number: "))
        if choice == 0:
            break
        selected_condiments.append(condiments[choice-1])
    return selected_condiments

def select_sides():
    selected_sides = []
    total = 0
    print("\nSelect sides (enter 0 to finish):")
    for i, (side, price) in enumerate(sides.items(), 1):
        print(f"{i}. {side} - ${price}")
    while True:
        choice = int(input("Enter number: "))
        if choice == 0:
            break
        side_name = list(sides.keys())[choice-1]
        selected_sides.append(side_name)
        total += sides[side_name]
    return selected_sides, total

def handle_payment(total_price):
    print(f"\nTotal amount due: ${total_price:.2f}")
    while True:
        try:
            payment = float(input("Enter amount paid: $"))
            if payment < total_price:
                print("Insufficient amount. Please pay at least the total price.")
            else:
                change = payment - total_price
                print(f"Payment accepted. Change: ${change:.2f}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def take_order():
    print("Welcome to Burger Shack!\n")
    
    # Select burger
    burger_name, burger_price = select_burger()
    
    # Select toppings
    selected_toppings, toppings_price = select_toppings()
    
    # Select condiments
    selected_condiments = select_condiments()
    
    # Select sides
    selected_sides, sides_price = select_sides()
    
    # Calculate total
    total_price = burger_price + toppings_price + sides_price
    
    # Show order summary
    print("\n--- Order Summary ---")
    print(f"Burger: {burger_name} - ${burger_price}")
    if selected_toppings:
        print("Toppings:", ", ".join(selected_toppings), f"- ${toppings_price:.2f}")
    if selected_condiments:
        print("Condiments:", ", ".join(selected_condiments))
    if selected_sides:
        print("Sides:", ", ".join(selected_sides), f"- ${sides_price:.2f}")
    print(f"Total: ${total_price:.2f}")
    
    # Handle payment
    handle_payment(total_price)
    print("Thank you for your order! Enjoy your meal!\n")


# ===== Menu Data =====
burgers = {
    "Beef Burger": 50,
    "Chicken Burger": 45,
    "Vegetarian Burger": 40
}

toppings = {
    "Cheese": 5,
    "Peanut Butter": 7,
    "Avocado": 8
}

condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]

sides = {
    "Fries": 15,
    "Soft Drink": 10,
    "Salad": 12
}

# ===== Run the program =====
if __name__ == "__main__":
    take_order()
