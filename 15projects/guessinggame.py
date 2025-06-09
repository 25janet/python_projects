import random
computer_choice = random.randint(0,100)
print("Guess a number between 0 -100")
score = 0
while True:
    try:
        user_input = int(input("Guess the number: "))
        score += 1
        if user_input < computer_choice:
            print("The number is too low")
        
        elif user_input > computer_choice:
            print("The number is too high")
        
        else:
            print("You have guessed the number correctly")
            break
    except ValueError:
        print("please enter a valid number")