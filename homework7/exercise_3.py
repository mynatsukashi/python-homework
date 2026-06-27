# Save a list to a file
shopping_list = [ 'egg', 'butter', 'bread']

with open ('text.txt', "w") as f:
    for item in shopping_list:
        f.write(item+"\n")