import calc_module
symbol = input("Enter the symbol: ")
calculator = calc_module.give_calculator(symbol)
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
try:
    result = calculator(a, b)
    print(f"The result of calculation is {result}")
except ZeroDivisionError:
    print("Cannot Divide by 0")
except TypeError:
    print("Invalid symbol provided, the valid ones are +, -, *, /, %")