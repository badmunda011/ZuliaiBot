import requests
import json

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        weather_data = data["weather"][0]
        weather_description = weather_data["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description}")
    else:
        print("City not found!")

city = input("Enter city name: ")
get_weather(city)

