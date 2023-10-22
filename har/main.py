import json
from haralyzer import HarParser, HarPage

import os

with open('/Users/Jonathan.Cohen/Downloads/www.usta.com.har') as f:
    har_parser = HarParser(json.loads(f.read()))
    
data = har_parser.har_data

for page in har_parser.pages:
    for entry in page.entries:
        print(entry['response']['content'].get('text', ''))



