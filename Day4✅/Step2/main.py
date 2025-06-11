from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")

time.sleep(3)

quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

# Click "Next" button
next_btn = driver.find_element(By.CLASS_NAME, "next")
next_btn.click()

time.sleep(3)

quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

driver.quit()
