import requests
import json

api = {
    "key": "2fa73590fd8b5a4c6e68098ad5625395",
    "base": "https://api.openweathermap.org/data/2.5/"
}

search_box =document.querySelector(".search-box")
search_box.addEventListener("keypress", set_query)

def set_query(evt):
    if evt.keyCode == 13:
        get_results(search_box.value)

def get_results(query):
    url = f"{api['base']}weather?q={query}&units=metric&APPID={api['key']}"
    response = requests.get(url)
    data = json.loads(response.text)
    display_results(data)

def display_results(weather):
    print(f"City: {weather['name']}, {weather['sys']['country']}")