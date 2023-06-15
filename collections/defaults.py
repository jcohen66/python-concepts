people: dict = {'mario': 1, 'luigi': 2}

# doesnt find so returns supplied value
print(people.get('asd', 0))
print(people)

# doesnt find so adds k:v to dict
print(people.setdefault('asd', 0))
print(people)
