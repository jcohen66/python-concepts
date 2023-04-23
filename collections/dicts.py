first_dict = { 
              "name": "freecodecamp",
              "founder": "Quincy Larson",
              "type": "charity",
              "age": 8,
              "price": "free",
              "work-style": "remote"
              }

# 1 - get()
founder = first_dict.get("founder")
print(founder)

# 2 - items()
items = first_dict.items()
[print(x) for x in items]
[print(i, end=' ') for i in items]

# 3 = keys()
keys = first_dict.keys()
[print(x) for x in keys]

# 4 = values()
values = first_dict.values()
[print(x) for x in  values]

# 5 - pop() - Mutates data
pop = first_dict.pop("age")
print(first_dict)
print(pop)
print(first_dict)

# 6 - popitme - same as pop but removes last item
first_dict.popitem()
print(first_dict)

# 7 - update() - adds item
first_dict.update({"editor": "Abbey Fox"})
print(first_dict)

# 8 - copy() - makes a deep copy
second_dict = first_dict.copy()
print(second_dict)
print(hex(id(first_dict)))
print(hex(id(second_dict)))

# 9 - clear() - Mutates 
second_dict.clear()
print(second_dict)
