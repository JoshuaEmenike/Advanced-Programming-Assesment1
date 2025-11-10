on=True
number_count=0
def display():
    print("welcome to the triangle calculator app")
    input1=float(input("Enter the length of first side of the triangle: "))
    input2=float(input("Enter the length of second side of the triangle: "))   
    input3=float(input("Enter the length of third side of the triangle: "))
    total=input1 + input2 + input3
    print(f"The perimeter of the triangle is {total}")
    
def quit():
    print(f"Goodbye User you continued  the prgram {number_count} times :) ")

        
def condtion():
    global number_count
    while True: 
       number_count+=1
       display() 
       y=input("Do you want to continue? Y/N: ")
       if y.upper()== "N":
            quit()
            break   
       elif y.upper()!= "Y" or "N":
            print("Invalid input, please enter Y or N")
            display()
           

condtion()
        
