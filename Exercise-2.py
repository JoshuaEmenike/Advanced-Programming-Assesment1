import random

joke_count = 0

# Read jokes from file into a list
with open('jokes.txt', 'r', encoding='utf-8') as f:
    jokes = f.readlines()  # each joke should be on a new line
    jokes = [j.strip() for j in jokes if j.strip()]  # remove empty lines

while True:
    user_input = input('Alexa tell me a joke / No?:\n')
    
    if user_input.lower() == "alexa tell me a joke":
        joke_tell = random.choice(jokes)  # pick a random joke each time
        print(joke_tell)
        joke_count += 1
    elif user_input.lower() in ["no", "quit", "exit"]:
        print("Okay, maybe next time!")
        break
    elif joke_count >= 1:
        print("You've heard at least one joke already!")
