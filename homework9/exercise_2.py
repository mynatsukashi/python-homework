# When are two things equal?

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
a = Coordinate(9,0)
b = Coordinate (3,7)
c = Coordinate(9,0)

print(a==b)
print(a==c)
print(b==c)