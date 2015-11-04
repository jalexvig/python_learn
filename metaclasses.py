import collections

class MyMetaClass(type):

    @classmethod
    def __prepare__(mcls, clsname, bases, **kwds):
        print("__prepare__ called")
        print("mcls = ", mcls)
        print("clsname = ", clsname)
        print("bases = ", bases)
        print("kwds = ", kwds, '\n')
        return collections.OrderedDict()

    def __new__(mcls, clsname, bases, namespace, **kwds):

        print("__new__ called")
        print("mcls = ", mcls)
        print("clsname = ", clsname)
        print("bases = ", bases)
        print("namespace = ", namespace)
        print("kwds = ", kwds, '\n')
        upper_attr_dict = {}
        for key, val in namespace.items():
            key_mod = key.upper() if key[:2] != '__' else key
            upper_attr_dict[key_mod] = val

        result = super().__new__(mcls, clsname, bases, upper_attr_dict)
        result.original_namespace = namespace
        return result

    def __init__(cls, clsname, bases, namespace, **kwds):

        print("__init__ called")
        print("cls = ", cls)
        print("clsname = ", clsname)
        print("bases = ", bases)
        print("namespace = ", namespace)
        print("kwds = ", kwds, '\n')

        return super().__init__(clsname, bases, namespace)

    def __call__(cls):
        print("__call__ called")
        print("cls = ", cls)
        print("super = ", super(), '\n')
        return super().__call__()

class Foo(object, metaclass=MyMetaClass, temp='hi'):

    def __new__(cls):
        print("Foo __new__ called\n")
        return super().__new__(cls)

    def __init__(self):
        print("Foo __init__ called\n")

    def my_func(self):
        print("My function\n")

    a = 3

if __name__ == '__main__':

    print('Start executing commands...\n')

    foo = Foo()
    print('Foo.__dict__ == ', Foo.__dict__)