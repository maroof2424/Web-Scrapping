Great! You're now on **⚡ Day 3: Advanced Scraping & Handling Dynamic Pages**. Below is a **complete Python script** that shows how to:

1. Use headers to avoid being blocked.
2. Extract data using **CSS selectors**.
3. Handle **pagination** to scrape multiple pages.

---

### 🐍 Example: Blog Title Scraper with Pagination

```python
import requests
from bs4 import BeautifulSoup

# Base URL with pagination (replace with actual site)
base_url = "https://quotes.toscrape.com/page/"

# Custom headers to avoid getting blocked
headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Scraping blog post titles...\n")

# Loop through multiple pages
for page in range(1, 6):  # Pages 1 to 5
    url = f"{base_url}{page}/"
    response = requests.get(url, headers=headers)

    # Check if page exists
    if response.status_code != 200:
        print(f"Page {page} not found!")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract quote text (like blog titles)
    quotes = soup.select("span.text")  # CSS selector

    print(f"\nPage {page} Results:")
    for quote in quotes:
        print("-", quote.get_text())
```

---

### ✅ Output:

```
Scraping blog post titles...

Page 1 Results:
- “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
...

Page 2 Results:
- “I have not failed. I've just found 10,000 ways that won't work.”
...
```

---

### 🔁 Modify for Your Target Site:

* Change `base_url` to your desired site.
* Use **Chrome DevTools → Inspect → Copy selector** to get the correct CSS path for titles.

---

Want to try this with a real **blog or eCommerce** website? Just send the URL and I’ll customize it for you!
