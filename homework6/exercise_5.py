# Build a dictionary from input

students = int(input('How many students? '))

scores = {}

for _ in range(students):
    name = input('Name: ').lower().strip()
    score = int(input('Score: '))
    scores[name] = score
print(scores)
print(f"{students} students recorded.")