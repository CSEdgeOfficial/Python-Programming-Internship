import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, filename):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    data_list = []
    for card in soup.find_all('div', class_='card'):
        title_element = card.find('div', class_='title').find('h3')
        description_element = card.find('div', class_='matter').find('p')
        if title_element and description_element:
            title = title_element.text.strip()
            description = description_element.text.strip()
            data_list.append([title, description])
        else:
            print("Missing title or description in card")

    if not data_list:
        print("No data found on the page")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Description'])
        writer.writerows(data_list)

    print(f"Data scraped successfully and saved to {filename}")

url = 'https://www.webstacknotes.com/'
filename = 'data.csv'
scrape_website(url, filename)
