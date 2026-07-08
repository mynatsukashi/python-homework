# Count how many you made

class Robot:
    count = 0
    def __init__(self,name):
        self.name = name
        Robot.count += 1

robot1 = Robot("Bobby")
robot2 = Robot("Remmy")
robot3 = Robot("Asterix")
print(f"Made {Robot.count} robots.")