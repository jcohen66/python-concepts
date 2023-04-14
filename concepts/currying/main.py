def multiply_setup(amount: float):  # 1) The setup is used
    def multiply(number: float):
        # 3) The function that we curried is called and returned with
        return amount * number

    # return the function ptr
    return multiply   # 2) The function we actually want to call is returned


def multiply_setup_lambda(amount: float):
    return lambda number: amount * number


double = multiply_setup(2)

print(double(10))
print(double(50))
print(double(100))

triple = multiply_setup(3)
print(triple(10))
print(triple(50))
print(triple(100))
