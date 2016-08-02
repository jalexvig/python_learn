import inspect
import os


# Note: Must be run from commandline line like `kernprof -l -v lprofile_kernprof.py`

class Prof(type):
    def __new__(mcls, clsname, bases, namesapce, **kwargs):
        method_namespace = {name: profile(val) for name, val in namesapce.items() if inspect.isfunction(val)}
        namesapce.update(method_namespace)

        return super().__new__(mcls, clsname, bases, namesapce)


class A(metaclass=Prof):
    def f1(self, x):
        res = self.f2(x)

        res += 1

        return res

    def f2(self, y):
        return y + 1


def ns_modifier(ns, module=None):
    for attr_str in dir(ns):
        if attr_str[:2] == '__':
            continue
        attr = getattr(ns, attr_str)
        if inspect.isclass(attr):
            ns_modifier(attr, module=module)
        if not (inspect.isfunction(attr) or inspect.ismethod(attr)):
            continue
        # if inspect.getmodule(attr) != module:
        #     continue
        attr = profile(attr)
        setattr(ns, attr_str, attr)


def lprofile_all(folder_path='.'):
    for fname in os.listdir(folder_path):
        if fname[-2:] != 'py' or 'ProfileEntryPoint' in fname or 'test' in fname:
            continue
        module_str = fname.split('.')[0]
        ns = __import__(module_str)
        ns_modifier(ns, module=ns)


if __name__ == '__main__':
    a = A()
    a.f1(3)
