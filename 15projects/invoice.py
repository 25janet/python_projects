import requests

def collect_info():
    name = input("Enter the name of the customer: ")
    items_purchased = []

    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == "done":
            break
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            items_purchased.append({
                "name": item_name,
                "quantity": quantity,
                "price": price
            })
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
    return name,items_purchased

def send_data(name,items_purchased):
    payload = {
        "customer_name": name,
        "purchases": items_purchased
    }

    url = "https://reqres.in/api/users"  
    try:
        response = requests.post(url, json=payload,timeout=9)
        if response.status_code == 201:
            try:
                response_data = response.json()
                print("\n✅ Data successfully sent!")
                print("📝 Server Response:")
                print(response_data)
            except requests.exceptions.JSONDecodeError:
                print("❌ Could not decode server response.")
                print("Raw response text:", response.text)
        else:
            print(f"❌ Failed to send data. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.Timeout:
         print("⏱️ Request timed out. Try again later.")
    except requests.exceptions.ConnectionError:
        print("🔌 Network error. Please check your internet connection.")
name,purchases = collect_info()
if purchases:
    send_data(name, purchases)
else:
    print("⚠️ No purchases recorded. Exiting...")







