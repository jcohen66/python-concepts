import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_PAGE = """
    <html>
        <head>Hello</head>
        <body>
            <p id="first">
                <div>Parse me</div>
                <div>Parse me too!</div>
            </p>
            <p id="second">Welcome To HTML</p>
        </body>
    </html>
"""

soup = BeautifulSoup(BASE_PAGE, "html.parser")
#print(soup.p)
#print(soup.p.name)
#print(soup.p.attrs)
#print(soup.p.parent)
#print(soup.p.contents)
# print(soup.p)
# print(soup.p.text)
# print(soup.p.div)
# print(soup.p.div)
# print(soup.p['id'])

PAGE_2 = """
    <html>
    <head>
        <title>Sample Website</title>
    </head>
    <body>
        <h1>Sample Website</h1>
        <p>Let's practice <b>scraping</b> on this page</p>
        <div>
            <p>Below are some useful links</p>
            <ul>
                <li><a href-="https://www.anaconda.com/distribution/" title="Anaconda Distribution">Anaconda Distribution</a></li>
                <li><a href="https://www.learnpython.org/" title="Learn Python">Learn Python Basics</a></li>
                <li><a href="http://www.simplehtmlguide.com/cheatsheet.php">HTML Cheat Sheet</a></li>
            </ul>
        </div>
        <div class="warning">
            <span style="color:red">This page is for demo only</sspan>
        </div>
        <div class="sample_table>
            <table>
                <tr><th>Tag</th>Description</th></tr>
                <tr><td>p</td><td>Paragraph</td></tr>
                <tr><td>b</td><td>Bold</td></tr>
                <tr><td>i</td><td>Italic</td></tr>
                <tr><td>br</td><td>Line Breaks</td></tr>
            </table>
        </div>
    </body>
    <html>
"""

# Create a soup object from the page
soup = BeautifulSoup(PAGE_2, "html.parser")

# Navigating down the tree examples
#print(soup.prettify())
soup.html.head.name
soup.html.head.parent
soup.html.head.text
soup.html.head.span
# print(soup.span.attrs)
# print(soup.ul.contents)
print(soup.ul.li.next_sibling.next_sibling)

# print(soup.ul.li.next_sibling.next_sibling)
# print(soup.ul.li.next_sibling.next_sibling.next_sibling)