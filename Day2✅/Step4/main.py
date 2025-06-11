import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all quotes
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print("Quote:", quote.text)

# Extract all authors
authors = soup.find_all("small", class_="author")
for author in authors:
    print("Author:", author.text)

# Extract all tags
tags = soup.select(".tags .tag")
for tag in tags:
    print("Tag:", tag.text)
