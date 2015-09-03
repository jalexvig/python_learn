# For objects, the machinery is in object.__getattribute__() which transforms b.x into
# type(b).__dict__['x'].__get__(b, type(b)). The implementation works through a precedence chain that gives data
# descriptors priority over instance variables, instance variables priority over non-data descriptors, and assigns
# lowest priority to __getattr__() if provided.

# For classes, the machinery is in type.__getattribute__() which transforms B.x into B.__dict__['x'].__get__(None, B).

# https://docs.python.org/3.4/howto/descriptor.html

class MyDesc(object):

    def __init__(self, val=None, name="var"):
        self._val = val
        self._name = name

    def __get__(self, obj, type=None):
        print(self, obj, type)
        print("Getting", self._name)
        return self._val

    def __set__(self, instance, value):
        print("Setting", self._name)
        self._val = value

class MyNonDataDesc(object):

    def __get__(self, obj, type=None):
        print(self, obj, type)
        return "Getting non data desc"

class Foo(object):
    x = MyDesc(4, 'x')
    y = 0
    z = MyNonDataDesc()

if __name__ == '__main__':
    f = Foo()
    print(Foo.__dict__)
    print(f.__dict__)
    f.x = 5
    print(f.__dict__)
    g = Foo()  # g.x now returns 5
    print(g.__dict__)
    g.z = 4
    print(g.__dict__)