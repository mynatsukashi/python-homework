# Safe lookup
num_book = {
    "natali": "555-123-424",
    "luka": "954-234-615",
    "levani": "912-363-632"
}

name = input('Whose number? ').lower().strip()

if name in num_book:
    print(f"{name}'s number is {num_book[name]} ")
else:
    print(f"Sorry, {name} is not in the numbook")

# Another way to write the code 
# result = num_book.get(name, "Sorry, this name isn't in our numBook")
# print(result)

