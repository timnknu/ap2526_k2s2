def strmagic_injector_universal(*args):
    def strmagic_injector(cls):
        def pretty_formatter(self):
            s = f"My very beautifu object has:"
            for a in args:
                s += f"{a} = {getattr(self, a)}, "
            return s
        cls.__str__ = pretty_formatter
        #setattr(cls, '__str__', pretty_formatter)
        return cls
    return strmagic_injector

@strmagic_injector_universal('par', 'b')
class A:
    def __init__(self):
        self.par = 12
        self.b = 25.01


obj = A()
print(obj)