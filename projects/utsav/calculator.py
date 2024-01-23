while True:
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    operator = input("Enter the operator ")

    if operator == "+":
        print(first_num + second_num)
    elif operator == "-":
        print(first_num - second_num)
    elif operator == "*":
        print(first_num * second_num)
    elif operator == "**":
        print(first_num ** second_num)
    elif operator == "%" or operator == "mod":
        print(first_num % second_num)
    elif operator == "/" or operator == "//":
        if second_num != 0:
            print(first_num / second_num)
        else:
            print("Cannot divide by 0")
    else:
        print("Invalid operator")
    next = input("Press 'n' if you wish to exit: ")
    if next == "n":
        break