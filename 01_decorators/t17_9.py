def modifier(F):
    res_storage = {}
    def newfunc(x):
        if x in res_storage:
            print('Computation optimized!', x)
            return res_storage[x]
        else:
            print('New computation', x)
            y = F(x)
            res_storage[x] = y
            return y
    return newfunc


@modifier  # Idential to: fib = modifier(fib)
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))
print('----------')
print(fib(5))