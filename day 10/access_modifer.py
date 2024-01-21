class Person:
    def __init__(self, name,age,password):
        self.name = name
        self._age = age
        self.__password=password
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password = password
        
    # def get_password(self):
    #     return self.__password
        
    # def set_password(self,password):
    #     self.__password = password
        
    # password=property(get_password,set_password)
        
binit=Person("binit",23,"binita@123")

print(binit.name)
print(binit._age)
binit.password="anjila@123"
print(binit.password)