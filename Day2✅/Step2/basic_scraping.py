import requests
from bs4 import BeautifulSoup

# Get URL from user
url = input("Enter URL to scrape: ")
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Get the tag name from user (like h1, p, a, etc.)
tag = input("Enter the tag you want to scrape: ")

# Find all tags
elements = soup.find_all(tag)

# Print text of each tag found
print(f"\nAll <{tag}> tags found:\n")
for element in elements:
    print(element.text.strip())
