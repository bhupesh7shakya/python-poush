from calc import *

if operation == "+":
    add(
        a = int(input("Enter first number:")),
        b = int(input("Enter Second number:"))
    )
    
elif operation == "-":
    sub(
        a = int(input("Enter first number:")),
        b = int(input("Enter Second number:"))
    )
    
elif operation == "*":
    mul(
        a = int(input("Enter first number:")),
        b = int(input("Enter Second number:"))
    )
    
elif operation == "/":
    div(
        a = int(input("Enter first number:")),
        b = int(input("Enter Second number:"))
    )
    
else:
    print("Invalid Operation")
