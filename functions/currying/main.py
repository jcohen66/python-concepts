def multiply_setup(amount: float):  # 1) The setup is used.
    def multiply(number: float):
        return amount * number      # 3) The function that we curried is called and returned. 
    
    return multiply                 # 2) The function we actually want to use is returned.


double = multiply_setup(2)

print(double(10))
print(double(1000))


def func1(a):
    def func2(b):
        return a, b
    
    return func2

def multiply_setup(amount: float):
    return lambda number:  amount * number

double = multiply_setup(2)
triple = multiply_setup(3)

print(double(10))
print(double(30))
print(double(1000))
print(triple(1000))