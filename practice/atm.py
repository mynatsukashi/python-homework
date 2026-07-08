class Atm:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough!")
        else:
            self.balance -= amount

my_atm =Atm()

my_atm.deposit(200)

print(my_atm.balance)