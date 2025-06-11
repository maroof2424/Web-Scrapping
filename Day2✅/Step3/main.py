from bs4 import BeautifulSoup

# Load the local HTML file
with open("sample.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# 1. Extract the main heading (h1)
main_heading = soup.find("h1").get_text()
print("Main Heading:", main_heading)

# 2. Extract all article titles (h2)
titles = soup.find_all("h2")
print("\nArticle Titles:")
for title in titles:
    print("-", title.get_text())

# 3. Extract all paragraph texts (p)
paragraphs = soup.find_all("p")
print("\nParagraphs:")
for para in paragraphs:
    print("-", para.get_text())

# 4. Extract all article links (a tags) and their href attributes
links = soup.find_all("a")
print("\nLinks:")
for link in links:
    print("-", link['href'])

# 5. Extract the footer text using its ID
footer = soup.find(id="footer").get_text()
print("\nFooter Text:", footer.strip())
