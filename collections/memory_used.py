import sys
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
print(f"size of list = {sys.getsizeof(list1)}")

name = 'pynative.com'
print(f"size of name = {sys.getsizeof(name)}")

dict = {"key1": 1, "Key2": 2, "key3": 3}
print(f"size of dict = {sys.getsizeof(dict)}")

class Car:
    def __init__(self, color):
        color=color
car = Car("black")        
print(f"size of dict = {sys.getsizeof(car)}")
