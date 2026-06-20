# Numbered list
# This is a solution based on a hint that was provided in the exercise
names = ["natali","khatuna", "mishiko", "emily", "mia"]

for i in range (len(names)):
    print(f"{i+1}.{names[i].title()}")

# This is another solution for the exercise that I solved by myself, before noticed a hint
print(f"<<<<<Another solution for this exercise>>>>>>\n")
for i,name in enumerate(names, 1):
    print(f"{i}.{name.title()}")