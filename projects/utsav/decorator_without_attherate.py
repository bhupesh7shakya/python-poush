def custom_star(num = 8):
    def star(func):
        def inner():
            print("*" * num)
            func()
            print("*" * num)
        return inner
    return star


def say_hello():
    print("hello")

custom_star(100)(say_hello)()