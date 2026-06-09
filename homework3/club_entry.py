age = int(input("How old are you?\n"))
name = input("What is your name?\n").lower().strip()

if not age >18:
    print("Sorry, you cannot enter")
elif age>=21 and name=="nino":
    print("Welcome, VIP")
elif age%2==0 or name == "giorgi":
    print("You get a free drink!")
else:
    print("Welcome in. Enjoy your evening!")