
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


from idecorators import my_decorator, do_twice

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

# Passing arguemnts to a decorator
##################################
# To change '@do_twice' into a '@repeat(num_times)' function, you must wrap your
# decorater and inner wrapper function with another function that accepts arguments.

def repeat(num_times):
    def repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for i in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return repeat


@repeat(num_times=4)
def say_hello(name):
    print(f'Hello {name}')


# Stateful class-based decorators
"""
The init method must store a reference to the function and can do any other necessary
initialization. The call method will be called instead of the decorated function.
It does essentially the same thing as the wrapper() function in earlier examples.
Note that you need to use the functools.update_wrapper() function insteald of
functools.wraps().
"""

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *arg, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*arg, **kwargs)


# function-based stateful decorator
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

# @count_calls
@CountCalls
def say_whee():
    print('whee!')


from time import sleep


# To set optional parameters, must include _func=None as first parameter.
# Optional arguments are key-word only args. 
def slow_down(_func=None, *, num_seconds=1):
    """Sleep given amount of seconds before calling the function."""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_sleep(*args, **kwargs):
            sleep(num_seconds)
            value = func(*args, **kwargs)
            return value
        return wrapper_sleep

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)



@slow_down(num_seconds=4)
def say_whee():
    print('whee!')


# Singletons
"""
A singleton is a class with only one instance. Singletons frequently used include
True, False, and None. Using 'is' returns True only for objects that are the exact
same instance. The following @singleton decorator turns a class into a singleton by
storing the first instance of the class as an attribute. Later attempts at creating
an instance return the stored instance.
"""

def singleton(cls):
    """Make a class a Singleton class (onlyone instance)."""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

"""
Singleton classes are not really used as often in Python as in other languages. The
effect of a singleton is usually better implemented as a global variable in a method.
"""

# Caching return values (memoization?)

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def cache(func):
    """Keep a cache of previous function calls."""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

# Last Recently Used(LRU) cache is also available in functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

from flask import Flask, request, abort

def validate_json(*expected_args):
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json


"""
@app.route('/whatever', methods=["POST"])
@validate_json('srudent_id')
def update_grade():
    json_data = request.get_json()
    # update database
    return "Success!"
"""
