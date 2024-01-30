class Mother:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, another_obj):
        return self.age == another_obj
    
    def __str__(self):
        return str({
            "Name": self.name,
            "age": self.age
        })
    

m1 = Mother("mother1", 50)
m2 = Mother("mother2", 50)
print(m1)
print(m1 == m2)