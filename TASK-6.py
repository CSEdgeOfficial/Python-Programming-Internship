import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from urllib.parse import urljoin

# Function to check robots.txt for scraping permission
def check_robots_txt(base_url):
    robots_url = urljoin(base_url, '/robots.txt')
    response = requests.get(robots_url)
    if response.status_code == 200:
        robots_txt = response.text
        if "Disallow: /" in robots_txt:
            return False
        return True
    return False

# Function to list all tables in the HTML
def list_tables(soup):
    tables = soup.find_all("table")
    if not tables:
        raise Exception("No tables found on the webpage.")
    table_summaries = []
    for i, table in enumerate(tables):
        summary = table.attrs.get("summary", f"Table {i+1}")
        table_summaries.append(summary)
    return tables, table_summaries

# Function to extract data from the selected table
def extract_data(table):
    data = []
    headers = [header.text.strip() for header in table.find_all("th")]
    rows = table.find_all("tr")[1:]  # Skipping the header row
    for row in rows:
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
    return headers, data

# Main function to perform web scraping
def main():
    # Read the URL from the user
    base_url = input("Enter the URL of the website to scrape: ")

    # Check if scraping is allowed
    if not check_robots_txt(base_url):
        print("It is not possible to perform web scraping on this website.")
        return

    # Send a GET request to fetch the raw HTML content
    response = requests.get(base_url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {base_url}")

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # List all tables
    try:
        tables, table_summaries = list_tables(soup)
    except Exception as e:
        print(f"Error during table listing: {e}")
        return

    # Display the tables to the user and ask for a selection
    print("Tables found on the webpage:")
    for i, summary in enumerate(table_summaries):
        print(f"{i + 1}: {summary}")
    
    try:
        table_index = int(input("Enter the number of the table you want to scrape: ")) - 1
        if table_index < 0 or table_index >= len(tables):
            raise ValueError("Invalid table number selected.")
    except ValueError as e:
        print(f"Error during table selection: {e}")
        return

    # Extract data from the selected table
    try:
        headers, data = extract_data(tables[table_index])
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Save to CSV
    df.to_csv("scraped_data.csv", index=False)

    # Save to JSON
    df.to_json("scraped_data.json", orient="records")

    print("Data has been scraped and saved to scraped_data.csv and scraped_data.json")

if __name__ == "__main__":
    main()
