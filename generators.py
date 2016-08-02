# This came from/was inspired by http://www.snarky.ca/how-the-heck-does-async-await-work-in-python-3-5


def bottom():
    return (yield 42)


def middle():
    return (yield from bottom())

if __name__ == '__main__':

    gen = middle()
    print(next(gen))
    try:
        print(gen.send(3))
    except StopIteration as e:
        print(e.value)
        raise
