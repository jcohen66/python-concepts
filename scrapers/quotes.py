from bs4 import BeautifulSoup
import requests
import csv

# Connect and load data
page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Extract the data
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# Write to CSV
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

# Headers
writer.writerow(["QUOTE", "AUTHOR"])

for quote, author in zip(quotes, authors):
    print(quote.text, author.text)
    writer.writerow([quote.text, author.text])
file.close()
