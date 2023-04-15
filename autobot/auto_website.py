# Automate a Website

#pip install selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch Website
browser = webdriver.Firefox()
browser.get('http://www.medium.com')

# Find Element by Class
browser.find_element_by_class_name('button-green')

# Find Element by ID
browser.find_element_by_id('email')

# Find Element by XPath
browser.find_element_by_xpath('//*[@id="email"]')

# Find Element by CSS Selector
browser.find_element_by_css_selector('#email')

# Click on Element
browser.find_element_by_id('email').click()

# Send Keys or Type
browser.find_element_by_id('email').send_keys('Data')

# Press Keys
browser.find_element_by_id('email').send_keys(Keys.HOME)
browser.find_element_by_id('email').send_keys(Keys.CONTROL + 'a')

# Wait for Element to Appear
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))

# Extract Extract
browser.find_element_by_id('email').get_attribute('value')

# Close Browser
browser.close()