
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


c1 = Contact('Jim', 'Gmail')
s1 = Supplier('Dave', 'Hotmail')
name_search = Contact.all_contacts.search('ji')
[c.name for c in name_search]


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

# Abstract base classes

"""In practice, it's rarely necessary to create new abstract
base classes."""

"""Most of the abstract base classes that exist in the Python
standard library live in the 'collections' module. The Container
class is implemented by List, Str and Dict classes to indicate
whether or not a given value is in that data structure
(3 in [1,2,3,4,5]). It can also be used to define a container
that tells us whether a given value is in the set of odd
integers."""

class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

"""We can instantiate an OddContainer object and determine that,
even though we did not extend Container, the class is a Container
object."""


"""One cool thing about the Container ABC is that any class that
implements it gets to use the in keyword for free. In fact, in is
just syntax sugar that delegates to the __contains__ method. Any
class that has a __contains__ method is a Container and can
therefore be queried by the in keyword, for example."""

3 in OddContainer()
4 in OddContainer()

# Case study

class IntroToPython:
    def lesson(self):
        return f"""
            Hello{self.student}. Define two variables,
            an integer named a value 1, and a
            string named b with a value 'hello'

        """

    def check(self, code):
        return code == "a = 1\nb = 'hello'"

# Using abstract base class
class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshood__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

# Using inheritance
class Statistics(Assignment):
    def lesson(self):
        return f"""
            Good work so far, {self.student}. Now,
            calculate the average of the numbers
            1, 5, 18, -3 and assign to a variable
            named 'avg'
        """

    def check(self, code):
        import Statistics

        code = f"import statistics\n{code}"

        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars)

        return local_vars.get('avg') == statistics.mean([1 ,5 ,8, -3])


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1

        return result

    def lesson(self):
        return self.assignment.lesson()

import uuid

class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods"
            )

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    """
    from grader import Grader
    from lessons import IntroToPython, Statistics

    grader = Grader()
    itp_id = grader.register(IntroToPython)
    """

    def start_assignment(self, student, id):
        self.student_graders[student] = AssignmentGrader(
            student, self.assignment_class[id]
        )

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
            {student}'s attempts at {grader.assignment.__class__.__name__}:

            attempts: {grader.attempts}
            correct: {grader.correct_attempts}
            passed: {grader.correct_attempts > 0}
        """

# Code to show how it all fits together

grader = Grader()
itp_id = grader.register(IntroToPython)
stat_id = grader.register(Statistics)

grader.start_assignment('Tammy', itp_id)
print("Tammy's Lesson:", grader.get_lesson('Tammy'))
print(
    "Tammy's Check:",
    grader.check_assignment("Tammy", "a = 1\nb = 'hello'")
)
print(
    "Tammy's other check:"
    grader.check_assignment("Tammy", "a = 1\nb = 'hello'")
)

print(grader.assignment_summary("Tammy"))

grader.start_assignment('Tammy', stat_id)
print("Tammy's Lesson:", grader.get_lesson("Tammy"))
print("Tammy's check:", grader.check_assignment("Tammy", "avg=5.25"))
print(
    "Tammy's other check:",
    grader.check_assignment(
    "Tammy", "avg = statistics.mean([1, 5, 18, -3])"
    ),
)
print(grader.assignment_summary("Tammy"))


# Exercises

book, magazine

computer, phone,
