class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length + self.width) * 2
    
rect = Rectangle(10, 4)

print(f"Area is {rect.area()} and parameter is {rect.perimeter()}")