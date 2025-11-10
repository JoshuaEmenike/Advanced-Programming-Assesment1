def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        choice = input("Enter choice (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print("Result:", a / b)
        elif choice == '5':
            print("Result:", a % b)

        again = input("Do you want another calculation? (yes/no): ")
        if again.lower() != 'yes':
            print("Goodbye!")
            break

calculator()
