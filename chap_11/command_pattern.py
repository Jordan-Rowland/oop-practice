"""
The command pattern adds a level of abstraction between actions that must be done and the
object that invokes those actions, normally at a later timer. In the command pattern,
client code creates a 'Command' objects that can be executed at a later date. This object
knows about a receiver object that manages its own internal state when the command is
executed on it. The 'Command' object implements a speific interface(typically, it has an
'execute' or 'do_action' method), and also keeps track of any argument required to perform
the action. Finally, one or more 'Invoker' objects execute the command at the correct
time.

A common example of the command pattern is actions on a graphical window. Often an action
can be invoked by a menu item on the menu bar, a keyboard shortcut, a toolbar icon, or a
context menu. These are all examples of 'Invoker' objects. The actions that actually
occur, such as Exit, Save, or Copy are implementations of the CommandInterface. A GUI
window to receive exit, a document to receive save and ClipboardManager to receive copy
commands, are all examples of possible Receivers.

Implementing a simply command pattern that provides commands for Save and Exit actions,
we'll start with some modest receiver classes with the following code:
"""

import sys


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def.save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)


# Invoker classes


class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


