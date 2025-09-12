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

nObjects = 0

class A(metaclass=MyMetaClass): # за замовчуванням (якщо нічого не вказувати) тут metaclass=type
    def square(self, x):
        print('This is square()')
        return x**2
    def __init__(self, x):
        print(">>I'm a A's constructor")
        self.xarg = x
    def __new__(*args, **kwargs):
        global nObjects
        if nObjects > 5:
            print("Забагато об'єктів")
            raise ValueError
        else:
            nObjects += 1
            print(f'__new__ from A {nObjects}:', args, kwargs)
            res = object.__new__(args[0], **kwargs)
            print('object says:', res)
            return res

print('=======================================')
obj = A('hello')
print(obj.square(12))
print(type(obj))
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
secondObject = A('world')
print(secondObject.square(14))
print('******************')
for i in range(10):
    y = A('new one')
