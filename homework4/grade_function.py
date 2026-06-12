n = float(input("Enter your grade here:\n"))

def score(n):
    if n>=90:
        return "A"
    if n>=80:
        return "B"
    if n>=70:
        return "C"
    return "F"
print(score(n))