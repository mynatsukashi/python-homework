import json # Import function to run json file smoothly

class Notebook: #Define class 
    def __init__(self):
        try: # Try to open this file
            with open ("notes.json") as f:
                self.notes = json.load(f)
        except FileNotFoundError: # If file doesn't exist
            self.notes = [] # Start with a new list

    def add(self, note): # Add new notes in the list
        self.notes.append(note)
        with open ("notes.json", "w") as f:
            json.dump(self.notes,f) #Two arguments, what and where to dump

nb = Notebook()
print(f"You have {len(nb.notes)} notes(s)")
for i, new_note in enumerate(nb.notes,1):
    print(f"{i}. {new_note}")
new_note = input("Add a note: ")
nb.add(new_note)
print("Saved!")
