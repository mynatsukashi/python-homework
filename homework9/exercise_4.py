# A family of classes

# Parent class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} makes sound!"

#Child classes 
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} makes ruff!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f"{self.name} makes meow!"

print(Dog("Bubu").speak())
print(Cat("Mimi").speak())

    



