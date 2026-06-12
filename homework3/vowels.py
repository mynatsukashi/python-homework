word = input("Choose a word:\n").strip().lower()
n=0

for char in word:
    if char == "a" or char=="o" or char=="e" or char=="i" or char=="u":
        n+=1
print(f"{word} has {n} vowels out of {len(word)} letters")
