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