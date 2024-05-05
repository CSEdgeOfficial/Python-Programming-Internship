from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "fe35e3bb6b21c465def7ea465e765f7f"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('index.html', show_weather=True, weather_data=weather_data)
    else:
        return render_template('index.html', show_weather=False)


if __name__ == '__main__':
    app.run(debug=True)