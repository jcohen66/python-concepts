import time


# Define decorator that takes function pointer
# and extracts the args then calls the function
# with the args.
def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"dt = {dt}")
        return result

    return wrapper


@timer
def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


prime_factorization_timer = timer(prime_factorization)
integers = [2**20 + 1, 2**23 + 1, 2**29 + 1, 2**32 + 1]


for n in integers:
    print(f"Prime factorization of {n} = {prime_factorization(n)}")
    print(20 * ".")
