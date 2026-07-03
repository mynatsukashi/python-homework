class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle(200, 18)
print(f"My car's max speed is {vehicle1.max_speed} and mile age is {vehicle1.mileage}")