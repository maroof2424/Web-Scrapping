Great, Maroof! Let's dive into **🔍 Day 2: Basic Web Scraping with BeautifulSoup**.
You'll learn how to **extract data from static websites** using Python.

---

## ✅ **📚 What You’ll Learn Today**

* How to use the `requests` library to fetch web pages.
* How to parse HTML with **BeautifulSoup**.
* How to extract **titles, paragraphs, links**, etc.

---

## 🔧 **Step 1: Install Required Libraries**

In your terminal or command prompt, run:

```bash
pip install beautifulsoup4 requests
```

---

## 🧠 **Step 2: Basic Scraping Example**

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # Replace with any real site later
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Extract the title of the page
title = soup.find("title").text
print("Title:", title)
```

---

## 📌 **Step 3: Learn Core BeautifulSoup Methods**

| Method            | Purpose                                |
| ----------------- | -------------------------------------- |
| `soup.find()`     | Finds the first matching element       |
| `soup.find_all()` | Finds all matching elements            |
| `soup.select()`   | Uses CSS selectors to find elements    |
| `element.text`    | Extracts text from an element          |
| `element.attrs`   | Returns a dictionary of tag attributes |

---

## 🧪 **Step 4: Practice Tasks**

Try this with any public static website (e.g., `https://quotes.toscrape.com/`):

```python
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
```

---

## 📁 **Mini Practice Challenge for Today**

**Scrape the following from [https://quotes.toscrape.com/](https://quotes.toscrape.com/):**

* All quotes on the first page
* Their authors
* Save the data in a `.txt` or `.csv` file

Want a solution file for that? Just say "Yes" and I’ll share it!

---

Ready for Day 3 after this? Or want a quiz/practice sheet first? 😊
