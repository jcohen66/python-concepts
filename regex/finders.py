import re

res = re.search("\w+", "$secret&...")
print(res)

res = list(re.finditer("\w+", "$secret&..."))[0]
print(res)