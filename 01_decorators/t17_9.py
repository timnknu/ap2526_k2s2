
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(3, 10):
    print(i, fib(i))

val = fib(3)
proc = fib

print(val, proc)
y = proc(4)
print(y)

G = lambda x: x**2 if x>0 else -1
u = G(10)
print(u)