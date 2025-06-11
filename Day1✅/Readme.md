Bilkul Maroof! 💥 Yeh raha **Day 1** ka **full detailed lesson** with explanations + practice. Aaj ka goal hai: **Python basics + Web fundamentals + Developer Tools**. Chalo shuru karte hain! 👨‍💻

---

## 🔰 **Day 1: Python & Web Basics**

### 📌 **Goal:**

Understand **Python basics**, how **websites work**, and how to inspect them using **Developer Tools**.

---

## 🐍 Part 1: Python Basics (Skip if already strong)

### ✅ 1.1 Python Concepts You Should Know:

Practice each one in your own `.py` file or in an online compiler like [replit.com](https://replit.com):

#### ✅ Variables & Data Types:

```python
name = "Maroof"
age = 16
price = 99.99
is_valid = True
```

#### ✅ Lists & Dictionaries:

```python
fruits = ["apple", "banana", "mango"]
user = {"name": "Maroof", "age": 16}
```

#### ✅ Loops:

```python
for fruit in fruits:
    print(fruit)
```

#### ✅ Functions:

```python
def greet(name):
    print("Hello", name)

greet("Maroof")
```

#### ✅ File Handling:

```python
with open("sample.txt", "w") as file:
    file.write("Hello from Python!")
```

---

### 🔍 1.2 Regular Expressions (`re` Module)

Used for pattern matching in text.

```python
import re

text = "My phone number is 0312-1234567"
pattern = r"\d{4}-\d{7}"
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
```

**Practice Idea:** Find email addresses, phone numbers, or names using regex.

---

## 🌍 Part 2: How Websites Work

### ✅ 2.1 Learn HTML/CSS Basics

#### Learn these HTML tags:

```html
<h1>Heading</h1>
<p>Paragraph</p>
<a href="#">Link</a>
<img src="image.jpg" />
<div class="box">Content</div>
```

> 🔗 [HTML Cheat Sheet](https://web.stanford.edu/group/csp/cs21/htmlcheatsheet.pdf)

#### Learn basic CSS (just read now):

* Classes: `.class-name`
* IDs: `#id-name`
* Selectors: `tag`, `.class`, `#id`

---

### ✅ 2.2 Understand HTTP Protocol

#### Common HTTP Methods:

* **GET** – Get data (like visiting a page)
* **POST** – Send data (like submitting a form)

#### Status Codes:

* `200`: OK
* `404`: Not Found
* `403`: Forbidden
* `500`: Server Error

---

## 🛠️ Part 3: Practice with Browser Developer Tools

### ✅ 3.1 How to Open DevTools:

* Press `F12` or `Ctrl + Shift + I` (Windows)
* Or right-click anywhere → **Inspect**

### ✅ 3.2 Tasks to Try:

Go to [https://quotes.toscrape.com](https://quotes.toscrape.com) and do the following:

| Task                      | How                                          |
| ------------------------- | -------------------------------------------- |
| Find all quotes           | Right-click on quote → Inspect               |
| Find class name of quotes | Hover over quote → see `<span class="text">` |
| Find author names         | Inspect author name tags                     |
| Find next page button     | Check its class/id in HTML                   |

---

## 🧠 Day 1 Summary

| Topic                     | Status |
| ------------------------- | ------ |
| Python basics             | ✅      |
| Regular expressions       | ✅      |
| HTML/CSS understanding    | ✅      |
| HTTP & requests knowledge | ✅      |
| DevTools hands-on         | ✅      |

---

## 🧪 Practice Challenge for Day 1:

1. Go to any simple blog or quote website like:
   🔗 [https://quotes.toscrape.com](https://quotes.toscrape.com)

2. Do these:

   * Note the tag/class of quote text.
   * Note the tag/class of author names.
   * Inspect the pagination button.

---

### 👋 Kal Day 2 mein hum `requests` aur `BeautifulSoup` use karke data extract karenge from live websites!

Agar tu chahta hai, main tujhe **Day 1 ka notebook (.ipynb)** bhi bana ke de sakta hoon for revision and practice.

Batana jab tu Day 1 complete kar le — then we move to **Day 2: BeautifulSoup scraping** 🔥

Good luck Maroof — let’s go hacker mode! 😎🕵️‍♂️
