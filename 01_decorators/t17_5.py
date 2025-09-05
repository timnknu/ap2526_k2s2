def arg_checker(giventype):
    def modifier(F):
        def newfunc(*args):
            for a in args:
                if isinstance(a, giventype):
                    print('ok')
                else:
                    raise ValueError
            #
            result = F(*args)
            print('Result is', result)
            return result
        return newfunc
    return modifier

@arg_checker(str)
def add(x, y):
    return x+y

print(add("a", "bbb"))
print(add(15, 12))
print(add(15, "bbb"))