import requests
import datetime

# Your OpenWeatherMap API key 
API_KEY = '69e7dd8a8069d4066de2a18ea5996e36'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

# Function to get current weather data
def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to get weather forecast data
def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Function to display weather data
def display_weather_data(city):
    current_weather = get_current_weather(city)
    forecast = get_forecast(city)
    
    if current_weather.get("cod") != 200 or forecast.get("cod") != "200":
        print("Failed to retrieve data. Please check the city name or API key.")
        return

    # Current weather
    print(f"\nCurrent weather in {city.capitalize()}:")
    print(f"Temperature: {current_weather['main']['temp']}°C")
    print(f"Weather: {current_weather['weather'][0]['description']}")
    print(f"Humidity: {current_weather['main']['humidity']}%")
    print(f"Wind Speed: {current_weather['wind']['speed']} m/s")
    
    # Forecast
    print(f"\n5-Day Forecast for {city.capitalize()}:")
    for item in forecast['list']:
        timestamp = item['dt']
        date_time = datetime.datetime.fromtimestamp(timestamp)
        if date_time.hour == 12:  # Show data for 12 PM each day
            temp = item['main']['temp']
            weather = item['weather'][0]['description']
            print(f"{date_time.strftime('%Y-%m-%d %H:%M:%S')}: {temp}°C, {weather}")

    # Temperature trends (Average temperatures per day)
    temp_trends = {}
    for item in forecast['list']:
        date = datetime.datetime.fromtimestamp(item['dt']).date()
        if date not in temp_trends:
            temp_trends[date] = []
        temp_trends[date].append(item['main']['temp'])
    
    print(f"\nTemperature Trends in {city.capitalize()}:")
    for date, temps in temp_trends.items():
        avg_temp = sum(temps) / len(temps)
        print(f"{date}: {avg_temp:.2f}°C")

# Main function
def main():
    city = input("Enter the city name: ")
    display_weather_data(city)

if __name__ == "__main__":
    main()
