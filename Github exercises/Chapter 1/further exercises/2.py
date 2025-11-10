number = input("Enter a number: ")
total = 0

for digit in number:
    total = total + int(digit)

print("Sum of digits =", total)
