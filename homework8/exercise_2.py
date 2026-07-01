# Roll the dice 
# This means that from random library import randint function and choice function
from random import randint, choice

food = choice(["pizza", "khinkali", "kebab"]) #Choice helps to choose a random item from non-empty sequence
print(f"You rolled a {randint(1,6)}")
print(f"Tonight: {food}")
