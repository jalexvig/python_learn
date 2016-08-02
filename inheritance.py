class A(object):
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        print('A init', self)


class B(A):
    def __new__(cls):
        print('B new', cls)
        return super().__new__(cls)

    def __init__(self):
        print('B init', self)
        print('B init super', super())
        super().__init__()


b = B()
print(B)
