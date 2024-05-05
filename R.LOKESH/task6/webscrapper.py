import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the elements containing the data you want to extract
        # Replace 'example' with actual HTML tags and classes/IDs
        data_elements = soup.find_all('div', class_='example')
        
        # Extract data from the elements and store in a list of dictionaries
        scraped_data = []
        for element in data_elements:
            # Example: Extract text from a specific tag within the element
            data = {
                'title': element.find('h2').text.strip(),
                'description': element.find('p').text.strip()
            }
            scraped_data.append(data)
        
        return scraped_data
    else:
        print("Error: Failed to fetch website")
        return []

def save_to_csv(data, filename):
    # Define CSV header based on keys of the first dictionary in the list
    fields = list(data[0].keys())
    
    # Write data to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        # Write header
        writer.writeheader()
        
        # Write rows
        for row in data:
            writer.writerow(row)

def main():
    url = "https://example.com"
    filename = "data.csv"
    
    # Scrape website
    scraped_data = scrape_website(url)
    
    # Save data to CSV
    save_to_csv(scraped_data, filename)
    
    print(f"Data has been scraped and saved to {filename}")

if __name__ == "__main__":
    main()
