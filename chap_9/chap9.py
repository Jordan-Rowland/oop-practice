class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        work = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


class File:
    def __init__(self, name):
        self.name = name


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.children = []


root = Folder("")
etc = Folder("etc")
root.children.append(etc)
etc.children.append(File("passwd"))
etc.children.append(File("groups"))
httpd = Folder("httpd")
etc.children.append(httpd)
httpd.children.append(File("http.conf"))
var = Folder("var")
root.children.append(var)
log = Folder("log")
var.children.append(log)
log.children.append(File("messages"))
log.children.append(File("kernel"))


def walk(file):
    if isinstance(file, Folder):
        yield file.name + '/'
        for f in file.children:
            yield from walk(f)
    else:
        yield file.name

for i in walk(root):
    print(i)


# Coroutines

def tally():
    score = 0
    while True:
        increment = yield score
        score += increment

cubs = tally()
next(cubs)
cubs.send(3)
cubs.send(3)

