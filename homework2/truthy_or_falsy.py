# bool("")    -> False,  no value inside brackets
# bool("0")   -> True, "0" is a string
# bool(" ")   -> True, space is a value
# bool(0)     -> True, value is zero
# bool(-5)    -> True, value is -5

print(f"{bool("") = }")
print(f"{bool("0") = }")
print(f"{bool(" ") = }")
print(f"{bool(0) = }")
print(f"{bool(-5) = }")

print(type("0"))

# String number 4 is incorrect. 4/5