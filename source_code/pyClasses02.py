# pyClasses02.py
# a simple class example
# with __init__()

class Student:

    # default constructor
    # instead of "self"
    # you can put any keyword
    def __init__(self, a, b):
        self.name = a
        self.department = b
 
    # another method
    def show_student(self):
        print("This is ", self.name, " from the ", self.department, " department!")

obj01 = Student("Mitsi", "Informatics")
obj01.show_student()
