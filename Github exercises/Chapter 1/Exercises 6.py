for i in range(0, 101,):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('Buzz')

    elif i % 5 == 0 and i % 3 == 0:
        print('fizzBuzz')
    else:
        print(i)

print(i)
