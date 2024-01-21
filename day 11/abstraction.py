from abc import ABC,abstractmethod

class Computer(ABC):
    def run(self,app):
        self.process(app)
    
    @abstractmethod
    def process(self,app):
        pass
    
class Mobile(Computer):
    def process(self, app):
        print(f'Mobile is running {app}')

class Laptop(Computer):
    def process(self, app):
        print(f'Laptop is running {app}')

samsung=Mobile()

samsung.run("Mobile legend")
asus=Laptop()
asus.run("valorant")
asus.run("pubggi")

