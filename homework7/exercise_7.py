# Comprehensions
numbers = [1,2,3,4,5,6]

num_doubled = [item*2 for item in numbers]
num_even = [n for n in numbers if n%2==0]
num_dict = {n:n*n for n in numbers}

print(num_doubled)
print(num_even)
print(num_dict)
