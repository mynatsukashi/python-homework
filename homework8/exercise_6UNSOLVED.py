# A class with behaviour

class Counter:
    def __init__(self, count):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def value(self): 
        return self.count
    


