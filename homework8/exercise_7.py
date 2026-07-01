class Wallet:
    def __init__ (self, balance = 0 ):
        self.balance = balance 
    
    def add(self,amount):
        return self.balance + amount

    def spend(self,amount):
        if amount > self.balance:
            print(f"Cannot spend {amount}! - only {self.balance} left")
        else:
            return self.balance - amount

money = Wallet (200)
print(money.add(50))
print(money.spend(300))
