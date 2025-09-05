
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# for i in range(3, 10):
#     print(i, fib(i))

def modifier():
    def newfunc(x):
        return x+1
    return newfunc

G = modifier()

#print(G(10))

def beautifier(func):
    print('------')
    func()
    print('********')

def print_copyright():
    print('Copyright (c) ........')

beautifier(print_copyright)
