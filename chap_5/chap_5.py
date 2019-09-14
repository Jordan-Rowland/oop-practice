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

