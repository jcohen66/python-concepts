from dataclasses import dataclass


class Fruit:
    def __init__(self, name:str, calories: float):
        self.name = name
        self.calories = calories
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

banana = Fruit('banana', 10)
apple = Fruit('apple', 50)

print(apple)


@dataclass(frozen=False, slots=True, kw_only=True)
class Fruit:
    #__slots__ = ['name', 'calories']
    
    name: str
    calories: float = 10
    
    def __str__(self):
        return f"{self.name}: {self.calories}"
    
banana = Fruit(name='banana', calories=10)
apple = Fruit(name='apple', calories=50)

print(apple)

banana = Fruit(name='banana', calories=10)
banana2 = Fruit(name='banana', calories=10)
print(banana == banana2)
print(banana)
