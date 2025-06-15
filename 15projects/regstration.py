import requests
def register_users(email,password):
    url = "https://reqres.in/api/register"
    headers = {
        "Content-Type" : "application/json",
        "User-Agent" : "MyPythonApp/1.0",
        "x-api-key": "reqres-free-v1"
    }
    data = {
        "email": email,
        "password":password
    }
    response = requests.post(url,json=data,headers=headers)
    try:
        res_json = response.json()
    except requests.exceptions.JSONDecodeError:
        print("invalid JSON response from the server.")
        print("raw message: ",response.text)
    if response.status_code == 200:
        token = res_json.get("token")
        print("Registration successful!")
        print(f"Token: {token}")
    else:
        print("registration failed")
        print("Message: ",res_json.get("error", "No error message provided"))
    
register_users("janet.weaver@reqres.in","22134gfh")
        


