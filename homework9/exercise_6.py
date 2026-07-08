#A computed value

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property 
    def area(self):
        return self.width * self.height
    
measures = Rectangle( 4, 10)
print(f"Area: {measures.area}")