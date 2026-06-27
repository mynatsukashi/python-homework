# A point that won't change
point = (3,7)

# point[0]=90

# File "c:\Users\Admin\Documents\GitHub\python-homework\homework7\exercise_1.py", line 4, in <module>
#     point[0]=90
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

x,y = point
print(point)
print(f"x = {x}, y = {y}")
