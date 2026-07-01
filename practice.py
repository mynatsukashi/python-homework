class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"
    
    def human_years(self):
        return self.age * 7
    
rex = Dog('Rex', 6)
bella = Dog ('Bella', 5)

print(rex.name)
print(rex.age)
print(rex.bark())

