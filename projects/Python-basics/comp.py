class Human():
    age =0

class Grandfather:
    def __init__(self) -> None:
        print("I am grandfather")
        self.house = 13
        print(f'I have {self.house}')
    
class Father (Grandfather):
    age = 22
    def __init__(self) -> None:
        print('I am father')
        super().__init__()
        self.house = 10
        print(f'I have {self.house}')
    car = "lambo"
    
    def __eq__(self, obj: object) -> bool:
        return self.age == obj.age
    
class Mother(Grandfather):
    age = 22
    def __init__(self) -> None:
        print('I am mother')
    jewalry = "gold"
    
class Son(Father, Mother):
    
    gaming_console = "PS5"
    
binit = Father()
binita = Mother()
print(binit.__eq__(binita))
# print(binit.gaming_console)
# print(binit.car)
# print(binit.house)
# print(binit.jewalry)