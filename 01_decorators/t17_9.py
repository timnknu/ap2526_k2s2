
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
