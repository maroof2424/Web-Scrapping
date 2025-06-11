import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com/page/"

for page in range(1, 6):  # Scrape pages 1 to 5
    url = base_url + str(page) + "/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        break
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    
    print(f"\n--- Quotes from page {page} ---")
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"{text} — {author}")
