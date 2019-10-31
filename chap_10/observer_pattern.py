class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)


i = Inventory()
c = ConsoleObserver(i)

i.attach(c)
i.product = 'widget'
i.quantity = 5


"""
The key idea is that we can attach multiple observers that fulfill a variety of duties,
i.e. backup data to a file, database, make API calls, etc. at the same time.

The observer pattern detaches the code being observed from the code doing the observing.
If we are not using this pattern, we would have had to put code in each of the properties
to handle the different cases that might come up; logging to the console, updating a
database or file, and so on. The code for each of these tasks would all be mixed in with
the observer object. Maintaining it would be a nightmate, and adding new monitoring
functionality at a later date would be painful.
"""
