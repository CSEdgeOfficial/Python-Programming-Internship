import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize a Chrome webdriver
driver = webdriver.Chrome()

# Open a web page
driver.get("https://example.com")

# Wait for the search box to be clickable
search_box = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "search-box"))
)

# Do something with the element, like typing text into it
search_box.send_keys("Your search query")

# Close the browser
driver.quit()

# Define the API parameters
api_key = "2fa73590fd8b5a4c6e68098ad5625395"
base_url = "https://api.openweathermap.org/data/2.5/"

# Define a function to get weather results
def get_results(query):
    url = f"{base_url}weather?q={query}&units=metric&APPID={api_key}"
    response = requests.get(url)
    data = response.json()
    display_results(data)


# Define a function to display weather results
def display_results(weather):
    print(f"City: {weather['name']}, {weather['sys']['country']}")


# Call the get_results function with a sample query
get_results("London")
