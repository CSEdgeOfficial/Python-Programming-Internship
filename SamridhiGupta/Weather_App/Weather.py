import requests

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "4e3bb6b4c5a92eaabcfef739e346e861"
# Function to get weather data from the API
def get_weather_data(city):
    
    url = f"{API_ENDPOINT}?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to display weather information
def display_weather_info(weather_data):
    
    if weather_data:
        # Get relevant data from the weather dictionary
        city_name = weather_data["name"]
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        
        # Display current weather conditions
        print(f"Current weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print("No weather data available.")

def main():
    city = input("Enter the name of a city: ")
    weather_data = get_weather_data(city)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()