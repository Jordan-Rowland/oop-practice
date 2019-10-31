"""
Unlike previously covered patterns, the adapter pattern is designed to interact with
existing code. We would not design a brand new set of objects that implement the
adapter pattern. Adapters are used to allow two preexisting objects to work together even
if their interfaces are not compatible, like an adapter objectthat allows you to plug
your micro-usb charging cable into a usb-c phone. An adapter objectsits between two
different interfaces, translating between them, on the fly. The adapter object's sole
purpose is to perform this translation. Adapting mayentail a variety of tasks, such as
converting arguments to a different format, rearranging the order of arguments, calling
a differently named method, or supplying default arguments.

In structure, the adapter pattern is similar to a simplified decorator pattern. Decorators
typically provide the same interface that they replace, wheras adapters map between two
different interfaces.

[interface1]--->[adapter[make_action(arg1,arg2)]]--->[interface2[other_action(arg3,arg2)]]

Here, interface1 is expecting to call a method called 'make_action'. We already have this
perfect interface2 class that does everything we want,(and to avoid duplication, we dont
want to rewrite it), but it provides a method called 'other_action' instead. The 'adapter'
class implements the 'make_action' interface and maps the arguments to the existing
interface.

The advantage here is that the code that maps from one interface to another is all in one
place. The alternative would be really ugly; we'd have to perform the translation in
multiple places whenever we need to access this code.

For example, imagine we have the following preexisting class, which takes a string date in
the format YYYY-MM-DD and calculates the person's age on that date.
"""

class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age
