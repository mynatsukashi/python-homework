# Import library 
import random

# Define list 
nums = []

# Generate random numbers inside nums list
# Range = 5, to get 5 numbers in our list
for _ in range (5):
    nums.append(random.randint(0,100))
print(nums)

# Define min number in the list
mn = nums[0]

# Define min number in the list, compared to mn

for num in nums:
    if num<mn:
        mn = num
print(mn)