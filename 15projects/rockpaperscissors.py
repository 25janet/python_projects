import random
def game():
    choices = ["rock","paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice(rock,paper,scissors): ").strip().lower()
    while user_choice not in choices:
        print("Invalid choices.Try again")
    print(f"Computer chose: {computer_choice} && User chose: {user_choice}")
    if computer_choice == user_choice:
        print("it is a tie.")
    elif computer_choice == "rock":
        if user_choice == "scissors":
            return "You lose! Computer won."
        else:
            return "You win!Paper covers rock"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            return "You lose. Scissors smashes rock."
        else:
            return "You win. Scissors cuts paper."
    elif computer_choice == "paper":
        if user_choice == "rock":
            return "You lose! paper cover rock"
        else:
            return "You win! scissors smashes rock"
    else:
        return "invalid operator"

while True:
    print("Let us play rock,paper,scissors")
    print(game())
    again = input("Do you want to continue the game(yes)").lower()
    if again != 'yes':
        print("goodbye")
        break

