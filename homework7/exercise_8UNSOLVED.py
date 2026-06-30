notes = []

with open ("notes.txt") as f:
    file = f.read()
print(file)

# I didn't understand how to write the block of TRY here, therefore I did it a little bit different
try:
    "notes.txt"
except FileNotFoundError:
    # If program doesn't find the file, it will print this message
    print("File is not found")
else: 
    # If file does exist, ask user to add a note
    add_note =input("Add a note: ")
    # Adds this note in notes list
    notes.append(add_note)
finally:
    # Here the structure of code is incorrect, as it doesn't work as it should
    def save_note():
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
            # I try to print final results in "notes.txt" file, but it doesn't work
        with open ("notes.txt","a") as f:
            f.write(save_note + "\n")
    print("Saved!")





