# 1 - append()

people: list[str] = ['Mario', 'Elon', 'Trump']
people.append('Luigi')
print(people)

# 2 - clear()
people.clear()
print(people)

# 3 - copy()
people: list[str] = ['Mario', 'Elon', 'Trump']

copy_people: list[str] = people.copy()
copy_people.remove('Trump')
print(people)
print(copy_people)

people: list[str] = ['Mario', ['Elon', 'Bob'], 'Trump']
copy_people: list[str] = people.copy()

# strange affects both with multi dim
copy_people.remove('Trump')
copy_people[1][1] = 'Cat'
print(people)
print(copy_people)


# 4 - count()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
elons = people.count('Elon')
print(elons)

# 5 - extend()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
people2: list[str] = ['Apple', 'Banana']
people.extend(people2)
print(people)
people.extend([people2])
print(people)
print(people[6])

# 6 - index()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
print(people.index('Trump'))

# 7 - insert()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
people.insert(1, 'Luigi')
print(people)

# 8 - pop()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
people.pop(0)
print(people)
print(people.pop())
print(people)

# 9 - remove()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
try:
    people.remove('Luigi')
except ValueError as ve:
    print(ve)

# 10 -  reverse()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon']
print(people)
people.reverse()
print(people)

# 11 - sort()
people: list[str] = ['Mario', 'Elon', 'Trump', 'Elon', 'Bob']
people.sort(key=lambda name: name.lower())
print(people)
people.sort(key=lambda name: len(name))
people.reverse()
print(people)
