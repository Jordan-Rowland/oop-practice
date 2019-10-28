"""
The state pattern is structurally similar to the strategy pattern, but its intent and
putpose are very different. The goal of the state pattern is to represent state-transition
systems: systems where it is obvious that an objet can be in a specific state, and that
certain activities may drive it to a different state.

To make this work, we need a manager, or context class that provides an interface for
switching states. Internally, this class contains a pointer to the current state. Each
state knows what the other states is is allowed to be in and will transition to those
states depending on actions invoked upon it.

Two types of classes: the context class and multiple state classes. The context class
maintains the current state, and forwards actions to the state class. The state classes
are typically hidden from any other objects that are calling the context; it acts like a
black box that happens to perform state management internally.
"""


class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        return self.tag_name


class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_node = None

        self.stats = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.pro(self.parse_string)


class FirstTag:
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find("<")
        i_end_tag = remaining_string.find(">")
        tag_name = remaining_string[i_start_tag + 1 : i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[i_end_tag + 1 :]



