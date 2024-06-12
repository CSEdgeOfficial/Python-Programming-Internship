import requests
from bs4 import BeautifulSoup

# Get the HTML text
url = "https://quotes.toscrape.com/"
response = requests.get(url)
text = response.text

# Parse the text with Beautiful Soup
soup = BeautifulSoup(text, "lxml")

# Extract authors
authors = soup.find_all("small", class_="author")
author_set = set(author.text.strip() for author in authors)

# Extract quotes
quotes = soup.find_all("span", class_="text")
quote_list = [quote.text.strip() for quote in quotes]

# Extract top ten tags
top_tags = soup.find("div", class_="tags-box")
tags = top_tags.find_all("a")
tag_list = [tag.text.strip() for tag in tags]

# Loop through all pages to get unique authors (if applicable)
def get_page_authors(page_url):
    # Your implementation here
    pass
