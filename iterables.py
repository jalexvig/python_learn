class MyIterator(object):
    def __init__(self):
        self._count = 0

    def __next__(self):
        if self._count < 5:
            self._count += 1
            return 'less than 5'
        raise StopIteration

    def __iter__(self):
        return self


class MyIterable(object):
    def __iter__(self):
        for i in range(4):
            yield i
            # return MyIterator()

    def my_fn(self):
        for i in range(4):
            yield i


def my_fn(x):
    for i in range(x):
        yield i


if __name__ == '__main__':
    m = MyIterable()
    print(type(m.my_fn()), type(iter(m)), type(my_fn(5)))
    for x in m:
        print(x)
