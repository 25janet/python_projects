products = {
    'milk': 50,
    'eggs': 13,
    'bread': 65,
    'banana': 10
}
cart = {}

def show_products():
    print("\nAvailable products are:")
    for item, price in products.items():
        print(f" - {item.capitalize()}: KSH {price}")

def add_cart():
    item = input("Enter the product name to add: ").lower()
    if item in products:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                return
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
            print(f"Added {quantity} {item}(s) to cart.")
        except ValueError:
            print("Please enter a valid integer for quantity.")
    else:
        print("Product not found.")

def remove_cart():
    item = input("Enter the product to be removed: ").lower()
    if item in cart:
        try:
            quantity = int(input("Enter the amount to be removed: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                return
            if quantity >= cart[item]:
                del cart[item]
                print(f"Removed all {item}(s) from cart.")
            else:
                cart[item] -= quantity
                print(f"Removed {quantity} {item}(s) from cart.")
        except ValueError:
            print("Please enter a valid integer for quantity.")
    else:
        print("Item not in cart.")

def view_cart():
    print("Your cart:")
    total = 0
    for item, qty in cart.items():
        price = products[item] * qty
        total += price
        print(f" - {item.capitalize()} x{qty} = Ksh {price}")
    print(f"💰 Total: Ksh {total}")

def checkout():
    view_cart()
    print("🧾 Thank you for shopping! Exiting now...")
    exit()

while True:
    print("\n📋 Menu:")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        show_products()
    elif choice == '2':
        add_cart()
    elif choice == '3':
        remove_cart()
    elif choice == '4':
        view_cart()
    elif choice == '5':
        checkout()
    else:
        print("❌ Invalid choice. Try again.")
