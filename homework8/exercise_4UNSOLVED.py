# Save a profile with json
import json 

profile = {
    "name": "Natali",
    "age": 24,
    "hobbies":[
        "Travelling", "Reading", "Spending time with friends"
    ]
}

with open("me.json", "w") as f:
    json.dump(profile,f)

with open ( "me.json", "r") as f:
    data = json.load(f)