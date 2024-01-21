while True:
    try:
        a = int(input("number"))
        if a == 5:
            raise Exception("first number cannot be 5")
        b = int(input("another number"))
        print(a/b)
    except ZeroDivisionError:
        print("zero cann be divided")
    except ValueError:
        print('Please only number value ..')
    except Exception as e:
        print('something went wrong', e)
