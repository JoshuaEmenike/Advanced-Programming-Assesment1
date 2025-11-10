def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Main program
nums = [2, 3, 4, 5]
result = product_of_list(nums)
print("The product of the list items is:", result)
