x = "This is a beautiful day"
n=1
if x == "":
    n=0
for char in x:
    print(char)
    if char == " ":
        n+=1
print(n)
print(len(x))
