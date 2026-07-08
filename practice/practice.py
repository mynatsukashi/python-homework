import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius * self.radius
 
c = Circle(5)
print(c.area)  # no () — like an attribute
c.radius = 10  # recomputes

