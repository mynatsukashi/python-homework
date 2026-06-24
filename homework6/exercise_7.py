# Package it 

def total_price(cart):
    total = 0
    for price in cart.values():
        total+=price
    return total

a = {'milk': 5, 'egg': 0.6, 'bread':1.2, 'jam': 8, 'cheese': 21}
b = {'egg': 2, 'bread': 1, 'milk': 2}

print(total_price(a))
print(total_price(b))


