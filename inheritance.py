
class A(object):
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        print(self)

class B(A):
    def __new__(cls):
        print(cls)
        return super().__new__(cls)

    def __init__(self):
        print(self)
        print(super())
        return super().__init__()

b = B()
print(B)
