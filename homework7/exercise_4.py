# Read it back
shopping_list = [ 'egg', 'butter', 'bread']

with open ("text.txt", "r") as f:
    for line in f:
        print(f"- {line.strip()}")
print(f"{len(shopping_list)} items in total")
        


