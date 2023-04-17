from dataclasses import dataclass

@dataclass(slots=True)
class Person:
    name:str
    age:int
    job: str
    friends: list[str] = None
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and works as a {self.job}.'
    
json: dict = {
    'name': 'Bob',
    'age': 10,
    'job': "Salesman",
    'friends': ['Mario', 'Luigi']
}

bob = Person(json['name'], json['age'], json['job'], json['friends'])

print(bob)
