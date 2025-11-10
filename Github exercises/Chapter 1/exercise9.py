list_1=[1,2,3,4,5,6,7,8,9,10]
for i in list_1:
 print(i)

print(f"the highest value is {list_1[0]} and the lowest value is {list_1[9]}")
list_1.sort()
list_1.append(11)
list_1.append(12)
list_1.sort(reverse=True)
print(list_1)