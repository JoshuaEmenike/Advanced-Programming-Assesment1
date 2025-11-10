marks = [
    ("CodeLab I", 67),
    ("Web Development", 75),
    ("CodeLab II", 74),
    ("Smartphone Apps", 68),
    ("Games Development", 70),
    ("Responsive Web", 65)
]

# Sort low to high
low_to_high = sorted(marks, key=lambda x: x[1])
print("Marks from low to high:")
print(low_to_high)

# Sort high to low
high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)
print("Marks from high to low:")
print(high_to_low)
