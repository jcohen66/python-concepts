import shelve

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
        
    def __str__(self):
        return f'{self.name}: {self.calories}'
    def func(self):
        print("hello")
    
data: dict = {
    'apple': Fruit('Apple', 10),
    'banana': Fruit('Banana', 15),
    'orange': Fruit('Orange', 20)
}

with shelve.open('FruitsDB') as db:
    db.update(data)
    
with shelve.open('FruitsDB') as db:
    print(dict(db))
    apple = db['apple']
    
print(apple)

with shelve.open('FruitsDB') as db:
    apple = db.get('apple')
    apple = db.setdefault('lemon', 0)
    print(apple)
