locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

print("Original list:", locations)
print("Length of list:", len(locations))

# temporary sorted (A–Z)
print("Sorted list (A-Z):", sorted(locations))
print("Original list again:", locations)

# temporary sorted (Z–A)
print("Sorted list (Z-A):", sorted(locations, reverse=True))
print("Original list again:", locations)

# reverse list permanently
locations.reverse()
print("List after reverse():", locations)

# sort permanently (A–Z)
locations.sort()
print("List after sort():", locations)

# sort permanently (Z–A)
locations.sort(reverse=True)
print("List after sort(reverse=True):", locations)
