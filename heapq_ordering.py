import heapq
import functools

@functools.total_ordering
class Foo(object):
    def __init__(self, x):
        self._x = x

    def __eq__(self, other):
        return self._x == other._x

f1 = Foo(1)
l = [f1]
heapq.heapify(l)
# This breaks in Python 3
f2 = Foo(2)
heapq.heappush(l, f2)
print(map(id, [f1, f2]))
print(l)