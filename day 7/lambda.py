def sum(a, b):
    return a+b


# print(sum(1, 2))


def x(a, b): return a+b

# print(x(1,2))


def myFunc(n):
    return lambda a: a*n


# lambda a:a*2
my_doubler = myFunc(2)
print(my_doubler(3))
