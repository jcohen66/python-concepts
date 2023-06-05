def decorator_demo(func):
    # args:     tuple of positional arguments
    # kwargs:   dict of keyword arguments
    def inner_function(*args, **kwargs):
        pass

    return inner_function


@decorator_demo
def f(x):
    pass


@function_decorator
def function_name():
    pass


@class_decorator
class Class_Name:
    @method_decorator
    def method_name(self):
        pass
