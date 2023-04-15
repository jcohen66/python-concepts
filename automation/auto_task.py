# Automate Webtasks
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set driver 
bot = webdriver.Chrome()
# Open Url by bot
bot.get('https://www.example.com/')
# Search element by name
search = bot.find_element(By.NAME, 'q')
# Serch element by xpath
search = bot.find_element(By.XPATH, '//*[@id="search"]')
# Search element by css selector
search = bot.find_element(By.CSS_SELECTOR, '#search')
# Search element by class name
search = bot.find_element(By.CLASS_NAME, 'search')
# Search element by tag name
search = bot.find_element(By.TAG_NAME, 'input')
# Send keys / Type text
search.send_keys('Hello World')
# Click element
search.click()
# Get element text
print(search.text)
# Get element attribute
print(search.get_attribute('href'))
# Close the browser
bot.close()
# Quit the browser
bot.quit()