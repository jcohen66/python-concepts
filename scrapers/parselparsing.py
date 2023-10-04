import requests
from parsel import Selector


resp = requests.get("https://books.toscrape.com/")

html = Selector(text=resp.text)

print(html.css("h1::text").get())

for item in html.css("article.product_pod"):
    book = {
        "name": item.css("h3 a").attrib["title"],
        "link": item.css("h3 a").attrib["href"],
        "price": item.css("p.price_color::text").get(),
        "img": item.css("img.thumbnail").attrib["src"],
    }
    print(book)
