# a = 10


# def hello():
#     global a
#     a = 11
#     print(a)


# print(a)
# hello()


a = 10


def outer():
    a = 12
    print('outer function sees a as', a)

    def inner():
        global a
        print('inner functionsees a as ', a)
    inner()


outer()
print(a)
