age = int(input("How old are you?\n"))
name = input("What is your name?\n").lower().strip()

def door_decision(name, age):
    if age < 18:
        return "Sorry, you cannot enter"
    if age>= 21 and name == "nino":
        return "Welcome, VIP!"
    if age%2==0 or name == "giorgi":
        return "You get a free drink"
    return "Welcome in. Enjoy your evening!"

print(door_decision(name, age))