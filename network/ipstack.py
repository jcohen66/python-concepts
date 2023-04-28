from dotenv import load_dotenv
import os
import requests

l = load_dotenv('.env')
print(l)
access_key = os.getenv('APIKEY')

ip = '134.291.259.155'
url = f'http://api.ipstack.com/{ip}/?access_key={access_key}'

r = requests.get(url)
if r.status_code == 200:
    print(r.json)
else:
    print("A network error occurred.")
