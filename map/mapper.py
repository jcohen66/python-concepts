# Map function - map(function, iterable)
#               Returns an iterator that applies a 
#               function to every item of iterable


def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num
    
x = [551, 641, 891, 122, 453, 223, 234, 343, 562, 115, 554, 111, 679, 516]

y = list(map(make_even, x))
y2 = list(map(lambda num:make_even(num), x))
y3 = list(map(lambda num: num if num%2==0 else num+1, x))

print(y)
print(y2)
print(y3)