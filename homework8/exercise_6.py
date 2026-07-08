# A class with behaviour

class Counter:
    def __init__(self, count = 0):
        self.count = count
    
    def increment(self):
        self.count += 1
    
    def value(self): 
        return self.count

con = Counter()
c2 = Counter()
print(con.value())
print(c2.value)