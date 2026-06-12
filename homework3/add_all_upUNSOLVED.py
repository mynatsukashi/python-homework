num = int(input("Choose a number:\n"))
total=0
# Numbers is range can be flexible, in range (1, num +1)
for i in range (num+1):
    total += i
print(total)