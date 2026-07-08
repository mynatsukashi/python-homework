import random
import datetime
import time
import json
#Declarative code
class TemperatureRecord:
     def __init__(self, value, dt):
          self.value = value
          self.datetime = dt
          
class Thermometer:
    def __init__(self, name):
         self.name = name
         self.history = []

    def current_temperature(self):
         current_temperature = random.randint(15,30)

         self.history.append(TemperatureRecord(current_temperature, datetime.datetime.now()))
         return current_temperature
    
    def show_history(self):
         print(f"\n---{self.name}---\n")
         for record in self.history:
            print(f"{record.value} - {record.datetime}")

    
        
#Imperative code
dev1 = Thermometer("Storage")
dev2 = Thermometer("Room1")

print(dev1)
# print(dev1.current_temperature())
# time.sleep(1)
# print(dev2.current_temperature())

# dev1.show_history()
# dev2.show_history()

