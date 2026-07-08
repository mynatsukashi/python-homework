#Build on the parent
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
        # I used __str__ to practice more, and it worked :) 
    def __str__(self):
        return f"{self.brand} with {self.doors} doors"

print(Car("Mini",4))
