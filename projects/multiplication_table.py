multiplier = int(input("Enter the number for which you want multiplication table: "))
for multiplicant in range(1, 11):
    print(f"{multiplier} x {multiplicant} = {int(multiplicant * multiplier)}")