
# This will modify the incoming args to 'func' and multiply them by two
def deco(func):
    def wrapper(*args, **kwargs):
        args = [i * 2 for i in args]
        return func(*args, **kwargs)
    return wrapper

def func(a, b):
    return a + b

func(2, 4)
deco_func = (deco(func))
deco_func(2, 4)

"""
A Decorator is a function that takes another function. It extends the behaviour
of that function without explicitly modifying the function.
"""

def parent():
    print('Printing from the parent() function.')

    def first_child():
        print('Printing from the first_child() function.')

    def second_child():
        print('Printing from the second_child() function.')

    second_child()
    first_child()


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first())
print(second())


from importing_decorator import my_decorator, do_twice

def say_whee():
    print('Whee!')

say_whee_decorated = my_decorator(say_whee)

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

say_whee_daytime = not_during_the_night(say_whee)

@do_twice
@my_decorator
def say_whee_sugar():
    print('Whee!')


"""
Use *args and **kwargs to the wrapper be able to add arguments to functions being
decorated.
"""

"""
@functools.wraps will preserve the information about the original function when using
help().
"""

import functools


def do_twice_args(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        # To return something from a decorated function, you must return the func
        # from within the wrapper/decorated function
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_args
def say_hi(name):
    print(f'Hello, {name}')

say_hi('David')

@do_twice_args
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'

hi_adam = return_greeting('Adam')

# Boilerplate decorator
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper



import time


def timer(func):
    """Print the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f'Finished {func.__name__!r} in {runtime:.4f} seconds.')
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10_000)])



def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k} = {v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        # Do something after
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper


@debug
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10_000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f"Whoa {name}, {age} already, you're growing up!"



def slow_down(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


@slow_down
def countdown(number):
    if number < 1:
        print('liftoff')
    else:
        print(number)
        countdown(number - 1)


# registering plugins

import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f'Hello {name}'

@register
def be_awesome(name):
    return f"Yo {name}, together we cool cats"

print(PLUGINS)

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


