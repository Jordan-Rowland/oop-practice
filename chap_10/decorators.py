import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print(f'Calling {func.__name__} with {args} and {kwargs}')
        return_value = func(*args, **kwargs)
        print(f'Executed {func.__name__} in {time.time() - now}ms')
        return return_value

    return wrapper

"""Two ways to apply decorators:
1) Manually apply the function to another function, and assign that to a variable.
2) Use the '@function' syntactic sugar.
"""

@log_calls
def test1(a, b, c):
    print('\ttest1 called')

@log_calls
def test2(a, b):
    print('\ttest2 called')

@log_calls
def test3(a, b):
    print('\ttest3 called')
    time.sleep(1)

# Manual way to decorate functions
# test1 = log_calls(test1)
# test2 = log_calls(test2)
# test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)


