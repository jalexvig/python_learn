
class CM:

    def __enter__(self):
        print('entering')
        return [0, 'a']

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')
        print('exception type', exc_type)
        print('exception val', exc_val)
        print('exception tb', exc_tb)

        # If truthy, will swallow exception
        # Otherwise will reraise

        return 1

if __name__ == '__main__':

    with CM() as a:
        print(a)
        raise ZeroDivisionError('my exception!!')
