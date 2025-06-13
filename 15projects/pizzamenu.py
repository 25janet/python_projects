def menu():
    print("\n🍕 Welcome to Pizza Hut! Place your order.")
    print("Small Pizza = $100")
    print("Medium Pizza = $200")
    print("Large Pizza = $300")
    print("Pepperoni for Small Pizza = $30")
    print("Pepperoni for Medium & Large Pizza = $50")
    print("Extra Cheese = $20\n")

def order_pizza():
    while True:
        try:
            menu()
            choice = input("Enter size (small / medium / large): ").lower().strip()
            choice2 = input("Do you want pepperoni? (yes/no): ").lower().strip()
            choice3 = input("Do you want extra cheese? (yes/no): ").lower().strip()

            total_cost = 0

            match choice:
                case "small":
                    total_cost += 100
                    if choice2 == "yes":
                        total_cost += 30
                    if choice3 == "yes":
                        total_cost += 20
                case "medium":
                    total_cost += 200
                    if choice2 == "yes":
                        total_cost += 50
                    if choice3 == "yes":
                        total_cost += 20
                case "large":
                    total_cost += 300
                    if choice2 == "yes":
                        total_cost += 50
                    if choice3 == "yes":
                        total_cost += 20
                case _:
                    print("❌ Invalid pizza size. Please try again.\n")
                    continue

            print(f"✅ Your total cost is: ${total_cost}")
            
            again = input("Do you want to order again? (yes/no): ").strip().lower()
            if again != "yes":
                print("👋 Goodbye! Thanks for ordering.")
                break

        except ValueError:
            print("⚠️ Invalid input! Please try again.")

# Run the program
order_pizza()
