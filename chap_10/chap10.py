# Decorator pattern

"""
Two primary uses of the decorator pattern:

1) Enhance the response of a component as it sends data to a second component.
2) Supporting multiple optional behaviours.

The second option is often a suitable alternative to multiple inheritance. We can
construct a core object, and then create a decorator wrapping that core. Since the
decorator object has the same interface as the core object, we can even wrap the
new object in other decorators.
"""

import socket


class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print(f'Sending {data} to {self.socket.getpeername()[0]}')
        self.socket.send(data)

    def close(self):
        self.socket.close()


def respond(client):
    response = input('Enter a value: ')
    # client.send(bytes(response, 'utf8'))
    client.close()


"""
When faced with a choice between decorators and inheritance, we should only use
decorators if we need to modify the object dynamically, according to some condition.
For example, we may only want to enable the logging decorator if the server is
currently in debugging mode. Decorators also beat multiple interitance when we have
more than one optional behaviour. As an example, we can write a second decorator
that compresses data using gzip compression whenever send is called:
"""

import gzip
from io import BytesIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


log_send = True
compress_hosts = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)

try:
    while True:
        client, addr = server.accept()
        # This examply shows that we can dynamically switch between them when 
        # responding. Noticethat none, either, or both of the decorators may be
        # enabled, depending on the configuration and connecting client. Writing
        # this with multiple inheritance would be very confusing.
        if log_send:
            client = LogSocket(client)
        # if client.getpeername()[0] in compress_hosts:
            client = GzipSocket(client)
        respond(client)
finally:
    server.close()


import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time
        print(f'Calling {func.__name__} with {args} and {kwargs}')
        return_value = func(*args, **kwargs)
        print(f'Executed {func.__name__} in {time.time() - now}ms')
        return return_value

    return wrapper

def test1(a, b, c):
    print('\ttest1 called')

def test2(a, b):
    print('\ttest2 called')

def test3(a, b):
    print('\ttest3 called')
    time.sleep(1)

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)


