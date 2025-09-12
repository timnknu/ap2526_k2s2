class A:
    def f1(self):
        print(123, self.xarg)
    def __init__(self, x):
        self.xarg = x

B2 = A
del A
obj = B2('hello')
obj.f1()
print(type(obj))

second_object = A('kkk')