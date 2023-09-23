# from bs4 import BeautifulSoup
# import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Connect and load data
browser_driver = Service("")
page_to_scrape = webdriver.Chrome()
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()
time.sleep(3)
username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")
username.send_keys("admin")
password.send_keys("1234")
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()


# Extract the data
quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

# Write to CSV
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

# Headers
writer.writerow(["QUOTE", "AUTHOR"])

for quote, author in zip(quotes, authors):
    print(quote.text, author.text)
    writer.writerow([quote.text, author.text])
file.close()
