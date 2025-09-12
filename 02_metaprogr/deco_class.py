def strmagic_injector(cls):
    def pretty_formatter(self):
        return f"My very beautifu object has a={self.a}"
    cls.__str__ = pretty_formatter
    #setattr(cls, '__str__', pretty_formatter)
    return cls

@strmagic_injector
class A:
    def __init__(self):
        self.a = 12
        self.b = 25.01


obj = A()
print(obj)