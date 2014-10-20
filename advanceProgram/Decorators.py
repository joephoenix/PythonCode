import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1
        
countdown(100000)

def decorator1(func):
    def modify(*args, **kwargs):
        variable = kwargs.pop('variable', None)
        print variable
        x, y = func(*args, **kwargs)
        return x, y
    return modify

@decorator1
def func(a, b):
    print a ** 2, b ** 2
    return a ** 2, b ** 2

func(a=4, b=5, variable="hi")
func(a=4, b=5)


class decorator(object):    
    def __init__(self, f):
        print("inside decorator.___init__()")
        f()  # prove that function definition has completed        
    def __call__(self):
        print("inside decorator.__call__()")
        
@decorator
def function():
    print("inside function()")

print("Finished decorating function()")

function()




