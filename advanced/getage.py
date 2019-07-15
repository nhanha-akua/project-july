class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
Junior = Person("Junior" , 28)
print(Junior.get_age())

    
    
    