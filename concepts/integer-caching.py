# Python caches integers from [-5-256]. 
a = 256
b = 256
print("a: ", a, " b: ", b, " a is b: ", a is b)

# >256 are stored as unique references
x = 100000000
y = 100000000
print("x: ", x, " y: ", y, " x is y: ", x is y)
