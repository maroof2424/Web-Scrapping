import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/page/"
headers = {
    "User-Agent" : "Mozilla/5.0"
}

print("Scraping blog post titles...\n")

for page in range(1,6):
    url = f"{base_url}{page}/"
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        print(f"page {page} not found!")
        break

    soup = BeautifulSoup(response.text,"html.parser")

    qoutes = soup.select("span.text")
    print(f"\nPage {page} Results:")
    for quote in qoutes:
        print(f"- {quote.get_text()}")