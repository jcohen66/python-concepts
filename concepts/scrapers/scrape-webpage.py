import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
response = requests.get('https://books.toscrape.com/')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the information you want to scrape
for article in soup.find_all('article'):
    title = article.find('h3').find('a').get('title')
    price = article.find(class_='price_color').get_text()
    print(f'Title: {title}\nPrice: {price}\n---')