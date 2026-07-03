# Save a profile with json
import json as js

profile = {
    "name": "Natali",
    "age": 24,
    "hobbies":[
        "Movies", "Books", "Music"
    ]
}

with open("me.json", "w") as f:
    js.dump(profile,f)
    print(f"Saved me.json")

with open ( "me.json", "r") as f:
    data = js.load(f)
    print(f"Loaded back: {data["name"]}, age {data["age"]}")