# __getattr__ is not implemented by default
# __getattribute__ run for every attribute access (w/o looking at attributes on object)
# __getattr__ only run when attribute not found in normal ways


class Foo(object):
    def __getattribute__(self, item):
        print('Foo called __getattribute__ on {0}'.format(item))
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('Foo called __getattr__ on {0}'.format(item))
        return super().__getattr__(item)


class Bar(Foo):
    def __getattribute__(self, item):
        print('Bar called __getattribute__ on {0}'.format(item))
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('Bar called __getattr__ on {0}'.format(item))
        return super().__getattr__(item)


if __name__ == '__main__':
    b = Bar()
    # b.x = 4
    b.x