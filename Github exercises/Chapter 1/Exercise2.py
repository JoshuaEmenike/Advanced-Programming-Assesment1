def addition(a, b):
    return a + b
    print(f"the addition of {a} and {b} is {a + b}")
def subtraction(a, b):
    return a - b
    print(f"the subtraction of {b} from {a} is {a - b}")
def multiplication(a, b):
    return a * b
    print(f"the multiplication of {a} and {b} is {a * b}")
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
    print(f"the division of {a} by {b} is {a / b}")
def modulus(a, b):
    return a % b
    print(f"remainder  of {a} divided by {b} is {a % b}")
    


print("Welcome to the simple calculator!")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
mode=input("Choose operation - add, subtract, multiply, divide, modulus: ").strip().lower()
if mode == "add":
    print(f"The result is: {addition(a, b)}")
elif mode == "subtract":
    print(f"The result is: {subtraction(a, b)}")
elif mode == "multiply":
    print(f"The result is: {multiplication(a, b)}")
elif mode == "divide":
    print(f"The result is: {division(a, b)}")   
elif mode == "modulus":
    print(f"The result is: {modulus(a, b)}")     

    