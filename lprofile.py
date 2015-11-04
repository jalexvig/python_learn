import pandas as pd
import sys
sys.path.append('/home/alex/Shared/mine/useful/my_py')
from my_decorators import do_lprofile

class A:

    def f(self, x):
        y = x + 1
        return y

    # @profile
    @do_lprofile(follow=['f'])
    def g(self):
        s = pd.Series(range(9))
        s.apply(self.f)

if __name__ == "__main__":
    a = A()
    a.g()
