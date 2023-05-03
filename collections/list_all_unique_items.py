def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

listOne = [123, 345, 456, 23, 567]
print(f"All list items are Unique: {isUnique(listOne)}")

listTwo = [123, 345, 567, 23, 567]
print(f"All list items are Unique: {isUnique(listTwo)}")

