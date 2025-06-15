import requests
def funcat_fetcher():
    response =  requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        data = response.json()
        print("The random fun cat fact: ")
        print({data['fact']})
    else:
        print("Failed to retrieve a fun fact about cat")
        print(response.status_code)

funcat_fetcher()