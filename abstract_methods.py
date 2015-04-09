import abc

class Foo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fn(self, x):
        print(x)

class Bar(Foo):
    def fn(self):
        print('hi')
        super().fn('d')

if __name__ == '__main__':
    # Note instantiation of Bar would throw TypeError if all abstractmethods weren't defined
    Bar().fn()
