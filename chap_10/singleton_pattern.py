"""
The singleton pattern is one of the most controversial patterns and is accused by many
of being an 'anti-pattern'. In Python, if someone is using the singleton pattern, they're
almost certainly doing something wrong,probably because they're coming froma more
restrictive programming language.

The basic idea behind the singleton pattern is to allow exactly one instance of a certain
object to exist. Typically, this object is a sort of manager class like those we discussed
in chapter 5. Such objects often need to be referenced by a wide variety of other objects
and padding references to the manager object around to the methods and constructors that
need them can make code hard to read.

Python does not have private constructors, so instead we can use the __new__ class method
to ensure that only one instance is ever created.
"""


class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls *args, **kwargs)
        return cla._singleton


"""
When __new__ is called, it normally constructs a new instance of that class. When we
override it, we first check whether our singleton instance has been created; if not, we
create it using a super() call. Thus whenever we call the constructor OneOnly, we always
get the exact same instance.
"""

o1 = OneOnly()
o2 = OneOnly()
print(o1 == o2)
print(id(o1))
print(id(o2))

"""
This example is not very transparent.Python coders frown upon forcing the users of their
code into a specific mindset. We may think only one instance of a class will ever be
required, but other programmers may have differnt ideas. Singletons can interfere with
distributed computing, parallel programming, and automated testing, for example. In all
those cases, it can be very useful to have multiple or alternative instances of a specific
object, even though a normal operation may never require one.
"""

# Module variables can mimic singletons

"""
Normally in Python, the singleton pattern can be sufficiently mimicked using module-level
variables. It's not as safe as a singleton in that people could reassign those variables
at any time, but as with the private variables we discussed in chapter 2, this is
acceptable in Python.

Ideally we should give them a mechanism to get access to the default singleton value,
while also allowing them to create other instances if they need them. While technically
not a singleton at all, it provides the most pythonic mechanism for singleton-like
behaviour.

To use module-level variables instead of a singleton, we instantiate an instance of the
class after we've defined it. We can improve out state pattern to use singletons. Instead
of creating a new object every time we change states, we can create a module-level
variable that is always accessible.
"""
