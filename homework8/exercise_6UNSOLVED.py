# A class with behaviour

class Counter:
    def __init__(self, count):
        self.count = count
    
    def increment(self):
        return self.count + 1
    
    def value(self): 
        return self.count

con = Counter(0)



    