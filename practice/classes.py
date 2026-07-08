# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return (self.length + self.width) * 2
    
# rect = Rectangle(10, 4)

# print(f"Area is {rect.area()} and parameter is {rect.perimeter()}")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return f"The restaurant {self.restaurant_name} is {self.cuisine_type}"
    
    def open_restaurant(self):
        return f"{self.restaurant_name} is open!"
    
class IcerCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name)
        self.flavours = []
    
claude_monet = Restaurant ("'Claude Monet'", "French")
tsiskvili = Restaurant ("Tsiskvili", "Georgian")
daphna = Restaurant("Daphna", "Georgian")
print(claude_monet.describe_restaurant())
print(claude_monet.open_restaurant())
print(tsiskvili.describe_restaurant())
print(daphna.describe_restaurant())

# class User:
#     def __init__(self,first_name, last_name, address):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address

#     def describe_user(self):
#         return f"User: {self.first_name} {self.last_name}, Address: {self.address} "
#     def greet_user(self):
#         return f"Hello, {self.first_name} {self.last_name}!"
    
# bob = User("Bob", "Brown", "Rustaveli Avenue 17")
# print(bob.describe_user())
# print(bob.greet_user())




















