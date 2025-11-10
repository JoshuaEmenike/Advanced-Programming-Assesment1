first_side=0
second_side=0
third_side=0
def display():
    print("welcome to the tringle calculator app")
    
def right_triangle():
        #("This function checks if the triangle is a right triangle or not
        if first_side==90 or second_side==90 or third_side==90:
            print("The triangle is a right triangle")
def equilateral_triangle():
        #This function checks if the triangle is an equilateral triangle or not
        if first_side==second_side and second_side==third_side:
            print("The triangle is an equilateral triangle")          

def obtuse_triangle():
        #This function checks if the triangle is an obtuse triangle or not
        if first_side>90 or second_side>90 or third_side>90:
            print("The triangle is an obtuse triangle")
            
def acute_triangle():
        #This function checks if the triangle is an acute triangle or not
        if first_side<90 and second_side<90 and third_side<90:
            print("The triangle is an acute triangle")
            
def isosceles_triangle():
        #This function checks if the triangle is an isosceles triangle or not
        if first_side==second_side or second_side==third_side or first_side==third_side:
            print("The triangle is an isosceles triangle")
            
def scalene_triangle():
        #This function checks if the triangle is a scalene triangle or not
        if first_side!=second_side and second_side!=third_side and first_side!=third_side:
            print("The triangle is a scalene triangle")
            
                        
display()
input1=float(input("Enter the length of first side of the triangle: "))
input2=float(input("Enter the length of second side of the triangle: "))
input3=float(input("Enter the length of third side of the triangle: "))
    
if input1 + input2 >= input3: 
    print("The triangle is valid")   
else:
    print("The triangle is not valid")

first_side=input1
second_side=input2  
third_side=input3   
    
if first_side==90 or second_side==90 or third_side==90:
         right_triangle() 
elif first_side==second_side and second_side==third_side:
         equilateral_triangle()
elif first_side>90 or second_side>90 or third_side>90:
         obtuse_triangle()
elif first_side<90 and second_side<90 and third_side<90:
         acute_triangle()
elif first_side==second_side or second_side==third_side or first_side==third_side:
         isosceles_triangle()
elif first_side!=second_side and second_side!=third_side and first_side!=third_side:
         scalene_triangle()
            
quit=input("Press q to quit the program: ")
if quit=='q':
    exit()
    

