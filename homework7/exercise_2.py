# Two values at once
def high_and_low(nums):
    biggest = nums[0]
    smallest = nums[0]
    for num in nums:
        if num<smallest:
            smallest = num
        elif num>biggest:
            biggest = num
    return smallest, biggest

low, high = high_and_low([1,2,3,4])
print(f"lowest: {low}\nhighest: {high}")
