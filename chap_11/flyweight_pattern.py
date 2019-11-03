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
purpose is to return a flyweight for a given key identifying that flyeright. It works like
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
"""
