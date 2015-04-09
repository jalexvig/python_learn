class MyMetaclass(type):

    def __init__(cls, clsname, bases, namespace, **kwds):
        cls.objects = []
        print("MyMetaClass init called")
        return super().__init__(clsname, bases, namespace)

    def __call__(cls):
        obj = super().__call__()
        cls.objects.append(obj)
        return obj

class Foo(metaclass=MyMetaclass):

    def __init__(self):
        print("object init called")

if __name__ == '__main__':
    foo = Foo()
    foo2 = Foo()
    print(Foo.objects)
    Goo = MyMetaclass('Goo', (), {'hi': 3})
    goo = Goo()
    print(Goo.objects)
    print(Goo.hi)
