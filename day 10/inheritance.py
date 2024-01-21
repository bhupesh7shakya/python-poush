class Human:
    age=0
class GrandFather(Human):
    def __init__(self):
        print('i am mother')
        self.house=13
        print(f'i have {self.house}')
    
class Mother(GrandFather):
    
    def __init__(self):
        print('i am mother')
    jewlary="gold"
    
class Father(GrandFather):
    
    def __init__(self):
        super().__init__()
        self.house=10
        print(f"i have {self.house}")
    car="lambo"
    
    def __eq__(self, obj) -> bool:
        return self.age==obj.age
    
class Son(Father,Mother):
    gaming_console="PS5"
    
binit=Father()
binita=Mother()
print(binit==binita)
# print(binit.gaming_console)
# print(binit.house)
# print(binit.car)
# print(binit.jewlary)