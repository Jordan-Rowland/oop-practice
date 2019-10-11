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
    client.send(bytes(response, 'utf8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()


"""
When faced with achoice between decorators and inheritance, we should only use
decorators if we need to modify the object dynamically, according to some condition.

For example, we may only want to enable the logging decorator if the server is
currently in debugging mode. Decorators also beat multiple interitance when we have
more than one optional behaviour. As an example, we can write a second decorator
that compresses data using gzip compression whenever send is called:
"""

"""
Unrelated to this chapter, play around with 'super()' method. Does calling super
overwrite the function completely?
"""
