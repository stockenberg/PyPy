# decorators are functions that take a function and return a function
# decorators allow to replace - enhance modify without changing the original function
import functools

def my_decorator(f):
    new_function = f
    return new_function
    pass


@my_decorator
def my_function():
    pass


def escape_unicode(f):

    @functools.wraps(f)  # to transfer the original metadata from the function gone through the decorator
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def vegetable():
    return 'blörk'


class MyDec:
    def __init__(self, f):  # f is not needed for line 41
        pass

    def __call__(self, *args, **kwargs):
        pass


@escape_unicode  # 2nd
@MyDec           # 1st
def func():
    pass


@MyDec()  # class instance as a decorator
def funcs():
    pass


class Test:

    @escape_unicode  # decorators can be used with methods
    def myMeth(self):
        pass