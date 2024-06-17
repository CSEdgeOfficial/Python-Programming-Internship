# Weather Information

## Overview

This Python program fetches and displays current weather information for a specified city using the OpenWeatherMap API. It provides details such as temperature, humidity, wind speed, and a brief description of the weather.

## Features

- **Fetch Weather Data**: Retrieves current weather data from the OpenWeatherMap API for a specified city.
- **Display Weather Information**: Displays the fetched weather information in a readable format.

## How to Use

1. **Enter a City Name**: When prompted, enter the name of the city for which you want to get the weather information.
2. **View Results**: The program will display the current weather conditions for the specified city.

### Example Usage

1. **Entering a City Name**:
    ```
    Enter the name of a city: London
    ```

2. **Viewing Weather Information**:
    ```
    Current weather in London:
    Description: clear sky
    Temperature: 15.0°C
    Humidity: 72%
    Wind speed: 3.5 m/s
    ```
## Error Handling
The program includes basic error handling to manage common issues:

1. **Invalid API Key:**

If the API key is invalid or missing, the program will display an error message: Error: 401 - {"cod":401,"message":"Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}

2. **City Not Found:**

If the specified city is not found, the program will display an error message: Error: 404 - {"cod":"404","message":"city not found"}

3. **Network Issues:**

If there are network issues or the API endpoint is unreachable, the program will display an appropriate error message: Error: <status_code> - <error_message>
