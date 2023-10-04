def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the exception
            print(f"An exception occurred: {str(e)}")
            # Optionally, perform additional error handling or logging
            # Reraise the exception if needed

    return wrapper


@exception_handler
def tester(n):
    x = 0
    100 / x


if __name__ == "__main__":
    tester(20)
