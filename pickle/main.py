import pickle
import json

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        
    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')
        
def main_raw():
    fruit: Fruit = Fruit('Banana', 100)
    fruit.describe_fruit()
    
    fruit.calories = 150
    
    with open('banana.json', 'w') as file:
        data = {'name': fruit.name, 'calories': fruit.calories}
        json.dump(data, file)
        
    with open('banana.json', 'r') as file:
        data = json.load(file)
        print(data)

def main_pickle():
    fruit: Fruit = Fruit('Banana', 100)
    fruit.describe_fruit()
    
    fruit.calories = 150
    
    with open('data.pickle', 'wb') as file:
        pickle.dump(fruit, file)
    
        
if __name__ == '__main__':
    main_pickle()
    
    with open('data.pickle', 'rb') as file:
        fruit = pickle.load(file)
    
        fruit.describe_fruit()
