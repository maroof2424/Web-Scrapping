Sure! Here's **Day 5** focusing on **Handling Pagination & Saving Data** — the natural next step after Day 4 Selenium basics.

---

## ⚡ **Day 5: Pagination & Saving Scraped Data**

📌 **Goal:**
Learn how to scrape multiple pages (pagination) and save the collected data to a CSV file.

---

### ✅ **Step 1: Understanding Pagination**

Many websites divide their content into multiple pages. To scrape all data, you need to:

* Detect the **Next page** button or URL pattern
* Loop through pages and scrape each page’s content

---

### ✅ **Step 2: Pagination Example with Requests + BeautifulSoup**

If website uses URLs like:

```
https://example.com/page/1
https://example.com/page/2
https://example.com/page/3
...
```

You can loop like this:

```python
import requests
from bs4 import BeautifulSoup

for page in range(1, 6):  # scrape pages 1 to 5
    url = f"https://example.com/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    titles = soup.select("h2.post-title")
    for title in titles:
        print(title.text)
```

---

### ✅ **Step 3: Pagination with Selenium**

Some websites load pages dynamically or require clicks on “Next” button:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/blog")

while True:
    titles = driver.find_elements(By.CLASS_NAME, "post-title")
    for title in titles:
        print(title.text)
    
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(2)  # wait for page load
    except:
        print("No more pages.")
        break

driver.quit()
```

---

### ✅ **Step 4: Save Data to CSV**

Using Python’s built-in `csv` module:

```python
import csv

data = [["Title 1", "Company 1"], ["Title 2", "Company 2"]]

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company"])
    writer.writerows(data)
```

---

### ✅ **Complete Practice Task**

* Scrape job titles and companies from 3 pages of a job site
* Save results to a CSV file

