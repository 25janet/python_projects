def start_game():
    print("🏰 Welcome to the Haunted Castle Adventure Game!")
    name = input("What is your name, adventurer? ").strip().capitalize()
    print(f"\nHello {name}! You wake up in a dusty room.")

    choice1 = input("There's a door to your LEFT, one to your RIGHT, and a dark hallway STRAIGHT ahead.\nWhich one do you choose? (left/right/straight): ").strip().lower()

    if choice1 == "left":
        print("\n🪞 You find a room full of mirrors.")
        print("A voice asks: 'Break a mirror or walk through the reflections?'")
        choice2 = input("Do you BREAK or WALK? ").strip().lower()
        if choice2 == "break":
            print("\n💥 Traps are triggered! Arrows shoot from the walls.")
            print("Game Over. ☠️")
            return
        elif choice2 == "walk":
            print("\n✨ You walk through the reflections and find a hidden passage!")
            print("You escape safely! 🎉")
        else:
            print("Invalid choice. The mirrors crack around you. Game Over. ☠️")

    elif choice1 == "right":
        print("\n📚 You enter a dusty library with a sleeping snake.")
        choice3 = input("Do you TIPTOE or THROW a book to distract it? ").strip().lower()
        if choice3 == "tiptoe":
            print("\n😌 You silently sneak past the snake and find treasure. You win! 🏆")
        elif choice3 == "throw":
            print("\n🐍 The snake wakes up and bites you. Game Over. ☠️")
        else:
            print("You hesitate too long... The snake wakes up. Game Over. ☠️")

    elif choice1 == "straight":
        print("\n🌫️ You walk into a hallway filled with fog and whispers.")
        choice4 = input("Do you FOLLOW the whispers or RUN through the fog? ").strip().lower()
        if choice4 == "follow":
            print("\n🕯️ The whispers guide you safely to the exit. You survive! 🎉")
        elif choice4 == "run":
            print("\n😵 You fall into a hidden pit. Game Over. ☠️")
        else:
            print("You get lost in the fog. Game Over. ☠️")

    else:
        print("\nInvalid choice. The room collapses around you. Game Over. ☠️")

# Start the game
start_game()
