from datetime import datetime

expenses = []

def add_expenses():
    try:
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the category (bills, transport, clothes, vacation): ").strip().lower()
        note = input("Optional note (press enter to skip): ")  
        date = datetime.now().strftime("%d-%m-%Y %H:%M")

        expense = {
            "amount": amount,
            "category": category,
            "date": date,
            "note": note
        }
        expenses.append(expense)
        print("✅ Expense added!")
    except ValueError:
        print("❌ Please enter a valid number for amount.")

def view_expenses():
    if not expenses:
        print("📭 The list is empty...")
    else:
        print("\n📒 All Expenses:")
        for e in expenses:
            print(f"{e['date']} - Ksh {e['amount']} | {e['category'].title()} | {e['note']}")

def total_amount():
    total = sum(e['amount'] for e in expenses)
    print(f"💰 The total spent: Ksh {total}")

def filter_by_category():
    cat = input("Enter the category to filter by: ").strip().lower()
    filtered = [e for e in expenses if e['category'] == cat]
    if filtered:
        print(f"\n📂 Expenses in category '{cat.title()}':")
        for e in filtered:
            print(f"{e['date']} - Ksh {e['amount']} | {e['note']}")
    else:
        print("❌ No expenses in that category.")

# 🌟 Main loop
while True:
    print("\n📌 Expense Tracker Menu:")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total")
    print("4. Filter by category")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_amount()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        print("🧾 Goodbye! Stay financially smart! 💡")
        break
    else:
        print("❌ Invalid choice.")
