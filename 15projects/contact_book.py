contact_book = []

def add_contact():
    print("📥 Adding a new contact.")
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    contact_book.append({"name": name, "phone number": phone_number, "email": email})
    print("✅ Contact added successfully!\n")

def search_contact():
    search_input = input("🔍 Enter the name to search: ")
    found = False
    for contact in contact_book:
        if contact["name"].lower() == search_input.lower():
            print(f"\n📇 Name: {contact['name']}")
            print(f"📞 Phone number: {contact['phone number']}")
            print(f"📧 Email: {contact['email']}\n")
            found = True
            break
    if not found:
        print("⚠️ The name is not in the contact book.\n")

def update_contact():
    update_input = input("✏️ Enter the name to update: ")
    for contact in contact_book:
        if contact["name"].lower() == update_input.lower():
            contact["name"] = input("Enter the new name: ")
            contact["phone number"] = input("Enter the new phone number: ")
            contact["email"] = input("Enter the new email: ")
            print("✅ Contact updated successfully!\n")
            return
    print("⚠️ The name is not in the contact book.\n")

def delete_contact():
    delete_input = input("🗑️ Enter the name to delete: ")
    for contact in contact_book:
        if contact["name"].lower() == delete_input.lower():
            contact_book.remove(contact)
            print("✅ Contact has been removed successfully!\n")
            return
    print("⚠️ Contact not found.\n")

def view_contacts():
    print("📒 Viewing contact book:")
    if not contact_book:
        print("🚫 The contact book is empty.\n")
    else:
        for i, contact in enumerate(contact_book, 1):
            print(f"\nContact {i}")
            print(f"Name: {contact['name']}")
            print(f"Phone number: {contact['phone number']}")
            print(f"Email: {contact['email']}")
        print()  # Extra line space at the end

def show_menu():
    while True:
        print("\n🔧 MENU")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. View contact list")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1–6): "))
            match choice:
                case 1:
                    add_contact()
                case 2:
                    search_contact()
                case 3:
                    update_contact()
                case 4:
                    delete_contact()
                case 5:
                    view_contacts()
                case 6:
                    print("👋 Exiting the contact book. Goodbye!")
                    break
                case _:
                    print("⚠️ Invalid option. Please choose 1 to 6.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Start the program
show_menu()
