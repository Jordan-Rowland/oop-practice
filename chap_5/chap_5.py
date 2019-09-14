# Objects are things that have both data and behaviour
# If there is only data, you're better off using a data struction of some kind.
# if there is only behaviour, you're better off using simple functions.

# Proficient Python programmers user built-in data structures unless(or until)
# there is an obvious need to define a class. There is no reasonto add an extra
# level of abstraction if it does not help organize our code. 

"""
We can often start out Python programs by storing data in a few variables.
As the program expands, we will later find that we are passing the same set
of related variables to a set of functions. This is the time to thin about
grouping both variables and function into a class. If we are designing
a program to model polygons in two-dimensional space, we might start with each
polygon represented as a list of points. The points would be modeled as two
tuples (x, y) describing where the point is located. This is all data, stored
in a set of nested data structures

If we want to calculate the distance around the perimeter of the polygon, we
need to sum the distances between each point.

We recognize that a 'polygon' class could encapsulate the list of points(data) and
the perimeter functions(behaviour). Further, a 'point' class such as we defined in
chaper two might enxapsulate the x and y coordinates and the 'distance' method.

The more important a set of data is, the more likely it is to have multiple 
functions specific to that data, and the more useful it is to use a class with
attributes and methods instead. 
"""

# 'property' method allows methods to act as attributes
class Color:
    def __init__(self, rgb, name):
        self.rgb = rgb
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name

    def _get_name(self):
        return self._name
            # This will allow the name setting to still have the validation
            # that a name is required, while accessing it like an attribute
    name = property(_get_name, _set_name)

c = Color('123', 'orange')
print(c.name)
c.name = 'red'
print(c.name)

"""
'property' constructor accepts 4 arguments; getter, setter, deleter, and a docstring.
In practive, properties are normally only defined with the first to parameters,
'getter' and 'setter' functions. If we want to supply a docstring, we can define it
on the getter, and it will default to this value with no doctring argument set. 
"""

# Using decorators to declare getters and setters. '@property' is the getter. Using
# the '@(variable).setter' on a method of the same variable will act as the setter.
class Color:
    def __init__(self, rgb, name):
        self.rgb = rgb
        self._name = name

    @property
    def name(self):
    """Docstring would still go here in the getter"""
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
    """deleter method has a decorator too"""
        del self._name


c = Color('321', 'purple')
print(c.name)
c.name = 'blue'
print(c.name)
