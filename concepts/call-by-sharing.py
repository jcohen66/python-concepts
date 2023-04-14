def updateNumber(val):
    val += 10
    print(val)

b = 5
updateNumber(b)
print(b)

def updateNumber_ref(val):
    print(id(val))

b = 5
print(id(b))
updateNumber_ref(b)
print(b)