def debug(func):
    def wrapper(*args, **kwargs):
        # print the function name and arguments
        print(f"Calling {func.__name__} with {args} kwargs: {kwargs}")
        # call the function
        result = func(*args, **kwargs)
        # print the results
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@debug
def tester(n):
    x = 0
    for i in range(n**6):
        x = x + 1000
    return x


if __name__ == "__main__":
    tester(20)
