class MyMetaClass(type):
    def __new__(*args, **kwargs):
        print('Metaclass __new__', args, kwargs)
        res = type.__new__(*args, **kwargs)
        print('-->', res)
        return res

    def __init__(*args, **kwargs):
        print('Metaclass __init__', args, kwargs)
        res = type.__init__(*args, **kwargs)
        print('-->', res)
        return res

    def __call__(*args, **kwargs):
        print('Metaclass __call__', args, kwargs)
        res = type.__call__(*args, **kwargs)
        print('-->', res)
        return res

class A(metaclass=MyMetaClass): # за замовчуванням (якщо нічого не вказувати) тут metaclass=type
    def square(self, x):
        print('This is square()')
        return x**2
    def __init__(self, x):
        self.xarg = x


obj = object.__new__(A)
obj.__init__('hello')
print(obj.square(12))
print(type(obj))
