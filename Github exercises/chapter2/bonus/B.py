from datetime import datetime

# Ask user for date of birth
dob_input = input("Enter your date of birth (DD/MM/YYYY): ")

# Convert input string to a date object
dob = datetime.strptime(dob_input, "%d/%m/%Y").date()

# Get today's date
today = datetime.today().date()

# Calculate age
age = today.year - dob.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print(f"Your age is {age} years")
