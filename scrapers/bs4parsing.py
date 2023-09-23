import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# load html code from a url
page = urllib.request.urlopen("http://docs.python.org/3/library/random.html")
soup = bs(page)

# find all function names
names = soup.body.findAll("dt")
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

# find all function descriptions
descriptions = soup.body.findAll("dd")
function_usage = []

for item in descriptions:
    item = item.text
    item = item.replace("\n", " ")
    function_usage.append(item)

print(function_names)
print(descriptions)
print(function_usage)

# create a dataframe
data = pd.DataFrame({"function name": function_names, "function_usage": function_usage})
print(data)

# target specific attributes
example = soup.body.findAll("div", attrs={"id": "bookkeeping-functions"})
print(example)

data.to_csv("my_data.csv")
