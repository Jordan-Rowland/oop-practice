"""
The Flyweight pattern is a memory optimization pattern. Novice Python programmers tend to
ignore memory optimization, assuming the built-in garbage collector will take care of
them. This is usually perfectly acceptable, but when deveoping larger applications with
many related objects, paying attention to memory concerns can have a huge payoff.

The flyweight pattern ensures that objects that share a state can use the same memory for
that shared state. It is normally implemented only after a program has demonstrated
memory problems. It may make sense to design an optimal configuration from the beginning
in some situations, but bear in mind that premature optimization is the most effective
way to create a program that is too complicated to maintain.

Each flyweight has no specific state. Any time it needs to perform an operation on a
SpecificState class, that state needs to be passed into the flyweight class by the calling
code. Traditionally, the factory that returns a flyweight is a separate object; it's
purpose is to return a flyweight for a given key identifying that flyweight. It works like
the singleton pattern; if the flyweight exists, we return it; otherwise, we create a new
one. In many language, the factory is implemented, not as a separate object, but as a
static method on the Flyweight class itself.

Using an inventory system for car sales as an example: Each individual care has a specific
serial numer, and is a specific color. But most of the detials about that car are the same
for all cars of a particular model. For example, the Honda Fit DX model is a bare-bones
car with few features. The LX model has A/C, tilt, cruise, and power windows and locks.
The Sport model has fancy wheels, a USB charger, and a spoiler. Without the flyweight
pattern, each individual car object would have to store a long list of which features it
did and did not have. Considering the number of cars Honda sells in a year, this would add
up to a huge amount of wasted memory.

Using the flyweight pattern, we can instead have shared objects for the list of features
associated with a model, and then simply reference that model, along with a serial number
and color, for individual vehicles. In Python, the flyweight factory is often implemented
using the __new__ constructor, similar to what we did with the singleton pattern.

Unlike the singleton pattern, which only needs to return one instance of the class, we
need to be able to return different instances depending on the keys. We could store the
items in a dictionary and look them up based on the key. This solution is problematic,
however, because the item will remain in memory as long as it is in the dictionary. If we
sold out of LX model Fits, the Fit flyweight would no longer be necessary, yet it would
still be in the dictionary. We could clean this up whenever we sell a car, but isnt that
what a garbage collector is for?

We can solve this by taking advantage of Python's "weakref" module. The module provides a
'WeakValueDictionary' object, which basically allows us to store items in a dictionary
without the garbage collector caring about them. If a value is in a weak referenced
dictionary and there are no other references to that object stored anywhere in the
application(that is, we sold out of LX models), the garbage collector will eventually
clean up for us.

Building the factory for our car flyweight:
"""

import weakref


class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model

        return model

    def __init__(self, model_name, air=False, tilt=False, cruise_control=False,
                 power_locks=False, alloy_wheels=False, usb_charger=False):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

    def check_serial(self, serial_number):
        print(
            f"Sorry, we are unable to check the serial number {serial_number} "
            f"on the {self.model_name} at this time."
        )

"""
Wheneve we construct a new flyweight with a given name, we first look up that name in the
weak referenced dictionary; if it exists, we return that model; if not, we create a new
one. Either way, we know the __init__ method on the flyweight will be called every time,
regardless of whether it is a new or existing object. Our __init__ method can therefore
look like the above.

The if statement ensures that we only initialize the object the first time __init__ is
called. This means that we can call the factory later with just the model name and get
the same flyweight object back. However, because the flyweight will be garbage-collected
if no external references to it exist, we must be careful to not accidentally create a new
flyweight with null values.
"""

class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)


dx = CarModel("FIT DX")
lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
car1 = Car(dx, "blue", "12345")
car2 = Car(dx, "black", "12346")
car3 = Car(lx, "red", "12347")

"""
Demonstrating the weak referencing at work in the following code snippet:
"""

print(id(lx))
del lx
del car3
import gc
gc.collect()
lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
print(id(lx))
lx = CarModel("FIT LX")
print(id(lx))
print(lx.air)
