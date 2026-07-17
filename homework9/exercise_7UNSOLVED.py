import math
class Shape:
    def __init__(self, type, area):
        self.area = area
        self.type = type
    def __str__(self):
        return f"{self.area} with area"
@property
class Square(Shape):
    def __init__(self, area, side):
        super().__init__(type, area)
        self.side = side
        return side * side

class Circle(Shape):
    def __init__(self, area, r):
        super().__init__(type, area)
        self.radius = r
        return math.pi * r * r

square = Shape ("Square", Square())
print(square)