"""
Handman Game 
The concept is to guess a word. 3 attempts.
"""
from random import choice
import time

mistake = 0
cities = ["tbilisi","mtskheta", "kazbegi", "telavi", "rustavi", "bolnisi", "dmanisi", "batumi", "poti", "gori", "kutaisi", "qobuleti"]

"""
- Write a function
"""
random_city = choice(cities)
print("Lem me choose the word...")
# time.sleep(2)
print("Let's go!")

def hint(random_city):
        print(random_city[0])

lst = (len(random_city)-1) * "_"
print(random_city[0].title(),lst)

ask_question = input("What word have I chosen?").lower().strip()

if ask_question != random_city:
        while mistake <3:
                print(mistake)
                mistake +=1
        print("Try again!")
elif mistake ==3:
        print("Game is over. You lost!")
else:
        print("Congratulations, you won!")

