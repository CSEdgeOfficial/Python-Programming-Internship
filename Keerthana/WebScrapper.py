import requests
import json

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Store the data in a JSON file
        data = {
            "url": url,
            "html_content": response.content.decode('utf-8')  # Decode bytes to string
        }
        
        with open('scraped_data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Data extracted and stored successfully!")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

# Example usage
url = 'https://www.geeksforgeeks.org/'
scrape_website(url)
