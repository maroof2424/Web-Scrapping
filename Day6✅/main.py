# scraper.py

import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect or create SQLite database
conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        author TEXT
    )
""")

base_url = "http://quotes.toscrape.com/page/"

for page in range(1, 6):
    url = base_url + str(page) + "/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        # Insert into database
        cursor.execute("INSERT INTO quotes (text, author) VALUES (?, ?)", (text, author))

    print(f"✅ Saved quotes from page {page}")

# Commit changes and close connection
conn.commit()
conn.close()
