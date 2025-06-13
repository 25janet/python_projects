import requests
def get_weather(city_name):
    api_key = "30c7b844a7de4316e364e5509fe0e3d7"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q':city_name,
        'appid' :api_key,
        'units': 'metric'

    }
    response = requests.get(base_url,params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature' : data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
         return {'error': 'City not found or API error'}
city = input("Enter city name: ")
weather = get_weather(city)
if 'error' in weather:
    print(weather['error'])
else:
    print(f"🌍 Weather in {weather['city']}:")
    print(f"🌡 Temperature: {weather['temperature']}°C")
    print(f"🌧 Description: {weather['description'].capitalize()}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"🌬 Wind Speed: {weather['wind_speed']} m/s")