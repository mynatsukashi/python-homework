# Your first class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def describe(self):
        return f"{self.name} is in grade {self.grade}"

student_1 = Student ("Nino", 8)
student_2 = Student ("Natali", 12)

print(student_1.describe())
print(student_2.describe())