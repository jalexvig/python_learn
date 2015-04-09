
class Base1(object):
    x = 1

class Base2(object):
    x = 2

class Child(Base1, Base2):
    x = 0

    def __init__(self):
        print(Child.__mro__)
        print(self.x)
        print(super(Child, self).x)
        print(super(Base1, self).x)
        # This raises an error because it tries to skip through Base2 in the MRO and object doesn't have x defined
        try:
            print(super(Base2, self).x)
        except AttributeError:
            print('super(Base2, self).x failed')
        print(super().x)

if __name__ == '__main__':
    Child()