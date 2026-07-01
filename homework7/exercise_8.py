# Name "notes.txt" with constant variable
FILE = "notes.txt"

# Define function that reads notes in FILE
def read_notes():
    try: 
        # Try to read the file
        with open ( FILE, "r") as f:
            # return only if line.strip(), so line has no spaces and new lines
            return [line.strip() for line in f if line.strip()]
        # If file doesn't exist
    except FileNotFoundError:
        # return empty file
        return []


# Define function that writes notes in the file
def save_notes(notes):
    with open (FILE, "w") as f:
        for note in notes:
            f.write(note + "\n")

notes = read_notes()
print(f"You have {len(notes)} note(s)")
for i, item in enumerate(notes, 1):
    print(f"{i}. {item}")

add_note = input("Add a note: ").strip()

if add_note: 
    notes.append(add_note)
    save_notes(notes)
    print("Saved!")
else:
    print("Nothing was added")
    




