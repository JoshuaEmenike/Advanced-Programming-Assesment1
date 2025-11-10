def square():
    s=int(input('what is the length of one of the sides\n'))
    Area=s * s
    print(f'the area is {Area} ')
    
def circle():
    r=int(input('what is the circles radius\n'))
    Area=3.14 * r
    print(f'the area is {Area} ')
        
def triangle():
    h=int(input('what is its height'))
    b=int(input('what is its breath'))
    Area= 0.5* h * b
    print (f'the area is {Area} ')
    
print ('hello, what shape area are you looking for')
shape=input('circle/triangle/ square\n')
if shape.lower()=='circle':
    circle()
elif shape.lower()=='triangle':
    triangle()
elif shape.lower()=='square':
    square()           