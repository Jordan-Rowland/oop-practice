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


# Adapter for this
import datetime


class DateAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)


# Another way using inheritance
class AgeableDate(datetime.date):
    def split(self, char):
        return self.year, self.month, self.day

"""
This class has a single method which takes an argument that we do nothing with. We then
return a tuple of year, month, day, as the original calculator calls 'birthday.split' and
returns these. The AgeCalculator class only cares if a 'strip' method exists, and returns
acceptable values; it doesn't care if we really passed in a string. The following code
works:
"""

bd = AgeableDate(1975, 6, 14)
today = AgeableDate.today()
print(today)
a = AgeCalculator(bd)
print(a.calculate_age(today))

"""
This works, but it's a bad idea. In this particular instance, such an adapter would be
hard to maintain. We'd soon forget why we needed to add a 'strip' method to a 'date'
class. The method name is ambiguous. That can be the nature of adapters, but creating an
adapter explicitly instead of using inheritance usually clarifies its purpose.

Instead of inheritence, we can sometimes also use monkey-patching to add a method to an
existing class. It won't work for the datetime object as it doesn't allow attributes to be
added at runtime. In normal classes, however, we can just add a new method that provides
the adapted interface that is required by calling code. Alternatively, we could extend or
monkey-patch the AgeCalculator itself to replace the calculate_age method with something
more amenable to our needs.

Finally, it is often possible to use a function as an adapter; this obviously doesn't fit
the actual design of the adapter pattern, but if we recall that functions are essentially
objects with a __call__ method, it becomes an obvious adapter adaptation.
"""
