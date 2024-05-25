import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = [title.text.strip() for title in soup.find_all('h1')]
    
    return titles

def save_to_csv(data, filename):
    # Write data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(['Title'])
       writer.writerows(data)

def save_to_json(data, filename):
    # Write data to a JSON file
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def main( ):
    url = input("Enter the URL of the website you want to scrape: ")
    
    
    output_format = input("Enter 'csv' or 'json' to choose the output format: ").lower()
    if output_format not in ['csv','json']:
        print("Invalid output format. Please enter 'csv' or 'json'.")
        return
    extracted_data = scrape_website(url)
    if output_format == 'csv':
        filename = input("Enter the filename to store the data (without extension): ") + '.csv'
        save_to_csv(extracted_data, filename)
        print(f"Data has been saved to {filename}")
    elif output_format == 'json':
        filename = input("Enter the filename to store the data (without extension): ") + '.json'
        save_to_json(extracted_data, filename)
        print(f"Data has been saved to {filename}")
if __name__ == "__main__":
    main()
        
