# pyClasses02b.py
# with __str__()

class Student:

    # default constructor
    # instead of "self"
    # you can put any keyword
    def __init__(self, a, b):
        self.name = a
        self.department = b
 
    def __str__(self):
        return f"This is {self.name} from the {self.department} department!"

obj01 = Student("Mitsi", "Informatics")
print(obj01)
