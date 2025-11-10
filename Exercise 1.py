import random
question_count=1
first_num=0
Second_num=0
correct_answer=0
level_display=0
quiz=True
#setting the points for the scores
points=0
#creating the functions to display a questions based on the operation chosen by the user
def operation():
    return random.choice(['+','-'])
#This displays the difficulty level at the beginning of program
def display():
   global level_display	
   print( f"choose according to serial number \n 1)Easy \n 2)Moderate \n 3)Advanced") 
    #asking the user to choose by picking serial number
   level_display=int(input('Time waits for no one, pick fast\n'))
    
    #this block of code provides the ranking system
def ranking(points):
    if points==100:
        print('You got an S rank')
    elif points>=70:
      print('you got A rank')
    elif points>=60:
        print("you got  B rank")
    elif points>=50:
        print('you got  C rank')        
    else:
        print('you failed woefully')        
#this block of code generates the random numbers that will be used in questioning the users

def random_number(level_display):
 global first_num,Second_num
 match level_display:  
    case 1:
       first_num=random.randint(0,9)
       Second_num=random.randint(0,9)  
    
    case 2:
        first_num=random.randint(10,80)
        Second_num=random.randint(10,99)
    case 3:
         first_num=random.randint(100,890)
         Second_num=random.randint(100,999)
    case _:
        print("Invalid selection, defaulting to Easy")
    
#this prints out the question for the user and takes input
def question(operate):
    global first_num,Second_num,question_count
    match operate:
        case '+':
              return int(input(f"q.{question_count} solve {first_num} {operate} {Second_num}"))
        case'-' :
          if Second_num>first_num:
             return int(input(f"q.{question_count} solve {Second_num} {operate} {first_num}"))
            
          else:
               return int(input(f"q.{question_count} solve {first_num} {operate} {Second_num}"))
  
   
#gets info from opration in order to determine the method that was used and the correct answer
def correct(operation):
    global first_num,Second_num,correct_answer
    match operation:
        case '+':
             correct_answer=first_num+Second_num
        case'-' :
          if Second_num>first_num:
             correct_answer=Second_num -first_num
            
          else:
              correct_answer=first_num-Second_num  
                                 
    #this function was made to check if the users input was the correct answer
def is_correct(question,operate):
   global first_num,Second_num,correct_answer,points,question_count
   
   if correct_answer==question:
        points+=10
        
        print(f"your answer is correct, you got {points} points")
   else:
        if correct_answer!=question:
            try:
                question = int(input(f"Try again: solve {first_num} {operate} {Second_num} = \t"))
                if question == correct_answer:
                    points += 5
                    print(f"your answer is correct, you got {points}")
                else:
                    print("youre wrong")
                   
            except ValueError:
             print("Please enter a valid integer.")
   question_count+=1

#this function was made to replay the program for the user that is if the user wants to or not
def replay():
    global points,question_count
    
    re=input('do you wanna play again?\n yes \t or \t no\t:     ') 
    if re.capitalize()=="Yes":
       points=0
       question_count=1
    elif re.capitalize()=="No":
         exit()
    else:
         print("Invalid prompt") 
         replay()
while quiz==True:               
    display()    
    while question_count<=10:
        random_number(level_display)
        operate=operation()
        correct(operate)
        quest=question(operate)
        is_correct(quest,operate)
        
    ranking(points)
    replay()
    