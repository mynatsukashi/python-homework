def average(numbers):
    total = 0
    for num in numbers:
        total+=num
    return total / len(numbers)

a = [1,2,3,4,5,6,7,8,9,10]
b = [1,1,1,1,1]

print(average(a))
print(average(b))

    

