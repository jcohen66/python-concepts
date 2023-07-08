"""
This wrapper function validates the input arguments of a 
function against specified conditions or data types. It can 
be used to ensure the correctness and consistency of the input data.

It is important to ensure that the order of the validation 
functions corresponds to the order of the arguments they are intended to validate.
"""


def validate_input(*validations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args) :]:
                    if not validations[len(args) :][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_input(lambda x: x > 0, lambda y: isinstance(y, str))
def divide_and_print(x, message):
    print(message)
    return 1 / x


if __name__ == "__main__":
    divide_and_print(5, "Hello!")
    divide_and_print(-5, "Hello!")
