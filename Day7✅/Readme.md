 **🕸️ Day 7: Large-Scale Scraping with Scrapy & Automation** explained step-by-step, with extra clarity:

---

## 🎯 **Goal:**

Use **Scrapy** to scrape data more efficiently — ideal for large-scale and automated scraping.

---

### ✅ **1. What is Scrapy?**

Scrapy is a **Python framework for web scraping** — fast, powerful, and great for crawling multiple pages or entire sites. It's better than BeautifulSoup for big projects.

---

### ✅ **2. Install Scrapy**

```bash
pip install scrapy
```

---

### ✅ **3. Start a Scrapy Project**

In your terminal, run:

```bash
scrapy startproject myproject
cd myproject
```

This creates the folder structure:

```
myproject/
├── myproject/
│   └── settings.py, middlewares.py, etc.
├── spiders/
│   └── your spiders go here
```

---

### ✅ **4. Create a Spider**

Inside the `spiders/` folder, create a file like `my_spider.py` and write:

```python
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://example.com"]

    def parse(self, response):
        title = response.css("title::text").get()
        yield {"title": title}
```

✅ `name`: Spider name to run from command line
✅ `start_urls`: List of URLs to start scraping
✅ `parse`: A function that receives the response and extracts data

---

### ✅ **5. Run the Spider**

In the terminal:

```bash
scrapy crawl my_spider
```

---

### ✅ **6. Save Data to CSV or JSON**

```bash
scrapy crawl my_spider -o output.csv
# OR
scrapy crawl my_spider -o output.json
```

---

### ✅ **7. Use CSS Selectors / XPath in Scrapy**

```python
response.css("div.quote span.text::text").getall()
# or
response.xpath("//div[@class='quote']/span[@class='text']/text()").getall()
```

---

### ✅ **8. Practice Task:**

* Scrape all quotes & authors from [http://quotes.toscrape.com](http://quotes.toscrape.com) using Scrapy.
* Save them into a CSV file using `-o quotes.csv`.

