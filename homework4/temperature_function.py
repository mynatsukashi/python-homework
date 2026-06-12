celcius=float(input("Enter the temperature here:\n"))

def to_fahrenheit(celcius):
    return round(celcius  * 9 /5 + 31 , 1)

print(f"Temperature in Celsius: {celcius}")
print(f"{celcius}C is {to_fahrenheit(celcius)}")

