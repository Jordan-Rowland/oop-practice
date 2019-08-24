
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


# c1 = Contact('Jim', 'Gmail')
# s1 = Supplier('Dave', 'Hotmail')
# name_search = Contact.all_contacts.search('ji')

# [c.name for c in name_search]


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


# Polymorphism

class AudioFile:
    """Base class for audio files, with subclasses
    for each file type that requires different
    methods of extraction"""
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid File Format')

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print(f'Decompressing and playing {self.filename} as mp3')


class WavFile(AudioFile):
    ext = 'wav'

    def play(self):
        print(f'Decompressing and playing {self.filename} as wav')


class OggFile(AudioFile):
    ext = 'ogg'

    def play(self):
        print(f'Decompressing and playing {self.filename} as ogg')

"""The __init__ method in the parent class is able
to access the 'ext' class variable from different
subclasses. This is polymorphism."""

"""Each subclass implements 'play()' in a different
way. This is also polymorphism. The media player can
use the exact same code to play a file, no matter what
the type is; it doesn't care what subclass it is looking
at. The details of decompressing the audio file are
'encapsulated'."""

"""Polymorphism is one of the most important reasons to
use inheritance in many object-oriented contexts. Because
any objects that supply the correct interface can be used
interchangeably in Python, it reduces the need for polymorphic
common superclasses. If all that isbeing shared is a public
interface, duck-typing is all that is required. This reduced
need for interitance also reduces the need for multiple
inheritance; often, when multiple inheritance appears to be
a valid solution, we can just use duck-typing to mimic one of
the multiple superclasses."""

"""Duck typed objects only need to provide methods and
attributes that are being accessed, it does not need to
provide the entire interface."""
