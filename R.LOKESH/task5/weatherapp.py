import requests
import json

def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    print("Current Weather Conditions:")
    print("---------------------------")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(api_key, city)
    if weather_data['cod'] == 200:
        display_weather(weather_data)
    else:
        print("Error fetching weather data. Please check your input.")

if __name__ == "__main__":
    main()
