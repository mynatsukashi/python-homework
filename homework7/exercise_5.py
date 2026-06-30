# Don't crash on bad input

# Asks users to choose a number
num = input("Pick up a number: ")

try:
    # num = int("text") is also an option
    num = int(num)
    # If program detects ValueError
except ValueError:
    # Type this message
    print("Oops, this is not a number!")
else:
    # If not, double the number
    print(num*2)
finally:
    # This code runs whatever is the outcome
    print("Let's move on")