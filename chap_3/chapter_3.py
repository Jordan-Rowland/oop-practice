# Extending bult-ins

class ContactList(list):
    """Extending a list to add a useful new method"""
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name.lower() in contact.name.lower():
                matching_contacts.append(contact)
        return matching_contacts


class LongNameDict(dict):
    """Extending dict class to add a useful method"""
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


# Multiple inheritance

class Contact:
    all_contacts = ContactList()
    """The all_contacts variable is shared accross
    all instances of this and extended classes"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    """Extending Contact class to add new methods"""
    def order(self, order):
        print(f'Ordered {order}')


# Overridding and super

class Friend(Contact):
    """To add another variable that can be set on
    initialization. Any method can be overwritten,
    not just __init__."""
    def __init__(self, name, email, phone):
        """super()__init__ will execute the original
        __init__ from the Contact class inside the
        new class."""
        super().__init__(name, email)
        """super() is being called inside this class'
        __init__"""
        self.phone = phone

"""The super() call can be made inside any method,
and can be made at any point in the method."""


# Multiple inheritance and mixins

"""Mixins are not intended to exist on their own,
but meant to be ingerited by other classes to
provide extra functionality"""

class MailSender: # Mixin
    def send_mail(self, message):
        print(f'Sending mail to {self.email}:')
        print(message)
        # Email logic here

class EmailableContact(Contact, MailSender):
    pass

"""An alternative to this mixin would be creating
a simple function for sending emails. Other solutions
on P.74"""


class AddressHolder:
    """Adding a class for Addresses"""
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder): #pylint: disable=E0102
    """Redefining Friend class to add AddressHolder
    mixin. This is NOT the approach you want to take
    for multiple inheritance initializations."""
    def __init__( #pylint: disable=R0913
            self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
    """Forgetting to explicitly call the initializer
    can cause hard-to-debug problems. This can also
    cause the issue of calling the initializer of the
    Object class(which all classes derive from) twice.
    The base class should only be called once. More
    details on this problem on P.75 - P.82, 'The
    Diamond Problem'"""






c1 = Contact('Jim', 'Gmail')
s1 = Supplier('Dave', 'Hotmail')
name_search = Contact.all_contacts.search('ji')

[c.name for c in name_search]
