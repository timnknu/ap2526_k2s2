# class A:
#     def f1(self):
#         print(123, self.xarg)
#     def __init__(self, x):
#         self.xarg = x


C = type('MyClass', tuple(), {
    'square': lambda self, x: x**2
})
obj = object.__new__(C)
print(obj.square(12))
print(type(obj))
