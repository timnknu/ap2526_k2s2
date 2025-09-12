class MyMetaClass(type):
    def __new__(cls, class_name, bases, members_dict, max_num_objs = 1):
        cls.max_num_objs = max_num_objs
        cls.nObjects = 0
        print('Metaclass __new__', cls, class_name, bases, members_dict)
        print('max_num_objs', max_num_objs)
        res = type.__new__(cls, class_name, bases, members_dict)
        print('-->', res)
        return res

    def __init__(cls, class_name, bases, attrs_dict, **kwargs):

        def alternative_new(*args, **kwargs):
            if cls.nObjects > cls.max_num_objs:
                print("Забагато об'єктів")
                raise ValueError
            else:
                cls.nObjects += 1
                print(f'__new__ from A {cls.nObjects}:', args, kwargs)
                res = object.__new__(args[0], **kwargs)
                print('object says:', res)
                return res
        cls.__new__ = alternative_new

        print('Metaclass __init__', cls, class_name, bases, attrs_dict, kwargs)
        res = type.__init__(cls, class_name, bases, attrs_dict, **kwargs)
        print('-->', res)
        return res

    def __call__(*args, **kwargs):
        print('Metaclass __call__', args, kwargs)
        res = type.__call__(*args, **kwargs)
        print('-->', res)
        return res

nObjects = 0

class A(metaclass=MyMetaClass, max_num_objs=3): # за замовчуванням (якщо нічого не вказувати) тут metaclass=type
    def square(self, x):
        print('This is square()')
        return x**2
    def __init__(self, x):
        print(">>I'm a A's constructor")
        self.xarg = x

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
