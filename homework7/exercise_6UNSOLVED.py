scores = {
    "natali": 95,
    "mia": 90,
    "emily": 60
}

choose_name = input("Whose score? ").lower().strip()
def chosen():
    if choose_name in scores:
        return scores[choose_name]
    
try:
    scores = scores.keys()
except KeyError:
    print(f"No score recorded for {choose_name}")
else:
    print(f"{choose_name}'s score is {chosen}")
finally:
    print("Well done!")

