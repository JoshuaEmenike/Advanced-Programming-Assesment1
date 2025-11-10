staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary",
         "Anmol", "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

counts = {}

for name in staff:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1

print("Item counts:")
for key in counts:
    print(key, ":", counts[key])
