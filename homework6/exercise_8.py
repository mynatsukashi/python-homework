# scores = {"nino": 90, "giorgi": 75}

# name = "luka"
# print(f"{name}'s score is {scores[name]}")

"""
Python recognizes only keys and values, it can't identify that "nino"(key),
is a name. Additionaly, key "luka" doesn't exist inside scores dictionary,
therefore this program would still crash. The solved version is provided
below.

"""
scores = {"nino": 90, "giorgi": 75}

name = "luka"
print(f"{name}'s score is {scores.get(name, "missed")}")

