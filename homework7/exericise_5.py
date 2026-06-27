# Don't crash on bad input
num = input("Choose a number: ")

try:
    number = int(num)
    if number is int:
        num*2
    else:
        print('Error')
except ValueError:
    print(f"{num.title()} is not a valid number.Try again")