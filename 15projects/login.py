import requests

def login_user(email, password):
    url = "https://reqres.in/api/login"
    data = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=data)
    print(response.status_code)

    try:
        response_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Server did not return valid JSON.")
        print("Response text:", response.text)
        return

    if response.status_code == 200:
        token = response_data.get("token")
        print("✅ Login successful!")
        print(f"🔑 Token: {token}")
    else:
        print("❌ Login failed.")
        print("Message:", response_data.get("error", "No error message provided"))

# ✅ Use the correct test credentials from Reqres
login_user("eve.holt@reqres.in", "cityslicka")
