def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
    raise

# try:
#     raise ValueError('This is an argument')
# except ValueError as e:
#     print(f'the arguments were {e.args}')

import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print(f'raising {choice}')
    if choice:
        raise choice('An Error')
except ValueError:
    print('Caught a ValueError')
except TypeError:
    print('Caught a TypeError')
except Exception as e:
    print(f'Caught some other error: {e.__class__.__name__}')
else:
    print('this code is called if there is no exception')
finally:
    print('This is cleanup code, and is always called')

class InvalidWithdrawal(Exception):
    pass

# raise InvalidWithdrawal('Not enough money in your account to withdraw')
