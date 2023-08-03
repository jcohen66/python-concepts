people = [
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 20},
  {"name": "Charlie", "age": 30}
]

# Use lambda to sort list of dictionaries
people.sort(key=lambda person: person["age"])

for person in people:
    print(f"{person['name']}: {person['age']}")
    

def call(func):
  func()
  

def add(x, y):
  return x + y


call(lambda: add(2,3))