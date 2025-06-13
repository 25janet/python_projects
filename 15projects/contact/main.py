contacts = {}
def add_contact():
    name = input("Enter a name: ").strip()
    phone = input("Enter a phone: ").strip()
    email = input("Enter an email: ").strip()
    contacts[name] = {'phone': phone, 'name': name, 'email':email}
    print(f"Contact for {name} added!")

def view_contact():
    if not  contacts:
        print("No contacts found!")
    else:
        for name,info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone:{info['phone']}")
            print(f"Email: {info['email']}")

def search_contact():
    name =  input("Enter contact to search").strip().title()
    if name in contacts:
        print(f"\n👤 Name: {name}")
        print(f"📞 Phone: {contacts[name]['phone']}")
        print(f"📧 Email: {contacts[name]['email']}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact {name} deleted.")
    else:
        print("❌ Contact not found.")

while True:
    print("\n📋 Contact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("👋 Goodbye! Exiting Contact Book.")
        break
    else:
        print("❌ Invalid option. Try again.")
