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

import datetime
print(f'{datetime.datetime.now():%Y-%m-%d %I:%M%p}')

import re
search_string = 'hello world'
pattern = 'hello world'

match = re.match(pattern, search_string)

if match:
    print('regex matches')
