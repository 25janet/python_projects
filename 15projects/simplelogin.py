import  requests
def login_user(email,password):
 url = "https://reqres.in/api/login"
 headers = {
  "x-api-key": "reqres-free-v1",
  "Content-Type": "application/json"
    }
 data = {
  "email": email,
  "password" : password
 }
 response = requests.post(url,json=data,headers = headers)
 try:
  response_data = response.json()
 except requests.exceptions.JSONDecodeError:
        print("❌ Server did not return valid JSON.")
        print("Response text:", response.text)
        return
 if response.status_code == 200:
    token = response_data.get("token")
    print("login successful")
    print(f"Token: {token}")
 else:
    print("❌ Login failed.")
    print("Message:", response_data.get("error", "No error message provided"))

login_user("janet.weaver@reqres.in","11keyshi")