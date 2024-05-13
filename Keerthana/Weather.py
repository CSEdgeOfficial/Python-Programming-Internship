import tkinter as tk
from tkinter import messagebox
import requests
def fetch_weather_data():
    api_key = "83514bedc3a5857be653cf3e591e19be"
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        display_weather_data(data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")

def display_weather_data(data):
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    result_label.config(text=f"Weather: {description}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")

root = tk.Tk()
root.title("Weather App")

label = tk.Label(root, text="Enter city name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Fetch Weather", command=fetch_weather_data)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()  