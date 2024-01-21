
def custom_star(num=0):
    def star(func):
        def wrapper(*args, **kwargs):
            print('*'*num)
            func(*args, **kwargs)
            print('*'*num)
        return wrapper
    return star


def hash(func):
    def wrapper():
        print('#'*10)
        func()
        print('#'*10)
    return wrapper


@custom_star(10)
def hello(*args, **kwargs):
    print(f'hello {args[0]}')


def bye():
    print('bye')

# star(hello)()


hello("test")

""" 
##########
**********
hello
**********
##########

"""
