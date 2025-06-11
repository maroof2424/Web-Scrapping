from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Automatically finds chromedriver in PATH
driver.get("https://w3schools.com")

title = driver.find_element(By.TAG_NAME, "h1").text
print("Page Title:", title)

driver.quit()
