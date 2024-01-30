def give_calculator(symbol):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: a / b,
        "*": lambda a, b: a * b,
        "%": lambda a, b: a % b
    }
    try:
        return operations[symbol]
    except Exception as exp:
        print(f"Error occured {exp}")