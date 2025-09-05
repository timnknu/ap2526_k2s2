
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# for i in range(3, 10):
#     print(i, fib(i))

def modifier(F):
    def newfunc(x):
        return F(x)+1
    return newfunc

@modifier
def square(x):
    return x**2
print(square(20))
#G = modifier(square)
#print(G(10))
