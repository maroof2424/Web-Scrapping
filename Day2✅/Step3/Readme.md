Got it, Maroof! Here's **📌 Step 3: Learn Core BeautifulSoup Methods** from **Day 2** — this is where you learn how to **extract data using key BeautifulSoup functions**.

---

## 📌 **Step 3: Learn Core BeautifulSoup Methods**

These are the **essential methods** you'll use to extract elements from HTML.

---

### ✅ 1. `soup.find()`

* Returns the **first** matching tag.

```python
title = soup.find("h1")
print(title.text)
```

---

### ✅ 2. `soup.find_all()`

* Returns **all** matching tags in a list.

```python
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
```

---

### ✅ 3. `tag.get_text()`

* Removes all HTML and gives you only the text.

```python
text = soup.find("h1").get_text()
print(text)
```

---

### ✅ 4. `tag.attrs` or `tag['attribute']`

* Get the value of an attribute (like `href`, `src`, etc.)

```python
link = soup.find("a")
print(link['href'])          # OR
print(link.attrs['href'])
```

---

### ✅ 5. `soup.select()` (CSS Selectors)

* Very powerful. Use CSS-like syntax to target elements.

```python
titles = soup.select("div.article h2")
for t in titles:
    print(t.text)
```

---

### ✅ Bonus: Search with class or id

```python
soup.find("div", class_="product")
soup.find(id="main-container")
```

---

### 🧪 Mini Practice Example

```python
from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

quotes = soup.find_all("span", class_="text")

for q in quotes:
    print(q.get_text())
```

---

Let me know if you want **an exercise or mini challenge** based on this step 👨‍💻 or ready to move to Day 3: Advanced Scraping & Pagination!
