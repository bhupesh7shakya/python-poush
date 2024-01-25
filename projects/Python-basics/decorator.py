def custom_star(num=0):
    def star(func):
        def wrapper():
            print("#" * num)
            print("*" * num)
            func()
            print("*" * num)
            print("#" * num)

        return wrapper

    return star


@custom_star(10)
def hello():
    print("hello")


def bye():
    print("BYE")


hello()