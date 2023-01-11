import time
from functools import wraps


# Decorator as a function
def check_time_by_arg(time_arg: str):
    def check_time(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            if time_arg == 'seconds':
                elapsed_time = elapsed_time / 1000
            print(f"Time elapsed is {elapsed_time}")
            return result

        return wrapped_func

    return check_time


@check_time_by_arg('seconds')
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Decorator as a class
class ErrorCheck:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)


# Decorator for all class methods

def time_all_class_methods(Cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            print(f"__init__() called with args: {args} and kwargs: {kwargs}")
            self.decorated_obj = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
                return x
            except AttributeError:
                x = self.decorated_obj.__getattribute__(s)
                if isinstance(x, Wrapper):
                    print(f"attribute belonging to decorated_obj: {s}")
                    return check_time_by_arg('seconds')(x)
                else:
                    return x

    return Wrapper


@time_all_class_methods
class MyCustomclassClass:
    def __init__(self):
        print('entering MyClass.__init__')
        time.sleep(1.8)
        print("exiting MyClass.__init__")

    def method_x(self):
        print("entering MyClass.method_x")
        time.sleep(0.7)
        print("exiting MyClass.method_x")

    def method_y(self):
        print("entering MyClass.method_x")
        time.sleep(1.2)
        print("exiting MyClass.method_x")


if __name__ == '__main__':
    print(fib(10))
    print(add_numbers(1, 2, 3))
    my_class = MyCustomclassClass()
    my_class.method_x()