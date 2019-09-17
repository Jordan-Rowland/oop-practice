"""
Tuples should generally store values that are somehow different from eachother. For
example, we would not put 3 stock symbols in a tuple, but we might create a tuple
containing a stock symbol with it's current, high, and low prices for the day. The
primary purpost of a tuple is to aggregate different pieces of tada together into
one container. Thus, a tuple can be the easiest tool to replace the 'object with no
data' idiom. 
"""

stock = 'fb', 177, 178, 175

"""
If grouping a tuple inside of some other objext, such as a function call, list
comprehension or generator, the parenthesis are required. Otherwise, it woule be
impossible for the interpreter to know whether it is a tuple or the next function
parameter.
"""

"""
What do we do when we want to group values together but know we're frequently going
to need to access them individually? Empty objects are rarely useful unless we know
we're going to be adding behaviour later. Dictionaries are also useful if we don't 
know exactly how much data or which specific data will be stored. 

Two other options are named tuples, and dataclasses. If we do not need to add 
behaviour to the object, and we know in advance which attributes we need to store, we
can use a named tuple. Name tuples are a great way to group read-only data together. 
"""

from collections import namedtuple
Stock = namedtuple('stock', ['symbol', 'current', 'high', 'low'])
stock = Stock('FB', 177, high=178, low=175)

"""
The namedtuple constructor accepts two arguments, the identifier for the named tuple
and alist of string attributes that the namedtuple requires. the result is an object
that can be called just like a normal class to instantiate other objects. The 
constructor must have exactly the corret number of arguments that can be passed in as
arguments or keyword arguments. As with normal objects, we can create as many 
instances of this 'class' as we like, with different values for each.
"""

"""
Like strings and tuples, named tuples are immutable. If we need to be able to change
stored data, a dataclass may be what we need instead. 
"""

from dataclasses import make_dataclass
Stock = make_dataclass('Stock', 'symbol', 'current', 'high', 'low')
stock = Stock('FB', 177, high=178, low-175)

"""
Data Classes let you define the class in one line instead of six. It also gives you 
a much more useful string representation, and a comparison operator.

dataclasses have many other useful features, but another more common way to define
a dataclass is below.
"""

@dataclass
class StockDecorated:
    name: str
    current: int
    high: int
    low: int

"""
This example uses type hints, but if you have an attribute that takes a value with a
complicated type or set of types, you can uses the Any type. You can pull the Any 
type by, 'from typing import Any'
"""

"""
Using the decorator constructor also gives the benefit of specifying a default value
for a dataclass.
"""

@dataclass
class StockDefaults:
    name: str
    current: 0
    high: 0
    low: 0

"""
You can construct this calss with just the stock name; the rest of the values will
take on the defaults. You can still specify values if you prefer.
"""


