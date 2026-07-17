"""
Handman Game 
The concept is to guess a word. 3 attempts.
"""
from random import choice
import time

cities = ["tbilisi","mtskheta", "kazbegi", "telavi", "rustavi", "bolnisi", "dmanisi", "batumi", "poti", "gori", "kutaisi", "kobuleti"]

rand_city = choice(cities)

def hint():
    hint = rand_city.title()[0] + (len(rand_city)- 1)* "_"
    return hint

attempt = 3
won = False

print("Choosing a word...")
time.sleep(1)
print(hint())

while 0 < attempt:
    chosen_city = input("What word have I chosen?").lower().strip()

    if chosen_city == rand_city:
        won = True
        break
    print(f"Wrong! Number of attempts:{attempt}")
    attempt-=1

if won:
    print("You won!")
else:
    print("You lost :(")

print(f"It was {rand_city.title()}")