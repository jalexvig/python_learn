class MyMetaClass(type):

    @classmethod
    def __prepare__(mcls, clsname, bases, **kwds):
        return dict()

    def __new__(mcls, clsname, bases, namespace, **kwds):

        personalized_namespace = {'m_' + k if k[:2] != 'm_' else k: v for k, v in namespace.items()}
        return super().__new__(mcls, clsname, bases, personalized_namespace)


class Foo(object, metaclass=MyMetaClass):
    def method(self):
        pass

    x = 1

print(Foo.__dict__)
