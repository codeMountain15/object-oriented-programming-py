# pyClasses04.py
# delete object

class Student:
   def __init__(self, name, department):
       self.name = name
       self.department = department

obj01 = Student("Manousos", "Informatics")
print(obj01)

del obj01
print(obj01.name) # error!
