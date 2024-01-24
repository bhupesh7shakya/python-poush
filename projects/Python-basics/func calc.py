# calculator using function

def Add(num1, num2):
    print(num1+num2)
def sub(num1, num2):
    print(num1-num2)
def mul(num1, num2):
    print(num1*num2)
def div(num1, num2):
    print(num1/num2)

    

select = int(input("Select operations from 1, 2, 3, 4:"))
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if select== 1:
    print(num1, "+", num2,"=", Add(num1, num2))
elif select== 2:
    print(num1, "-", num2,"=", sub(num1, num2))
elif select== 3:
    print(num1, "*", num2,"=", mul(num1, num2))
elif select== 4:
    print(num1, "/", num2,"=", sub(num1, num2))
else:
    print("Invalid input")
    
    
# multiplication table using function
def multiply(num,count):
  return num * count

n = int(input("Enter any Number  :"))
i = 1
for i in range(1,11):
    print(n," * ",i," = ",multiply(n,i))
    i = i + 1