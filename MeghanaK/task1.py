import requests

def get_weather_data(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_current_weather(data):
    print("Current Weather Conditions:")
    print("---------------------------")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def get_forecast(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_forecast(data):
    print("\nWeather Forecast for the next 5 days:")
    print("-------------------------------------")
    for forecast in data['list']:
        print(f"Date: {forecast['dt_txt']}")
        print(f"Weather: {forecast['weather'][0]['description']}")
        print(f"Temperature: {forecast['main']['temp']}°C")
        print("")

def main():
    api_key = 'b73f861c9b47fe465e680a5d330e01eb' 
    city_name = input("Enter city name: ")
    
    current_weather_data = get_weather_data(api_key, city_name)
    display_current_weather(current_weather_data)
    
    forecast_data = get_forecast(api_key, city_name)
    display_forecast(forecast_data)

if __name__ == "__main__":
    main()
