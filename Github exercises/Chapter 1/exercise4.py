def comparison():
    if fisrt_num > sec_num and fisrt_num > third_num:
        print(f'The first number {fisrt_num} is the greatest among the three')
    elif sec_num > fisrt_num and sec_num > third_num:
        print(f'The second number {sec_num} is the greatest among the three')
    elif third_num > fisrt_num and third_num > sec_num:
        print(f'The third number {third_num} is the greatest among the three')


print("Hello User")
fisrt_num= int(input('kindly tell us your first number: \n'))
sec_num= int(input('kindly tell us your second number: \n'))
third_num= int(input('kindly tell us your third number: \n'))

comparison()