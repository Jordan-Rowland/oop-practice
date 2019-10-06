import re
import datetime
import sys

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print(f'{total:0.2f}')

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]

print('PRODUCT    QUANTITY    PRICE    SUBTOTAL')
for product, price, quantity in orders:
    print(
        f"{product:10s}{quantity: ^9d}"
        f"${price: <8.2f}${subtotal: <10.2f}"
)

print(f'{datetime.datetime.now():%Y-%m-%d %I:%M%p}')

search_string = 'hello world'
pattern = 'hello world'

match = re.match(pattern, search_string)

if match:
    print('regex matches')

pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string, pattern))

from threading import Timer
import datetime
from urllib.request import urlopen


class UpdatedURL:
    def __init__(self, url):
        self.url = url
        self. contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url().read())
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state

    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()

