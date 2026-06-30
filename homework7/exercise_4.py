# Read it back
shopping_list = [ 'egg', 'butter', 'bread']

with open ("shopping.txt", "w") as f:
    for line in shopping_list:
        f.write(f"- {line.strip() +"\n"}")
print(f"{len(shopping_list)} items in total.")

        


