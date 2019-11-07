"""
The composite patters allows complex tree-like structures to be built from simple
components. The components, called composite objects, are able to behave sort of like a
container and sort of like a variable, depending on whether they have child components.
Composite objects are container objects where the content may actually be another
composite object.

Traditionally, each component in a composite object must be either a leaf node(that cannot
contain other objects), or a composite node. The keyis that both composite and lead nodes
can have the same interface.

The composite patternis commonly useful in file/folder-like trees. Regardless of whether a
node in the tree is a normal file or folder, it is still subjetto operations such as
moving, copying, or deleting the node. We can create a component interface that supports
these operations, and then use a composite object to represent folders, and leaf nodes to
represent normal files.

In Python, once again, we can take advantage of duck typing to implicitely provide the
interface, so we only need to write two classes.
"""

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        pass

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass


class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def move(self, new_path):
        pass

    def copy(self, new_path):
        pass

    def delete(self):
        pass


"""
For each folder(composite) object, wemaintain a dictionary of children. For many composite
implementations, a list is sufficient, but in the case, a dictionary will be userful for
looking up children by name. Our paths will be specified as node names separated the '/'
character, similar to paths in a Unix shell.

Thinking about the methods involved, we can see that moving or deleting a node behaves in
a similar way, regardless of whether or not it is a file or folder node. Copying, however,
has to do a recursive copy for folder nodes, while copying a file node is a trivial
operation.

To take advantage of the similar operations, we can extract some of the common methods
into a parent class. Let's take that discarded 'Component' interface and change it to a
base class with the following code.
"""

class Component:
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self):
        pass

    def copy(self, new_path):
        pass


class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass


root = Folder("")

def get_path(path):
    names = path.split("/")[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node


def add_child(self, child):
    child.parent = self
    self.children[child.name] = child


"""
The composite pattern is extremely useful for a variety of tree-like structures, including
GUI widget hierarchies, file hierarchies, tree sets, graphs, and HTML DOM. It can be a
useful pattern in Python when implemented according to the traditional implementation, as
in the example demonstrated earlier. Sometimes, if only a shallow tree is being created,
we can get away with a list of lists or a dictionary of dictionaries, and do not need to
implement custome component, leaf, and composite classes. Other times, we can get away
with implementing only one composite class, and treating leaf anf composite objects as a
single class. Alternately, Python's duck typing can make it easy to add other objects to a
composite hierarchy, as long as they have the correct interface.
"""
