# Use with big dictionaries to improve speed.
import shelve

with shelve.open('TestDB') as db:
    db['a'] = 1
    db['b'] = 2
    db['c'] = 3
    
with shelve.open('TestDB') as db:
    print(type(db))
    print(dict(db))
    print(db['c'])
    
data: dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
} 

with shelve.open('TestDB') as db:
    db.update(data)
    print(dict(db))


