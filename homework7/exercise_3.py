# Save a list to a file
shopping_list = [ 'egg', 'butter', 'bread']

with open ('shopping.txt', "w") as f:
    for item in shopping_list:
        f.write(item+"\n")

print("Wrote 3 items to shopping.txt")