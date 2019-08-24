
class ContactList(list):
    # Extending a list to add a useful new method
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name.lower() in contact.name.lower():
                matching_contacts.append(contact)
        return matching_contacts


class LongNameDict(dict):
    # Extending dict class to add a useful method
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


class Contact:
    all_contacts = ContactList()
    # The all_contacts variable is shared accross
    # all instances of this and extended classes
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    # Extending Contact class to add new methods
    def order(self, order):
        print(f'Ordered {order}')


class Friend(Contact):
    # To add another variable that can be set on
    # initialization
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


c1 = Contact('Jim', 'Gmail')
s1 = Supplier('Dave', 'Hotmail')
name_search = Contact.all_contacts.search('ji')

[c.name for c in Contact.all_contacts.search('Ji')]
