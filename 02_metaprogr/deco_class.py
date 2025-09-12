class A:
    def __init__(self):
        self.a = 12
        self.b = 25.01
    def __str__(self):
        return f"My very beautifu object has a={self.a}"

obj = A()
print(obj)