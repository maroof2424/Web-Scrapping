import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

title = soup.find("title")

print(f"The Title is {title}")